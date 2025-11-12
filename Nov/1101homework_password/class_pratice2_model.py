# models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
Base = declarative_base()

# class MessageLog(Base):
#     __tablename__ = 'password_info'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(String, nullable=False)
#     site_url = Column(String, nullable=False)
#     site_username =Column(String, nullable=False)
#     site_password = Column(String, nullable=False)
#     created_at = Column(DateTime, default=datetime.now)

class UserAccount(Base):
    __tablename__ = 'user_login_accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(150), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)  # store a hashed password
    created_at = Column(DateTime, default=datetime.now)

    # Relationship (optional)
    messages = relationship("MessageLog", back_populates="user")

    def __repr__(self):
        return f"<UserAccount(username='{self.username}', email='{self.email}')>"

class MessageLog(Base):
    __tablename__ = 'password_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user_login_accounts.id'), nullable=False)
    site_url = Column(String, nullable=False)
    site_username = Column(String, nullable=False)
    site_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    # Relationship (optional)
    user = relationship("UserAccount", back_populates="messages")

    def __repr__(self):
        return f"<MessageLog(user_id={self.user_id}, site_url='{self.site_url}')>"