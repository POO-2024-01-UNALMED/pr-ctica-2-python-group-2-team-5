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
                    break

    def descripcionServicio(self):
            return f"{self.idServicio} --- Cita con el Dr. {self.doctor.nombre} el {self.fecha}"


#getters y setters

    @property
    def doctor(self):
        return self._doctor

    @doctor.setter
    def doctor(self, value):
        self._doctor = value

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        self._fecha = value

