#!/usr/bin/python3
"""this is the base model class"""
import json
import turtle
import csv



class Base:
    """base class for id attribute"""
    
    __nb_objects = 0

    def __init__(self, id=None):
        """making a start for the bnew base"""
        if id is not None:
            self.id = id
        else:
            base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
