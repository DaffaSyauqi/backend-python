from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.predict import router as predict_router

app = FastAPI(
    title="UMKM Production Predictor API",
    version="1.0.0",
    redirect_slashes=False
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict_router, prefix="/api/v1")
