from flask import Flask, request, jsonify, redirect, render_template
from flask_cors import *
import json
from werkzeug.utils import secure_filename
import os
import requests

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.debug = True
app.secret_key = 'helloworld!!'

testInfo = {}


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        data = json.loads(request.get_data())
        print(data)
        return jsonify("success")
    else:
        return jsonify("fail")


@app.route('/province', methods=['POST', 'GET'])
def province():
    if request.method=='POST':
        rev=request.get_json()['user']
        print(rev)
        if(rev=="user1"):
            result = ["19", "97", "1", "23"]
        elif(rev=="user2"):
            result = ["19", "97", "10", "31"]
        elif (rev == "user3"):
            result = ["19", "97", "10", "10"]
        else:
            result = ["0", "0", "0", "0"]
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
