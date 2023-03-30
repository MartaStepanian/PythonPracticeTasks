"""
    The company has decided to give a 5% bonus to the employee if their work experience is more than 5 years.
     Please verify the employee's salary and work experience and print the amount of bonus.
"""

salary = int(input("Salary: "))
yearsOfExperience = int(input("Years of experience: "))

if yearsOfExperience > 5:
    reward = (salary * 5) / 100
    print("The amount of reward is: ", reward)
else:
    print("No reward")
