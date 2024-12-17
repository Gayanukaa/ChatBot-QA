from pydantic import BaseModel

class Query(BaseModel):
    user_input: str