from gestorAplicacion.servicios.Cita import Cita


#Elaborado por Jerónimo

class CitaVacuna(Cita):
    #Atributos e inicializador
    def  __init__(self, fecha, paciente, vacuna):
        super().__init__(paciente, None, fecha)
        self.vacuna = vacuna



    def descripcionServicio(self):
        return f"{self.IDSERVICIO} - Vacuna: {self.vacuna.nombre} ({self.fecha})"


    def validarPago(self, paciente, idServicio):
        for citaVacuna in paciente.HISTORIACLINICA.historialVacunas:
            if citaVacuna.IDSERVICIO == idServicio:
                citaVacuna.estadoPago = True
                break
    #setters y getters

    def getVacuna(self):
        return self.vacuna

    def setVacuna(self, vacuna):
        self.vacuna = vacuna
