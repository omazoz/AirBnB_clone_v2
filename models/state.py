#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ State class inhirit from base """
    if storage_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='delete')
    else:
        name = ""
        @property
        def cities(self):
            cities_list = []
            all_cities = models.storage.all(City).values()
            for city in all_cities:
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
