from gestorAplicacion.personas import Doctor
from gestorAplicacion.servicios import Servicio

#Elaborado por Jeronimo

class Cita(Servicio):
    #inicializador y atributos
    def __init__(self, doctor, fecha, paciente):
        super().__init__(paciente)
        self.doctor = doctor
        self.fecha = fecha
#metodos
        def validar_pago(self, paciente, id_servicio):
            for cita in paciente.historia_clinica.getHistorialCitas:
                if cita.id_servicio == id_servicio:
                    cita.estado_pago = True

        def descripcion_servicio(self):
            return f"Cita con el Dr. {self.doctor.nombre} el {self.fecha}"
        
        def mensaje(self):
            return "del servicio cita médica"
        
