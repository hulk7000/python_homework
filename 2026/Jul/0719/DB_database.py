from sqlalchemy import create_engine, inspect, desc
from sqlalchemy.orm import sessionmaker
from DB_Model import *
import os


DB_FILENAME = "game.db"

DB_PATH = os.path.join(
    os.path.dirname(__file__),
    DB_FILENAME
)

DATABASE_URL = f"sqlite:///{DB_PATH}"


engine = create_engine(
    DATABASE_URL,
    echo=False
)


Session = sessionmaker(bind=engine)
session = Session()


inspector = inspect(engine)


# Create tables
Base.metadata.create_all(engine)



class Maze_record:

    def __init__(
        self,
        player_name,
        game_type,
        steps,
        time_used,
        winner,
        status,
        opponent_name=None
    ):

        self.player_name = player_name
        self.game_type = game_type
        self.steps = steps
        self.time_used = time_used
        self.winner = winner
        self.status = status
        self.opponent_name = opponent_name


    def add_info(self):

        record = Maze_game(

            player_name=self.player_name,

            game_type=self.game_type,

            opponent_name=self.opponent_name,

            steps=self.steps,

            time_used=self.time_used,

            winner=self.winner,

            status=self.status
        )


        session.add(record)

        session.commit()


        print(
            f"Maze saved: {self.player_name} - {self.status}"
        )


    @staticmethod
    def get_player_games(player_name):

        records = (
            session.query(Maze_game)
            .filter_by(player_name=player_name)
            .order_by(desc(Maze_game.id))
            .all()
        )

        return records