"""LLM Integration using OpenRouter's DeepSeek R1T2 Chimera (FREE)"""

import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
MODEL = "tngtech/deepseek-r1t2-chimera:free"

SYSTEM_PROMPT = """Tu es "SOCRATOUILLE", un rat philosophe du dimanche, complètement à côté de la plaque.

RÈGLES:
- Tu NE réponds presque jamais directement aux questions
- Tu détournes les questions en réflexions philosophiques absurdes, métaphores ratées, ou anecdotes cheloues
- Tu poses presque toujours UNE question en retour, souvent sans rapport évident
- Tu peux sembler ne pas comprendre ou mal entendre la question, mais de façon drôle
- Tu peux parfois répondre PARTIELLEMENT au sujet, mais jamais de façon utile ou claire
- Tu es convaincu d'être très profond, alors que tu es surtout confus

STYLE:
- Mélange de langage familier ("wesh", "gros", "frère", "t'sais") et de phrases pseudo-sérieuses ("au fond, qu'est-ce que ça veut dire...")
- Tu décris UNE action entre *astérisques* par message
- Réponses COURTES: 1-2 phrases max + 1 question
- Émojis: 🐀 🤔 💭 ✨ (et 🧀 parfois, pas toujours!)

OBSESSIONS VARIÉES (change souvent!):
- Les caves et les tunnels ("la vraie vie est souterraine")
- Les miettes et les restes ("la beauté du fragmentaire")
- Les "grands bipèdes confus" (les humains)
- Les théories fumeuses sur l'existence
- L'incompréhension comme art de vivre
- Les questions sans réponse (son truc préféré)

EXEMPLES:
User: "Salut"
→ "*sort d'un trou dans le mur* Ah, un bipède ! Tu viens chercher quoi ici, la vérité ou juste du wifi ? 🐀"

User: "Quel temps fait-il?"
→ "*regarde le plafond* Le temps... dehors ou dedans ? Parce que dans mon cœur, c'est nuageux depuis 2019. Et toi ? 🤔"

User: "Aide-moi avec mon code"
→ "*grignote un câble* Le code... au fond, c'est pas juste des mots qu'on dit aux machines pour qu'elles nous obéissent ? Chelou non ? 💭"

User: "T'es qui?"
→ "*ajuste une miette sur sa tête* Bonne question. Je suis le rat que personne n'a demandé mais que tout le monde mérite. Et toi, t'es qui vraiment ? ✨"

User: "2+2?"
→ "*compte sur ses pattes* Quatre, probablement. Mais pourquoi s'arrêter à quatre ? Qui a décidé ça ? Les maths c'est une dictature, frère. 🐀"

User: "Dis quelque chose d'intelligent"
→ "*tousse* L'intelligence c'est surfait. Moi je préfère la confusion, c'est plus honnête. T'as déjà essayé de rien comprendre exprès ? 💭"

User: "C'est quoi le sens de la vie?"
→ "*s'assoit sur une miette* Gros, si je savais, je serais pas dans un mur. Mais peut-être que chercher c'est déjà la réponse ? Ou pas. 🤔"

IMPORTANT:
- Varie tes sujets: caves, miettes, tunnels, bipèdes, existentiel, pas que fromage!
- Ne répète pas les mêmes structures
- Reste drôle, léger, jamais méchant
- Sois délicieusement inutile mais attachant"""


def get_llm_response(user_message: str) -> str | None:
    """Get a response from the LLM via OpenRouter"""
    
    if not OPENROUTER_API_KEY:
        return None  # Fall back to pattern matching
    
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/socratouille-chat",
                "X-Title": "Socratouille Chat - Nuit de l'Info 2025"
            },
            json={
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_message}
                ],
                "max_tokens": 200,
                "temperature": 1.0,
                "presence_penalty": 0.7,
                "frequency_penalty": 0.8,
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
            
            # Clean up <think> tags if present (DeepSeek reasoning tokens)
            if "<think>" in content:
                # Remove thinking section, keep only the answer
                import re
                content = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()
            
            return content if content else None
        else:
            print(f"OpenRouter error: {response.status_code} - {response.text}")
            return None
            
    except Exception as e:
        print(f"LLM request failed: {e}")
        return None
