# Week 1.5, Session 1: Task 4

from geometry import Point, Circle

x = float(input("Enter the x-coordinate of the circle centre: "))
y = float(input("Enter the y-coordinate of the circle centre: "))
radius = float(input("Enter the radius of the circle: "))

centre = Point(x, y)
circle = Circle(radius, centre)

print(f"Area: {circle.area():.4f}")
print(f"Perimeter: {circle.perimeter():.4f}")
