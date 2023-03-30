"""
    The age of three people is entered by the user and it is determined who is the oldest and who are the minors.
"""

firstAge = int(input("Enter the first person's grade: "))
secondAge = int(input("Enter the second person's grade: "))
thirdAge = int(input("Enter the third person's grade: "))

oldest = max(firstAge, secondAge, thirdAge)
younger = min(firstAge, secondAge, thirdAge)

print("The oldest person's age is: ", oldest)
print("The younger person's age is: ", younger)