from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from class_pratice2_model import Base, MessageLog
import os

db_path = os.path.join(os.path.dirname(__file__), 'password.db')
engine = create_engine(f'sqlite:///{db_path}', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)


class PasswdMgmt:
    def __init__(self,site_url,site_username,site_password,user_id="hulk"):
        self.user_id = user_id
        self.site_url = site_url
        self.site_username = site_username
        self.site_password = site_password

    def add_info(self):
        entry = MessageLog(
            user_id=self.user_id,
            site_url=self.site_url,
            site_username=self.site_username,
            site_password=self.site_password
        )
        session.add(entry)
        session.commit()
        print(f"✅ 已添加到数据库: {self.site_url} ({self.site_username})")

# ✅ 独立函数：显示日志
def showid(id=None, user_id="hulk"):
    if id is not None:
        # 按 ID 查询单条记录
        record = session.get(MessageLog, id)
        if record:
            print(f"🔹 ID={record.id}, Site={record.site_url}, User={record.site_username}, Password={record.site_password}")
        else:
            print(f"❌ 未找到 ID={id} 的记录")
    else:
        # 按 user_id 查询所有记录
        records = session.query(MessageLog).filter_by(user_id=user_id).all()
        if records:
            print(f"📜 {user_id} 的记录如下：")
            for r in records:
                print(f"🔹 ID={r.id}, Site={r.site_url}, User={r.site_username}, Password={r.site_password}")
        else:
            print(f"⚠️ 没有找到 user_id={user_id} 的记录")

def showall():
    records = session.query(MessageLog).all()
    if records:
        print("📜 数据库中所有记录如下：")
        for r in records:
            print(f"🔹 ID={r.id}, User={r.user_id}, Site={r.site_url}, Username={r.site_username}, "
                  f"Password={len(r.site_password)*"*"}, Created_at={r.created_at}")
    else:
        print("⚠️ 数据库中没有任何记录")


# ✅ 独立函数：删除日志
def deleteid(id):
    entry = session.get(MessageLog, id)
    if entry:
        session.delete(entry)
        session.commit()
        print(f"✅ 已删除 ID={id} 的记录")
    else:
        print(f"❌ 未找到 ID={id} 的记录")

if __name__ == "__main__":
    m = PasswdMgmt("sina_blog","maggie123","123456")
    # m.add_info()
    # showid()
    # deleteid(3)
    showall()