from flask import Flask, render_template, make_response, request, redirect
from flask_cors import CORS
from flask_restplus import Resource, Api
import json
import os


app = Flask(__name__)
cors = CORS(app)

json_folder = './json_files'
data_posted = 'N/A'
cur_json = ''

api = Api(app,
          version='1.0',
          title='Mental Maths Practice',
          description='Mental Maths Practice (MMP) RESTful API',
          doc='/apis')


# Routing
@api.route('/questions')
class QuestionFactory(Resource):
    def get(self):
        res = {"questions": ["1 + 1", "2 + 2", "3 + 3"]}
        return res


if __name__ == '__main__':
    app.run(debug=True)
