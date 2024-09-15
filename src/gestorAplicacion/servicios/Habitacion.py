from symbol import return_stmt

from src.gestorAplicacion.administracionHospital.CategoriaHabitacion import CategoriaHabitacion
from src.gestorAplicacion.administracionHospital.Hospital import Hospital
from src.gestorAplicacion.servicios.Servicio import Servicio


#Clase Habitacion, que permite la revisión de disponibilidad de habitaciones y separación por categorías
class Habitacion(Servicio):
    #Inicializador.
    def __init__(self, numero, categoria, ocupada, paciente, dias):
        super().__init__(paciente)
        self.numero = numero
        self.categoria = categoria
        self.ocupada = ocupada
        self.dias = dias
        

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
    def BuscarOtraCategoria(cls, categoria):
        if categoria == "UCC":
            return CategoriaHabitacion.UCI
        elif categoria == "UCI":
            return CategoriaHabitacion.OBSERVACION
        elif categoria == "OBSERVACION":
            return CategoriaHabitacion.DOBLE
        elif categoria == "DOBLE":
            return CategoriaHabitacion.INDIVIDUAL
        elif categoria == "INDIVIDUAL":
            return CategoriaHabitacion.CAMILLA
        else:
            return None

    #Métodos implementados de la clase Servicio.
    def validarPago(self, paciente, idServicio):
        if paciente.getHabitacionAsignada().getIdServicio() == idServicio:
            paciente.getHabitacionAsignada.setEstadoPago(True)

    def descripcionServicio(self):
        return f"{self.idServicio} - Habitación {self.numero} ocupada {self.dias} dias."

    #Setters y getters.
    def getNumero(self):
        return self.numero

    def setNumero(self, numero):
        self.numero = numero

    def getCategoria(self):
        return self.categoria

    def setCategoria(self, categoria):
        self.categoria = categoria

    def isOcupada(self):
        return self.ocupada

    def setOcupada(self, ocupada):
        self.ocupada = ocupada

    def getDias(self):
        return self.dias

    def setDias(self, dias):
        self.dias = dias

    def getPaciente(self):
        return self.paciente

    def setPaciente(self, paciente):
        self.paciente = paciente