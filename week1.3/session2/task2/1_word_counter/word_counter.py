# Week 1.3, Session 2: Word Counter

from pathlib import Path

# We want to read in a text file, and calculate how many words are in it.
# You can use any of the .txt files to test this - or even make your own.

filename = input("Enter the filename: ")
script_dir = Path(__file__).resolve().parent
file_path = Path(filename)

if not file_path.is_absolute():
    candidate = script_dir / filename
    if candidate.exists():
        file_path = candidate

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

words = content.split()
word_count = len(words)

print(f"The file contains {word_count} words.")

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210