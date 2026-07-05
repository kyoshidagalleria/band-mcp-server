from fastapi import FastAPI
from tools.search import search_band

app = FastAPI(title="GALLERIA Live Assistant")


@app.get("/")
def root():
    return {
        "service": "GALLERIA Live Assistant",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/band")
def get_band_info(name: str):
    return search_band(name)