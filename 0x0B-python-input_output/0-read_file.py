#!/usr/bin/python3
"""
7A function that reads a text file (UTF8) and prints it to stdout
========
Task - Read file - 0-read_file.py
========
"""


def read_file(filename=""):

    with open(filename,"r")as f:
        data = f.read()
        print(data, end="")
