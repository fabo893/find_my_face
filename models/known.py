#!/usr/bin/python3
"""
    Known class
"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, BLOB


class Known(BaseModel, Base):
    """ Representation of known picture """
    __tablename__ = 'known_img'
    name = Column(String(128), nullable=False)
    image = Column(BLOB)


    def __init__(self, *args, **kwargs):
        """initializes known"""
        super().__init__(*args, **kwargs)