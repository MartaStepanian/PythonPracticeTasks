"""
    Take the values of the length and width from the user and check if it is a square or not.
"""

length = int(input("Enter the length of rectangle: "))
height = int(input("Enter the height of rectangle: "))

if length == height:
    print("The rectangle is a square.")
else:
    print("The rectangle is not a square.")