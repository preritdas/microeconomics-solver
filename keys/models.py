"""Models for secrets."""
from pydantic import BaseModel


class OpenAIModel(BaseModel):
    """API key for OpenAI."""
    api_key: str


class Keys(BaseModel):
    """Keys for various APIs."""
    OpenAI: OpenAIModel
