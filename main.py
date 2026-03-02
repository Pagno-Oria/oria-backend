from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Oria está online"}

@app.get("/webhook")
async def verify(request: Request):
    params = request.query_params
    if params.get("hub.mode") == "subscribe":
        return int(params.get("hub.challenge"))
    return {"status": "verification failed"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Mensagem recebida:", data)
    return {"status": "received"}
