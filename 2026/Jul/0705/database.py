from sqlalchemy import create_engine, Column, Integer, String , desc
from sqlalchemy.orm import sessionmaker
import json
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

class Horse_record:
    def __init__(self, player_name,bet_amount,balance,horse_choice,win_amount,winner_house, winner_house_time, rankings, race_info,status):
        self.player_name = player_name
        self.bet_amount = bet_amount
        self.balance = balance
        self.horse_choice = horse_choice
        self.win_amount = win_amount
        self.winner_house = winner_house
        self.winner_house_time = winner_house_time
        self.rankings = rankings
        self.race_info = race_info
        self.status = status

    def add_info(self):
        record = Horse_game(
            player_name =self.player_name,
            bet_amount=self.bet_amount,
            balance=self.balance,
            horse_choice=self.horse_choice,
            win_amount=self.win_amount,
            winner_house=self.winner_house,
            winner_house_time=self.winner_house_time,
            rankings=json.dumps(self.rankings),  # 改这里
            race_info=json.dumps(self.race_info),  # 改这里
            status=self.status
        )
        session.add(record)
        session.commit()

    @staticmethod
    def get_latest_balance(username):

        last_record = (
            session.query(Horse_game)
            .filter_by(player_name=username)
            .order_by(desc(Horse_game.id))
            .first()
        )
        if last_record:
            return last_record.balance
        return 0  # 默认余额为 0

class User_record:
    def __init__(self, player_name, balance_change):
        self.player_name = player_name
        self.balance_change = balance_change

    def update_balance(self):
        user = (
            session.query(User_info)
            .filter_by(player_name=self.player_name)
            .first()
        )

        if user:
            user.balance += self.balance_change
        else:
            user = User_info(
                player_name=self.player_name,
                balance=self.balance_change
            )
            session.add(user)
        session.commit()

    @staticmethod
    def get_latest_balance(username):

        last_record = (
            session.query(User_info)
            .filter_by(player_name=username)
            .order_by(desc(User_info.id))
            .first()
        )
        if last_record:
            return last_record.balance
        return 0  # 默认余额为 0