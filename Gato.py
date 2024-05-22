"""
Clase Gato.
:author: Jaime Rabasco Ronda.
"""
class Gato:
    def __init__(self):
        self.__maulla = 'Miau'

    def maullar(self):
        return self.__maulla

g = Gato();
g.maullar();
