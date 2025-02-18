#!/usr/bin/python3
""" State Module for HBNB clone project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class for hbnb clone project """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)

        cities = relationship("City", cascade="all, delete", backref="states")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state module"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Returns the list of City objects linked to the current State
            Returns: cities in a state
            """
            from models.city import City

            return [
                city for city in models.storage.all(City).values()
                if city.state_id == self.id
            ]
