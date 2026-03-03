from fastapi import FastAPI, Request
from typing import Any, Dict, Optional

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Oria está online"}

@app.get("/webhook")
async def verify(request: Request):
    params = request.query_params
    if params.get("hub.mode") == "subscribe":
        # aqui você normalmente valida hub.verify_token também
        return int(params.get("hub.challenge"))
    return {"status": "verification failed"}

@app.post("/webhook")
async def webhook(payload: Optional[Dict[str, Any]] = None):
    if payload is None:
        # corpo vazio -> não quebra
        return {"status": "received", "detail": "empty body"}
    print("Mensagem recebida:", payload)
    return {"status": "received"}
