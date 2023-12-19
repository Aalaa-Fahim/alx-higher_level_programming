#!/usr/bin/python3
"""A Square module."""


class Square:
    """Defines a Square class."""

    def __init__(self, size=0):
        """Method.

        Args:
            size: the length of a side of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Property for the length of the square's side.

        Raises:
            TypeError: if the size is not an integer value
            ValueError: if the size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The area of this square.

        Returns:
            the size squared.
        """
        return self.__size ** 2

    def my_print(self):
        """prints the square."""
        for i in range(self.size):
            for k in range(self.size):
                print("#", end="\n" if k is self.size - 1 and i != k else "")
        print()
