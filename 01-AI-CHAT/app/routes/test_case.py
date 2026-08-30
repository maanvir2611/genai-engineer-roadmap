from fastapi import APIRouter
from datetime import datetime
from schema.test_case import TestCaseRequest, TestCaseResponse
from database import chats_collection

router = APIRouter()

@router.post("/test-cases", response_model=TestCaseResponse)
def create_test_case(request: TestCaseRequest):
    document = {
        "requirement": request.requirement,
        "created_at": datetime.now().isoformat()
    }
    
    result = chats_collection.insert_one(document)
    document["_id"] = result.inserted_id
    
    return TestCaseResponse(
        id=str(document["_id"]),
        requirement=document["requirement"],
        created_at=document["created_at"]
    )
