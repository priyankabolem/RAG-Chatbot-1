import streamlit as st
import os
from main import run_chatbot  # Make sure this imports successfully

st.set_page_config(page_title="NWMSU RAG Chatbot")
st.title("🎓 NWMSU Q&A Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Ask a question about NWMSU:")
if st.button("Ask") and user_input:
    try:
        st.session_state.history.append({"user": user_input})
        response = run_chatbot(user_input)
        st.session_state.history.append({"bot": response})
    except Exception as e:
        st.error(f"Something went wrong: {e}")

for msg in st.session_state.history:
    role = "🧑 You" if "user" in msg else "🤖 Bot"
    st.write(f"**{role}:** {msg.get('user') or msg.get('bot')}")
