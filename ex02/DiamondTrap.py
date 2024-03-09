from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """el puto joffrey"""
    def __init__(self, first_name, is_alive=True):
        """init"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, colour: str):
        """seteame esta"""
        self.eyes = colour

    def get_eyes(self):
        """cogeme esta"""
        return self.eyes

    def set_hairs(self, colour: str):
        """seteame esta"""
        self.hairs = colour

    def get_hairs(self):
        """cogeme esta"""
        return self.hairs
