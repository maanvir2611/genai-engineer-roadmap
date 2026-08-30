from fastapi import APIRouter
from schema.chat_schema import ChatRequest, ChatResponse
from datetime import datetime
from openai import AsyncOpenAI
from database import chats_collection
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    client = AsyncOpenAI()
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": request.question}
        ]
    )
    document = {
        "question": request.question,
        "answer": response.choices[0].message.content,
        "created_at": datetime.now().isoformat()
    }
    result = chats_collection.insert_one(document)
    document["_id"] = result.inserted_id
    return ChatResponse(id=str(document["_id"]), answer=document["answer"], created_at=document["created_at"])
