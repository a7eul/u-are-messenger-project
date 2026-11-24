from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_db
from models import User
from schemas import UserCreate, UserResponse, UserLogin, Token
from auth import create_access_token, get_current_user, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
import bcrypt

router = APIRouter(tags=["auth"])

@router.post("/register", response_model=UserResponse, operation_id="register_user")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    existing = await db.execute(select(User).where(User.username == user.username))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    db_user = User(
        username=user.username,
        password_hash=hashed_password,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        birth_date=user.birth_date
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

@router.post("/login", response_model=Token)
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == user.username))
    db_user = result.scalar_one_or_none()
    
    if not db_user:
        raise HTTPException(status_code=400, detail="Неверный логин или пароль")
    
    password_valid = bcrypt.checkpw(
        user.password.encode('utf-8'),
        db_user.password_hash.encode('utf-8')
    )
    
    if not password_valid:
        raise HTTPException(status_code=400, detail="Неверный логин или пароль")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_user.user_id},
        expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user