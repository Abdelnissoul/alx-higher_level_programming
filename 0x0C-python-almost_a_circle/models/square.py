#!/usr/bin/python3
"""module defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class odf a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """making a new Square.

        Args:
            size : The size of the Square.(int)
            x : The x axis of the Square.(int)
            y : The y axis of the Square.(int)
            id : The id of the Square.(int)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """setting up the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating the Square."""
        if args and len(args) != 0:
            i = 0
            for argum in args:
                if i == 0:
                    if argum is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = argum
                elif i == 1:
                    self.size = argum
                elif i == 2:
                    self.x = argum
                elif i == 3:
                    self.y = argum
                i += 1

        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif key == "size":
                    self.size = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """Return the square representation to the dictiopnarty"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}

    def __str__(self):
        """Returns string infos about this square"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)