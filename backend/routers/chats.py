from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc
from typing import List
from database import get_db
from models import User, Chat, ChatMember, Message
from schemas import ChatResponse, ChatPrivateCreate, ChatGroupCreate, LastMessage
from auth import get_current_user

router = APIRouter(prefix="/chats", tags=["chats"])

@router.get("", response_model=List[ChatResponse])
async def get_chats(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(ChatMember.chat_id).where(ChatMember.user_id == current_user.user_id)
    )
    chat_ids = [row[0] for row in result.fetchall()]
    
    if not chat_ids:
        return []
    
    chats = []
    for chat_id in chat_ids:
        chat = await db.get(Chat, chat_id)
        
        members_count = await db.execute(
            select(func.count(ChatMember.member_id)).where(ChatMember.chat_id == chat_id)
        )
        participants_count = members_count.scalar()
        
        last_msg_result = await db.execute(
            select(Message)
            .where(Message.chat_id == chat_id, Message.is_deleted == False)
            .order_by(desc(Message.created_at))
            .limit(1)
        )
        last_msg = last_msg_result.scalar_one_or_none()
        
        last_message = None
        if last_msg:
            sender = await db.get(User, last_msg.sender_id)
            last_message = LastMessage(
                content=last_msg.content,
                created_at=last_msg.created_at,
                sender_name=sender.username if sender else "Unknown"
            )
        
        display_title = chat.title
        if chat.type == "private":
            other_member = await db.execute(
                select(ChatMember.user_id)
                .where(ChatMember.chat_id == chat_id, ChatMember.user_id != current_user.user_id)
            )
            other_id = other_member.scalar_one_or_none()
            if other_id:
                other_user = await db.get(User, other_id)
                if other_user:
                    display_title = f"{other_user.first_name} {other_user.last_name or ''}".strip()
        
        chats.append(ChatResponse(
            chat_id=chat.chat_id,
            type=chat.type,
            title=display_title,
            avatar_url=chat.avatar_url,
            last_message=last_message,
            participants_count=participants_count
        ))
    
    chats.sort(key=lambda c: c.last_message.created_at if c.last_message else c.chat_id, reverse=True)
    
    return chats

@router.post("/private", response_model=ChatResponse)
async def create_private_chat(
    data: ChatPrivateCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).where(User.username == data.username))
    other_user = result.scalar_one_or_none()
    
    if not other_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    
    if other_user.user_id == current_user.user_id:
        raise HTTPException(status_code=400, detail="Нельзя создать чат с самим собой")
    
    existing = await db.execute(
        select(ChatMember.chat_id).where(
            ChatMember.user_id.in_([current_user.user_id, other_user.user_id])
        )
    )
    common_chat_ids = [row[0] for row in existing.fetchall()]
    
    for chat_id in common_chat_ids:
        chat = await db.get(Chat, chat_id)
        if chat.type == "private":
            members = await db.execute(
                select(ChatMember.user_id).where(ChatMember.chat_id == chat_id)
            )
            member_ids = [row[0] for row in members.fetchall()]
            if set(member_ids) == {current_user.user_id, other_user.user_id}:
      
                return ChatResponse(
                    chat_id=chat.chat_id,
                    type="private",
                    title=f"{other_user.first_name} {other_user.last_name or ''}".strip(),
                    avatar_url=None,
                    last_message=None,
                    participants_count=2
                )
    
    new_chat = Chat(type="private", created_by=current_user.user_id)
    db.add(new_chat)
    await db.flush()
    
    db.add(ChatMember(chat_id=new_chat.chat_id, user_id=current_user.user_id))
    db.add(ChatMember(chat_id=new_chat.chat_id, user_id=other_user.user_id))
    await db.commit()
    await db.refresh(new_chat)
    
    return ChatResponse(
        chat_id=new_chat.chat_id,
        type="private",
        title=f"{other_user.first_name} {other_user.last_name or ''}".strip(),
        avatar_url=None,
        last_message=None,
        participants_count=2
    )

@router.post("/group", response_model=ChatResponse)
async def create_group_chat(
    data: ChatGroupCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    if not data.title.strip():
        raise HTTPException(status_code=400, detail="Название группы не может быть пустым")
    
    new_chat = Chat(
        type="group",
        title=data.title,
        created_by=current_user.user_id
    )
    db.add(new_chat)
    await db.flush()
    
    db.add(ChatMember(chat_id=new_chat.chat_id, user_id=current_user.user_id))
    
    for user_id in data.user_ids:
        if user_id == current_user.user_id:
            continue
        user = await db.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail=f"Пользователь с id {user_id} не найден")
        db.add(ChatMember(chat_id=new_chat.chat_id, user_id=user_id))
    
    await db.commit()
    await db.refresh(new_chat)
    
    participants_count = len(data.user_ids) + 1
    
    return ChatResponse(
        chat_id=new_chat.chat_id,
        type="group",
        title=new_chat.title,
        avatar_url=new_chat.avatar_url,
        last_message=None,
        participants_count=participants_count
    )