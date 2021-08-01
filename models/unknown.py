#!/usr/bin/python3
"""
    Unknown class
"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, BLOB, ForeignKey


class Unknown(BaseModel, Base):
    """ Representation of unknown picture """
    __tablename__ = 'unknown_img'
    name = Column(String(128), nullable=False)
    image = Column(BLOB)

    def __init__(self, *args, **kwargs):
        """initializes unknown"""
        super().__init__(*args, **kwargs)