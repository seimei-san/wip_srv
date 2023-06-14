from flask import Flask, render_template, url_for, request
from src import app
import json


@app.route('/')
def index():
    msg = "hoge fuga"
    return render_template('index.html', text=msg)


