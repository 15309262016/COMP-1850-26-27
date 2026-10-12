# Worksheet 1.2: Task 1 Solution

import sys

grade_text = input("Enter grade: ")

if not grade_text.isdecimal() or not 0 <= int(grade_text) <= 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

grade = int(grade_text)

if grade >= 70:
    result = "Distinction"
elif grade >= 40:
    result = "Pass"
else:
    result = "Fail"

print(f"{grade} is a {result}")
