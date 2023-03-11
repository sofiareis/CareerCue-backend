from flask import Flask
from cohere.cohere import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# assumes text input
@app.route("/feedback")
def feedback():
    answer = request.args.get("answer")
    sentiment = classify_sentiment(answer)
    word_choice = classify_word_choice(answer)

    return {"sentiment": sentiment, "word_choice": word_choice}