from pydantic import BaseModel
from typing import List

class Ingredient(BaseModel):
    name: str
    amount: int
    unit: str

class PredictRequest(BaseModel):
    food_name: str
    ingredients: List[Ingredient]
