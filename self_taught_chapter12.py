# 1.
class Apple:
    def __init__(self, color, size, weight, status):
        self.color = color
        self.size = size
        self.weight = weight
        self.status = status

# 2.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * math.pi

a_circle = Circle(2)
print(a_circle.area())

# 3.
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

a_triangle = Triangle(3, 2)
print(a_triangle.area())

# 4.
class Hexagon:
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return radius * 6

a_hexagon = Hexagon(6)
print(a_hexagon.calculate_perimeter())
