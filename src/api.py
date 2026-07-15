from flask import Flask, Response
import pandas as pd
import os

app = Flask(__name__)


@app.route("/")
def root():
    return {"hello": "world"}


@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/training_data")
def training_data():
    data = pd.read_csv(os.path.join("data", "auto-mpg.csv"), sep=";")
    return Response(data.to_json(), mimetype="application/json")
