from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional, List

class UserCreate(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: Optional[str] = None
    email: EmailStr
    birth_date: date

class UserResponse(BaseModel):
    user_id: int
    username: str
    first_name: str
    last_name: Optional[str]
    email: str
    birth_date: date
    avatar_url: Optional[str]
    about: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True

class ChatCreate(BaseModel):
    title: Optional[str] = None
    type: str
    description: Optional[str] = None
    user_ids: List[int]

class MessageCreate(BaseModel):
    content: str
    reply_to_id: Optional[int] = None