from gestorAplicacion.servicios import Cita

class Doctor:
    
    # Constructor
    def __init__(self, cedula: int, nombre: str, tipoEps: str, especialidad: str):
        self.cedula = cedula
        self.nombre = nombre
        self.tipoEps = tipoEps
        self.especialidad = especialidad
        self.agendaDoctor = [
            Cita(self, "3 de Noviembre, 8:00 am", None),
            Cita(self, "4 de Noviembre, 3:00 pm", None),
            Cita(self, "5 de Noviembre, 10:00 am", None)
        ]

    # Muestra la agenda disponible de un doctor (citas que no tienen paciente asignado)
    def mostrarAgendaDisponible(self):
        agendaDisponible = [cita for cita in self.agendaDoctor if cita.paciente is None]
        return agendaDisponible

    # Metodo que asigna el paciente a una determinada cita de un doctor
    def actualizar_agenda(self, pacienteAsignado, numeroCita: int, agendaDisponible):
        if numeroCita <= 0 or numeroCita > len(agendaDisponible):
            return None  # por si se equivocan y escriben un numero demasiado grande
        citaAsignada = None
        for cita in self.agendaDoctor:
            if cita.fecha == agendaDisponible[numeroCita - 1].fecha:
                cita.paciente = pacienteAsignado
                citaAsignada = cita
                break  

        return citaAsignada

    # Metodo para dar la bienvenida
    def bienvenida(self):
        return f"Bienvenido, Doctor {self.nombre}"

    # este es el to string
    def __str__(self):
        return f"Nombre: {self.nombre}\nCedula: {self.cedula}\nTipo de EPS: {self.tipoEps}\nEspecialidad: {self.especialidad}"

    # Métodos get y set
    def get_especialidad(self):
        return self.especialidad

    def set_especialidad(self, especialidad: str):
        self.especialidad = especialidad

    def get_agenda_doctor(self):
        return self.agendaDoctor

    def set_agenda_doctor(self, agenda):
        self.agendaDoctor = agenda

