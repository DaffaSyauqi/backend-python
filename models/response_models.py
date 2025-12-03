from pydantic import BaseModel

class PredictResponse(BaseModel):
    result: str
