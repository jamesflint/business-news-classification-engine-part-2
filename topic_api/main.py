# This Python file uses the following encoding: utf-8
# USAGE
# Start the server:
# 	python main.py
# Submit a request via cURL:
# 	curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'
# Submit a request via Python:
#	import requests
#   import json
#   url = 'https://afternoon-shelf-15457.herokuapp.com/predict'
#   s = {"title":"foo", "body":"bar"}
#   s_json = json.dumps(s)
#   headers = {'Content-Type': 'application/json'}
#   r = requests.post(url, data=s_json, headers=headers)
#   print(r.text)


# import the necessary packages

from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import numpy
import flask
import os
import pickle
from flask import Flask, render_template, request
import re


MAX_NUM_WORDS = 2000
MAX_SEQUENCE_LENGTH = 150

MODEL_DIR = "./models"

CATEGORIES = ["Artificial intelligence",
              "Battery technology",
              "Blackswans",
              "Blockchain",
              "Carbon eradication",
              "Counterparty risk",
              "Digital advertising",
              "Digital currency",
              "Digital health",
              "Education technology",
              "Financial services",
              "Internet of things",
              "Property",
              "Sharing economy"]

# initialize our Flask application and the Keras model
app = Flask(__name__)
model = None
tokenizer = None

# load the pre-trained Keras model
model = load_model(os.path.join(MODEL_DIR, "LSTM-body-text+title-19-epochs.h5"))

# load the saved Keras tokenizer, for text pre-processing
with open("tokenizer_LSTM.pickle", "rb") as handle:
    tokenizer = pickle.load(handle)

def remove_html_tags(data):
    '''Remove any html tags from submitted text'''
    p = re.compile(r"<.*?>")
    return p.sub("", data)

def predict_category(text_to_predict):
    '''Process text and predict category'''
    # pre-process the text and create
    # embeddable vector of the right length
    cleantext = remove_html_tags(text_to_predict)
    sequence = tokenizer.texts_to_sequences([cleantext])
    trans_text = pad_sequences(sequence, maxlen=MAX_SEQUENCE_LENGTH)
    # use the model to predict the right category
    prediction = model.predict(numpy.array(trans_text))
    # match the prediction number to the right label
    predicted_label = CATEGORIES[numpy.argmax(prediction)]
    # print(predicted_label, "\n")
    return predicted_label

@app.route("/predict", methods=["POST"])
def predict():
    '''Handle the POST api request'''
    if flask.request.method == "POST":
        if request.headers["Content-Type"] == "application/json":
            payload = request.json
            title = payload["title"]
            body = payload["body"]
            text_to_predict = str(title + " " + body)

            predicted_label = predict_category(text_to_predict)

            return flask.jsonify(predicted_label)

    else:
        return "415 Unsupported Media Type ;)"

# load a webform for entering a query text manually
@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/submitted", methods=["POST"])
def submitted_form():
    # load the saved Keras tokenizer, for text pre-processing

    title = request.form["title"]
    body = request.form["body"]

    text_to_predict = str(title + " " + body)

    predicted_label = predict_category(text_to_predict)

    return render_template(
        "submitted_form.html",
        title=title,
        body=body,
        topic=predicted_label)


# if this is the main thread of execution then start the server
if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))

    app.run()


