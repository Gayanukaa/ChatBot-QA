from fastapi import FastAPI
from app.routes import router

app = FastAPI()

# Include routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "AI-Powered Chatbot Platform is running!"}