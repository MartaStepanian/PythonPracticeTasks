"""
 Write a Python program that calculates the area of a circle based on the radius entered by the user.
"""


def calculate_area(radius):
    return 3.14 * radius ** 2


radius = float(input("Radius of the circle: "))

area = calculate_area(radius)

print("Area:", area)
