from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from feedback.cohere import *
from emails.send_email import *

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
    clarity = classify_clarity(answer)

    response = jsonify({"sentiment": sentiment, "word_choice": word_choice, "clarity": clarity})

    return response

@app.post("/email")
def email():
    # data is {email: receiver@mail.com, feedback: [{question, response, word_choice, clarity, tone, timing}]}
    data = request.get_json()
    print(data)
    send_email(data)

    return jsonify({"status": 200})