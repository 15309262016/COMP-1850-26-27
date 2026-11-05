# Week 1.3, Session 1: Task 2c

from pathlib import Path

# open a named text file for reading using open() function
# the `with` statement closes the file automatically as the block of code finishes executing
file_path = Path(__file__).with_name('file_data.txt')

with open(file_path, 'r') as file:

    while True:
        # read by character
        char = file.read(1)            # read exactly 1 character from the file
        if not char:
            break

        print(char)

# This example shows a common while-break pattern - reading from a file

# Test it - you can also modify the text file to add more data

# We will study this in more detail later on, but in this case we read character by character
# We use 'break' to exit the reading process at the end of the file.

# Why do we use an infinite 'while True' loop for this process?
# We do not know in advance how many characters are in the file, so we keep reading
# until the end-of-file marker is reached. At that point, file.read(1) returns an
# empty string, and the break statement exits the loop.