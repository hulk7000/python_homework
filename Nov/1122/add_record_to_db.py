from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from class_pratice2_model import Base, Guess_game
import os

db_path = os.path.join(os.path.dirname(__file__), 'guessgame.db')
engine = create_engine(f'sqlite:///{db_path}', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)


class Record_game:
    def __init__(self,play_name,tries):
        self.play_name = play_name
        self.tries = tries
        # self.created_at = created_at

    def add_record(self):
        entry = Guess_game(
            play_name=self.play_name,
            tries=self.tries,
            # created_at=self.created_at
        )
        session.add(entry)
        session.commit()
        print(f"✅ 已添加到数据库: {self.play_name} ({self.tries})")

if __name__ == "__main__":
    m = Record_game("frank","9999")
    m.add_record()