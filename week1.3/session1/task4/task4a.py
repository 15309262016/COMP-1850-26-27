# Week 1.3, Session 1: Task 4a

sum = 0

for k in range(0, 21, 2):
    sum = sum + k ** 2
    print(f"Running total: {sum}")

print(f"Final sum: {sum}")

# This sums the squares of even numbers up to and including 20
# and prints the running total at each iteration.