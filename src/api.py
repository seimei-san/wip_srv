from src import app
from flask import Flask, render_template, request, redirect
import json


@app.route('/')
def index():
    print("index")
    msg = "hoge fuga hoge"
    return render_template('index.html', text=msg)

@app.route('/msgs', methods=["POST"])
def insert_msgs():
    if request.method == "POST":
        print("OK")
    else:
        print("NG")

    tmp = json.loads(request.data.decode('utf-8'))
    print(tmp.get('display_name'))
    print(tmp.get('user_id'))
    print(tmp.get('conversation_id'))
    print(tmp.get('message_id'))
    print(tmp.get('timestamp'))
    print(tmp.get('message'))
    return tmp

