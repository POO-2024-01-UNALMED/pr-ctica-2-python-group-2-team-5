


#Clase persona como referencia para Doctor y Paciente
class Persona:
    #Inicializador.
    def __init__(self, cedula, nombre, tipoEps):
        self.cedula = cedula
        self.nombre = nombre
        self.tipoEps = tipoEps

    #Método bienvenida.
    def bienvenida(self):
        return "Bienvenid@, " + self.nombre

    #Setters y getters.
    def getCedula(self):
        return self.cedula

    def setCedula(self, cedula):
        self.cedula = cedula

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getTipoEps(self):
        return self.tipoEps

    def setTipoEps(self, tipoEps):
        self.tipoEps = tipoEps