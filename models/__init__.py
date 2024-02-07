#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.filestorage import FileStorage


storage = FileStorage()
storage.reload()
