import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class PhishingModel:

    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

    def train(self, messages, labels):
        X = self.vectorizer.fit_transform(messages)
        self.model.fit(X, labels)

    def predict(self, message):
        X = self.vectorizer.transform([message])
        prediction = self.model.predict(X)
        return prediction[0]


if __name__ == "__main__":

    # Sample training data
    messages = [
        "verify your bank account now",
        "urgent payment required",
        "click this link to win prize",
        "meeting scheduled tomorrow",
        "your package has been delivered",
        "project discussion at 3pm"
    ]

    labels = [1, 1, 1, 0, 0, 0]  # 1 = phishing, 0 = normal

    model = PhishingModel()
    model.train(messages, labels)

    test_message = "urgent verify your bank account"

    result = model.predict(test_message)

    if result == 1:
        print("Phishing Message Detected")
    else:
        print("Safe Message")
