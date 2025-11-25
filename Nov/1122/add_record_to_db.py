from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from class_pratice2_model import Base, Guess_game
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


class Message_table(Base):
    __tablename__ = "message_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)

    def __init__(self, content):
        self.content = content

    def add(self):
        session.add(self)
        session.commit()
        print("Message added:", self.content)


if __name__ == "__main__":
    input_info_json = json.dumps([1, 8, 9])
    m = Record_game("frank_demo_test_insert_db", "9999", input_info_json)
    m.add_record()

    msg = Message_table("Hello message")
    msg.add()
