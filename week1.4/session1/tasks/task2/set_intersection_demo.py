"""
Python set.intersection() method demo.

Description:
    Return a new set containing the elements that are common to this set
    and one or more other sets (or iterable objects).

Inputs:
    The method is called on a set, and it can take one or more arguments.
    Each argument can be a set or any iterable such as a list, tuple, or
    another set.

Output:
    A new set containing only the shared elements.

Type note:
    The original sets remain unchanged. The result is a new set object.
"""

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}
set_c = {5, 7, 9}

common = set_a.intersection(set_b)
print("A ∩ B =", common)

common_three = set_a.intersection(set_b, set_c)
print("A ∩ B ∩ C =", common_three)

# You can also pass a list as an iterable
letters_a = {"a", "b", "c", "d"}
letters_b = ["c", "d", "e", "f"]
print("letters_a ∩ letters_b =", letters_a.intersection(letters_b))
