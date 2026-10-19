# function implementation

def rectangle_area(width, height):
    """Return the area of a rectangle."""
    return width * height


def even_numbers_up_to(limit):
    """Return a list of even integers from 0 to the given limit."""
    return [number for number in range(0, limit + 1, 2)]


def mean_average(numbers):
    """Return the mean average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# testing the functions
print(f"Area is {rectangle_area(5, 8)}")
print(f"Even numbers up to 10 are {even_numbers_up_to(10)}")
values = [2, 4, 6, 8, 10]
print(f"Mean average of {values} is {mean_average(values)}")