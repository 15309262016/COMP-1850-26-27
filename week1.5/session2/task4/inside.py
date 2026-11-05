# Week 1.5, Session 2: Task 4

from geometry import Circle, Point

circle = Circle(5, Point(0, 0))
inside_point = Point(2, 3)
outside_point = Point(6, 0)

print(inside_point in circle)
print(outside_point in circle)
