from sqlalchemy import create_engine, Column, Integer, String , desc
from sqlalchemy.orm import sessionmaker
from class_pratice2_model import Base, Guess_game, Message, Rock_paper_scissors, Speed_type,Horse_game, Car_game
import os
import json

db_path = os.path.join(os.path.dirname(__file__), 'guessgame.db')
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

class Type_record:
    def __init__(self, username, time_taken, typed_word, status):
        self.username = username
        self.time_taken = time_taken
        self.typed_word = typed_word
        self.status = status

    def add_info(self):
        record = Speed_type(
            username=self.username,
            time_taken=self.time_taken,
            typed_word=self.typed_word,
            status=self.status
        )
        session.add(record)
        session.commit()

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


class Car_record:
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
        record = Car_game(
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
    def get_latest_balance(player_name):
        last_record = (
            session.query(Car_game)
            .filter_by(player_name=player_name)
            .order_by(desc(Car_game.id))
            .first()
        )
        if last_record:
            return last_record.balance
        return 0  # 默认余额为 0


if __name__ == "__main__":
    # Car_record('tester','win',1000,'Abc','123',10.34,'2','2','3','3').add_info()
    latest = Car_record.get_latest_balance("tester")
    print(latest)
    # Horse_record('1','2',3,'4','5','6',7.2,'8','8','9').add_info()
    pass
    # input_info_json = json.dumps([1, 8, 9])
    # m = Record_game("frank_demo_test_insert_db", "9999", input_info_json)
    # m.add_record()
    #
    # msg = Add_message('k','message')
    # msg.add_content()
    # Horse_record("1","4","1","1","finish").add_info()
