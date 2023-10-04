#!/usr/bin/python3

""" This creates a class called a Rectangle that defines a rectangle. """


class Rectangle:

    """ This class contains some class attributes, private
    instance attributes and  methods.

    Attributes:
        number_of_instances (int): the number of Rectangle instances
        print_symbol (any): the symbol for string representation

    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):

        """ Initializes the data.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.

        """

        type(self).number_of_instances += 1

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):

        """ Retrieves the value of width """

        return self.__width

    @width.setter
    def width(self, value):

        """ Sets the value of the width of the Rectangle class.

        Args:
            value (int): the value assigned to width.

        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """ Retrieves the value of height """

        return self.__height

    @height.setter
    def height(self, value):

        """ Sets the value of the height of the Rectangle class.

        Args:
            value (int): the value assigned to height.

        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        """ Returns the area of Rectangle

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.

        """

        return self.__width * self.__height

    def perimeter(self):

        """ Returns the perimeter of Rectangle using the class attributes

            Attributes:
                width (int): the width of the rectangle.
                height (int): the height of the rectangle.

        """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        """ Returns the biggest rectangle based on the area.

        Args:
            rect_1: The first Rectangle.
            rect_2: The second Rectangle.

        Raises:
            TypeError: if either rect_1 or rect_2 is not a
            Rectangle.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):

        """ Returns a new Rectangle instance with width == height == size.

        Args:
            size (int): The size of the sides of the Rectangle.
        """

        return (cls(size, size))

    def __str__(self):

        """ Returns a printable representation of a rectangle
        using the # character. """

        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):

        """ Returns a string representation of the rectangle. """

        obj = "Rectangle(" + str(self.__width)
        obj += ", " + str(self.__height) + ")"
        return (obj)

    def __del__(self):

        """ Prints a message when an instance has been destroyed """

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
