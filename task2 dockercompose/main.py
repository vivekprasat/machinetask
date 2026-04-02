from fastapi import FastAPI
import redis
import os

app = FastAPI()

redis_host = os.getenv("REDIS_HOST", "localhost")
client = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.get("/")
def read_root():
    client.set("message", "Hello from Redis + FastAPI!")
    value = client.get("message")
    return {"message": value}

@app.get("/health")
def health():
    return {"status": "OK"}
