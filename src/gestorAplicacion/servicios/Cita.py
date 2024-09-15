from src.gestorAplicacion.servicios.Servicio import Servicio


#Elaborado por Jeronimo

class Cita(Servicio):
    #inicializador y atributos
    def __init__(self, paciente, doctor, fecha):
        super().__init__(paciente)
        self.doctor = doctor
        self.fecha = fecha
#metodos
    def validarPago(self, paciente, idServicio):
            for cita in paciente.historiaClinica.historialCitas:
                if cita.idServicio == idServicio:
                    cita.estadoPago = True

    def descripcionServicio(self):
            return f"Cita con el Dr. {self.doctor.nombre} el {self.fecha}"
        
    def mensaje(self):
            return "del servicio cita médica"
        

#getters y setters

    def getDoctor(self):
        return self.doctor
    
    def setDoctor(self, doctor):
        self.doctor = doctor

    def getFecha(self):
        return self.fecha
    
    def setFecha(self, fecha):
        self.fecha = fecha

        
