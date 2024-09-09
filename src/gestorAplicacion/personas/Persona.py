
from baseDatos import Serializador

#Clase persona como referencia para Doctor y Paciente
class Persona(Serializador):
    #Inicializador.
    def __init__(self, cedula, nombre, tipoEps):
        self.cedula = cedula
        self.nombre = nombre
        self.tipoEps = tipoEps

    #Método bienvenida.
    def bienvenida(self):
        return "Bienvenid@, " + self._nombre

    #Setters y getters.
    def getCedula(self):
        return self._cedula

    def setCedula(self, cedula):
        self._cedula = cedula

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getTipoEps(self):
        return self._tipoEps

    def setTipoEps(self, tipoEps):
        self._tipoEps = tipoEps