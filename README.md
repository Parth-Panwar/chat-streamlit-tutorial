# 💬 Chat Streamlit Tutorial

A conversational AI chatbot built with **Streamlit** and **Groq**, powered by the `llama-3.3-70b-versatile` model. The bot acts as a friendly programming tutor, helping users learn coding concepts with clear explanations and examples.

---

## 🚀 Features

- Real-time chat interface using Streamlit
- Persistent chat history within a session
- **Reset chat** button to clear conversation history
- **Temperature slider** to control response creativity
- Powered by Groq's ultra-fast LLM inference
- Programming tutor persona with focused responses
- Secure API key management via `.env` or Streamlit Cloud secrets

---

## 🛠️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/chat-streamlit-tutorial.git
cd chat-streamlit-tutorial
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Groq API key

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

> Get your API key from [console.groq.com](https://console.groq.com)

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`.

---

## 📁 Project Structure

```
chat-streamlit-tutorial/
├── app.py              # Main Streamlit app
├── functions.py        # Helper functions (get_secret, reset_chat)
├── .env                # API key (not committed to git)
├── .gitignore          # Excludes .env and other sensitive files
├── requirements.txt    # Python dependencies
└── README.md
```

---

## 🎛️ Sidebar Controls

| Control | Description |
|---|---|
| Temperature Slider | Controls response randomness (0.0 = focused, 2.0 = creative) |
| Reset Chat | Clears the current conversation history |

---

## 📦 Requirements

```
streamlit
groq
python-dotenv
```

---

## ☁️ Deploying to Streamlit Cloud

1. Push your code to GitHub (make sure `.env` is in `.gitignore`)
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. In the app settings, add your secret:
   - **Key:** `GROQ_API_KEY`
   - **Value:** your Groq API key

---

## ⚠️ Important Notes

- **Never commit your `.env` file or paste API keys in public chats/code** — keys can be auto-revoked if exposed
- Always generate a new key from the Groq console if your key stops working
- The app uses `override=True` in `load_dotenv()` to ensure the latest key is always loaded

---

## 📄 License

MIT