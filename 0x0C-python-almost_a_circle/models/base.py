#!/usr/bin/python3
"""this is the base model class"""
import json
import turtle
import csv
from json import dumps, loads


class Base:
    """base class for id attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """making a start for the bnew base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returning JSON list of dicts.

        Args:
            list_dictionaries: A list for dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saving the JSON list of objects to a file.

        Args:
            list_objs: the list of objects inherited from Base.
        """
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Return the beginning stats of a JSON string
        ///this for taking it back"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """function returns from a dictionary of attributes.

        Args:
            **dictionary : dictionary value of attributes.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes from a file of JSON strings.

        Reads from `<cls.__name__>.json`.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """function that saves objects (to csv file).

        Args:
            list_objs : A list of object inherited from base.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """function loads from a CSV file.
        and
        Reads from `<cls.__name__>.csv`.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles: list of Rectangle objects.
            list_squares: list of Squares objects.
        """
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for a in list_rectangles + list_squares:
            turt = turtle.Turtle()
            turt.color((randrange(255), randrange(255), randrange(255)))
            turt.pensize(1)
            turt.penup()
            turt.pendown()
            turt.setpos((a.x + turt.pos()[0], a.y - turt.pos()[1]))
            turt.pensize(10)
            turt.forward(a.width)
            turt.left(90)
            turt.forward(a.height)
            turt.left(90)
            turt.forward(a.width)
            turt.left(90)
            turt.forward(a.height)
            turt.left(90)
            turt.end_fill()

        time.sleep(5)

