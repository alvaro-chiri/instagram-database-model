import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    haircolor = Column(String)
    eyecolor = Column(String)

class Planet(Base):
    __tablename__ = 'planet' 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    climate = Column(String)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    password = Column(String(16))
    email = Column(String, unique = True)
    firstname = Column(String)
    lastname = Column(String)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    character = relationship(Character)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet = relationship(Planet)
    Planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'))

    def validate():
        if not self.planet_id and not self.character_id:
            return False
        return True






## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')