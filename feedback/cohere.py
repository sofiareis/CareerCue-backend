import cohere
from feedback.training import *

API_KEY = 'fyTCYfZc3ubA4J9ynNiZwWVmKkBDGVyCFQeIN7vd'
co = cohere.Client(API_KEY)

def classify_sentiment(input):
    response = co.classify(
        model='large',
        inputs=[input],
        examples=sentiment_examples,
    )

    return response.classifications[0].prediction

def classify_word_choice(input):
    response = co.classify(
        model='large',
        inputs=[input],
        examples=word_choice_examples,
    )

    return response.classifications[0].prediction

# add classify clarity

