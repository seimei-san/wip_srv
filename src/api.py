#################################################
### API receiving the message from Chatbot  #####
#################################################


from src import app
from flask import Flask, render_template, request, redirect
import json

from src import ai
from src import msg_processor
from src import mongo_func
from src import ai_msg_processor
from src.mysql_func import MySqlDb

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
    mongo_func.insert_msg(msg_in)

    print("######### Requesting AI #########")

    response_org = ai.ask_ChatCompletion(ai.prompt_generator(msg_in))
    print("AI_RESPONSE: ", response_org)
    print("######### AI Response ##########")

    if len(response_org) == 0:
        print("api.py: ERRROR: AI response is empty!")
    else:
        response = ai_msg_processor.ai_msg_parser(msg_in['company_id'], msg_in['chat_sys'], msg_in['display_name'], msg_in['user_id'], msg_in['conversation_id'], "", msg_in['message_id'], msg_in['date'], msg_in['time'], response_org)
        mongo_func.insert_msg(response)

        score = ai_msg_processor.ai_msg_score(msg_in['company_id'], msg_in['chat_sys'], msg_in['display_name'], msg_in['user_id'], msg_in['conversation_id'], "", msg_in['message_id'], msg_in['date'], msg_in['time'], response_org)
        mysqldb = MySqlDb()
        try:
            result = mysqldb.insert_wip_score(score)
        except Exception as e:
            print("api.py: ERROR: cannot insert score into MySQL: %s", e)

        print('######### Completed #########')

        return render_template('index.html')



# 