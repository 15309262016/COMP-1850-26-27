# Worksheet 1.2: Task 2 Solution

import sys
from util import read_numbers

numbers = read_numbers()

if not numbers:
    sys.exit("Error: no numbers provided")

minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / len(numbers)
sorted_numbers = sorted(numbers)
mid = len(sorted_numbers) // 2

if len(sorted_numbers) % 2 == 0:
    median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
else:
    median = sorted_numbers[mid]

print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")
