#########################################################################
#### Process the messages from Chatbot in order to supply to ChatGPT  ###
#########################################################################



import json
from bs4 import BeautifulSoup
import datetime

#############################################
# format a message from Symphony Chatbot into the WIP stadard message
##############################################
def msg_formatter_sym(msg_org):
  company = "D159BDX9"
  chat_sys = "sym"
  orgin = 'user'
  msg = json.loads(msg_org.decode('utf-8'))
  display_name = msg.get('display_name')
  user_id = msg.get('user_id')
  conversation_id = msg.get('conversation_id')
  thread_id = ""
  message_id = msg.get('message_id')
  datetime_stamp = datetime.datetime.fromtimestamp(msg.get('timestamp') / 1000)
  date = datetime_stamp.date().strftime('%Y-%m-%d')
  time = datetime_stamp.time().strftime('%X')
  message = msg.get('message')

  # Extract the message from Symphony presentationHTML format message
  msg_msg = BeautifulSoup(message, "html.parser").find('p').text
  
  msg_json = {'company': company, 'chat_sys': chat_sys, 'origin': orgin, 'display_name': display_name, 'user_id': user_id, 'conversation_id': conversation_id, 'thread_id': thread_id, 'message_id': message_id, 'date': date, 'time': time, 'message': msg_msg}
  return msg_json





if __name__ == "__main__":
    
  msg_org = b'{"display_name": "Symbot3 Kurosawa", "user_id": 349026222360289, "conversation_id": "elNBjhvc4uirR7ZEyB_7XH___ndWQpHtdA", "message_id": "9UY7BO9r5warSpNbiGK5L3___ndA8CMObQ", "timestamp": 1686832667889, "message": "<div data-format=\\"PresentationML\\" data-version=\\"2.0\\" class=\\"wysiwyg\\"><p>\\u305b\\u3044\\u3081\\u3044\\u3055\\u3093\\u3001\\u4eca\\u65e5\\u306e\\u5915\\u65b9\\u306e\\u6253\\u3061\\u5408\\u308f\\u305b\\u304a\\u9858\\u3044\\u3057\\u307e\\u3059\\u3002</p></div>"}'
  tmp = msg_formatter_sym(msg_org)
  print(tmp)
