from pydantic import BaseModel
from datetime import datetime

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    id: str
    answer: str
    created_at: datetime

