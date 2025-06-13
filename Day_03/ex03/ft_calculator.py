class Calculator:
    """
    Calculate simple arithmetics and returns a list.
    """

    def __init__(self, vector):
        """
        Method used when the class is instanciated, sets the attribut.
        """
        self.v = vector

    def __add__(self, other) -> None:
        """
        Add two vectors, pairing elements from both vectors to operate. If no
        second vector but a single element, a simple addition is done.
        """
        if isinstance(
            other, Calculator
        ):  # si l'other est de la meme nature que Calculator (un vecteur)
            if len(self.v) != len(other.v):
                raise ValueError("Compared others(tuples) are not the same size.")
            result = [a + b for a, b in zip(self.v, other.v)]
        else:
            result = [a + other for a in self.v]
        print(result)

    def __mul__(self, other) -> None:
        """
        Multiply two vectors, pairing elements from both vectors to operate.
        If no second vector but a single element, a simple multiplication is done.
        """
        if isinstance(other, Calculator):
            if len(self.v) != len(other.v):
                raise ValueError("Compared others(tuples) are not the same size.")
            result = [a * b for a, b in zip(self.v, other.v)]
        else:
            result = [a * other for a in self.v]
        print(result)

    def __sub__(self, other) -> None:
        """
        Substract two vectors, pairing elements from both vectors to operate.
        If no second vector but a single element, a simple soustraction is done.
        """
        if isinstance(other, Calculator):
            if len(self.v) != len(other.v):
                raise ValueError("Compared others(tuples) are not the same size.")
            result = [a - b for a, b in zip(self.v, other.v)]
        else:
            result = [a - other for a in self.v]
        print(result)

    def __truediv__(self, other) -> None:
        """
        Divise two vectors, pairing elements from both vectors to operate. If no
        second vector but a single element, a simple division is done.
        """
        if isinstance(other, Calculator):
            if len(self.v) != len(other.v):
                raise ValueError("Compared others(tuples) are not the same size.")
            for element in other.v:
                if element == 0:
                    raise ValueError("Division by zero is forbidden.")
            result = [a / b for a, b in zip(self.v, other.v)]
        else:
            if other == 0:
                raise ValueError("Division by zero is forbidden.")
            else:
                result = [a / other for a in self.v]
        print(result)
