import pymongo
import datetime
from dotenv import load_dotenv
import os
import json
from bson.json_util import dumps


def mongodb_conn():
  try:
    return pymongo.MongoClient(os.getenv('MONGO_URL'))
  except pymongo.errors.ConnectionFailure as e:
    print("ERROR: could not connect to mongoDB: %s") % e


def get_msg():
  db_client = mongodb_conn()
  if db_client is None:
    return
  
  try:
    db = db_client[os.getenv('MONGO_DB')]
    cols = db[os.getenv('MONGO_COLS')]
    ret = cols.find()
    return ret
  except:
    print('No Collection in DB')


def insert_msg(msg_json):
  db_client = mongodb_conn()
  if db_client is None:
    return

  try:
    db = db_client[os.getenv('MONGO_DB')]
    cols = db[os.getenv('MONGO_COLS')]
    cols.insert_one(msg_json)
  except:
    print('Could not insert a msg to DB')



load_dotenv()


insert_msg({
    'msg': 'honya honya',
    'date_time': '2023-06-12 10:20:23'  
})

print(dumps(get_msg()))
    

