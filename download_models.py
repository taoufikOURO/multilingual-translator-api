"""Module for pre-downloading translation models for all language pairs (en-fr, fr-en, en-ee, ee-en, fr-ee, ee-fr) to ensure faster inference later on. This script uses the Hugging Face Transformers library to download the necessary tokenizers and models for each language pair."""

import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

PAIRS = ["en-fr", "fr-en", "en-ee", "ee-en", "fr-ee", "ee-fr"]
MODEL_NAME = "EPL-TL26/translation"

print("--- DÉBUT DU PRÉ-TÉLÉCHARGEMENT DES MODÈLES ---")

for pair in PAIRS:
    print(f"Téléchargement de la paire : {pair}...")
    try:
        AutoTokenizer.from_pretrained(MODEL_NAME, subfolder=pair, token=HF_TOKEN)
        AutoModelForSeq2SeqLM.from_pretrained(
            MODEL_NAME, subfolder=pair, token=HF_TOKEN
        )
        print(f"Paire {pair} téléchargée avec succès !")
    except Exception as e:
        print(f"Erreur ou paire non disponible pour {pair} : {e}")

print("--- TOUS LES MODÈLES ONT ÉTÉ TÉLÉCHARGÉS ---")
