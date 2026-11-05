# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math


class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        """
        Create a Point object with x and y coordinates.

        Args:
            x (float): The x-coordinate.
            y (float): The y-coordinate.
        """
        self.x = x
        self.y = y

    def distance(self):
        """
        Calculate the distance of this point from the origin.

        Returns:
            float: The Euclidean distance from (0, 0) to the point.
        """
        return math.hypot(self.x, self.y)


class Circle:
    """
    A circle defined by its centre point and radius.
    """

    def __init__(self, radius, centre=Point(0.0, 0.0)):
        """
        Create a Circle object.

        Args:
            radius (float): The radius of the circle.
            centre (Point): The centre point of the circle.
        """
        self.radius = radius
        self.centre = centre

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


# Don't add any testing code to this file!
