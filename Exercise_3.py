"""
    The school uses the following grading system:
    a) Below 25 - F
    b) 25-45 - E
    c) 45-50 - D
    d) 50-60 - C
    e) 60-80 - B
    f) Above 80 - A

    Ask the user to input their score and print their corresponding grade.
"""

grade = int(input("Score: "))

if 0 <= grade <= 25:
    print("F")
elif 25 < grade <= 45:
    print("E")
elif 45 < grade <= 50:
    print("D")
elif 50 < grade <= 60:
    print("C")
elif 60 < grade <= 80:
    print("B")
elif 80 < grade <= 100:
    print("A")
else:
    print("Wrong input")