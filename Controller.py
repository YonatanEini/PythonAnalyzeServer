from http.server import HTTPServer, BaseHTTPRequestHandler

import flask
from flask import Flask, make_response, jsonify
from flask_restful import Api, Resource
from flask import request
from data_object import DataAnalyzedObjectDto
from pandas_analyze_data import DecodedData
from flask_cors import CORS
import sys

import json

app = Flask(__name__)
CORS(app)

api = Api(app)
data_analyzed = DataAnalyzedObjectDto(0, 0, 0, 0, 0, 0, 0, 0)


class HandleRequests(Resource):
    def get(self):
        # will return analyst object(avg height, avg speed,height-time data, height-fuel data)
        print('get request!')
        return data_analyzed.to_Json()

    def post(self):
        request_data = request.get_json()
        print("post request!")
        decoded_items = request_data['DecodedItems']
        decoded_hour = request_data['Hour']
        decoded_date = request_data['DecodingTime']
        new_data = DecodedData(decoded_items, decoded_hour, decoded_date)
        new_data.analyze_data_frame(data_analyzed)


api.add_resource(HandleRequests, "/")

if __name__ == '__main__':
    app.run(host="localhost", port=5000,debug=True)
