#!/usr/bin/python3
""" City Model"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """This class represents a City."""

    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)

    places = relationship('Place', backref='cities',
	cascade='all, delete-orphan')
