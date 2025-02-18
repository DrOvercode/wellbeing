import streamlit as st
import requests
import json

url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}

st.title("Wellbeing Chatbot")

user_input = st.text_input("How can I help you? : ")

if st.button("Send"):
    data = {"model": "ALIENTELLIGENCE/psychologist", "prompt": user_input, "stream": False}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        st.write("Chatbot : ", actual_response)
    else:
        st.write("Error:", response.status_code, response.text)