import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello_IoT():
    return 'Hello, IoT'

if __name__ == '__main__':
	app.run(
    host="0.0.0.0",
    port=7777,
    debug=True)