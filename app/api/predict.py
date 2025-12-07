from fastapi import APIRouter
from app.models.request_models import PredictRequest
from app.services.predictor_service import predict_production

router = APIRouter(prefix="/predict")

@router.post("/")
async def predict(req: PredictRequest):
    result = predict_production(req.food_name, req.ingredients)
    return {"result": result}
