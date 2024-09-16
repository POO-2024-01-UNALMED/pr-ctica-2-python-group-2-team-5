from src.gestorAplicacion.servicios.Cita import Cita
from src.gestorAplicacion.personas.Persona import Persona


class Doctor(Persona):
    
    # Constructor
    def __init__(self, cedula, nombre, tipoEps, especialidad):
        super().__init__(cedula, nombre, tipoEps)
        self.especialidad = especialidad
        self.agendaDoctor = [
            Cita(self, None, "3 de Noviembre, 8:00 am"),
            Cita(self, None, "4 de Noviembre, 10:00 am"),
            Cita(self, None, "5 de Noviembre, 12:00 m"),
            Cita(self, None, "5 de Noviembre, 3:00 pm")
        ]

    # Muestra la agenda disponible de un doctor (citas que no tienen paciente asignado)
    def mostrarAgendaDisponible(self):
        agendaDisponible = []

        for cita in self.getAgendaDoctor():
            if cita.paciente is None:
                agendaDisponible.append(cita)
        if len(agendaDisponible) != 0:
            return agendaDisponible
        else:
            pass # Todo: Hacer la excepcion aca


    # Metodo que asigna el paciente a una determinada cita de un doctor
    def actualizarAgenda(self, pacienteAsignado, numeroCita, agendaDisponible):
        citaSeleccionada = None

        for cita in self.getAgendaDoctor():
            if cita.fecha == agendaDisponible[numeroCita - 1].fecha:
                cita.paciente = pacienteAsignado
                citaSeleccionada = cita
            return citaSeleccionada

    # Metodo para dar la bienvenida
    def bienvenida(self):
        return f"Bienvenido, Doctor {self.nombre}"

    # este es el to string
    def __str__(self):
        return f"Nombre: {self.nombre}\nCedula: {self.cedula}\nTipo de EPS: {self.tipoEps}\nEspecialidad: {self.especialidad}"

    # Métodos get y set
    def getEspecialidad(self):
        return self.especialidad

    def setEspecialidad(self, especialidad: str):
        self.especialidad = especialidad

    def getAgendaDoctor(self):
        return self.agendaDoctor

    def setAgendaDoctor(self, agenda):
        self.agendaDoctor = agenda


