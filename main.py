from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/echo")
def echo(message: str):
    return {"message": message}

@app.get("/healthy")
def healthy():
    return {"status": "ok"}