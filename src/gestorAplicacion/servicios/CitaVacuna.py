from src.gestorAplicacion import Vacuna
from src.gestorAplicacion import Paciente
from src.gestorAplicacion import Cita
#elaborado por Jerónimo

class Cita_Vacuna(Cita):
    #Atributos e inicializador

    def __init__(self, fecha: str, paciente: Paciente, vacuna: Vacuna):
        super().__init__(None, fecha, paciente)# El primer argumento de super() se omite al no ser necesario
        self.vacuna = vacuna

    def validar_pago(self, paciente, id_servicio):
        for cita_vacuna in paciente.historia_clinica.historial_vacunas:
            if cita_vacuna.id_servicio == id_servicio:
                cita_vacuna.estado_pago = True

    def descripcion_servicio(self):
        return f"{self.id_servicio} - Vacuna: {self.vacuna.nombre} ({self.fecha})"
    
    def mensaje(self):
        return "del servicio de vacunas"

