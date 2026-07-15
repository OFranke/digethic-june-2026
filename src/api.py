from flask import Flask, Response, request
import pandas as pd
import os
import pickle

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


@app.route("/predict")
def predict():
    file_to_open = open(os.path.join("data", "models", "baummethoden_lr.pickle"), "rb")

    trained_model = pickle.load(file_to_open)
    file_to_open.close()

    # load data that we want predictions for

    zylinder = float(request.args.get("zylinder"))
    ps = float(request.args.get("ps"))
    gewicht = float(request.args.get("gewicht"))
    beschleunigung = float(request.args.get("beschleunigung"))
    baujahr = float(request.args.get("baujahr"))

    predictions = trained_model.predict(
        [[zylinder, ps, gewicht, beschleunigung, baujahr]]
    )

    return {"result": predictions[0]}
