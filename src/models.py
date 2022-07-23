import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    password = Column(String(16))
    email = Column(String, unique=True)
    firstname = Column(String)
    lastname = Column(String)
    description = Column(String, nullable=True)

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'))

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    post = relationship(Post)
    post_id = Column(Integer, ForeignKey('post.id'))
    url = Column(String)

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String)
    author = relationship(User)
    author_id = Column(Integer, ForeignKey('user.id'))
    post = relationship(Post)
    post_id = Column(Integer, ForeignKey('post.id'))

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user = relationship(User)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')