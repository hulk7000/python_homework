# models.py
from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
Base = declarative_base()

class Guess_game(Base):
    __tablename__ = 'game_record'
    id = Column(Integer, primary_key=True, autoincrement=True)
    play_name = Column(String, nullable=False)
    tries = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

