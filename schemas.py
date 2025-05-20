from pydantic import BaseModel
from typing import List

class LeftEntry(BaseModel):
    id: int
    question_id: int
    text: str

class RightEntry(BaseModel):
    id: int
    question_id: int
    text: str

class Question(BaseModel):
    id: int
    prompt: str
    left_entries: List[LeftEntry]
    right_entries: List[RightEntry]

    class Config:
        orm_mode = True
