#!/usr/bin/python3

"""
A Function that adds a new
attribute to an object
============
Task - Can I? - 101-add_attribute.py
============
"""


def add_attribute(a_class, name, value):
    """Add new attribute to an object"""

    cannot_add = {int, str, float, list, dict, tuple, frozenset, type, object}

    if type(a_class) in cannot_add:
        raise TypeError("can't add new attribute")

    a_class.__setattr__(name, value)
