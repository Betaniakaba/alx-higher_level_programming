#!/usr/bin/python3
# 12-fizzbuzz.py
# Betania B kaba <betania.berhanu@outlook.com>

def fizzbuzz():

	   """ For Multiples of 3 and 5, print FizzBuzz.
	   """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
    elif number % 3 == 0:
            print("Fizz ", end="")
    elif number % 5 == 0:
            print("Buzz ", end="")
    else:
            print("{} ".format(number), end="")
