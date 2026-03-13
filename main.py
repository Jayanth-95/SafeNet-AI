from agents.message_agent import detect_phishing
from agents.url_agent import check_url

def analyze_message(message, url=None):

    message_risk = detect_phishing(message)

    if url:
        url_risk = check_url(url)
    else:
        url_risk = 0

    risk_score = (message_risk + url_risk) / 2

    if risk_score > 0.7:
        return "High Risk Scam Detected"
    elif risk_score > 0.4:
        return "Suspicious Message"
    else:
        return "Safe Message"

message = "Urgent! Verify your bank account immediately!"
url = "http://fake-bank-login.com"

print(analyze_message(message, url))
