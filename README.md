# Multilingual Translator API

A REST API for automatic translation between  **French** ,  **English** , and **Ewe** (a local language spoken in Togo and Ghana), built with FastAPI and models hosted on Hugging Face.

**Supported language pairs:**

* English → French (`en-fr`)
* French → English (`fr-en`)
* Ewe → French (`ee-fr`)
* French → Ewe (`fr-ee`)
* Ewe → English (`ee-en`)
* English → Ewe (`en-ee`) *(coming soon)*

## Requirements

* Python 3.10+
* A Hugging Face account with access to the [EPL-TL26/translation](https://huggingface.co/EPL-TL26/translation) private repository

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/taoufikOURO/multilingual-translator-api.git
cd multilingual-translator-api
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

Edit `.env`:

```env
HF_TOKEN=your_huggingface_token_here
```

> To get your token: go to [huggingface.co](https://huggingface.co/) → Settings → Access Tokens → New token (Read access is enough).

---

## Running the API

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

Interactive documentation (Swagger UI): `http://127.0.0.1:8000/docs`

---

## Usage

### Translate text

**Endpoint:** `POST /translate/{pair}`

**Path parameter:** `pair` — the language pair (e.g. `en-fr`, `ee-fr`, `ee-en`)

**Request body:**

```json
{
  "text": "Hello, how are you?"
}
```

**Response:**

```json
{
  "translation": "Bonjour, comment allez-vous ?"
}
```

### Example with curl

```bash
curl -X POST http://127.0.0.1:8000/translate/en-fr \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello, how are you?"}'
```

---

## Project Structure

```
multilingual-translator-api/
├── app/
│   └── main.py          # FastAPI app and translation logic
├── .env                 # Environment variables (not committed)
├── .env.example         # Example environment file
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Environment Variables

| Variable     | Description                          |
| ------------ | ------------------------------------ |
| `HF_TOKEN` | Hugging Face API token (Read access) |

---

## Tech Stack

[FastAPI](https://fastapi.tiangolo.com/) — API framework

[Hugging Face Transformers](https://huggingface.co/docs/transformers) — model loading

[python-dotenv](https://pypi.org/project/python-dotenv/) — environment variable management
