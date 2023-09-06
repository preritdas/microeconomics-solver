"""Models for secrets."""
from pydantic import BaseModel


class OpenAIModel(BaseModel):
    """API key for OpenAI."""
    api_key: str


class WolframAlphaModel(BaseModel):
    """API key for WolframAlpha."""
    app_id: str


class Keys(BaseModel):
    """Keys for various APIs."""
    OpenAI: OpenAIModel
    WolframAlpha: WolframAlphaModel
