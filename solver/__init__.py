"""Agent solver."""
from langchain.chat_models import ChatOpenAI
from langchain.agents import ZeroShotAgent
from langchain.agents import AgentExecutor

from keys import KEYS


llm = ChatOpenAI(openai_api_key=KEYS.OpenAI.api_key)