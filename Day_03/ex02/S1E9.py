from abc import ABC, abstractmethod


class Character(ABC):
    """
    This class takes a first_name as first mandatory parameter, is_alive as a
    non mandatory second set to True

    """

    def __init__(self, first_name, is_alive=True):
        """
        Constructor docstring : parent class constructor.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(
        self,
    ):
        pass


class Stark(Character):
    """
    This class should inherit the Character class.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Inheriting class constructor : Stark.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Method docstring : from alive to dead.
        """
        self.is_alive = False
