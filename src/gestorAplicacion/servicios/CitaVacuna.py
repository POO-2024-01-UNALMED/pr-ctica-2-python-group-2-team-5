from gestorAplicacion.administracionHospital import Vacuna
from gestorAplicacion.personas import Paciente
from gestorAplicacion import Cita
#Elaborado por Jerónimo

class CitaVacuna(Cita):
    #Atributos e inicializador

    def __init__(self, fecha: str, paciente, vacuna):
        super().__init__(None, fecha, paciente)# El primer argumento de super() se omite al no ser necesario
        self.vacuna = vacuna

    def validarPago(self, paciente, idServicio):
        for citaVacuna in paciente.historiaClinica.historialVacunas:
            if citaVacuna.id_servicio == idServicio:
                citaVacuna.estado_pago = True

    def descripcionServicio(self):
        return f"{self.idServicio} - Vacuna: {self.vacuna.nombre} ({self.fecha})"
    
    def mensaje(self):
        return "del servicio de vacunas"


    #setters y getters

    def getVacuna(self):
        return self.vacuna
    
    def setVacuna(self, vacuna):
        self.vacuna = vacuna
