import streamlit as st
import requests

# FastAPI endpoint
FASTAPI_ENDPOINT = "http://127.0.0.1:8000/chat"

st.title("AI-Powered Chatbot Platform")

user_input = st.text_input("Ask me a question:")
if st.button("Send"):
    if user_input:
        response = requests.post(
            FASTAPI_ENDPOINT,
            json={"user_input": user_input}
        )
        if response.status_code == 200:
            st.write(f"AI Response: {response.json()['response']}")
        else:
            st.error("Error in backend processing")
    else:
        st.error("Please enter a question")
