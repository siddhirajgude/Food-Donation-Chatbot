## 🍱 Food Donation Chatbot ❤️

A web-based chatbot system that helps people donate leftover food to those in need.  
Users can either **donate food (Sender)** or **receive food (Receiver)** through a simple and interactive interface.

## 🚀 Features

- 🤖 AI-powered chatbot for guidance  
- 🍲 Easy food donation process  
- 🥗 Simple food receiving system  
- 🔐 User login and registration  
- 📧 Email notification support  
- 💬 Clean and structured chatbot responses  

## 🛠️ Technologies Used

- Frontend: HTML, CSS  
- Backend: Python (Flask)  
- AI Integration: Gemini API  
- Libraries: Flask-Mail  

## ⚙️ Libraries 
- Flask – Web framework  
- dotenv – Manage environment variables  
- json – Handle JSON data  
- random – Random responses  
- re – Text formatting  
- google.generativeai – AI response generation  
- os – Access environment variables  

## ⚙️ How It Works

1. **User Input**
   The user types a message in the chatbot interface.

2. **Request Sent to Backend**
   The message is sent to the Flask backend using a POST request (`/get` route).

3. **Intent Detection**
   The system checks the user message:
    First, it tries to match with predefined intents (from a JSON file).
    If no match is found, it uses the Gemini API for generating a response.

4. **AI Response Generation**
   The chatbot uses AI (Google Gemini API) to generate smart and meaningful replies.

5. **Response to User**
   The generated response is sent back and displayed in the chat interface.

## 📂 Project Structure
Food-Donation-Chatbot/
│── app.py
│── intents.json
│── .env
|── venv
│── README.md
│── requirements.txt
│
├── static/
│   ├── bg.png
│   ├── script.js
│   ├── style.css
│
├── templates/
│   ├── index.html
│
├── Project_Screen

2. Install dependencies
pip install flask flask-mail python-dotenv

3. Add your API key in `.env` file
GEMINI_API_KEY=my_api_key_here

4. Run the app
python app.py

5. Open in browser:
http://127.0.0.1:5000/

## API Key Note
The Gemini API key is stored securely using environment variables (`.env`) and is not exposed in the code.

## Example Flow
User: "How can I donate food?"
→ Chatbot checks intents
→ If matched, returns predefined answer
→ Else, uses Gemini API
→ Displays response to user

## Screen Recording:
Project_Screen.mp4

### 🎯 Future Improvements
📱 Mobile responsive UI
🤝 NGO integration

## 👩‍💻 Author
Siddhi Rajgude.

## Contribution
Feel free to contribute and improve this project!