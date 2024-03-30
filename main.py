import streamlit as st
from langchain_helper import get_chain

st.title("PC Factory: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = get_chain()
    response = chain.invoke(question)

    st.header("Answer")
    st.write(response['result'])