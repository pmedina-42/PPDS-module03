from abc import ABC, abstractmethod


class Character(ABC):
    """Character"""
    def __init__(self, first_name, is_alive=True):
        """init"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """muere perra"""
        self.is_alive = False


class Stark(Character):
    """Stark"""
    def __init__(self, first_name, is_alive=True):
        """xDD"""
        super().__init__(first_name, is_alive)

    def die(self):
        """muere zorra"""
        self.is_alive = False
