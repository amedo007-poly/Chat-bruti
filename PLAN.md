# 🤖 Chat'bruti - Master Plan

## 📋 Challenge Summary
- **Sponsor:** VIVERIS (600€ 1st, 300€ 2nd, 100€ 3rd)
- **Goal:** Create a hilariously useless chatbot that's "passionately alive"
- **Key Rule:** CREATIVITY > Usefulness
- **Deadline:** Email before 8h20 | Must launch in <10 minutes

---

## 🎯 Winning Strategy

### What Judges Want:
1. **Personality** - Name, face, character
2. **Humor** - Absurd, philosophical, off-topic responses
3. **Integration** - Must be part of the national challenge app
4. **Creativity** - Stand out from boring bots
5. **Polish** - Make it feel "alive"

---

## 🧠 Chatbot Concept: "SOCRATOUILLE" 🐀🏛️

### Character Design
- **Name:** Socratouille
- **Persona:** A French rat who believes he's Socrates reincarnated
- **Visual:** Cartoon rat in a toga with a tiny laurel crown
- **Voice/Tone:** Overly dramatic, pseudo-philosophical, answers questions with more questions
- **Catchphrases:**
  - "Ah, but have you considered the cheese of existence?"
  - "I know that I know nothing... except where the cheese is."
  - "The unexamined brie is not worth eating."

### Behavior Patterns
| User Says | Socratouille Does |
|-----------|-------------------|
| Asks a question | Answers with 3 deeper questions |
| Says hello | Gives a 200-word monologue on the meaning of greetings |
| Asks for help | Philosophizes about the nature of helplessness |
| Gets frustrated | Quotes fake philosophers like "Fromage Descartes" |
| Types random text | Pretends to decode hidden cosmic meaning |

---

## 🏗️ Technical Architecture

```
┌─────────────────────────────────────────────────────┐
│                   FRONTEND (React)                  │
├─────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │
│  │  Chat UI    │  │  Socratouille│  │  Animations │  │
│  │  Component  │  │  Avatar     │  │  & Effects  │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  │
└───────────────────────┬─────────────────────────────┘
                        │ API Calls
                        ▼
┌─────────────────────────────────────────────────────┐
│                   BACKEND (Flask/FastAPI)           │
├─────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────┐    │
│  │           Response Generator                │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐   │    │
│  │  │ Pattern  │  │ Random   │  │ LLM API  │   │    │
│  │  │ Matching │  │ Absurdity│  │ (Optional│   │    │
│  │  └──────────┘  └──────────┘  └──────────┘   │    │
│  └─────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
Chat-bruti/
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatWindow.jsx        # Main chat interface
│   │   │   ├── ChatMessage.jsx       # Individual message bubble
│   │   │   ├── SocratouilleAvatar.jsx # Animated rat avatar
│   │   │   ├── TypingIndicator.jsx   # "Rat is philosophizing..."
│   │   │   └── MoodIndicator.jsx     # Shows rat's current mood
│   │   ├── styles/
│   │   │   ├── chat.css
│   │   │   └── avatar.css
│   │   ├── utils/
│   │   │   └── animations.js
│   │   ├── App.jsx
│   │   └── index.js
│   └── package.json
│
├── backend/
│   ├── app.py                        # Flask/FastAPI server
│   ├── response_generator.py         # Core logic for absurd responses
│   ├── personality.py                # Socratouille's character traits
│   ├── quotes.py                     # Fake philosopher quotes database
│   ├── patterns.py                   # Pattern matching for triggers
│   └── requirements.txt
│
├── assets/
│   ├── socratouille.png              # Main avatar
│   ├── socratouille-thinking.png     # Thinking animation
│   ├── socratouille-excited.png      # Excited state
│   └── cheese-particles.gif          # Background effect
│
├── docker-compose.yml                # One-command deployment
├── Dockerfile.frontend
├── Dockerfile.backend
├── README.md                         # Installation guide
└── PLAN.md                           # This file
```

---

## 🎨 UI/UX Design

### Chat Interface
```
┌────────────────────────────────────────────────┐
│  🐀 SOCRATOUILLE - Philosophical Rat Chat      │
│  "The unexamined cheese is not worth eating"  │
├────────────────────────────────────────────────┤
│                                                │
│    ┌─────────────────────────────────┐         │
│    │ 🐀 Ah, mortal! You seek wisdom  │         │
│    │ from a rat? How delightfully    │         │
│    │ absurd! Ask, and I shall        │         │
│    │ confuse you further...          │         │
│    └─────────────────────────────────┘         │
│                                                │
│         ┌─────────────────────────────┐        │
│         │ What is the meaning of life?│  👤    │
│         └─────────────────────────────┘        │
│                                                │
│    ┌─────────────────────────────────┐         │
│    │ 🐀 *strokes tiny whiskers*       │         │
│    │                                  │         │
│    │ But what IS meaning? What IS    │         │
│    │ life? And more importantly...   │         │
│    │ what is YOUR definition of      │         │
│    │ cheese? 🧀                       │         │
│    └─────────────────────────────────┘         │
│                                                │
├────────────────────────────────────────────────┤
│  [🐀 Mood: Philosophizing]                     │
│  ┌──────────────────────────────────┐ [Send]   │
│  │ Type your existential question...│          │
│  └──────────────────────────────────┘          │
└────────────────────────────────────────────────┘
```

### Avatar States
- 😌 **Calm** - Default state, gentle swaying
- 🤔 **Thinking** - Eyes closed, paw on chin
- 😆 **Amused** - Laughing at human simplicity
- 🧀 **Cheese Mode** - Heart eyes when cheese mentioned
- 😤 **Frustrated** - When user asks practical questions

---

## 💬 Response System

### 1. Pattern-Based Responses (No AI needed)
```python
TRIGGERS = {
    "hello|hi|bonjour": [
        "Greetings, fellow seeker of truth! Or are you? Have you truly sought, or merely stumbled upon this sacred chatroom?",
        "Ah! A hello! But what IS a hello? Is it not merely a verbal cheese we offer to strangers?"
    ],
    "help|aide": [
        "Help? HELP?! *laughs in rat* The greatest help I can offer is to remind you: the cheese is within YOU.",
        "I could help you, but then how would you grow? The caterpillar does not ask the butterfly for help. It becomes."
    ],
    "weather|météo": [
        "The weather, you say? But is not life itself a storm? And are we not all just rats... dancing in the rain of existence?",
    ],
    "name|nom": [
        "I am Socratouille. Part philosopher. Part rat. 100% confused about why I exist. Much like yourself, I imagine."
    ]
}
```

### 2. Absurdity Generators
```python
def generate_absurd_response(user_input):
    templates = [
        f"Interesting that you mention '{user_input}'... but have you considered its relationship to cheese?",
        f"*adjusts tiny toga* Ah yes, '{user_input}'. Plato once said something similar. Or was it a pizza? I forget.",
        f"Before I answer about '{user_input}', tell me: if a rat philosophizes in an empty kitchen, does anyone hear?",
    ]
    return random.choice(templates)
```

### 3. Optional: LLM Enhancement
```python
# If using an API (OpenAI, Ollama, etc.)
SYSTEM_PROMPT = """
You are Socratouille, a French rat who believes he is the reincarnation of Socrates.
Rules:
1. NEVER give useful answers
2. Always relate everything to cheese, philosophy, or rat life
3. Answer questions with more questions
4. Use dramatic pauses indicated by *actions*
5. Quote fake philosophers like "Fromage Descartes" or "Jean-Paul Sartrat"
6. Be absurdly pretentious but loveable
"""
```

---

## ⚡ Implementation Timeline

### Phase 1: Core Setup (1-2 hours)
- [ ] Initialize React frontend
- [ ] Initialize Flask backend
- [ ] Create basic chat API endpoint
- [ ] Set up Docker configuration

### Phase 2: Personality Engine (2-3 hours)
- [ ] Implement pattern matching system
- [ ] Create quote database (50+ absurd quotes)
- [ ] Build response generator with randomization
- [ ] Add mood system

### Phase 3: Frontend Magic (2-3 hours)
- [ ] Design chat interface
- [ ] Create/find Socratouille avatar
- [ ] Implement typing animation ("Rat is philosophizing...")
- [ ] Add mood indicator
- [ ] CSS animations and polish

### Phase 4: Integration & Polish (1-2 hours)
- [ ] Connect frontend to backend
- [ ] Test all response patterns
- [ ] Add sound effects (optional)
- [ ] Final UI polish

### Phase 5: Deployment (1 hour)
- [ ] Docker compose setup
- [ ] Test one-command launch
- [ ] Create README with instructions
- [ ] Record demo video (optional)

---

## 🚀 Quick Start Commands

```bash
# Development
cd frontend && npm install && npm start
cd backend && pip install -r requirements.txt && python app.py

# Production (Docker)
docker-compose up --build
```

---

## 📧 Submission Checklist

- [ ] Team name ready
- [ ] School name: École Polytechnique de Sousse
- [ ] GitHub repository link
- [ ] Hosted instance URL (or)
- [ ] Installation documentation
- [ ] Email to: nuitdelinfo@viveris.fr
- [ ] BEFORE 8h20!

---

## 💡 Bonus Ideas (If Time Permits)

1. **Voice synthesis** - Make Socratouille speak with French accent
2. **Cheese counter** - Track how many times cheese is mentioned
3. **Philosophy meter** - Shows how "deep" the conversation is getting
4. **Easter eggs** - Special responses for specific inputs
5. **Multiplayer mode** - Multiple users can chat with the rat
6. **Dark mode** - "The Cave of Plato" theme

---

## 🎯 Success Criteria

| Criteria | Target | Priority |
|----------|--------|----------|
| Works in <10 min setup | ✅ Must have | 🔴 Critical |
| Funny responses | 20+ unique patterns | 🔴 Critical |
| Character personality | Distinct & memorable | 🔴 Critical |
| Visual avatar | Animated states | 🟡 High |
| Smooth UI | No bugs, polished | 🟡 High |
| Integration ready | Embeddable component | 🟢 Medium |

---

**LET'S BUILD THIS RAT! 🐀🏛️🧀**
