from pydantic import BaseModel
from typing import List, Optional

class Alternative(BaseModel):
    name: str
    estimated_output: float
    unit: str

class Details(BaseModel):
    low_estimate: float
    high_estimate: float
    limiting_factor: str
    calculation_reason: str

class PredictResponse(BaseModel):
    product_name: str
    prediction_type: str
    estimated_output: float
    output_unit: str
    details: Details
    alternatives: Optional[List[Alternative]] = None
