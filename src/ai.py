import openai

from dotenv import load_dotenv
import os
import json

load_dotenv()

openai.organization=os.getenv('AI_ORG')
openai.api_key=os.getenv('AI_KEY')

def ask_ChatCompletion(msgs_json):
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = msgs_json,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0.5
    )
    response = completion.choices[0].message.content
    # response = completion
    return response


def ask_Completion():
    completion = openai.Completion.create(
        model = "text-davinci-003",
        prompt = 
            'Please identify these elements such as "who to do", "by when", "untile when", "what to do", "at where", "in where", "to where", "how to do", "how much", "how many" and "why" from the following Japanese text. If an element cannot be identifed, state NONE: "黒澤さん、明日の会議で社長が説明するための資料を今日の夕方までに作成できますか"',
      temperature=0.7,
      max_tokens=1024,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    response = completion.choices[0].text
    return response
 

msg = [
    {"role":"user", "content": "黒澤さん、明日の会議の資料を今日の夕方までに作成できますか"},
    {"role":"user", "content": "社長が明日の会議で説明するためにその資料が必要なんです。"},
    {"role":"user", "content": "最悪、明後日の午前１０時まで待てます"},
    {"role":"user", "content": 'Please identify these elements such as "who to do", "by when", "untile when", "what to do", "at where", "in where", "to where", "how to do", "how much", "how many" and "why" from the above Japanese messages in Japanese. If an element cannot be identifed, state "none".'},
    ]
print(ask_ChatCompletion(msg))
# print(ask_Completion())