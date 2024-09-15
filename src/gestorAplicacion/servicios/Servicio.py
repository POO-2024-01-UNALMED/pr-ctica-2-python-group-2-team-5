from abc import ABC, abstractmethod


#Clase abstracta Servicio que sirve de referencia para los demás servicios en el hospital
class Servicio(ABC):
    #Atributo de clase.
    generadorID = 1000

    #Inicializador.
    def __init__(self, paciente):
        self.idServicio = Servicio.generadorID
        Servicio.generadorID += 1
        self.paciente = paciente
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
        historiaClinicaPaciente = paciente.historiaClinica
        listaServiciosSinPagar = []

        listaServiciosSinPagar.extend(historiaClinicaPaciente.historialCitas)
        listaServiciosSinPagar.extend(historiaClinicaPaciente.listaFormulas)
        if paciente.getHabitacionAsignada() != None:
            listaServiciosSinPagar.append(paciente.habitacionAsignada)
        listaServiciosSinPagar.extend(historiaClinicaPaciente.historialVacunas)

        for servicio in listaServiciosSinPagar:
            if servicio.isEstadoPago() == True:
                listaServiciosSinPagar.remove(servicio)

        return listaServiciosSinPagar

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