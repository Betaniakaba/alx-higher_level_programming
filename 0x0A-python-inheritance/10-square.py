#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Module with a class BaseGeometry based
on 9-rectangle.py
=========
Task - Square #1 - 10-square.py
=========
"""


class Square(Rectangle):
    """BaseGeometry inherited onto Rectangle inherited by Square class"""

    def __init__(self, size):
        """Instantiation method for the attrubutes"""

    super().__init__(size, size)
    self.integer_validator("size", size)
    self.__size = size

    def area(self):
        """rectangle area"""

        return self.__size ** 2
