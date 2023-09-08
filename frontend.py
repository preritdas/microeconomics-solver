"""Frontend interface for AlphaDenti."""
import streamlit as st
from pathlib import Path
from solver import solve

# Theme and Styling
st.set_page_config(
    page_title="AlphaDenti",
    page_icon=":bulb:" 
)

# Header
st.title(":brain: AlphaDenti")
st.info(
    ":wave: \tHey. I'm an AI designed to help you with Microeconomics with Calculus.\n\n"
    ":book: I have access to the textbook, can do math, create plots, research, and more.\n\n"
    ":teacher: Use me to ask follow-up questions, check your work, or just to learn more.\n\n"
)
st.divider()

# Body
question = st.text_input("Ask a question/paste a problem.", value="What does the textbook say about market equilibrium? Show me visually.")
button = st.button("Solve")

if question and button:
    response = solve(question, st.container())
    st.divider()
    st.markdown(response)

    # Check for interpreter files
    for file in Path("interpreter_files").iterdir():
        st.image(str(file.absolute()))
