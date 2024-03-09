class calculator:
    @staticmethod
    def dotproduct(V1, V2):
        """multiplicame esta"""
        try:
            result = sum(x * y for x, y in zip(V1, V2))
            print(f"Dot product is: {result}")
        except Exception:
            print('Algo raro has metido')

    @staticmethod
    def add_vec(V1, V2):
        """sumame esta"""
        try:
            result = [float(x) + float(y) for x, y in zip(V1, V2)]
            print(f"Add Vector is : {result}")
        except Exception:
            print('Algo raro has metido')

    @staticmethod
    def sous_vec(V1, V2):
        """restame esta"""
        try:
            result = [float(x) - float(y) for x, y in zip(V1, V2)]
            print(f"Sous Vector is: {result}")
        except Exception:
            print('Algo raro has metido')
