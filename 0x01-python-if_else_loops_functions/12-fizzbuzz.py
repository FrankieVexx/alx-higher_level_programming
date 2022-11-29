#!/usr/bin/python3                                                                                       
#Task 12 - FizzBuzz.py                                                                                   
#Francis O. Onyach <franblog7@gmail.com>

def fizzbuzz():
    """Print numbers from 1 to 100 separated with a space
    For multiples of 3 print Fizz in place of the number
    For multiples of 5 print Buzz in place of the number
    For multiplesof 3 and 5 print FIzzBuzz in place of the number 
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
