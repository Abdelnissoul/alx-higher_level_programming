#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''A Class for Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Starting a new rectanfgle
        with defining height and width (int)'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''setting uop the width for the rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''function gives the height of rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''x axis of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''y axis of the rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''function to see wether the value is validated'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''Gives the area of the rectangle.'''
        return self.width * self.height

    def display(self):
        '''Prints string of # of this rectangle.'''
        str = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(str, end='')

    def __str__(self):
        '''Returns string info about this rectangle.'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def update(self, *args, **kwargs):
        '''Updates instance attributes from no-keyword & keyword args.'''
        if args and len(args) != 0:
            i = 0
            for argum in args:
                if i == 0:
                    if argum is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = argum
                elif i == 1:
                    self.width = argum
                elif i == 2:
                    self.height = argum
                elif i == 3:
                    self.x = argum
                elif i == 4:
                    self.y = argum
                i += 1

        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        '''Returns the class reopresentatuion into dictionary.'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}