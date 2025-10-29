# models.py
from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
Base = declarative_base()

class MessageLog(Base):
    __tablename__ = 'password_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, nullable=False)
    site_url = Column(String, nullable=False)
    site_username =Column(String, nullable=False)
    site_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)