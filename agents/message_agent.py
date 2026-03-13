import re

def detect_phishing(message):
    suspicious_keywords = [
        "urgent",
        "bank",
        "verify",
        "account suspended",
        "click link",
        "payment required"
    ]

    score = 0

    for word in suspicious_keywords:
        if re.search(word, message.lower()):
            score += 0.2

    return min(score, 1)
