import React, { useState, useEffect, useRef } from 'react';
import './styles/Chat.css';
import soundPlayer from './hooks/useSound';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

// Typing indicator phrases
const TYPING_PHRASES = [
  "Philosophe en action...",
  "Consulte le fromage...",
  "Médite sur l'existence...",
  "Caresse ses moustaches...",
  "Canalise Socrate...",
  "Questionne la réalité...",
  "Cherche la sagesse...",
  "Contemple le Brie...",
];

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [typingPhrase, setTypingPhrase] = useState(TYPING_PHRASES[0]);
  const [mood, setMood] = useState('thoughtful');
  const [cheeseCount, setCheeseCount] = useState(0);
  const [soundEnabled, setSoundEnabled] = useState(true);
  const messagesEndRef = useRef(null);

  // Count cheese mentions in text
  const countCheese = (text) => {
    const cheeseWords = /fromage|cheese|brie|camembert|gruyère|roquefort|comté|🧀/gi;
    return (text.match(cheeseWords) || []).length;
  };

  // Scroll to bottom when messages update
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isTyping]);

  // Get intro message on load
  useEffect(() => {
    const getIntro = async () => {
      try {
        const response = await fetch(`${API_URL}/api/intro`);
        const data = await response.json();
        setMessages([{ type: 'rat', content: data.message }]);
        setMood(data.mood);
        setCheeseCount(countCheese(data.message));
      } catch (error) {
        // Fallback intro if backend not available
        const fallbackMsg = "*sort la tête d'un Camembert* Yo ! Moi c'est Socratouille, le rat qui pose des questions chelou. Tu veux parler de quoi ? 🐀🧀";
        setMessages([{ type: 'rat', content: fallbackMsg }]);
        setCheeseCount(countCheese(fallbackMsg));
      }
    };
    getIntro();
  }, []);

  // Update typing phrase randomly + play typing sound
  useEffect(() => {
    if (isTyping) {
      const interval = setInterval(() => {
        setTypingPhrase(TYPING_PHRASES[Math.floor(Math.random() * TYPING_PHRASES.length)]);
        soundPlayer.playTyping();
      }, 1500);
      return () => clearInterval(interval);
    }
  }, [isTyping]);

  // Toggle sound
  const toggleSound = () => {
    const enabled = soundPlayer.toggle();
    setSoundEnabled(enabled);
  };

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = input.trim();
    setInput('');

    // Play send sound
    soundPlayer.playSend();

    // Add user message
    setMessages(prev => [...prev, { type: 'user', content: userMessage }]);

    // Show typing indicator
    setIsTyping(true);

    try {
      // Random delay to simulate "thinking" (0.5 - 2 seconds)
      await new Promise(resolve => setTimeout(resolve, 500 + Math.random() * 1500));

      const response = await fetch(`${API_URL}/api/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMessage }),
      });

      const data = await response.json();

      // Update cheese counter and play cheese sound if cheese mentioned
      const newCheeseCount = countCheese(data.response) + countCheese(userMessage);
      if (newCheeseCount > 0) {
        soundPlayer.playCheese();
      }
      setCheeseCount(prev => prev + newCheeseCount);

      // Play receive sound
      soundPlayer.playReceive();

      setMessages(prev => [...prev, {
        type: 'rat',
        content: data.response,
        cheeseMode: data.mood === 'ecstatic'
      }]);
      setMood(data.mood);
    } catch (error) {
      // Fallback response if backend unavailable
      const fallbackResponses = [
        "*gratte sa moustache* Oups, j'ai perdu le wifi. Réessaie gros ! 🧀",
        "*regarde autour* Hé, le serveur fait une sieste. Deux sec'... 🐀",
        "*baille* Bug technique, mon pote. Clique encore ? ✨",
      ];
      setMessages(prev => [...prev, {
        type: 'rat',
        content: fallbackResponses[Math.floor(Math.random() * fallbackResponses.length)]
      }]);
    }

    setIsTyping(false);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const getMoodEmoji = () => {
    const moods = {
      'thoughtful': '🤔',
      'ecstatic': '🧀',
      'contemplative': '💭',
      'amused': '😏',
      'philosophical': '🏛️',
      'welcoming': '👋',
      'enlightened': '✨',
      'confused': '😵',
      'deep': '🌀'
    };
    return moods[mood] || '🐀';
  };

  const getMoodText = () => {
    const moodTexts = {
      'thoughtful': 'Pensif',
      'ecstatic': 'En extase',
      'contemplative': 'Contemplatif',
      'amused': 'Amusé',
      'philosophical': 'Profond (il croit)',
      'welcoming': 'Accueillant',
      'enlightened': 'Illuminé',
      'confused': 'Confus',
      'deep': 'Très deep'
    };
    return moodTexts[mood] || 'Perdu';
  };

  // Random rat thoughts that appear sometimes
  const getRandomThought = () => {
    const thoughts = [
      "pourquoi les murs ont des coins...",
      "est-ce que les miettes ont des rêves...",
      "si je suis dans un mur, où est le mur...",
      "les bipèdes sont chelous quand même...",
      "j'ai oublié ce que je pensais...",
      "le fromage c'est juste du lait qui a réfléchi...",
      "pourquoi 'pourquoi'...",
      "les tunnels mènent où au fond...",
    ];
    return thoughts[Math.floor(Math.random() * thoughts.length)];
  };

  return (
    <div className="chat-container">
      {/* Header */}
      <header className="chat-header">
        <div className="header-left">
          <div className="header-avatar" onClick={() => soundPlayer.playSqueak()} title="Clic pour un squeak!">
            <div className="thought-bubble">
              <span>💭 {getRandomThought()}</span>
            </div>
            <span className="avatar-emoji">🐀</span>
            <span className="avatar-glow"></span>
          </div>
          <div className="header-info">
            <h1>SOCRATOUILLE</h1>
            <p className="tagline">le rat qui répond à côté depuis 2025</p>
          </div>
        </div>
        <div className="header-right">
          <button 
            className={`sound-toggle ${soundEnabled ? 'enabled' : 'disabled'}`}
            onClick={toggleSound}
            title={soundEnabled ? 'Désactiver le son' : 'Activer le son'}
          >
            {soundEnabled ? '🔊' : '🔇'}
          </button>
          <div className="cheese-counter" title="Questions évitées">
            <span className="cheese-icon">❓</span>
            <span className="cheese-count">{cheeseCount}</span>
          </div>
          <div className="mood-indicator">
            <span className="mood-emoji">{getMoodEmoji()}</span>
            <span className="mood-text">{getMoodText()}</span>
          </div>
        </div>
      </header>

      {/* Messages */}
      <div className="messages-container">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`message ${msg.type} ${msg.cheeseMode ? 'cheese-mode' : ''}`}
          >
            <span className="message-avatar">
              {msg.type === 'rat' ? '🐀' : '👤'}
            </span>
            <div className="message-content">
              {msg.content}
            </div>
          </div>
        ))}

        {/* Typing Indicator */}
        {isTyping && (
          <div className="typing-indicator">
            <span className="typing-avatar">🐀</span>
            <div className="typing-dots">
              <span></span>
              <span></span>
              <span></span>
            </div>
            <span className="typing-text">{typingPhrase}</span>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="input-container">
        <div className="input-wrapper">
          <input
            type="text"
            className="chat-input"
            placeholder="Pose une question à Socratouille..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            disabled={isTyping}
          />
          <button
            className="send-button"
            onClick={sendMessage}
            disabled={isTyping || !input.trim()}
          >
            Envoyer 🧀
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
