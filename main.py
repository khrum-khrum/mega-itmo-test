from fastapi import FastAPI

app = FastAPI(title="Simple HTTP Server", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}

@app.get("/ping")
def ping():
    return {"ping": "pong"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)