def add_one(x):
    return x + 1


def test_answer():
    assert add_one(3) == 6


def test_trained_model():
    import pandas as pd
    import pickle
    import os

    # load trained model
    file_to_open = open(os.path.join("data", "models", "baummethoden_lr.pickle"), "rb")
    trained_model = pickle.load(file_to_open)
    file_to_open.close()

    # load data that we want predictions for
    prediction_data = pd.read_csv(os.path.join("data", "prediction-data.csv"), sep=";")

    assert trained_model.predict(prediction_data) is not None
