"""Interface."""
import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler

from solver import solve


st.title("AlphaDenti")
st.subheader("An AI-powered problem solver for Micro with Calc.")


question = st.text_input("Problem here...")
button = st.button("Solve")

if question and button:
    response = solve(question, st.container())
