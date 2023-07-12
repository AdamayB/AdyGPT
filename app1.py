from langchain.llms import GPT4All
import streamlit as st
import gradio as gr
# Instantiate the model. Callbacks support token-wise streaming
model = GPT4All(model="C:/Users/adama/gpt4all/ggml-vicuna-7b-1.1-q4_2.bin")
#Site interface
title='🦜️🔗GPT using GPT4ALL '
description='This is an open source project. Created by Adamay Bhardwaj'
#prompt=st.text_input("Your prompt goes here:")
#Generate the story
def generate(prompt):
    if prompt:
        #Pass prompt to llm chain
        response = model(prompt)
        return response
#theme = gr.themes.Soft(
    #primary_hue="cyan",
    #neutral_hue="slate",
#)
theme='HaleyCH/HaleyCH_Theme'
gr.Interface(fn=generate, inputs=["text"], outputs=["text"],
             # Pass through title and description
             title=title, description=description,
             # Set theme and launch parameters
             theme=theme).launch(server_port=8080, share=True)
