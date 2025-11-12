from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash
from class_pratice2_model import Base, UserAccount
from verify_login import verify_login,create_user

# Setup in-memory SQLite for example
engine = create_engine('sqlite:///password.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



# Try to log in'
create_user(session, "alice2", "alice@example.com", "anotherpass")
# success, result = verify_login(session, "alice2", "anotherpass")
# if success:
#     print("✅ Login successful:", result.username)
# else:
#     print("❌ Login failed:", result)
