from fastapi import APIRouter, HTTPException
from app.services import generate_response
from app.schemas import Query

router = APIRouter()

@router.post("/chat")
async def chat(query: Query):
    try:
        response = generate_response(query.user_input)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
