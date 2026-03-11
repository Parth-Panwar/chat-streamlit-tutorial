import streamlit as st
import os
from dotenv import load_dotenv
import json
from datetime import datetime

def get_secret(key: str) -> str | None:
    try:
        return st.secrets[key]
    except Exception:
        load_dotenv(override=True)
        return os.getenv(key)

def reset_chat():
    st.session_state.chat_history = []

def language_selector():
    if "language" not in st.session_state:
        st.session_state.language = "English"

    options = ["English", "Spanish", "French", "German", "Chinese", "Japanese", "Arabic", "Hindi", "Portuguese", "Italian", "Haryanvi"]
    
    language = st.sidebar.selectbox(
        label="Select Language",
        options=options,
        index=options.index(st.session_state.language)
    )
    return language

def save_chat(chat_history):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"chat_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(chat_history, f, indent=2)
    return filename

def load_chat(uploaded_file):
    data = json.load(uploaded_file)
    return data