from fastapi import FastAPI

app = FastAPI(title="Simple HTTP Server", version="1.0.0")

@app.get("/ping")
def ping():
    """Ping endpoint that returns pong"""
    return {"message": "pong"}

@app.get("/pong")
def pong():
    """Pong endpoint that returns ping"""
    return {"message": "ping"}

@app.post("/echo")
def echo(message: str):
    """Echo endpoint that returns the received message"""
    return {"message": message}

@app.get("/healthy")
def healthy():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)