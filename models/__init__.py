#!/usr/bin/python3
"""
    Initialization of the models package
"""

from models.engine.db_storage import DBStorage


storage = DBStorage()
storage.reload()