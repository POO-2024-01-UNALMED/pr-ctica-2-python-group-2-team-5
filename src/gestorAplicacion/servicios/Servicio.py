#Importar lo necesario...
from abc import ABC, abstractmethod
from baseDatos import Serializador
from gestorAplicacion.personas import Paciente
from gestorAplicacion.administracionHospital import HistoriaClinica

#Clase abstracta Servicio que sirve de referencia para los demás servicios en el hospital
class Servicio(ABC, Serializador):
    #Atributo de clase.
    generadorID = 1000

    #Inicializador.
    def __init__(self, paciente):
        self.paciente = paciente
        self.idServicio = Servicio.generadorID + 1
        self.estadoPago = False

    #Métodos.

    #Métodos abstractos a implementar por las subclases.
    @abstractmethod
    def validarPago(self, paciente, idServicio):
        pass

    @abstractmethod
    def descripcionServicio(self):
        pass

    #Método para realizar una busqueda de los servicios sin pagar por el paciente.
    @classmethod
    def obtenerServiciosSinPagar(cls, paciente):
        historiaClinicaPaciente = paciente.getHistoriaClinica()
        listaServicios = []

        listaServicios.extend(historiaClinicaPaciente.getHistorialCitas())
        listaServicios.extend(historiaClinicaPaciente.getListaFormulas())
        if paciente.getHabitacionAsignada() != None:
            listaServicios.append(paciente.getHabitacionAsignada())
        listaServicios.extend(historiaClinicaPaciente.getHistorialVacunas())

        for servicio in listaServicios:
            if servicio.isEstadoPago():
                listaServicios.remove(servicio)

        return listaServicios

    #Setters y getters
    def getPaciente(self):
        return self.paciente

    def setPaciente(self, paciente):
        self.paciente = paciente

    def getIdServicio(self):
        return self.idServicio

    def isEstadoPago(self):
        return self.estadoPago

    def setEstadoPago(self, estadoPago):
        self.estadoPago = estadoPago