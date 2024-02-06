#!/usr/bin/python3
"""Defining a class Student."""


class Student:
    """Class represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student
        by defining their full name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function to get the dictionary of the Student

        Args:
            attrs : list of The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Reload from json to the attributes of the Student."""
        for k, val in json.items():
            setattr(self, k, val)
