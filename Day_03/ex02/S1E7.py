from S1E9 import Character


class Baratheon(Character):
    """
    Representing the Baratheon family.
    """
    def __init__(
        self,
        first_name,
        is_alive=True,
    ):
        """
        Inheriting class constructor : Baratheon.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        Method docstring : from alive to dead.
        """
        self.is_alive = False

    def __str__(self):
        """
        Represents the function by a string expliciting its action.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def __repr__(self):
        """
        This function is destinated to devs, it describs more fully what the
        function is used for.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"


class Lannister(Character):
    """
    Representing the Lannister family.
    """

    def __init__(
        self,
        first_name,
        is_alive=True,
    ):
        """
        Inheriting class constructor : Lannister.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Creates a new instance of the class.
        """
        return cls(first_name, is_alive)

    def __str__(self):
        """
        Represents the function by a string expliciting its action.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def __repr__(self):
        """
        This function is destinated to devs, it describs more fully what the
        function is used for.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def die(self):
        """
        Method docstring : from alive to dead.
        """
        self.is_alive = False
