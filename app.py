import streamlit as st
from backend import ask_gpt, chat_history


st.set_page_config(page_title="Chatbot Groq", page_icon="🤖", layout="wide")

st.title("🤖 Chatbot Groq")
st.markdown("Bienvenue ! Posez vos questions et discutez avec votre assistant AI.")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = chat_history


chat_container = st.container()

with chat_container:
    for i, msg in enumerate(st.session_state.chat_history):
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        elif msg["role"] == "assistant":
            st.chat_message("assistant").write(msg["content"])


if prompt := st.chat_input("Tapez votre message ici..."):
    # Afficher immediatement le message utilisateur
    st.chat_message("user").write(prompt)

    # Obtenir la réponse de l'assistant
    with st.spinner("L'assistant réfléchit..."):
        response = ask_gpt(prompt)

    # Afficher la reponse
    st.chat_message("assistant").write(response)

    # Mettre à jour l'historique de session
    st.session_state.chat_history = chat_history
