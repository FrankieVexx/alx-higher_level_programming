#!/usr/bin/python3
#Task 12 - FizzBuzz.py
#Francis O. Onyach <franblog7@gmail.com>

def fizzbuzz():
    """Prints out numbers from 1 t0 100 separated with a space

    For multiples of 3 replace the number with Fizz.
    For multiples of 5 replace number with Buzz.
    For multiples of 3 and 5 replacenumber with FizzBuzz. """

    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{}".format(number), end="")
