from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import tell_me_score

app = Flask(__name__)
CORS(app)
api = Api(app)

# Require a parser to parse our POST request.
parser = reqparse.RequestParser()
parser.add_argument("arg01")


class MyApi(Resource):
    def post(self):
        print('--- in api ---')
        args = parser.parse_args()
        val = args['arg01']
        print('val: ', val)
        score = tell_me_score.tell_me_score(val)
        print('--- out api ---')
        return {"score": round(score, 3)}


api.add_resource(MyApi, "/myapi")

if __name__ == "__main__":
    app.run('127.0.0.1', 5003, debug=True)
