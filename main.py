from fastapi import FastAPI
import uvicorn

app = FastAPI()


def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


@app.get("/ping")
async def ping():
    return "pong"


@app.get("/echo/{message}")
async def echo(message: str):
    return message


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/fibonacci/{n}")
async def get_fibonacci(n: int):
    if n < 0:
        return {"error": "Input must be a non-negative integer"}
    return {"result": fibonacci(n)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
