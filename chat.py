import streamlit as st
import random
import time

st.title("Anema chat")
tab1, tab2 = st.tabs(["Google Bard", "Hugging Face Hub"])

# Object notation
with st.sidebar:
    st.write('*Extra Features*')

    # Create a microphone button
    microphone_button = st.button(label="Microphone")

    # Create an audio button
    audio_button = st.button(label="Audio")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


def generate_response(prompt):
  from bardapi import Bard
  import os
  os.environ['_BARD_API_KEY']= "cgixw-J5jyDplvYpFLQzVdsrSqWsp28lxRy7310QlUtFGjcKMKTs685Q_K4rc3Q7-3urHQ."

  response = Bard().get_answer(prompt)['content']

  print(prompt)
  print(response)
  return response

def hub_response(prompt):
    import requests

    API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    response = query({
        "inputs": {
            "past_user_inputs": prompt,
            "generated_responses": ["It is Die Hard for sure."],
            "text": "Can you explain why ?"
        },
    })

    # Accept user input
if prompt := st.chat_input():

    with tab1:

            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)
                response = generate_response(prompt)

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                assistant_response = response
                # Simulate stream of response with milliseconds delay
                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                    # Add a blinking cursor to simulate typing
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

    with tab2:
            prompt = st.chat_input()

            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)
                response = hub_response(prompt)

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                assistant_response = response
                # Simulate stream of response with milliseconds delay
                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                    # Add a blinking cursor to simulate typing
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
