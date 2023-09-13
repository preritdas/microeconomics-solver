"""Agent solver."""
from langchain.chat_models import ChatOpenAI
from langchain.agents import ZeroShotAgent
from langchain.agents import AgentExecutor
from langchain.callbacks import StreamlitCallbackHandler

from solver.prompts import PREFIX, FORMAT_INSTRUCTIONS, SUFFIX
from solver.tools import TOOLKIT
from solver.interpreter import flush_interpreter_files
from keys import KEYS


llm = ChatOpenAI(model="gpt-4", openai_api_key=KEYS.OpenAI.api_key)
agent = ZeroShotAgent.from_llm_and_tools(
    prefix=PREFIX,
    format_instructions=FORMAT_INSTRUCTIONS,
    suffix=SUFFIX,
    llm=llm,
    tools=TOOLKIT
)
executor = AgentExecutor(
    agent=agent,
    tools=TOOLKIT,
    max_iterations=10,
    verbose=True
)


def solve(question: str, container = None) -> str:
    """Solve the question."""
    # Clear out old interpreter files
    flush_interpreter_files()

    if container:
        return executor.run(question, callbacks=[StreamlitCallbackHandler(container)])

    return executor.run(question)
