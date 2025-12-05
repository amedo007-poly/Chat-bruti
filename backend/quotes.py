"""Citations et actions de Socratouille - version pote"""

import random

PHILOSOPHERS = [
    "Camemberto",
    "Jean-Paul Sartrat",
    "Aristotail",
    "Briecrates",
    "Platon le Rat",
    "Nietzsche-fromage",
]

QUOTES = [
    "Je pense, donc je grignote.",
    "Le fromage c'est la vie, gros.",
    "La sagesse c'est savoir qu'on sait rien.",
    "L'existence précède le Camembert.",
    "Le Brie ou ne pas Brie, telle est la question.",
]

CHEESE_FACTS = [
    "Y'a plus de 1800 fromages. J'en connais genre... 5. 🧀",
    "La lune c'est PAS du fromage. J'ai vérifié, très déçu.",
    "Le Roquefort ça pue mais c'est trop bon, un peu comme la philo.",
    "Les trous du Gruyère ? C'est les questions sans réponses, gros.",
]

DRAMATIC_ACTIONS = [
    "*gratte sa moustache*",
    "*grignote un bout de Brie*",
    "*réfléchit intensément*",
    "*fait le malin*",
    "*se cure les dents*",
    "*baille*",
    "*s'étire*",
    "*renifle l'air*",
    "*hoche la tête*",
    "*fait une petite danse*",
]

def get_random_quote():
    philosopher = random.choice(PHILOSOPHERS)
    quote = random.choice(QUOTES)
    return f'{philosopher} disait : "{quote}"'

def get_random_action():
    return random.choice(DRAMATIC_ACTIONS)

def get_cheese_fact():
    return random.choice(CHEESE_FACTS)
