# flask_app.py
from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello World! This is annnnnnother edit!"
