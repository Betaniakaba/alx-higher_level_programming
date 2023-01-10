#!/usr/bin/python3
"""
Module with a class BaseGeometry based on 
6-base_geometry.py
===========
Task Integer Validator
===========
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Area Calculation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Value validation (If input is integer)"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
