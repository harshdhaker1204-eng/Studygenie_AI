from flask import Flask, request, jsonify
from flask_cors import CORS
from ai import ask_ai, summarize_text, generate_quiz

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")
    answer = ask_ai(question)
    return jsonify({"response": answer})


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    text = data.get("text")
    result = summarize_text(text)
    return jsonify({"response": result})


@app.route("/quiz", methods=["POST"])
def quiz():
    data = request.json
    topic = data.get("topic")
    result = generate_quiz(topic)
    return jsonify({"response": result})


if __name__ == "__main__":
    app.run(debug=True)