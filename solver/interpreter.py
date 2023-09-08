"""Code Interpreter tool for plotting."""
# Set CodeBox API key first
from keys import KEYS
import os; os.environ["CODEBOX_API_KEY"] = KEYS.CodeBox.api_key

from codeinterpreterapi import CodeInterpreterSession, settings

from pathlib import Path


# Set the API keys and configs
settings.OPENAI_API_KEY = KEYS.OpenAI.api_key
settings.MODEL = "gpt-4"


# Create the interpreter_files directory if it doesn't exist
if not Path("interpreter_files").exists():
    Path("interpreter_files").mkdir()


def _flush_interpreter_files():
    """Flush the interpreter_files directory."""
    for file in Path("interpreter_files").iterdir():
        file.unlink()


def run(query: str) -> str:
    """Run the query."""
    # Clear any old files
    _flush_interpreter_files()

    with CodeInterpreterSession() as session:
        response = session.generate_response(query)

    for res_file in response.files:
        res_file.save(f"interpreter_files/{res_file.name}")

    return response.content
