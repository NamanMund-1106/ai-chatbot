from flask import Flask, request, jsonify, render_template
from chatbot import get_response
from database import init_db, save_conversation

app = Flask(__name__)

# Initialize database when app starts
init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    bot_response = get_response(user_message)
    save_conversation(user_message, bot_response)
    
    return jsonify({
        "user_message": user_message,
        "bot_response": bot_response
    })

if __name__ == "__main__":
    app.run(debug=True)