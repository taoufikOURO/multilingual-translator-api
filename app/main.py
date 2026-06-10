"""
This module defines a FastAPI application that provides an endpoint for translating text between different languages using a pre-trained translation model. The application loads the appropriate model based on the specified language pair and returns the translated text as a JSON response. The translation models are cached to improve performance on subsequent requests.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from functools import lru_cache
from dotenv import load_dotenv
import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

app = FastAPI()


@lru_cache(maxsize=None)
def load_model(pair: str):
    """Load the translation model for the given language pair. The model is cached to improve performance on subsequent requests."""
    model_name = "EPL-TL26/translation"
    tokenizer = AutoTokenizer.from_pretrained(
        model_name, subfolder=pair, token=HF_TOKEN
    )
    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_name, subfolder=pair, token=HF_TOKEN
    )
    return tokenizer, model


class TranslationRequest(BaseModel):
    """Pydantic model for the translation request. It contains a single field 'text' which is the text to be translated."""

    text: str


@app.post("/translate/{pair}")
def translate(pair: str, req: TranslationRequest):
    """Endpoint to translate text from one language to another. The 'pair' path parameter specifies the language pair (e.g., 'en-fr' for English to French). The request body should contain the text to be translated. The function loads the appropriate model for the language pair, performs the translation, and returns the result as a JSON response."""
    if not req.text.strip():
        return {"translation": ""}
    tokenizer, model = load_model(pair)
    inputs = tokenizer([req.text], return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    result = tokenizer.decode(translated[0], skip_special_tokens=True)
    return {"translation": result}
