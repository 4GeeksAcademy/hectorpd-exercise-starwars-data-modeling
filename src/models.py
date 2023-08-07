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

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer)
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

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)

class Planets(Base):
    __tablename__ = 'planets'
    planetid = Column(Integer)
    characteristics = Column(String, primary_key=True)
    characteristics = relationship("PlanetsDetails", back_populates="Planets")
    

class StarShips(Base):
    __tablename__ = 'starships'
    starshipsid = Column(Integer)
    characteristics = Column(String, primary_key=True)
    characteristics = relationship("StarShipsDetails", back_populates="StarShips")

class Characters(Base):
    __tablename__ = 'characters'
    charactersid = Column(Integer)
    characteristics = Column(String, primary_key=True)
    characteristics = relationship("CharactersDetails", back_populates="Characters")

class PlanetsDetails(Base):
    __tablename__ = 'planetsdetails'
    planetid = Column(Integer)
    name = Column(String(250), nullable=False)

class StarShipsDetails(Base):
    __tablename__ = 'starshipsdetails'
    starshipid = Column(Integer)
    name = Column(String(250), nullable=False)

class CharactersDetails(Base):
    __tablename__ = 'charactersdetails'
    characterid = Column(Integer)
    name = Column(String(250), nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
