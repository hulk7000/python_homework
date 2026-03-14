from sqlalchemy import create_engine
from model import Base
import os

db_path = os.path.join(os.path.dirname(__file__), 'find_info_on_web.db')
engine = create_engine(f'sqlite:///{db_path}', echo=True)

table_name = 'find_info_on_web'

if not engine.dialect.has_table(engine.connect(), table_name):
    Base.metadata.create_all(engine)
    print(f"✅ 表 {table_name} 不存在，已重新创建")
else:
    print(f"ℹ️ 表 {table_name} 已存在，跳过创建")
