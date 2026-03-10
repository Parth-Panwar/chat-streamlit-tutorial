import streamlit as st
from groq import Groq
from functions import get_secret, reset_chat, language_selector

# Load Groq API key
api_key = get_secret("GROQ_API_KEY")
client = Groq(api_key=api_key)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "language" not in st.session_state:
    st.session_state.language = "English"

if not st.session_state.chat_history:
    st.session_state.chat_history.append(
        {"role": "assistant", "content": "Hi! How can I help you?"}
    )

# Sidebar controls
temperature = st.sidebar.slider(
    label="Select the temperature",
    min_value=0.0,
    max_value=2.0,
    value=1.0
)

language = language_selector()

if st.sidebar.button("Apply Language"):
    st.session_state.language = language
    reset_chat()

if st.sidebar.button("Reset chat"):
    reset_chat()

# Display existing chat messages
for message in st.session_state.chat_history:
    st.chat_message(message["role"]).write(message["content"])

# Take user input
user_message = st.chat_input("Type your message...")

if user_message:
    st.chat_message("user").write(user_message)
    st.session_state.chat_history.append({"role": "user", "content": user_message})

    system_prompt = f"""
    You are a friendly programming tutor.
    Always explain concepts in a simple and clear way, using examples when possible.
    If the user asks something unrelated to programming, politely bring the conversation back to programming topics.
    Always respond in {st.session_state.language} If the language is Haryanvi, use authentic Haryanvi dialect and vocabulary, not just Hindi..
    """
    messages = [{"role": "system", "content": system_prompt}] + st.session_state.chat_history

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=temperature,
        max_tokens=1000
    )

    assistant_reply = response.choices[0].message.content
    st.chat_message("assistant").write(assistant_reply)
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_reply})