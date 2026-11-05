# Week 1.5, Session 1: Task 3

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

    def distance_to(self, other):
        """
        Calculate the distance between this point and another point.

        Args:
            other (Point): The point to calculate the distance to.

        Returns:
            float: The Euclidean distance between the two points.
        """
        return math.hypot(self.x - other.x, self.y - other.y)


# Finally, add code here to demonstrate use of Point
point_a = Point(3, 4)
point_b = Point(0, 0)

print(f"Point A coordinates: ({point_a.x}, {point_a.y})")
print(f"Distance from origin: {point_a.distance()}")
print(f"Distance from A to B: {point_a.distance_to(point_b)}")
