#Importar lo necesario...
from enum import Enum

class CategoriaHabitacion(Enum):
    CAMILLA = 50000
    INDIVIDUAL = 150000
    DOBLE = 320000
    OBSERVACION = 500000
    UCI = 1300000
    UCC = 1500000

    def __init__(self, valor):
        self.valor = valor

    def getValor(self):
        return self.valor