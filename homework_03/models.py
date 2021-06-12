"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import (
    declarative_base,
    relationship,
    joinedload,
    selectinload,
    sessionmaker,
)
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    func,
    select,
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:password@localhost:8002/project"


engine = create_async_engine(PG_CONN_URI, echo=True)
Base = declarative_base()
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default='', server_default='')
    username = Column(String, nullable=False, default='', server_default='')
    email = Column(String, nullable=False, default='', server_default='')

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__} " \
               f"(id={self.id}, name={self.name!r}, username={self.username}), email={self.email}"

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, default='', server_default='')
    body = Column(String, nullable=False, default='', server_default='')

    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship('User', back_populates="posts")

    def __str__(self):
        return f"{self.__class__.__name__} " \
               f"(id={self.id}, title={self.title!r}, body={self.body}), user_id={self.user_id}"

    def __repr__(self):
        return str(self)
