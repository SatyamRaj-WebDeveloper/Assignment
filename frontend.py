import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO

st.title("🚢 Titanic Dataset Chatbot")

st.write("Ask me anything about the Titanic dataset!")

# User input
question = st.text_input("Enter your question:")

if st.button("Ask"):
    if question:
        response = requests.get(f"http://127.0.0.1:8000/query", params={"question": question})
        data = response.json()

        if "response" in data:
            st.write(data["response"])

        if "image" in data:
            img_data = base64.b64decode(data["image"])
            img = Image.open(BytesIO(img_data))
            st.image(img, caption="Generated Visualization")