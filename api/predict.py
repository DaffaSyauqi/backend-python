from fastapi import APIRouter
from app.core.kolosal import call_kolosal

router = APIRouter(prefix="/predict")

@router.post("/")
def predict(item: dict):
    product = item.get("product")
    ingredients = item.get("ingredients")

    prompt = f"""
    Kamu adalah AI prediksi produksi makanan.
    Produk: {product}
    Bahan: {ingredients}
    Berikan prediksi jumlah yang bisa dibuat + alasan singkat.
    """

    result = call_kolosal(prompt)
    return {"result": result}
