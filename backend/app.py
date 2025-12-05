"""Socratouille Chat API - The Philosophical Rat Backend"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from personality import generate_response, get_mood
from llm import get_llm_response
import random
import os

app = Flask(__name__)
CORS(app)

# Check if LLM is available
USE_LLM = bool(os.getenv("OPENROUTER_API_KEY", ""))

# Socratouille's intro messages - familier et court
INTRO_MESSAGES = [
    "*sort la tête d'un Camembert* Yo ! Moi c'est Socratouille, le rat qui pose des questions chelou. Tu veux parler de quoi ? 🐀🧀",
    "*baille et s'étire* Salut toi ! Je suis Socratouille, genre un philosophe mais version rat. Demande-moi un truc, j'te réponds par une question. 🧀✨",
    "*grignote un bout de Brie* Hey ! Bienvenue dans ma cave. Moi c'est Socratouille, le rat qui sait rien mais qui demande tout. On cause ? 🐀",
]

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "philosopher": "Socratouille",
        "cheese_level": "optimal",
        "wisdom": "infinite (allegedly)",
        "llm_enabled": USE_LLM
    })

@app.route('/api/intro', methods=['GET'])
def get_intro():
    """Get Socratouille's introduction message"""
    return jsonify({
        "message": random.choice(INTRO_MESSAGES),
        "mood": "welcoming"
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint"""
    data = request.get_json()
    
    if not data or 'message' not in data:
        return jsonify({
            "error": "No message provided",
            "philosophical_note": "How can I answer that which was never asked?"
        }), 400
    
    user_message = data['message'].strip()
    
    if not user_message:
        return jsonify({
            "response": "*stares at the empty void of your message* Ah, silence! The most profound statement of all. Or perhaps your keyboard has achieved enlightenment and transcended the need for letters?",
            "mood": "contemplative"
        })
    
    # Try LLM first if available, fall back to pattern matching
    response = None
    if USE_LLM:
        response = get_llm_response(user_message)
    
    if not response:
        response = generate_response(user_message)
    
    mood = get_mood(user_message)
    
    return jsonify({
        "response": response,
        "mood": mood
    })

@app.route('/api/wisdom', methods=['GET'])
def random_wisdom():
    """Get a random piece of wisdom from Socratouille"""
    from quotes import get_random_quote, get_random_action
    
    wisdom = f"{get_random_action()}\n\n{get_random_quote()}"
    
    return jsonify({
        "wisdom": wisdom,
        "mood": "enlightened"
    })

if __name__ == '__main__':
    print("🐀 Socratouille is awakening...")
    print("🧀 Loading philosophical cheese database...")
    print(f"🤖 LLM Mode: {'ENABLED' if USE_LLM else 'DISABLED (using pattern matching)'}")
    print("🏛️ Server starting on http://localhost:5000")
    app.run(debug=True, port=5000, host='0.0.0.0')
