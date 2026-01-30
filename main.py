from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/ping")
async def ping():
    return "pong"

@app.get("/echo/{message}")
async def echo(message: str):
    return message

@app.get("/healthy")
async def healthy():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
