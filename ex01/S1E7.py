from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for init"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """muere perra"""
        self.is_alive = False

    @classmethod
    def create_baratheon(cls, first_name, is_alive=True):
        """creame esta"""
        return cls(first_name, is_alive)

    def __str__(self):
        """str"""
        return f"Vector: ('{self.family_name}', \
'{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """repr"""
        return f"Vector: ('{self.family_name}', \
'{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        """xDDD"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        """muere zorra"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """creame esta"""
        return cls(first_name, is_alive)

    def __str__(self):
        """str"""
        return f"Vector: ('{self.family_name}', \
'{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """repr"""
        return f"Vector: ('{self.family_name}', \
'{self.eyes}', '{self.hairs}')"
