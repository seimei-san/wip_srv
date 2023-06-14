import openai
from flask import Flask, render_template, url_for, request
from dotenv import load_dotenv
import os
import json
import pymongo
import datetime
from bson.json_util import dumps

load_dotenv()

app=Flask(__name__)