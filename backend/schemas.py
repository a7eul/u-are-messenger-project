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

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[int] = None

class LastMessage(BaseModel):
    content: str
    created_at: datetime
    sender_name: str

class ChatResponse(BaseModel):
    chat_id: int
    type: str
    title: Optional[str]
    avatar_url: Optional[str]
    last_message: Optional[LastMessage] = None
    participants_count: int
    
    class Config:
        from_attributes = True

class ChatPrivateCreate(BaseModel):
    username: str

class ChatGroupCreate(BaseModel):
    title: str
    user_ids: List[int]