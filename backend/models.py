from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Date, ForeignKey
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    email = Column(String(150), unique=True, nullable=False)
    birth_date = Column(Date, nullable=False)
    avatar_url = Column(Text)
    about = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_seen = Column(DateTime(timezone=True), server_default=func.now())

class Chat(Base):
    __tablename__ = "chats"
    
    chat_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    type = Column(String(20), nullable=False)
    description = Column(Text)
    avatar_url = Column(Text)
    created_by = Column(Integer, ForeignKey("users.user_id", ondelete="SET NULL"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ChatMember(Base):
    __tablename__ = "chat_members"
    
    member_id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey("chats.chat_id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    joined_at = Column(DateTime(timezone=True), server_default=func.now())

class Message(Base):
    __tablename__ = "messages"
    
    message_id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey("chats.chat_id", ondelete="CASCADE"), nullable=False)
    sender_id = Column(Integer, ForeignKey("users.user_id", ondelete="SET NULL"))
    reply_to_id = Column(Integer, ForeignKey("messages.message_id", ondelete="SET NULL"))
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_deleted = Column(Boolean, default=False)

class Attachment(Base):
    __tablename__ = "attachments"
    
    attachment_id = Column(Integer, primary_key=True, index=True)
    message_id = Column(Integer, ForeignKey("messages.message_id", ondelete="CASCADE"), nullable=False)
    file_url = Column(Text, nullable=False)
    file_name = Column(String(255))
    file_size = Column(Integer)