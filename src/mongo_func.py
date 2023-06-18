####################################################
### Connect, insert, get documents from MongoDB  ###
####################################################

import pymongo
import datetime
from dotenv import load_dotenv
import os
import json
from bson.json_util import dumps

load_dotenv()

######################
# Connect to MongoDB
######################
def mongodb_conn():
  try:
    return pymongo.MongoClient(os.getenv('MONGO_URL'))
  except pymongo.errors.ConnectionFailure as e:
    print("mongo.py: ERROR: could not connect to mongoDB: %s") % e


######################
# get documents from MongoDB
######################
def get_msg():
  db_client = mongodb_conn()
  if db_client is None:
    return
  
  try:
    db = db_client[os.getenv('MONGO_DB')]
    cols = db[os.getenv('MONGO_COLS')]
    ret = cols.find()
    db_client.close()
    return ret
  except:
    print('mongo.py: ERROR: No Collection in DB')

####################
# Insert a document into MongoDB
###################
def insert_msg(msg_json):
  db_client = mongodb_conn()
  if db_client is None:
    return

  try:
    db = db_client[os.getenv('MONGO_DB')]
    cols = db[os.getenv('MONGO_COLS')]
    cols.insert_one(msg_json)
    db_client.close()
  except:
    print('mongo.py: ERROR: Could not insert a msg to DB')


##################
# !!! Use for DEV only !!!
# All Documents in the collection  
##################
def delete_msg_all():
  db_client = mongodb_conn()
  db = db_client[os.getenv('MONGO_DB')]
  db[os.getenv('MONGO_COLS')].delete_many({})


if __name__ == "__main__":


##################
# !!! Use for DEV only !!!
# All Documents in the collection  
##################
  delete_msg_all()
  print("All documents have been deleted!")
    

