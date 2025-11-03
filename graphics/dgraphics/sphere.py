import math

def area(radius):
    return 4 * math.pi * radius ** 2

def perimeter(radius):
    # A sphere has no perimeter; we’ll return circumference of a great circle
    return 2 * math.pi * radius
