# models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MessageLog(Base):
    __tablename__ = 'message_logs'
    id = Column(Integer, primary_key=True)
    message = Column(String, nullable=False)
    # name =Column(String, nullable=False)
    # password = Column(String, nullable=False)