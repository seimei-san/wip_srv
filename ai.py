import openai

from dotenv import load_dotenv
import os
import json

load_dotenv()

print(os.getenv('AI_KEY'))
openai.organization=os.getenv('AI_ORG')
openai.api_key=os.getenv('AI_KEY')

def ask_ChatGPT(msg):
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{
            "role":"user",
            "content": msg,
        }],
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0.5
    )
    response = completion.choices[0].message.content
    return response

msg = "G's Academy はどんな学校ですか？"

print(ask_ChatGPT(msg))