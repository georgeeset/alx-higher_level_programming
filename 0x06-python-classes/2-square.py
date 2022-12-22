#!/usr/bin/python3
"""Define a class called Square"""

class Square():
        """Represents a square.
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """

        def __init__(self, size = 0):
            """Initializes the data. raise exception
            if size is not an integer
            """
            if not isinstance(size, int):
                    raise TypeError("size must be an integer")
            elif size < 0:
                    raise ValueError("size must be >= 0")
            else:
                    self.__size = size
