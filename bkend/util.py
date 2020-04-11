from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import pathlib
import json
import numpy as np

PATH_RANKING_TABLE = '../data/ranking_table.csv'
PATH_PARTICIPANTS_DATA = '../data/participant.json'


def tell_me_score(text):
    submission = text2df(text)
    current_dir = str(pathlib.Path(__file__).resolve().parent)
    path_y_te = str(current_dir)+'/../data/y_test.csv'
    df_y_te = pd.read_csv(path_y_te)
    logic = all(df_y_te['series_id'].values == submission['series_id'].values)
    assert logic, 'series_id が一致しません'

    y_true = df_y_te['surface'].values
    y_pred = submission['surface'].values

    le = LabelEncoder()
    le.fit(y_true)

    y_true = le.transform(y_true)
    y_pred = le.transform(y_pred)

    return accuracy_score(y_true, y_pred)


def text2df(text):
    text = text.split('\n')
    arr = []
    for i in range(len(text)-1):
        te = text[i].split(',')
        arr.append(te)
    df = pd.DataFrame(arr[1:], columns=arr[0])
    df['series_id'] = df['series_id'].astype(int)
    return df


def update_participants_data(name, score):
    score = round(score, 3)
    # fp = open(PATH_PARTICIPANTS_DATA, 'r')
    # j = json.load(fp)  # str読み込み
    try:
        # ローカルJSONファイルの読み込み
        with open(PATH_PARTICIPANTS_DATA, 'r') as f:
            j = json.load(f)
    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)
    j = json.loads(j)  # str ---> dict
    j[name]['scores'].append(score)

    # dict-->json(text)
    text = json.dumps(j)
    # save

    with open(PATH_PARTICIPANTS_DATA, 'w') as outfile:
        json.dump(text, outfile)
    # fw = open(PATH_PARTICIPANTS_DATA, 'w')
    # json.dump(text, fw)
    print('------')
    update_ranking_table()
    print('------')


def update_ranking_table():
    print('----- python-↓update_ranking_table')
    fp = open(PATH_PARTICIPANTS_DATA, 'r')
    j = json.load(fp)  # str読み込み
    j = json.loads(j)  # str ---> dict

    names = list(j.keys())
    best_scores = np.array([max(j[name]['scores']) for name in names])
    rank_idxs = np.argsort(-best_scores)  # 降順にするために'-'をつけた
    rank_names = []
    rank_scores = []
    rank_n_subs = []
    for i in range(len(names)):
        name = names[rank_idxs[i]]
        n_sub = len(j[name]['scores'])
        score = best_scores[rank_idxs[i]]
        rank_names.append(name)
        rank_scores.append(score)
        rank_n_subs.append(n_sub)
    df_rank = pd.DataFrame(np.arange(1, len(names)+1), columns=['#'])
    df_rank['Name'] = rank_names
    df_rank['Score'] = rank_scores
    df_rank['N_Submission'] = rank_n_subs
    df_rank.to_csv(PATH_RANKING_TABLE, index=False)


def get_ranking_table():
    df = pd.read_csv(PATH_RANKING_TABLE)
    json_str = ''
    for i in range(len(df)):
        a = df.iloc[i, :]
        s = f"{a['#']}, {a['Name']}, {a['Score']}, {a['N_Submission']} \n"
        json_str = f'{json_str} {s}'
    json_str = json_str[:-1]
    return json_str
