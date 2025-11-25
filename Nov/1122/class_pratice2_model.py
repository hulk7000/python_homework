from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Guess_game(Base):
    __tablename__ = "guess_game"
    id = Column(Integer, primary_key=True)
    play_name = Column(String)
    tries = Column(String)
    input_info = Column(String)

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, nullable=False)
    content = Column(String, nullable=False)
