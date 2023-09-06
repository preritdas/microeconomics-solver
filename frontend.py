"""Interface."""
import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler

from solver import solve


st.title("AlphaDenti")
st.subheader("An AI-powered problem solver for Micro with Calc.")


if (question := st.text_input("Problem here...")) and (button := st.button("Solve")):
    response = solve(question, st.container())
