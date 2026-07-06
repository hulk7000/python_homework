from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime

Base = declarative_base()

class Guess_game(Base):
    __tablename__ = "guess_game"
    id = Column(Integer, primary_key=True)
    play_name = Column(String)
    tries = Column(String)
    input_info = Column(String)
    created_time = Column(DateTime, default=datetime.now)

class Rock_paper_scissors(Base):
    __tablename__ = "rps_game"

    id = Column(Integer, primary_key=True, autoincrement=True)
    bot = Column(String, nullable=False)
    player = Column(String, nullable=False)
    result = Column(String, nullable=False)
    created_time = Column(DateTime, default=datetime.now)

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, nullable=False)
    content = Column(String, nullable=False)