#!/usr/bin/python3
"""[class Rectangle that defines a rectangle]

Raises:
    TypeError: [width must be an integer
    ValueError: [width must be >= 0]
    TypeError: [height must be an integer]
    ValueError: [height must be >= 0]

Returns:
    [int]: self.__width & self.__height
"""


class Rectangle:
    """[class Rectangle that defines a rectangle]
    """
    def __init__(self, width=0, height=0):
        """[class Rectangle that defines a rectangle]

        Args:
            width (int): [description]. Defaults to 0.
            height (int): [description]. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """[summary]

        Returns:
            [int]: self.__width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """[summary]

        Args:
            width ([int]): rectangle's width

        Raises:
            TypeError: [width must be an integer]
            ValueError: [width must be >= 0]
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """[summary]

        Returns:
            [int]: self.__height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """[summary]

        Args:
            height ([int]): rectangle's height

        Raises:
            TypeError: [height must be an integer]
            ValueError: [height must be >= 0]
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
