import streamlit as st
import requests

api_link = "http://127.0.0.1:8000/rag/query" # Fast API link 


def main_layout():
    st.markdown("# RAGtuber")
    st.markdown("A expert youtuber who knows a lot of Data Engineering!")
    text_input = st.text_input("Ask me a question") # Makes the user to be able to ask a question or explain about 
    
    if st.button("Send") and text_input.strip() != "":
        response = requests.post(api_link, json={"prompt": text_input})
        json_data = response.json()
        st.markdown("## Question:")
        st.markdown(text_input)
        st.markdown("## Answer:")
        st.markdown(json_data["answer"])
        
               
if __name__ == '__main__':
    main_layout()        