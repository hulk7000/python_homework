from sqlalchemy import create_engine, Column, Integer, String , desc
from sqlalchemy.orm import sessionmaker
import json
from DB_update_database import *
import os
from DB_model import *


db_path = os.path.join(os.path.dirname(__file__), 'game.db')
engine = create_engine(f'sqlite:///{db_path}', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

class Record_game:
    def __init__(self, player_name, bet_amount, balance, tries, input_info, win_amount, result):
        self.player_name = player_name
        self.bet_amount = bet_amount
        self.balance = balance
        self.tries = tries
        self.input_info = input_info
        self.win_amount = win_amount
        self.result = result

    def add_record(self):
        entry = Guess_game(
            player_name=self.player_name,
            bet_amount=self.bet_amount,
            balance=self.balance,
            tries=self.tries,
            input_info=self.input_info,
            win_amount=self.win_amount,
            result=self.result
        )

        session.add(entry)
        session.commit()

        print(
            f"Info added: {self.player_name}, "
            f"Bet: {self.bet_amount}, "
            f"Result: {self.result}, "
            f"Balance: {self.balance}"
        )

    @staticmethod
    def get_latest_balance(player_name):
        latest_record = (
            session.query(Guess_game)
            .filter_by(player_name=player_name)
            .order_by(Guess_game.id.desc())
            .first()
        )

        if latest_record:
            return latest_record.balance
        else:
            return 0

class RPS_record_game:
    def __init__(self, player_name, bet_amount, balance, player_choice, bot_choice, win_amount, result):
        self.player_name = player_name
        self.bet_amount = bet_amount
        self.balance = balance
        self.bot_choice = bot_choice
        self.player_choice = player_choice
        self.win_amount = win_amount
        self.result = result

    def add_info(self):
        entry = RPS_game(
            player_name=self.player_name,
            bet_amount=self.bet_amount,
            balance=self.balance,
            bot_choice=self.bot_choice,
            player_choice=self.player_choice,
            win_amount=self.win_amount,
            result=self.result,
        )

        session.add(entry)
        session.commit()

        print(
            f"Info added: {self.player_name}, "
            f"Bet: {self.bet_amount}, "
            f"Result: {self.result}, "
            f"Balance: {self.balance}"
        )

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
    def __init__(self, player_name,bet_amount,pre_balance,new_balance,horse_choice,win_amount,winner_house, winner_house_time, rankings, race_info,status):
        self.player_name = player_name
        self.bet_amount = bet_amount
        self.pre_balance = pre_balance
        self.new_balance = new_balance
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
            pre_balance=self.pre_balance,
            new_balance=self.new_balance,
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

class Guess_hand_record:
    def __init__(self, player_name, bet_amount, pre_balance, new_balance, player_choice, hidden_item, win_amount, status):
        self.player_name = player_name
        self.bet_amount = bet_amount
        self.pre_balance = pre_balance
        self.new_balance = new_balance
        self.player_choice = player_choice
        self.hidden_item = hidden_item
        self.win_amount = win_amount
        self.status = status

    def add_info(self):

        record = Guess_hand_game(
            player_name=self.player_name,
            bet_amount=self.bet_amount,
            pre_balance=self.pre_balance,
            new_balance=self.new_balance,
            player_choice=self.player_choice,
            hidden_item=self.hidden_item,
            win_amount=self.win_amount,
            status=self.status,
        )

        session.add(record)
        session.commit()

        print(
            f"Info added: {self.player_name}, "
            f"Bet: {self.bet_amount}, "
            f"Result: {self.status}, "
            f"Balance: {self.new_balance}"
        )

    @staticmethod
    def get_latest_balance(username):

        last_record = (
            session.query(Guess_hand_game)
            .filter_by(player_name=username)
            .order_by(desc(Guess_hand_game.id))
            .first()
        )

        if last_record:
            return last_record.new_balance

        return 0

class Coin_flip_record:
    def __init__(self, player_name, bet_amount, pre_balance, new_balance, player_choice, coin_result, win_amount, status):
        self.player_name = player_name
        self.bet_amount = bet_amount
        self.pre_balance = pre_balance
        self.new_balance = new_balance
        self.player_choice = player_choice
        self.coin_result = coin_result
        self.win_amount = win_amount
        self.status = status

    def add_info(self):
        record = Coin_flip_game(
            player_name=self.player_name,
            bet_amount=self.bet_amount,
            pre_balance=self.pre_balance,
            new_balance=self.new_balance,
            player_choice=self.player_choice,
            coin_result=self.coin_result,
            win_amount=self.win_amount,
            status=self.status,
        )

        session.add(record)
        session.commit()

class Whack_record:
    def __init__(self, player_name, bet_amount, pre_balance, new_balance, hits, misses, score, win_amount, status):
        self.player_name = player_name
        self.bet_amount = bet_amount
        self.pre_balance = pre_balance
        self.new_balance = new_balance
        self.hits = hits
        self.misses = misses
        self.score = score
        self.win_amount = win_amount
        self.status = status

    def add_info(self):
        record = Whack_game(
            player_name=self.player_name,
            bet_amount=self.bet_amount,
            pre_balance=self.pre_balance,
            new_balance=self.new_balance,
            hits=self.hits,
            misses=self.misses,
            score=self.score,
            win_amount=self.win_amount,
            status=self.status,
        )

        session.add(record)
        session.commit()