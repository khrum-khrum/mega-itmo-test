from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/ping")
async def ping():
    return "pong"

@app.api_route("/echo", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH", "TRACE"])
async def echo(request: Request):
    if request.method == "GET":
        return dict(request.query_params)
    else:
        return await request.json()

@app.get("/healthy")
async def healthy():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
