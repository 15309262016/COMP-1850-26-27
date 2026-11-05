# Week 1.5, Session 2: Task 5

from data import Dataset

filename = input("Enter a filename: ")
values = Dataset(filename)

print(f"Dataset size: {len(values)}")
print(f"Mean: {values.mean()}")
print(f"Median: {values.median()}")

for value in values:
    print(value)
