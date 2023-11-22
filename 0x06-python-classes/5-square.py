#!/usr/bin/python3
""" Defines a class named square with private instance """


class Square:
    """ Contains a private instance attribute """
    def __init__(self, size=0):
        """ Method to initialize size """
        self.__size = size

    @property
    def size(self):
        """ Getter method for size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Method to return area of square """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square using # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                    print()
