#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Module with a class BaseGeometry based
on 9-rectangle.py
===========
Task - Square #2 - 11-square.py
===========
"""


class Square(Rectangle):
    """Square class >> from Rectangle >>from BaseGeometry"""

    def __init__(self, size):
        """Instatiation method for the attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """rectangle area"""

        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
