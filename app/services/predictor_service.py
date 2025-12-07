import json
from typing import List, Dict, Any
from app.core.kolosal import call_kolosal


def clean_and_parse_json(raw: str):
    """
    Membersihkan ```json, ```, dan karakter backtick.
    Lalu coba parse JSON.
    """
    cleaned = (
        raw.replace("```json", "")
           .replace("```", "")
           .replace("`", "")
           .strip()
    )

    try:
        return json.loads(cleaned)
    except Exception as e:
        return {
            "error": "Failed to parse JSON",
            "exception": str(e),
            "raw": raw
        }


def build_prompt(food_name: str, ingredients: List[Any]):
    """
    Membuat prompt rapi sesuai format JSON wajib.
    """
    return f"""
Anda adalah asisten AI yang hanya boleh memberikan output dalam format JSON VALID.

DATA USER:
- Nama makanan: {food_name}
- Daftar bahan:
{chr(10).join([f"  - {i.name}: {i.amount} {i.unit}" for i in ingredients])}

TUGAS:
Analisis bahan dan berikan prediksi hasil produksi makanan.

FORMAT OUTPUT (WAJIB JSON VALID TANPA BACKTICK, TANPA MARKDOWN):
{{
  "product_name": "...",
  "prediction_type": "quantity",
  "estimated_output": 0,
  "output_unit": "...",
  "details": {{
      "low_estimate": 0,
      "high_estimate": 0,
      "limiting_factor": "...",
      "calculation_reason": "..."
  }},
  "alternatives": [
      {{
          "name": "...",
          "estimated_output": 0,
          "unit": "..."
      }}
  ]
}}

WAJIB:
- Jangan gunakan ```json
- Jangan gunakan markdown
- Hanya kirim JSON valid
- Tidak boleh ada teks di luar JSON
"""


def predict_production(food_name: str, ingredients: List[Any]):
    """
    1. Build prompt
    2. Panggil Kolosal AI
    3. Clean + JSON parse
    """
    prompt = build_prompt(food_name, ingredients)

    ai_res = call_kolosal(prompt)

    # Jika Kolosal error → return langsung
    if isinstance(ai_res, str) and ai_res.startswith("Error calling"):
        return {
            "error": "API error",
            "raw": ai_res
        }

    # Parse hasil AI
    return clean_and_parse_json(ai_res)
