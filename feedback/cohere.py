import cohere
from feedback.training import *
from feedback.api_key import *

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

def classify_clarity(input):
    response = co.classify(
        model='large',
        inputs=[input],
        examples=clarity_examples,
    )

    return response.classifications[0].prediction

def classify_structure(input):
    response = co.classify(
        model='large',
        inputs=[input],
        examples=structure_examples,
    )

    return response.classifications[0].prediction

def classify_specific(input):
    response = co.classify(
        model='large',
        inputs=[input],
        examples=specific_examples,
    )

    return response.classifications[0].prediction

