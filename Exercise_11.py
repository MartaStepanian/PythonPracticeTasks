"""
    Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17,
     return twice the absolute difference.
"""


number = float(input("Number: "))

if number <= 17:
    difference = 17 - number
else:
    difference = 2 * abs(17 - number)

print("Difference: ", difference)
