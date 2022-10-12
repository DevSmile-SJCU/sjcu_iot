import os
from flask import Flask, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/hello')
def hello_IoT():
    return 'Hello, IoT'

# Simple Method Test
@app.route('/method', methods=['GET', 'POST'])
@app.route('/method/<data>', methods=['GET', 'POST'])
def method(data = 'None'):
    if request.method == 'GET':
        return 'Method - GET ' + data
    else:
        return 'Method - POST ' + data
    
# API Test : URL Encoded
# ~/data
# ~/data?msg=hello
@app.route('/data')
def data():
    value = request.args.get('msg')
    if value == None:
        try:
            fileValue = open('./data/msg.txt', 'r')
        except FileNotFoundError: 
            return 'No Data'
        else:
            value = fileValue.read()
            fileValue.close()
            return value
    else:
        fileValue = open('./data/msg.txt', 'w')
        fileValue.write(value)
        fileValue.close()
        return 'Data Saving...'
    
# JSON 데이터로 응답하기
# {"name" : "Chris", "Age" : 30}
@app.route('/data/<param>')
def data_get(param):
    return jsonify({"param" : param, "result" : 1})

# POST 데이터 전송 : JSON, 일반 텍스트
@app.route('/data', methods=['POST']) # post method 
def data_post():
    if request.is_json:
        data = request.get_json()
        print(data['param'])
        return jsonify(data)
    else:
        data = request.get_data().decode('utf-8')
        print(data)
        return data

# 잘못된 요청에 대한 처리 
@app.errorhandler(404)
def fileNotFond(error):
    return '404 Not Found', 404

# Redirect (재전송)
@app.route('/')
def index():
    return redirect(url_for('hello_IoT'))

if __name__ == '__main__':
	app.run(
    host="0.0.0.0",
    port=7777,
    debug=True)