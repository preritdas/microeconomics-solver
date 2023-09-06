"""Agent solver."""
from langchain.chat_models import ChatOpenAI
from langchain.agents import ZeroShotAgent
from langchain.agents import AgentExecutor

from solver.prompts import PREFIX, FORMAT_INSTRUCTIONS
from solver.tools import TOOLKIT
from keys import KEYS


llm = ChatOpenAI(openai_api_key=KEYS.OpenAI.api_key)
agent = ZeroShotAgent.from_llm_and_tools(
    prefix=PREFIX,
    format_instructions=FORMAT_INSTRUCTIONS,
    llm=llm,
    tools=TOOLKIT
)
executor = AgentExecutor(
    agent=agent,
    tools=TOOLKIT,
    max_iterations=10,
    verbose=True,
    callbacks=None  # TODO
)


def solve(question: str) -> str:
    """Solve the question."""
    return executor.run(question)
