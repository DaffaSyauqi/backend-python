from pydantic import BaseModel
from typing import Dict

class PredictRequest(BaseModel):
    product_type: str
    ingredients: Dict[str, float]

