import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv(KOLOSAL_API_KEY)
openai.base_url = "https://api.kolosal.ai/v1"

DEFAULT_MODEL = "claude-3.5-sonnet"

def call_kolosal(prompt: str, model: str = DEFAULT_MODEL):
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error calling Kolosal AI: {str(e)}"
