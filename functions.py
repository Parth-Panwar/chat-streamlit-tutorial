import streamlit as st
import os
from dotenv import load_dotenv

def get_secret(key: str) -> str | None:
    try:
        return st.secrets[key]  # For Streamlit Cloud
    except Exception:
        load_dotenv(override=True)  # override=True forces reload of .env
        return os.getenv(key)   # For local development