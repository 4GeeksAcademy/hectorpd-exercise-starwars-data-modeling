import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    userid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorites = relationship("Favorites", back_populates="user")
    posts = relationship("Post", back_populates="user")
    comments = relationship("Comments", back_populates="user")

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey('user.userid'))
    name = Column(String(250), nullable=False)
    url = Column(String(250))
    user = relationship("User", back_populates="favorites")
    planet = relationship("Planets", back_populates="favorites")
    character = relationship("Characters", back_populates="favorites")
    starship = relationship("StarShips", back_populates="favorites")
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey('user.userid'))
    body = Column(String(250))
    user = relationship("User", back_populates="posts")

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey('user.userid'))
    body = Column(String(250))
    user = relationship("User", back_populates="comments")

class Planets(Base):
    __tablename__ = 'planets'
    planetid = Column(Integer, primary_key=True)
    characteristics = Column(String, nullable=False)
    favorites = relationship("Favorites", back_populates="planet")
    

class StarShips(Base):
    __tablename__ = 'starships'
    starshipsid = Column(Integer, primary_key=True)
    characteristics = Column(String, nullable=False)
    favorites = relationship("Favorites", back_populates="starship")

class Characters(Base):
    __tablename__ = 'characters'
    charactersid = Column(String, primary_key=True)
    characteristics = Column(String, nullable=False)
    favorites = relationship("Favorites", back_populates="character")

class PlanetsDetails(Base):
    __tablename__ = 'planetsdetails'
    planetid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    planet = relationship("Planets", back_populates="planetsdetails")

class StarShipsDetails(Base):
    __tablename__ = 'starshipsdetails'
    starshipid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    starship = relationship("StarShips", back_populates="starshipsdetails")

class CharactersDetails(Base):
    __tablename__ = 'charactersdetails'
    characterid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    character = relationship("Characters", back_populates="charactersdetails")
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
