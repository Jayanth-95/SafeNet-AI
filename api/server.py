from flask import Flask, request, jsonify
from main import analyze_message

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json
    message = data.get("message")
    url = data.get("url")

    result = analyze_message(message, url)

    return jsonify({"status": "processed"})

if __name__ == "__main__":
    app.run(debug=True)
