from fastapi import FastAPI
from app.api.predict import router as predict_router

app = FastAPI(
    title="UMKM Production Predictor API",
    version="1.0.0"
)

app.include_router(predict_router, prefix="/api/v1")
