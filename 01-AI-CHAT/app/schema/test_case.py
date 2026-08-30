from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TestCaseRequest(BaseModel):
    requirement: str

class TestCaseResponse(BaseModel):
    id: str
    requirement: str
    created_at: datetime
