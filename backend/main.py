from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
from pydantic import BaseModel
from datetime import datetime
from bson import ObjectId
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


    from pydantic import BaseModel
from datetime import datetime
from bson import ObjectId

class Ticket(BaseModel):
    customer_name: str
    issue: str
    category: str
    priority: str

@app.post("/tickets")
def create_ticket(ticket: Ticket):
    ticket_data = ticket.model_dump()
    ticket_data["ticket_id"] = "AXN-" + str(int(datetime.now().timestamp()))
    ticket_data["status"] = "Open"
    ticket_data["created_at"] = datetime.now()

    result = db["tickets"].insert_one(ticket_data)

    return {
        "message": "Ticket created successfully",
        "ticket_id": ticket_data["ticket_id"],
        "database_id": str(result.inserted_id)
    }