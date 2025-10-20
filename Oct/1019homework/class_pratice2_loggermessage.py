from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from class_pratice2_model import Base, MessageLog
import os

db_path = os.path.join(os.path.dirname(__file__), 'message_logs.db')
engine = create_engine(f'sqlite:///{db_path}', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

class MessageLogger:
    def __init__(self, message):
        self.message = message

    def log(self):
        entry = MessageLog(message=self.message)
        session.add(entry)
        session.commit()
        print(f"✅ 插入日志到数据库 : {self.message}")

    def showlog(self):
        result = session.query(MessageLog).filter_by(message=self.message).first()
        if result:
            return f"log: {self.message}"
        else:
            return f"{self.message} not found in log."


# 示例用法
if __name__ == "__main__":
    m = MessageLogger("hello world 2")
    m.log()
    print(m.showlog())
