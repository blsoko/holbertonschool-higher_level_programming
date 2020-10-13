#!/usr/bin/python3
"""[class Rectangle that defines a rectangle]"""


class Rectangle:
    """[class Rectangle that defines a rectangle]"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """[class Rectangle that defines a rectangle]"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """[rectangle's width]"""
        return self.__width

    @width.setter
    def width(self, width):
        """[rectangle's width]"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """[rectangle's height]"""
        return self.__height

    @height.setter
    def height(self, height):
        """[rectangle's height]"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """[rectangle's area]"""
        return (self.__height * self.__width)

    def perimeter(self):
        """[rectangle's perimeter]"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """[bigger or equal applying isinstance method]"""
        count_1, count_2 = 0, 0
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        for i in str(rect_1):
            if i != '\n':
                count_1 += 1
        for i in str(rect_2):
            if i != '\n':
                count_2 += 1
        if count_2 > count_1:
            return rect_2
        else:
            return rect_1

    def __str__(self):
        """[return the representation of the rectangle in #]"""
        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return rectangle
        for j in range(self.__height):
            for k in range(self.__width):
                if self.print_symbol is str:
                    rectangle += self.print_symbol
                else:
                    rectangle += str(self.print_symbol)
            if j < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """[return string representation of the rectangle]"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """[destructor]"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
