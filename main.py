from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import requests

app = FastAPI()

templates = Jinja2Templates(directory="templates")

MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")
if not MISTRAL_API_KEY:
    raise ValueError("MISTRAL_API_KEY environment variable is not set.")

MODEL = "mistral-large-latest"
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Главная страница приложения."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate-solidity/")
async def generate_solidity(prompt: str = Form(...)):
    """Генерация кода на Solidity через языковую модель."""
    if not prompt:
        return {"error": "Prompt cannot be empty."}
    
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": f"Generate a Solidity smart contract that {prompt}."}],
    }

    try:
        response = requests.post(MISTRAL_API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        content = result["choices"][0]["message"]["content"]
        return {"solidity_code": content}
    except Exception as e:
        return {"error": f"Error generating Solidity code: {e}"}
