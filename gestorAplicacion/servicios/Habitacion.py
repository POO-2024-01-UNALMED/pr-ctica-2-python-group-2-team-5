#Importar lo necesario...
from gestorAplicacion.servicios.Servicio import Servicio
from gestorAplicacion.administracionHospital.CategoriaHabitacion import CategoriaHabitacion
from gestorAplicacion.administracionHospital.Hospital import Hospital
from gestorAplicacion.personas.Paciente import Paciente

#Clase Habitacion, que permite la revisión de disponibilidad de habitaciones y separación por categorías
class Habitacion(Servicio):
    #Inicializador.
    def __init__(self, numero, categoria, ocupada, dias, paciente):
        self._numero = numero
        self._categoria = categoria
        self._ocupada = ocupada
        self._dias = dias
        super().__init__(paciente)

    #Métodos.

    #Buscar habitaciones libres.
    @classmethod
    def BuscarHabitacionDisponible(cls, categoria):
        habitacionesDisponibles = []
        for habitacion in Hospital.getListaHabitaciones():
            if not habitacion.isOcupada() and habitacion.getCategoria() == categoria:
                habitacionesDisponibles.append(habitacion)
        if len(habitacionesDisponibles) == 0:
            return None
        return habitacionesDisponibles

    #Método para asignar la categoría de la haitación a reservar.
    @classmethod
    def BuscarOtraCategoria(cls, categoria): #Terminar método
        if categoria == "UCC":
            return CategoriaHabitacion.UCC

    #Métodos implementados de la clase Servicio.
    def validarPago(self, paciente, idServicio):
        if paciente.getHabitacionAsignada().getIdServicio() == idServicio:
            paciente.getHabitacionAsignada.setEstadoPago(True)

    def descripcionServicio(self):
        return f"{self._IDSERVICIO} - Habitación {self._numero} ocupada {self._dias} dias."

    #Setters y getters.
    def getNumero(self):
        return self._numero

    def setNumero(self, numero):
        self._numero = numero

    def getCategoria(self):
        return self._categoria

    def setCategoria(self, categoria):
        self._categoria = categoria

    def isOcupada(self):
        return self._ocupada

    def setOcupada(self, ocupada):
        self._ocupada = ocupada

    def getDias(self):
        return self._dias

    def setDias(self, dias):
        self._dias = dias
