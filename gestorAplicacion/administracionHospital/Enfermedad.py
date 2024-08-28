#Importar lo necesario...


#Clase enfermedad que lleva registro de las enfermedades que se tratanen el hospital
class Enfermedad:
    #Atributo de clase.
    enfermedadesRegistradas = []

    #Inicializador.
    def __init__(self, especialidad, nombre, tipologia):
        self._especialidad = especialidad
        self._nombre = nombre
        self._tipologia = tipologia
        self._enfermos = 1
        Enfermedad.enfermedadesRegistradas.append(self)

    #Métodos.

    #Método para contar los enfermos de determinada enfermedad.
    def nuevoEnfermo(self):
        self._enfermos += 1

    #Método __str__().
    def __str__(self):
        return self._nombre + " " + self._tipologia + " Especialidad que la trata: " + self._especialidad

    #Setters y getters.
    def getEspecialidad(self):
        return self._especialidad

    def setEspecialidad(self, especialidad):
        self._especialidad = especialidad

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getTipologia(self):
        return self._tipologia

    def setTipologia(self, tipologia):
        self._tipologia = tipologia

    def getEnfermos(self):
        return self._enfermos

    def setEnfermos(self, enfermos):
        self._enfermos = enfermos

    @classmethod
    def getEnfermedadesRegistradas(cls):
        return cls.enfermedadesRegistradas

    @classmethod
    def setEnfermedadesRegistradas(cls, enfermedadesRegistradas):
        cls.enfermedadesRegistradas = enfermedadesRegistradas