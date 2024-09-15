from gestorAplicacion.servicios.Cita import Cita


#Elaborado por Jerónimo

class CitaVacuna(Cita):
    #Atributos e inicializador

    def __init__(self, fecha, paciente, vacuna):
        super().__init__(None, None, None)
        self.vacuna = vacuna

    def validarPago(self, paciente, idServicio):
        for citaVacuna in paciente.historiaClinica.historialVacunas:
            if citaVacuna.idServicio == idServicio:
                citaVacuna.estadoPago = True
                break

    def descripcionServicio(self):
        return f"{self.idServicio} - Vacuna: {self.vacuna.nombre} ({self.fecha})"


    #setters y getters

    def getVacuna(self):
        return self.vacuna
    
    def setVacuna(self, vacuna):
        self.vacuna = vacuna
