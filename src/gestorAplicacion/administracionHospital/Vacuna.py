
from gestorAplicacion.servicios import CitaVacuna
from gestorAplicacion.personas import Paciente
from baseDatos import Serializador


#Clase vacuna para llevar un registro de las vacunas que se ofrecen en el hospital.
class Vacuna(Serializador):
    def __init__(self, tipo, nombre, precio, tipoEps):
        self.tipo = tipo
        self.nombre = nombre
        self.precio = precio
        self.tipoEps = tipoEps
        self.agenda = []

        self.agenda.append(CitaVacuna("23 de Septiembre de 2024. Hora 7:45 am", None, self))
        self.agenda.append(CitaVacuna("26 de Septiembre de 2024. Hora 11:20 am", None, self))
        self.agenda.append(CitaVacuna("27 de Septiembre de 2024. Hora 8:45 am", None, self))
        self.agenda.append(CitaVacuna("28 de Septiembre de 2024. Hora 3:45 pm", None, self))
        self.agenda.append(CitaVacuna("29 de Septiembre de 2024. Hora 12:30 pm", None, self))
        self.agenda.append(CitaVacuna("30 de Septiembre de 2024. Hora 10:00 am", None, self))

    #Métodos.

    #Buscar los horarios disponibles para aplicarse una vacuna.
    def mostrarAgendaDisponible(self):
        agendaDisponible = []
        for i in self.agenda:
            if i.getPaciente() == None:
                agendaDisponible.append(i)
        return agendaDisponible

    #Actualizar agenda al asignar una cita para vacunación.
    def actualizarAgenda(self, pacienteAsignado, numeroCita, agendaDisponible):
        citaAsignada = None
        for i in self.agenda:
            if i.getFecha() == agendaDisponible[numeroCita - 1].getFecha():
                i.setPaciente(pacienteAsignado)
                citaAsignada = i
        return citaAsignada

    #Setters y getters
    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio):
        self.precio = precio

    def getTipoEps(self):
        return self._tipoEps

    def setTipoEps(self, tipoEps):
        self.tipoEps = tipoEps

    def getAgenda(self):
        return self.agenda

    def setAgenda(self, agenda):
        self.agenda = agenda
