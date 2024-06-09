import streamlit as st
import google.generativeai as genai
from google.generativeai import GenerativeModel
import json
from config import GEMINI_API_KEY

# Configure the Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

generation_config = {
    'temperature': 1,
    'top_p': 0.95,
    'top_k': 64,
    'max_output_tokens': 8192,
    'response_mime_type': 'text/plain'
}

safety_settings = [
    {'category': 'HARM_CATEGORY_HARASSMENT', 'threshold': 'BLOCK_MEDIUM_AND_ABOVE'},
    {'category': 'HARM_CATEGORY_HATE_SPEECH', 'threshold': 'BLOCK_MEDIUM_AND_ABOVE'},
    {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'threshold': 'BLOCK_MEDIUM_AND_ABOVE'},
    {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'threshold': 'BLOCK_MEDIUM_AND_ABOVE'}
]

with open('gemini_instructions.md', 'r') as file:
    gemini_instructions = file.read()

llm = GenerativeModel(
    model_name='gemini-1.5-flash-latest',
    generation_config=generation_config,
    safety_settings=safety_settings,
    system_instruction=gemini_instructions
)

# Initialize chat session
if 'chat_session' not in st.session_state:
    st.session_state.chat_session = llm.start_chat(history=[])

def chat():
    st.set_page_config(
        page_title='Gods Eye - Chat',
        page_icon='assets/favicon.png',
        layout='wide',
        initial_sidebar_state='collapsed'
    )
    st.markdown(
        "<h1 style='text-align: center;'>Perspec AI</h1>",
        unsafe_allow_html=True
    )
    st.divider()

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    if prompt := st.chat_input('Ready for a new perspective?'):
        st.chat_message('user').markdown(prompt)
        st.session_state.messages.append({'role': 'user', 'content': prompt})

        # Generate response from Gemini AI
        chat_session = st.session_state.chat_session
        response = chat_session.send_message(prompt)

        # Extract the text content from the response
        if response.candidates:
            assistant_response = response.candidates[0].content.parts[0].text
        else:
            assistant_response = "I'm sorry, but I couldn't generate a response."

        with st.chat_message('assistant'):
            st.markdown(assistant_response)
        st.session_state.messages.append({'role': 'assistant', 'content': assistant_response})

chat()