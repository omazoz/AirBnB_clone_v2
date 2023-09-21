#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

class Amenity(BaseModel, Base):
    """Amenity class
    """
    if storage_type == 'db':

        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""
