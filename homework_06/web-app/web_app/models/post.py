from sqlalchemy import Column, Integer, String

from .database import db


class Post(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    body = Column(String, nullable=False)
