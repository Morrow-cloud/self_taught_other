# 13- 1, 2, 3.
# 14- 1, 2
class Shape:
    def what_am_i(self):
        return 'I am a shape'

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return self.height * 2 + self.width * 2

class Square(Shape):
    square_list = []
    def __init__(self, length):
        self.length = length
        square_list.append(self)

    def calculate_perimeter(self):
        return self.length * 4

    def change_size(self, add_length):
        self.length += add_length

    def __repr__(self):
        return '{0} by {0} by {0} by {0}'.format(self.length)

a_rectangle = Rectangle(2, 4)
print(a_rectangle.calculate_perimeter())

a_square = Square(2)
print(a_sqaure.calculate_perimeter())

print(a_rectangle.what_am_i())
print(a_square.what_am_i())

# 4.
class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

deep_impact = Horse()
y_take = Rider()
print(deep_impact.rider.name)

# 14- 3.
def a_is_b(a, b):
    return a is b
