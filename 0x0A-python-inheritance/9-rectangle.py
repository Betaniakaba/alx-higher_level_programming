#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Module with a class BaseGeometry based
on 7-base_geometry.py
=========
Task - Full Rectangle - 9-rectangle.py
=========
"""


class Rectangle(BaseGeometry):
    """Basegeometry inherited onto a Rectangle class"""

    def __init__(self, width, height):
        """Instantiation method for the attrubutes"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area is redefined in the parent class"""

        return self.__width * self.__height

    def __str__(self):
        """__str__ method represents the class objects as a string"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
