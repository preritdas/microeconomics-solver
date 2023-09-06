"""Tools for the solver agent."""
from langchain.tools import Tool
from langchain.utilities import WolframAlphaAPIWrapper

from keys import KEYS


TOOLKIT = [
    Tool(
        name="Wolfram Alpha",
        func=WolframAlphaAPIWrapper(wolfram_alpha_appid=KEYS.WolframAlpha.app_id).run,
        description=(
            "Useful for when you need to do math or anything quantitative/computational. "
            'Input should ideally be math expressions, ex. "8^3", but can also be '
            "natural language if a math expression is not possible."
        ),
    )
]
