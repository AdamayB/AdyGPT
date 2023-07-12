from langchain.llms import GPT4All
import streamlit as st

# Instantiate the model. Callbacks support token-wise streaming
model = GPT4All(model="C:/Users/adama/gpt4all/ggml-vicuna-7b-1.1-q4_2.bin")
#Site interface
st.title('🦜️🔗GPT using GPT4ALL ')

prompt=st.text_input("Your prompt goes here:")
#Generate the story

if prompt:
    #Pass prompt to llm chain
    response = model(prompt)
    st.write(response)
