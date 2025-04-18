from collections import namedtuple

# Create a namedtuple class
Point = namedtuple("Point", ["x", "y"])

# Create an instance of the Point class
p = Point(10, 20)

# Access elements by name
print(p.x)  # Output: 10
print(p.y)  # Output: 20

# Access elements by index
print(p[0])  # Output: 10
print(p[1])  # Output: 20
