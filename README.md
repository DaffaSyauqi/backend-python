
# Backend UMKMTOOL

Backend UMKMTOOL adalah proyek backend berbasis Python yang dibangun dengan struktur modular. Di dalamnya terdapat folder utama seperti api, core, models, dan services yang mengatur logika aplikasi, endpoint API, model data, serta pemrosesan bisnis.


## library
```
flask            # pip install flask
FastApi          # pip install fastapi
uvicorn          # pip install uvicorn
pydantic         # pip install pydantic
sqlalchemy       # pip install sqlalchemy
requests         # pip install requests
python-dotenv    # pip install python-dotenv


```

## Installation

# 1. Clone repository
git clone https://github.com/isyahaishi-glitch/hackathon-kolosal.git
cd hackathon-kolosal

# 2. Buat virtual environment
python3 -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 3. Install library yang diperlukan
pip install flask uvicorn pydantic sqlalchemy requests python-dotenv


    
## Cara Menjalankan

```bash
  uvicorn main:app --reload

```
Setelah berjalan, buka di browser atau Postman:
```
http://localhost:8000/
```

## Demo

<a href="https://drive.google.com/file/d/1yxgJXfxVo1fqtnpQVn16HuMgfmraPtq0/view?usp=sharing">

