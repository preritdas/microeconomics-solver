"""Agent solver."""
from langchain.chat_models import ChatOpenAI
from langchain.agents import ZeroShotAgent
from langchain.agents import AgentExecutor

from keys import KEYS


llm = ChatOpenAI(openai_api_key=KEYS.OpenAI.api_key)
agent = ZeroShotAgent.from_llm_and_tools(
    llm=llm,
    tools=None
)
executor = AgentExecutor(
    agent=agent,
    tools=None, # YO
    max_iterations=5,
    verbose=True,
    callbacks=None # YO
)


def solve(question: str) -> str:
    """Solve the question."""
    return executor.run(question)
