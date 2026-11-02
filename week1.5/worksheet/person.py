# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name, birth):
        """
        Initializes a Person with a name and a date of birth.
        Raises TypeError or ValueError if arguments are invalid.
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if name.strip() == "":
            raise ValueError("name cannot be empty")
        if not isinstance(birth, date):
            raise TypeError("birth must be a date object")
        self.name = name
        self.birth = birth

    def initials(self):
        """
        Returns the uppercased initials of each part of the person's name as a single string.
        """
        return ''.join([part[0].upper() for part in self.name.split() if part])

    def is_birthday(self):
        """
        Returns True if today is the person's birthday, False otherwise.
        """
        today = date.today()
        return today.month == self.birth.month and today.day == self.birth.day
