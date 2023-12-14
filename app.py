import os
from apiKey import apiKey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

os.environ['OPENAI_API_KEY'] = apiKey

# UI
st.title('🦜️🔗 LangChain')
prompt = st.text_input('Inserta tu prompt aquí')


# Prompt templates
title_template = PromptTemplate(
    input_variables=['topic'],
    template='write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables=['title'],
    template='write me a youtube video script based on this title TITLE: {title}'
)



#Llms
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True)
sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain], verbose=True)


#show stuff to the screen if theres a prompt
if prompt:
    response = sequential_chain.run(prompt)
    st.write(response)