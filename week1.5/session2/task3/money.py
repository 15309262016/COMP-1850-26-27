# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        if isinstance(pounds, bool) or not isinstance(pounds, int):
            raise TypeError("pounds must be an integer.")
        if pounds < 0:
            raise ValueError("pounds must not be negative.")
        if isinstance(pence, bool) or not isinstance(pence, int):
            raise TypeError("pence must be an integer.")
        if pence < 0 or pence > 99:
            raise ValueError("pence must be between 0 and 99.")

        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        return f"£{self.pounds}.{self.pence:02d}"

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        if not isinstance(other, Money):
            raise TypeError("other must be a Money object.")

        total_pence = self.pence + other.pence
        pounds = self.pounds + other.pounds + (total_pence // 100)
        pence = total_pence % 100

        return Money(pounds, pence)
