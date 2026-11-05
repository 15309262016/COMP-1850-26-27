# Week 1.3, Session 2: Write User Information to a File

from pathlib import Path

name = input("Enter your name: ")
age = input("Enter your age: ")
favourite_colour = input("Enter your favourite colour: ")

output_file = Path(__file__).with_name("user_info.txt")

with output_file.open("w", encoding="utf-8") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Favourite colour: {favourite_colour}\n")

print(f"Your information has been saved to {output_file.name}.")

# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
