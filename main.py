from fastapi import FastAPI

app = FastAPI(title="Mega ITMO Test API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to Mega ITMO Test API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/test")
def test_endpoint():
    return {"test": "success", "value": 10}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)