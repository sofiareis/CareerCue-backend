from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from feedback.cohere import *

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# assumes text input
@app.get("/feedback")
def feedback():
    answer = request.args.get("answer")
    sentiment = classify_sentiment(answer)
    word_choice = classify_word_choice(answer)

    response = jsonify({"sentiment": sentiment, "word_choice": word_choice})
    #response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')

    return response