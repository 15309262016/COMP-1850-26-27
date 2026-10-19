"""
Python input() function demo.

The input() function reads a line of text from the user.
- It takes an optional prompt string.
- It always returns data as a string.
- You can convert it to int, float, etc. if needed.
"""

name = input("Enter your name: ")
print(f"Hello, {name}!")

age_text = input("Enter your age: ")
age = int(age_text)
print(f"You are {age} years old.")

# The input() function can also be used without a prompt:
city = input()
print(f"You live in {city}.")
