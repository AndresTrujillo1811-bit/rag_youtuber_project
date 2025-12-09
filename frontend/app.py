import streamlit as st
import requests
from dotenv import load_dotenv
import os


load_dotenv()
BASE_URL = f"https://ragtuber.azurewebsites.net"

def main_layout():
    st.markdown("# RAGtuber")
    st.markdown("A expert youtuber who knows a lot of Data Engineering!")
    text_input = st.text_input(label="Ask me a question or send a message", key="user_input") # Makes the user to be able to ask a question or explain about 
    
    if st.button("Send") and text_input.strip() != "":
        response = requests.post(f"{BASE_URL}/rag/query", json={"prompt": text_input})
        json_data = response.json()
        st.markdown("## Question/Message:")
        st.markdown(text_input)
        st.markdown("## Answer:")
        st.markdown(json_data["answer"])
        
               
if __name__ == '__main__':
    main_layout()        