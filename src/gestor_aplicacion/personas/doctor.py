
from src.gestor_aplicacion.personas.persona import Persona
from src.gestor_aplicacion.servicios.cita import Cita
from src.manejo_errores.error_aplicacion import SinAgenda


# Clase destinada a crear doctores

class Doctor(Persona):

    # Atributos y constructor
    def __init__(self, cedula, nombre, tipo_eps, especialidad):
        super().__init__(cedula, nombre, tipo_eps)
        self._especialidad = especialidad
        self._agenda = [
            Cita(None, self, "3 de Abril, 8:00 am"),
            Cita(None, self, "4 de Abril, 3:00 pm"),
            Cita(None, self, "5 de Abril, 10:00 am")
        ]

    # Metodos

    # Muestra la agenda disponible de un doctor (citas que no tienen paciente asignado)
    # No recibe ningun parametro y devuelve una lista de objetos Cita
    def mostrar_agenda_disponible(self):
        agenda_disponible = []
        for cita in self.agenda:
            if cita.paciente is None:
                agenda_disponible.append(cita)
        if len(agenda_disponible) != 0:
            return agenda_disponible
        else:
            raise SinAgenda()

    # Método que asigna el paciente a una determinada cita de un doctor
    # recibe un objeto de Paciente, un entero y una lista de Cita_Vacuna
    def actualizar_agenda(self, paciente_seleccionado, numero_cita, agenda_disponible):
        cita_seleccionada = None
        for cita in self.agenda:
            if cita.fecha == agenda_disponible[numero_cita - 1].fecha:
                cita.paciente = paciente_seleccionado
                cita_seleccionada = cita
        return cita_seleccionada

    def __str__(self):
        return self._nombre + " Especialidad: " + self._especialidad

    @property
    def agenda(self):
        return self._agenda

    @agenda.setter
    def agenda(self, value):
        self._agenda = value

    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, value):
        self._especialidad = value

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


