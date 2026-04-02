import requests

def ask_ai(question):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "tinyllama",
            "prompt": question,
            "stream": False
        }
    )
    return response.json()["response"]

def summarize_text(text):
    return ask_ai(f"Summarize this in simple points:\n{text}")

def generate_quiz(topic):
    return ask_ai(f"Create 5 MCQ questions with answers:\n{topic}")