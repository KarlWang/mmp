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
          title='Octopus Target Generator',
          description='Octopus Target Generator RESTful API',
          doc='/apis')


# Routing
@api.route('/questions')
class QuestionFactory(Resource):
    def get(self):
        res = {"questions": ["1 + 1", "2 + 2", "3 + 3"]}
        return res


@api.route('/json_data')
class JsonData(Resource):
    def get(self):
        '''Get the content of the current selected JSON file'''
        json_data = {}
        if cur_json != '':
            with open(json_folder + '/' + cur_json) as json_file:
                json_data = json.load(json_file)
        return json_data

    def post(self):
        '''Save to current JSON file'''
        data_posted = request.json['body']
        with open(json_folder + '/' + cur_json, 'w') as outfile:
            json.dump(data_posted, outfile)
        print("Data posted: {}".format(data_posted))
        return request.json, 201


@api.route('/file_list')
class ListFiles(Resource):
    def get(self):
        files = []
        ret_json = {"folder": "", "files": []}
        # r=root, d=directories, f = files
        for r, d, f in os.walk(json_folder):
            for file in f:
                if '.json' in file:
                    files.append(file)

        ret_json["files"] = files
        ret_json["folder"] = os.path.abspath(json_folder)
        print(ret_json)
        return ret_json


@api.route('/json_file')
class JsonFile(Resource):
    def get(self):
        '''Get the current JSON file name'''
        return cur_json

    def post(self):
        '''Set the current JSON file'''
        global cur_json
        cur_json = request.json['body']['json_file']
        print('Set current JSON file to {}'.format(cur_json))
        return cur_json, 201


if __name__ == '__main__':
    app.run(debug=True)
