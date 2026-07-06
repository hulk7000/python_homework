from sqlalchemy import create_engine, Column, Integer, String , desc
from sqlalchemy.orm import sessionmaker
from init_db import *
import os
from model import *

db_path = os.path.join(os.path.dirname(__file__), 'game.db')
engine = create_engine(f'sqlite:///{db_path}', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

class Record_game:
    def __init__(self, play_name, tries, input_info):
        self.play_name = play_name
        self.tries = tries
        self.input_info = input_info

    def add_record(self):
        entry = Guess_game(
            play_name=self.play_name,
            tries=self.tries,
            input_info=self.input_info,
        )
        session.add(entry)
        session.commit()
        print(f"✅ 已添加到数据库: {self.play_name} ({self.tries}) {self.input_info}")

class RPS_record_game:
    def __init__(self, bot, player, result):
        self.bot = bot
        self.player = player
        self.result = result

    def add_info(self):
        entry = Rock_paper_scissors(
            bot=self.bot,
            player=self.player,
            result=self.result,
        )

        session.add(entry)
        session.commit()
        print(f"info added:, {self.bot},{self.player}")

class Add_message:
    def __init__(self, category, content):
        self.category = category
        self.content = content

    def add_content(self):
        entry = Message(
            category=self.category,
            content=self.content,
        )

        session.add(entry)
        session.commit()
        print(f"Message added:, {self.category},{self.content}")