from fastapi import FastAPI

app = FastAPI(
    title="Axonix Support AI",
    description="AI-powered customer support automation API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Axonix Support AI API is running!",
        "status": "success"
    }
