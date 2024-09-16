from src.gestorAplicacion.servicios.CitaVacuna import CitaVacuna


#Clase vacuna para llevar un registro de las vacunas que se ofrecen en el hospital.
class Vacuna:
    def __init__(self, tipo, nombre, tipoEps, precio):
        self.tipo = tipo
        self.nombre = nombre
        self.precio = precio
        self.tipoEps = tipoEps
        self.agenda = [self.agenda.append(CitaVacuna("23 de Septiembre de 2024. Hora 7:45 am", None, self)),
        self.agenda.append(CitaVacuna("26 de Septiembre de 2024. Hora 11:20 am", None, self)),
        self.agenda.append(CitaVacuna("27 de Septiembre de 2024. Hora 8:45 am", None, self)),
        self.agenda.append(CitaVacuna("28 de Septiembre de 2024. Hora 3:45 pm", None, self)),
        self.agenda.append(CitaVacuna("29 de Septiembre de 2024. Hora 12:30 pm", None, self)),
        self.agenda.append(CitaVacuna("30 de Septiembre de 2024. Hora 10:00 am", None, self))
        ]
    #Métodos.

    #Buscar los horarios disponibles para aplicarse una vacuna.
    def mostrarAgendaDisponible(self):
        agendaDisponible = []
        for cita in self.agenda:
            if cita.paciente is None:
                agendaDisponible.append(cita)
        if len(agendaDisponible) != 0:
            return agendaDisponible
        else:
            pass # Todo: Haer la excepcion aca

    #Actualizar agenda al asignar una cita para vacunación.
    def actualizarAgenda(self, pacienteAsignado, numeroCita, agendaDisponible):
        citaAsignada = None
        for cita in self.agenda:
            if cita.fecha == agendaDisponible[numeroCita - 1].fecha:
                cita.paciente = pacienteAsignado
                citaAsignada = cita
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
        return self.precio

    def setPrecio(self, precio):
        self.precio = precio

    def getTipoEps(self):
        return self.tipoEps

    def setTipoEps(self, tipoEps):
        self.tipoEps = tipoEps

    def getAgenda(self):
        return self.agenda

    def setAgenda(self, agenda):
        self.agenda = agenda
