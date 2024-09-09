
from baseDatos import Serializador


#Clase enfermedad que lleva registro de las enfermedades que se tratanen el hospital
class Enfermedad(Serializador):
    #Atributo de clase.
    enfermedadesRegistradas = []

    #Inicializador.
    def __init__(self, especialidad, nombre, tipologia):
        self.especialidad = especialidad
        self.nombre = nombre
        self.tipologia = tipologia
        self.enfermos = 1
        Enfermedad.enfermedadesRegistradas.append(self)

    #Métodos.

    #Método para contar los enfermos de determinada enfermedad.
    def nuevoEnfermo(self):
        self.enfermos += 1

    #Método __str__().
    def __str__(self):
        return self.nombre + " " + self.tipologia + " Especialidad que la trata: " + self.especialidad

    #Setters y getters.
    def getEspecialidad(self):
        return self.especialidad

    def setEspecialidad(self, especialidad):
        self.especialidad = especialidad

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getTipologia(self):
        return self.tipologia

    def setTipologia(self, tipologia):
        self.tipologia = tipologia

    def getEnfermos(self):
        return self.enfermos

    def setEnfermos(self, enfermos):
        self.enfermos = enfermos

    @classmethod
    def getEnfermedadesRegistradas(cls):
        return cls.enfermedadesRegistradas

    @classmethod
    def setEnfermedadesRegistradas(cls, enfermedadesRegistradas):
        cls.enfermedadesRegistradas = enfermedadesRegistradas