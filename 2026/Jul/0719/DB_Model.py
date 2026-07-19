from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

Base = declarative_base()


class Maze_game(Base):
    __tablename__ = "maze_game"

    id = Column(Integer, primary_key=True, autoincrement=True)
    player_name = Column(String, nullable=False)
    game_type = Column(String, nullable=False)
    opponent_name = Column(String, nullable=True)
    steps = Column(Integer, nullable=False)
    time_used = Column(Float, nullable=False)
    winner = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_time = Column(
        DateTime,
        default=datetime.now
    )