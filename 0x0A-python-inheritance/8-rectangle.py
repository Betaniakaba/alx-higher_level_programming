#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
Module with a class Rectangle based
on 7-base-geometry.py

=======
Task Rectangle - 8-rectangle.py
=======
"""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
