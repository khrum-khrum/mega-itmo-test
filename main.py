from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return "pong"

@app.get("/echo")
async def echo(message: str = ""):
    return {"message": message}

@app.get("/health")
async def health():
    return "OK"
