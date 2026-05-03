import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# You must use VARIABLE NAME, not API key
api_key = os.getenv("GROQ_API_KEY")

# Stop if API key is missing
if not api_key:
    st.error(" GROQ_API_KEY not found in .env file")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

# UI config
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 manohar AI Chatbot")

# System prompt
SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are a helpful, professional AI assistant. Give clear and structured answers."
}

# Session memory
if "messages" not in st.session_state:
    st.session_state.messages = [SYSTEM_PROMPT]

# Display chat history
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=st.session_state.messages
        )
        ai_reply = response.choices[0].message.content

    except Exception as e:
        ai_reply = f" Error: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})

    with st.chat_message("assistant"):
        st.markdown(ai_reply)

# Reset button
if st.button("🔄 Reset Chat"):
    st.session_state.messages = [SYSTEM_PROMPT]
    st.rerun()
