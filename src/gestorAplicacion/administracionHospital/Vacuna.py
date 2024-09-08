
from src.gestorAplicacion import Cita_Vacuna


#Clase vacuna para llevar un registro de las vacunas que se ofrecen en el hospital.
class Vacuna:
    def __init__(self, tipo, nombre, precio, tipoEps):
        self._tipo = tipo
        self._nombre = nombre
        self._precio = precio
        self._tipoEps = tipoEps
        self._agenda = []

        self._agenda.append(Cita_Vacuna("23 de Agosto de 2024. Hora 7:45 am", None, self))
        self._agenda.append(Cita_Vacuna("26 de Agosto de 2024. Hora 11:20 am", None, self))
        self._agenda.append(Cita_Vacuna("27 de Agosto de 2024. Hora 8:45 am", None, self))
        self._agenda.append(Cita_Vacuna("28 de Agosto de 2024. Hora 3:45 pm", None, self))
        self._agenda.append(Cita_Vacuna("29 de Agosto de 2024. Hora 12:30 pm", None, self))
        self._agenda.append(Cita_Vacuna("30 de Agosto de 2024. Hora 10:00 am", None, self))

    #Métodos.

    #Buscar los horarios disponibles para aplicarse una vacuna.
    def mostrarAgendaDisponible(self):
        agendaDisponible = []
        for i in self._agenda:
            if i.getPaciente() == None:
                agendaDisponible.append(i)
        return agendaDisponible

    #Actualizar agenda al asignar una cita para vacunación.
    def actualizarAgenda(self, pacienteAsignado, numeroCita, agendaDisponible):
        citaAsignada = None
        for i in self._agenda:
            if i.getFecha() == agendaDisponible[numeroCita - 1].getFecha():
                i.setPaciente(pacienteAsignado)
                citaAsignada = i
        return citaAsignada

    #Setters y getters
    def getTipo(self):
        return self._tipo

    def setTipo(self, tipo):
        self._tipo = tipo

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio):
        self._precio = precio

    def getTipoEps(self):
        return self._tipoEps

    def setTipoEps(self, tipoEps):
        self._tipoEps = tipoEps

    def getAgenda(self):
        return self._agenda

    def setAgenda(self, agenda):
        self._agenda = agenda
