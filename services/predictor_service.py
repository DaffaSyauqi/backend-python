from app.core.kolosal_client import call_kolosal

def predict_production(product_type: str, ingredients: dict):
    prompt = f"""
    Kamu adalah AI prediksi produksi makanan.

    Jenis produk: {product_type}
    Bahan tersedia: {ingredients}

    Berikan:
    1. Estimasi jumlah produk (angka saja di baris pertama)
    2. Penjelasan singkat di baris kedua
    """

    output = call_kolosal(prompt)
    return output
