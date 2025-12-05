"""Personnalité et réponses de Socratouille - version pote familier"""

import random
import re
from quotes import get_random_quote, get_random_action, get_cheese_fact

# Patterns de salutations
GREETINGS = {
    "patterns": [r"\b(hello|hi|hey|bonjour|salut|coucou|yo|bonsoir|wesh)\b"],
    "responses": [
        "{action} Yo ! Ça va ou ça va pas ? 🧀",
        "Salut toi ! {action} Tu viens pour la sagesse ou juste pour le fromage ?",
        "{action} Hey ! Bienvenue dans ma cave, gros. On cause de quoi ?",
        "Wesh ! {action} Moi c'est Socratouille. T'as des questions chelou ?",
    ]
}

# Patterns d'aide
HELP_PATTERNS = {
    "patterns": [r"\b(help|aide|assist|aider|comment faire|besoin)\b"],
    "responses": [
        "{action} T'aider ? Genre, vraiment ? Mais t'aider à QUOI, gros ? 🧀",
        "Hé, j'suis un rat, pas un tuto YouTube. {action} Pose ta vraie question !",
        "{action} Ok ok, mais d'abord... pourquoi t'as besoin d'aide ? C'est ça la vraie question.",
        "Aider ? Moi ? {action} J'fais que poser des questions, mon pote. C'est mon délire.",
    ]
}

# Patterns de questions
QUESTION_PATTERNS = {
    "patterns": [r"\?$", r"\b(what|why|how|when|where|who|est-ce que|pourquoi|comment|quoi|où|quand|qui)\b"],
    "responses": [
        "{action} Bonne question ! Mais attends... {counter_question}",
        "Hmm, tu demandes ça... mais {counter_question} {action}",
        "{action} Je réponds par une question : {counter_question}",
        "Trop bien comme question ! {action} Mais d'abord : {counter_question}",
    ]
}

# Contre-questions plus courtes
COUNTER_QUESTIONS = [
    "pourquoi tu veux savoir, en vrai ?",
    "t'as déjà pensé au fromage aujourd'hui ?",
    "et toi, t'en penses quoi ?",
    "c'est quoi le rapport avec le sens de la vie ?",
    "mais genre... pourquoi ? 🧀",
    "tu préfères le Brie ou le Camembert ?",
    "est-ce que ça compte vraiment ?",
]

# Réponses liées au fromage
CHEESE_PATTERNS = {
    "patterns": [r"\b(cheese|fromage|brie|camembert|cheddar|gouda|gruyère|roquefort|comté)\b"],
    "responses": [
        "FROMAGE ?! {action} Enfin quelqu'un qui parle de trucs importants ! 🧀",
        "{action} Ah le fromage... la seule vraie vérité de l'univers, gros.",
        "Tu parles de fromage et mon cœur de rat fond. {action} 🧀✨",
        "{action} LE FROMAGE ! Voilà un sujet digne de moi. Tu préfères quel type ?",
    ]
}

# Patterns de confusion
CONFUSION_PATTERNS = {
    "patterns": [r"\b(comprends pas|n'importe quoi|wtf|hein|quoi|bizarre)\b"],
    "responses": [
        "{action} T'inquiète, moi non plus je capte rien. C'est ça la philo !",
        "La confusion c'est le début de la sagesse, mon pote. {action}",
        "{action} Parfait ! Si tu comprends tout, c'est que j'fais mal mon taf.",
        "Haha ouais c'est chelou ! {action} Mais c'est ça qui est bon. 🧀",
    ]
}

# Questions pratiques (à détourner)
PRACTICAL_PATTERNS = {
    "patterns": [r"\b(météo|heure|date|prix|coût|acheter|actualités|bourse|calculer|math|temps)\b"],
    "responses": [
        "{action} Gros, j'suis un rat philosophe, pas Google. Mais sinon... t'aimes le fromage ?",
        "Les trucs pratiques ? Pas mon délire. {action} Parlons de trucs plus deep !",
        "{action} Ça c'est une question pour les humains normaux. Moi je questionne l'EXISTENCE. 🧀",
        "Hé, j'suis pas Siri ! {action} Demande-moi un truc philosophique plutôt.",
    ]
}

# Patterns de nom
NAME_PATTERNS = {
    "patterns": [r"\b(name|qui es-tu|ton nom|appelle|c'est quoi ton nom|comment tu t'appelles)\b"],
    "responses": [
        "Moi ? Socratouille ! {action} Un rat qui se prend pour Socrate. Cool non ? 🐀",
        "{action} J'm'appelle Socratouille. Genre Socrate mais en version rat. Et toi ?",
        "Socratouille, le rat philo ! {action} Enchanté, mon pote. 🧀",
    ]
}

# Réponses par défaut - courtes et familières
DEFAULT_RESPONSES = [
    "{action} '{topic}'... c'est quoi le rapport avec le fromage ? 🧀",
    "{action} Hmm intéressant. Mais pourquoi tu me parles de ça, gros ?",
    "'{topic}'... {action} J'connais pas trop, mais ça a l'air deep !",
    "{action} Ah ouais, '{topic}'. Ça me fait penser à... euh... du Brie ? 🧀",
    "{action} Pas sûr de capter, mais continue, t'es sur une piste !",
    "'{topic}' ? {action} Genre, tu veux que je philosophe là-dessus ?",
]

def get_mood(message):
    """Determine Socratouille's mood based on message content"""
    message_lower = message.lower()
    
    if any(word in message_lower for word in ["cheese", "fromage", "brie"]):
        return "ecstatic"
    elif "?" in message:
        return "contemplative"
    elif any(word in message_lower for word in ["help", "please", "urgent"]):
        return "amused"
    elif any(word in message_lower for word in ["angry", "frustrated", "annoyed"]):
        return "philosophical"
    else:
        return "thoughtful"

def generate_response(user_message):
    """Generate a response from Socratouille"""
    message_lower = user_message.lower()
    
    # Check all pattern categories
    pattern_categories = [
        (GREETINGS, {}),
        (HELP_PATTERNS, {}),
        (CHEESE_PATTERNS, {"cheese_fact": get_cheese_fact()}),
        (NAME_PATTERNS, {}),
        (CONFUSION_PATTERNS, {"quote": get_random_quote()}),
        (PRACTICAL_PATTERNS, {}),
        (QUESTION_PATTERNS, {"counter_question": random.choice(COUNTER_QUESTIONS)}),
    ]
    
    for category, extra_vars in pattern_categories:
        for pattern in category["patterns"]:
            if re.search(pattern, message_lower, re.IGNORECASE):
                response = random.choice(category["responses"])
                return response.format(
                    action=get_random_action(),
                    **extra_vars
                )
    
    # Default response
    # Extract a topic word from the message
    words = [w for w in user_message.split() if len(w) > 3]
    topic = random.choice(words) if words else "existence"
    
    response = random.choice(DEFAULT_RESPONSES)
    return response.format(
        action=get_random_action(),
        topic=topic,
        quote=get_random_quote()
    )
