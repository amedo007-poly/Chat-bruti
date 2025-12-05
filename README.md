# 🐀 SOCRATOUILLE - Chat'bruti Challenge

> *"ton pote rat qui pose trop de questions"* 🧀

Le chatbot le plus hilarant et inutile de la Nuit de l'Info 2025 !

---

## 🚀 Lancement Rapide (< 5 minutes!)

### Option 1: Docker (Recommandé)
```bash
docker-compose up --build
```
Ouvrir http://localhost:3000

### Option 2: Manuel

**Backend (Terminal 1):**
```bash
cd backend
pip install -r requirements.txt
python app.py
```

**Frontend (Terminal 2):**
```bash
cd frontend
npm install
npm start
```
Ouvrir http://localhost:3000

---

## 🎭 C'est quoi Socratouille ?

Un petit rat parisien qui se prend pour Socrate ! Il:
- ❌ Ne donne JAMAIS de réponses utiles
- ❓ Répond aux questions par des questions
- 🧀 Ramène TOUT au fromage
- 📚 Cite des "philoSOURIphes" inventés (Camemberto, Briecrates, Aristotail...)
- 🗣️ Parle comme un vrai pote français (familier, tutoiement)

---

## ✨ Fonctionnalités

| Feature | Description |
|---------|-------------|
| 🤖 **IA** | Propulsé par LLM (DeepSeek via OpenRouter) |
| 🧀 **Compteur de fromage** | Compte les mentions de fromage ! |
| 🔊 **Effets sonores** | Sons rigolos (squeak, pop, etc.) |
| 🎨 **Design Ratatouille** | Palette chaude inspirée du film |
| 📱 **Responsive** | Fonctionne sur mobile |
| 🐳 **Docker** | Déploiement en une commande |

---

## 🛠️ Stack Technique

- **Frontend:** React 18 + CSS custom
- **Backend:** Flask + Flask-CORS
- **IA:** OpenRouter API (DeepSeek R1T2 Chimera - GRATUIT)
- **Deploy:** Docker Compose

---

## 📁 Structure
```
Chat-bruti/
├── frontend/           # App React
│   ├── src/
│   │   ├── App.jsx     # Composant principal
│   │   ├── styles/     # CSS
│   │   └── hooks/      # Son
├── backend/            # API Flask
│   ├── app.py          # Endpoints
│   ├── llm.py          # Intégration LLM
│   ├── personality.py  # Pattern matching
│   └── quotes.py       # Citations absurdes
├── docker-compose.yml  # Déploiement
└── README.md
```

---

## 🏆 Équipe

- **Développeur:** Ahmed Dinari
- **École:** École Polytechnique de Sousse
- **Challenge:** Chat'bruti by VIVERIS (600€ 1er prix!)

---

## 📧 Soumission
Email: nuitdelinfo@viveris.fr (avant 8h20!)

---

## 🐀 Exemples de Conversations

```
Toi: Salut !
Socratouille: *sort la tête d'un Camembert* Yo ! Ça va ou ça va pas ? 🧀

Toi: Quelle heure il est ?
Socratouille: *regarde un cadran en gruyère* Gros, le temps c'est qu'une illusion. La vraie question: t'as faim ? 🐀

Toi: Tu sers à quoi ?
Socratouille: *gratte sa moustache* Servir ? Genre, vraiment ? Mais la vraie question c'est: toi, tu sers à quoi ? 🧀✨
```

---

Made with 🧀 and existential questions for Nuit de l'Info 2025
