# Week 1.3, Session 1: Task 6b

values = [1,4,2,6,3,7]

print(values)

newval = []
for i in values:
    if i % 2 == 0:
        newval.append(2 * i)
    else:
        newval.append(i)

print(newval)

newval_comp = [2 * i if i % 2 == 0 else i for i in values]
print(newval_comp)

# This is the equivalent list comprehension to the for loop above.

