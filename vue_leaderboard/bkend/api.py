from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

# Require a parser to parse our POST request.
parser = reqparse.RequestParser()
parser.add_argument("arg01")


class MyApi(Resource):
    def post(self):
        args = parser.parse_args()
        val = args['arg01']
        val_val = val + ' ---> flask'
        return {"after_api": val_val}


api.add_resource(MyApi, "/myapi")

if __name__ == "__main__":
    app.run('127.0.0.1', 5002, debug=True)
