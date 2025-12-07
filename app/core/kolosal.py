import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Ambil API KEY dari .env
KOLOSAL_API_KEY = os.getenv("KOLOSAL_API_KEY")

# Client Kolosal AI
client = OpenAI(
    api_key=KOLOSAL_API_KEY,
    base_url="https://api.kolosal.ai/v1"
)

DEFAULT_MODEL = "Claude Sonnet 4.5"

def call_kolosal(prompt: str, model: str = DEFAULT_MODEL):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error calling Kolosal AI: {str(e)}"
