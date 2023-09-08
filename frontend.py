"""Interface."""
import streamlit as st

from pathlib import Path
from solver import solve


st.title("AlphaDenti")
st.subheader("An AI-powered problem solver for Micro with Calc.")


question = st.text_input("Paste the problem here.", value="Who are you?")
button = st.button("Solve")

if question and button:
    response = solve(question, st.container())

    # Display answer
    st.divider()
    st.markdown(response)

    # Check for interpreter files
    for file in Path("interpreter_files").iterdir():
        st.image(str(file.absolute()))
