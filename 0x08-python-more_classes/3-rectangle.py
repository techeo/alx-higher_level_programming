#!/usr/bin/python3

"""
Python project 0x08 task 3.
"""

class Rectangle:
    """
    Represents a rectangle with width and height attributes.

    Args:
        width (int): Horizontal dimension of the rectangle, defaults to 0.
        height (int): Vertical dimension of the rectangle, defaults to 0.
    """

    def __init__(self, width=0, height=0):
        # Attribute assignment here invokes the setters defined below
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: Horizontal dimension of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): Horizontal dimension of the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            int: Vertical dimension of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): Vertical dimension of the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: Area of the rectangle, given by width * height.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: Perimeter of the rectangle, or 0 if either dimension is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """
        Formats a string of '#' and '\n' characters to represent the rectangle.

        Returns:
            str: String suitable for printing the rectangle (final newline omitted).
        """
        rectangle_str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                rectangle_str += '#'
            if self.__width != 0 and row < (self.__height - 1):
                rectangle_str += '\n'
        return rectangle_str

    def __str__(self):
        """
        Provides a string representation of the rectangle.

        Returns:
            str: Output of _draw_rectangle, creating a string suitable for printing.
        """
        return self._draw_rectangle()

