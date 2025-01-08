#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), nullable=False, primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False, primary_key=True)
)


class Place(BaseModel, Base):
    """Place class"""
    __tablename__ = 'places'
    name = Column(String(128), nullable=False)
    amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)
