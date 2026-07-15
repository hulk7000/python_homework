from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime

Base = declarative_base()

class Guess_game(Base):
    __tablename__ = "guess_game"
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_name = Column(String, nullable=False)
    bet_amount = Column(Integer, nullable=False)
    balance = Column(Integer, nullable=False)
    tries = Column(Integer, nullable=False)
    input_info = Column(String, nullable=False)
    win_amount = Column(Integer, nullable=False)
    result = Column(String, nullable=False)
    created_time = Column(DateTime, default=datetime.now)

class RPS_game(Base):
    __tablename__ = "rps_game"

    id = Column(Integer, primary_key=True, autoincrement=True)
    player_name = Column(String, nullable=False)
    bet_amount = Column(Integer, nullable=False)
    balance = Column(Integer, nullable=False)
    player_choice = Column(String, nullable=False)
    bot_choice = Column(String, nullable=False)
    win_amount = Column(Integer, nullable=False)
    result = Column(String, nullable=False)
    created_time = Column(DateTime, default=datetime.now)

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, nullable=False)
    content = Column(String, nullable=False)

class Horse_game(Base):
    __tablename__ = "horse_game"

    id = Column(Integer, primary_key=True, autoincrement=True)
    player_name = Column(String, nullable=False)
    bet_amount = Column(String, nullable=False)
    pre_balance = Column(Integer, nullable=False)
    new_balance = Column(Integer, nullable=False)
    horse_choice = Column(String, nullable=False)
    win_amount = Column(String, nullable=False)
    winner_house = Column(String, nullable=False)
    winner_house_time = Column(Float, nullable=False)
    rankings = Column(String, nullable=False)
    race_info = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_time = Column(DateTime, default=datetime.now)

class User_info(Base):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    player_name = Column(String(50), unique=True, nullable=False)
    balance = Column(Integer, default=0)
    created_time = Column(DateTime, default=datetime.now)

class Guess_hand_game(Base):
    __tablename__ = "guess_hand_game"

    id = Column(Integer, primary_key=True, autoincrement=True)
    player_name = Column(String, nullable=False)
    bet_amount = Column(Integer, nullable=False)
    pre_balance = Column(Integer, nullable=False)
    new_balance = Column(Integer, nullable=False)
    player_choice = Column(String, nullable=False)
    hidden_item = Column(String, nullable=False)
    win_amount = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
    created_time = Column(DateTime, default=datetime.now)

class Coin_flip_game(Base):
    __tablename__ = "coin_flip_game"

    id = Column(Integer, primary_key=True, autoincrement=True)
    player_name = Column(String, nullable=False)
    bet_amount = Column(Integer, nullable=False)
    pre_balance = Column(Integer, nullable=False)
    new_balance = Column(Integer, nullable=False)
    player_choice = Column(String, nullable=False)
    coin_result = Column(String, nullable=False)
    win_amount = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
    created_time = Column(DateTime, default=datetime.now)