# flask_app.py
from flask import Flask, jsonify
import pandas as pd
#import requests

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello World! This is an edit!"

@app.route("/api")
def hello_2():
    return jsonify(pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}).to_dict(orient='records'))