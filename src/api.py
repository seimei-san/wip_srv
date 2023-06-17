#################################################
### API receiving the message from Chatbot  #####
#################################################


from src import app
from flask import Flask, render_template, request, redirect
import json

from src import ai
from src import msg_processor
from src import mongo
from src import ai_msg_processor

@app.route('/')
def index():
    print("index")
    msg = "hoge fuga hoge"
    return render_template('index.html', text=msg)


##########################
# API for receiving messags from Symphony Chatbot
##########################
@app.route('/api/v1/msg/sym', methods=["POST"])
def insert_msgs():
    if request.method == "POST":
        print("api.py: Method=POST")
    else:
        print("api.py: Methed!=POST")
        return render_template('index.html')

    msg_in = msg_processor.msg_formatter_sym(request.data)
    mongo.insert_msg(msg_in)

    print("######### Requesting AI #########")

    response = ai.ask_ChatCompletion(ai.prompt_generator(msg_in))
    print(response)

    response = ai_msg_processor.ai_msg_parser(msg_in['company'], msg_in['chat_sys'], msg_in['display_name'], msg_in['user_id'], msg_in['conversation_id'], "", msg_in['message_id'], msg_in['date'], msg_in['time'], response)
    mongo.insert_msg(response)
    print('######### Completed #########')

    return render_template('index.html')



# 