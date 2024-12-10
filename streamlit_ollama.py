import streamlit as st
from langchain_community.llms import Ollama

prompt_input: str = st.text_input('Prompt')
button:bool = st.button("GO")

if button and prompt_input != "":
    llm_model: any =  Ollama(model = "qwen2.5:0.5b")

    response : any = llm_model.invoke(prompt_input)

    st.markdown(response)