class calculator:
    """calculame esta"""
    def __init__(self, vector):
        """init"""
        self.vector = vector

    def __add__(self, object) -> None:
        """suma tu madre + puta"""
        try:
            self.vector = [val + object for val in self.vector]
            print(self.vector)
        except Exception:
            print('Bro?')

    def __mul__(self, object) -> None:
        """multiplica tu madre x guarra"""
        try:
            self.vector = [val * object for val in self.vector]
            print(self.vector)
        except Exception:
            print('Bro?')

    def __sub__(self, object) -> None:
        """resta tu madre - dignidad = tu madre también porque no tiene"""
        try:
            self.vector = [val - object for val in self.vector]
            print(self.vector)
        except Exception:
            print('Bro?')

    def __truediv__(self, object) -> None:
        """divide"""
        try:
            if object == 0:
                raise ValueError("Division by zero is not allowed")
            self.vector = [val / object for val in self.vector]
            print(self.vector)
        except ValueError as ve:
            print(f'{type(ve).__name__}: {ve}')
        except Exception:
            print('Bro?')
