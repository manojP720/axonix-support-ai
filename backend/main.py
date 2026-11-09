from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Axonix Support AI")

client = MongoClient(os.getenv("MONGODB_URI"))
db = client[os.getenv("DATABASE_NAME")]

@app.get("/")
def home():
    return {
        "message": "Axonix Support AI is running!",
        "status": "success"
    }

@app.get("/health")
def health():
    try:
        client.admin.command("ping")
        return {
            "api": "running",
            "database": "connected"
        }
    except Exception as e:
        return {"database": "disconnected", "error": str(e)}