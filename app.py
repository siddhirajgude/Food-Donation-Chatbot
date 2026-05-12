from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import json
import random
import re

# pyright: reportPrivateImportUsage=false
import google.generativeai as genai
import os

load_dotenv()

app = Flask(__name__)

# Configure API
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-3-flash-preview")

# Load intents JSON
with open('intents.json', encoding='utf-8') as file:
    intents = json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

# Chat API
@app.route("/get", methods=["POST"])
def chatbot():
    user_msg = request.json.get("message")
    print("User:", user_msg)

    user_msg = user_msg.lower().strip()

    #Step 1: Check intents
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_msg:  
                reply = random.choice(intent["responses"])
                print("Matched intent:", intent["tag"], "Reply:", reply)  # Debug
                return jsonify({"reply": reply})

    #Step 2: If not found → use Gemini
    ai_reply = get_ai_response(user_msg)
    print("AI reply:", ai_reply)  
    return jsonify({"reply": ai_reply})

def format_response(text):
    text = re.sub(r'(\d+\.)', r'\n\1', text)
    text = re.sub(r'(-|\•)', r'\n\1', text)
    text = re.sub(r'\n+', '\n', text)
    return text.strip()

def get_ai_response(user_msg):
    try:
        prompt = f"""
You are a Food Donation Chatbot.

This platform helps people donate and receive leftover food.

Explain BOTH Sender and Receiver processes in ONE response.

⚠️ Important:
- Do NOT write in one paragraph
- Use proper headings
- Use numbered steps
- Use spacing between sections

🤖Food Donation System – How It Works

🍱Sender (Donate Food)\n
1.Click "Send" button on homepage
2.Fill the form:
   - Food type
   - Quantity
   - Location
3.Click Submit
4.Donation becomes visible to receivers \n 

🥗Receiver (Get Food)\n
1.Click "Receive" button
2.Register or Login
3.View available food
4.Contact sender
5.Collect food \n

Rules:
- Keep it simple and friendly
- Always structured format
- No single paragraph answer

User question: {user_msg}
"""
        response = model.generate_content(prompt)

        if response.text:
            return format_response(response.text)
        else:
            return "Sorry, I couldn’t understand that."

    except Exception as e:
        print("Gemini Error:", e)
        return "I'm not sure about that, but I can help you with food donation 😊"
    
if __name__ == "__main__":
    app.run(debug=True)