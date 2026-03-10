import streamlit as st
from groq import Groq
from functions import get_secret

# Load Groq API key
api_key = get_secret("GROQ_API_KEY")
print(f"API key loaded: {repr(api_key)}")  # Debug line
client = Groq(api_key=api_key)  # Use the variable, not a hardcoded key

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if not st.session_state.chat_history:
    st.session_state.chat_history.append(
        {"role": "assistant", "content": "Hi! How can I help you?"}
    )

# Display existing chat messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Take user input
user_message = st.chat_input("Type your message...")

if user_message:
    # Display user message immediately
    st.chat_message("user").write(user_message)
    
    # Append user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_message})
    
    # Optional system prompt
    system_prompt = """
    You are a friendly programming tutor.
    Always explain concepts in a simple and clear way, using examples when possible.
    If the user asks something unrelated to programming, politely bring the conversation back to programming topics.
    """
    messages = [{"role": "system", "content": system_prompt}] + st.session_state.chat_history
    
    # Generate assistant response from Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    
    assistant_reply = response.choices[0].message.content
    
    # Display assistant message
    st.chat_message("assistant").write(assistant_reply)
    
    # Append assistant reply to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_reply})