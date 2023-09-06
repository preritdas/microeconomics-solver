"""Tools for the solver agent."""
from langchain.tools import Tool
from langchain.utilities import WolframAlphaAPIWrapper

from solver.serper_wrapper import GoogleSerperAPIWrapperURL
from solver.internet import WebsiteAnswerer
from keys import KEYS


ANSWERER_JSON_STRING_INPUT_INSTRUCTIONS = (
    'Input must be a JSON string with the keys "source" and "query".'
)


TOOLKIT = [
    Tool(
        name="Wolfram Alpha",
        func=WolframAlphaAPIWrapper(wolfram_alpha_appid=KEYS.WolframAlpha.app_id).run,
        description=(
            "Useful for when you need to do math or anything quantitative/computational. "
            'Input should ideally be math expressions, ex. "8^3", but can also be '
            "natural language if a math expression is not possible."
        )
    ),
    Tool(
        name="Query Textbook",
        func=lambda query: "Unfortunately this tool is not yet available.",
        description=(
            "Useful for when you want to get some clarification or microeconomics-specific "
            "questions answered if it is necessary to understand how to solve the given "
            "problem. Input should be a question posed directly to the textbook."
        )
    ),
    Tool(
        name="Google Search",
        func=GoogleSerperAPIWrapperURL(serper_api_key=KEYS.GoogleSerper.api_key).run,
        description=(
            "Useful for when you need to search Google. Provides links to search results "
            "that you can use Website Answerer to answer for more information."
        )
    ),
    Tool(
        name="Website Answerer",
        func=WebsiteAnswerer.answer_json_string,
        description=(
            "Useful for when you need to answer a question about the content on a website. "
            "You can use this to answer questions about links found in Google Search results. "
            f'{ANSWERER_JSON_STRING_INPUT_INSTRUCTIONS} "source" is the URL of the website. '
            "Do not make up websites to search - you can use Google Search to find relevant urls."
        )
    )
]

# TODO: add textbook tool
