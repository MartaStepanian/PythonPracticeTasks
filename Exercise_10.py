"""
 Write a Python program to calculate the number of days between two dates.
"""


from datetime import datetime

date1 = input("First date (yyyy-mm-dd): ")
date2 = input("Second date (yyyy-mm-dd): ")

date1_obj = datetime.strptime(date1, '%Y-%m-%d')
date2_obj = datetime.strptime(date2, '%Y-%m-%d')

num_days = abs((date2_obj - date1_obj).days)

print("The number of days between", date1, "and", date2, "is", num_days)
