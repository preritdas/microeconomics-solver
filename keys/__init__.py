"""
Read keys.yaml. Prioritizes keys.yaml if it exists, otherwise checks for Streamlit secrets.
"""
import streamlit as st

import os
import yaml

from keys import models


keys_path = os.path.join(
    (current_dir := os.path.realpath(os.path.dirname(__file__))),
    "..",  # parent dir since module is in a subdirectory
    "keys.yaml"
)

if not os.path.exists(keys_path) and not st.secrets:
    raise FileNotFoundError("keys.yaml file not found.")

if not os.path.exists(keys_path) and st.secrets:
    KEYS = models.Keys(
        OpenAI=models.OpenAIModel(api_key=st.secrets["OPENAI_API_KEY"]),
        WolframAlpha=models.WolframAlphaModel(st.secrets["WOLFRAM_APP_ID"])
    )

if os.path.exists(keys_path):
    with open(keys_path, "r", encoding="utf-8") as f:
        RAW_KEYS = yaml.safe_load(f)


    # Validate the keys and expose KEYS
    KEYS = models.Keys(**RAW_KEYS)
