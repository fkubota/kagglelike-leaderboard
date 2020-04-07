from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import pathlib


def tell_me_score(text):
    submission = text2df(text)
    current_dir = str(pathlib.Path(__file__).resolve().parent)
    path_y_te = str(current_dir)+'/y_test.csv'
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
