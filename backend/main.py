from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import engine, Base, get_db
from models import User
from schemas import UserCreate, UserResponse
import bcrypt

app = FastAPI(title="u&are API")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/register", response_model=UserResponse)
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

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user