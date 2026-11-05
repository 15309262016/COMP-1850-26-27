# Week 4, Session 1: 

# You are given an incomplete function isBond with a docstring. Your task
# is to complete the function based on the details in the docstring.


def isBond(intList):
    """
    This function accepts a list of integers and returns True if the
    sequence 0, 0, 7 appears in the list, in that order. Return False
    otherwise. The numbers do not need to be consecutive, but must appear
    in the specified order.
    """
    for first_zero_index in range(len(intList)):
        if intList[first_zero_index] != 0:
            continue

        for second_zero_index in range(first_zero_index + 1, len(intList)):
            if intList[second_zero_index] != 0:
                continue

            for later_index in range(second_zero_index + 1, len(intList)):
                if intList[later_index] == 7:
                    return True
            return False

    return False

# Check if the following lines of code produce the correct output
print(isBond([1, 2, 4, 0, 0, 7, 5]))   # True
print(isBond([1, 0, 2, 4, 0, 5, 7]))   # True
print(isBond([1, 7, 2, 0, 4, 5, 0]))   # False
