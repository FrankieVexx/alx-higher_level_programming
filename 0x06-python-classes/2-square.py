#!/usr/bin/python3

# Done by: Francis Onyach <Franblog7@gmail.com>

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new square.
        Arguments: size (int): the size of the nes square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
