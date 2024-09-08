from src.gestorAplicacion import Cita

class Doctor:
    
    # Constructor
    def __init__(self, cedula: int, nombre: str, tipo_eps: str, especialidad: str):
        self.cedula = cedula
        self.nombre = nombre
        self.tipo_eps = tipo_eps
        self.especialidad = especialidad
        self.agenda_doctor = [
            Cita(self, "3 de Abril, 8:00 am", None),
            Cita(self, "4 de Abril, 3:00 pm", None),
            Cita(self, "5 de Abril, 10:00 am", None)
        ]

    # Muestra la agenda disponible de un doctor (citas que no tienen paciente asignado)
    def mostrar_agenda_disponible(self):
        agenda_disponible = [cita for cita in self.agenda_doctor if cita.paciente is None]
        return agenda_disponible

    # Metodo que asigna el paciente a una determinada cita de un doctor
    def actualizar_agenda(self, paciente_asignado, numero_cita: int, agenda_disponible):
        if numero_cita <= 0 or numero_cita > len(agenda_disponible):
            return None  # por si se equivocan y escriben un numero demasiado grande
        cita_asignada = None
        for cita in self.agenda_doctor:
            if cita.fecha == agenda_disponible[numero_cita - 1].fecha:
                cita.paciente = paciente_asignado
                cita_asignada = cita
                break  

        return cita_asignada

    # Metodo para dar la bienvenida
    def bienvenida(self):
        return f"Bienvenido, Doctor {self.nombre}"

    # este es el to string
    def __str__(self):
        return f"Nombre: {self.nombre}\nCedula: {self.cedula}\nTipo de EPS: {self.tipo_eps}\nEspecialidad: {self.especialidad}"

    # Métodos get y set
    def get_especialidad(self):
        return self.especialidad

    def set_especialidad(self, especialidad: str):
        self.especialidad = especialidad

    def get_agenda_doctor(self):
        return self.agenda_doctor

    def set_agenda_doctor(self, agenda):
        self.agenda_doctor = agenda

