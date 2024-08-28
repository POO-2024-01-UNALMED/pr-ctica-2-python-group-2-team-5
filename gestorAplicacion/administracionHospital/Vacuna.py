#Importar lo necesario...


#Clase vacuna para llevar un registro de las vacunas que se ofrecen en el hospital.
class Vacuna:
    def __init__(self, tipo, nombre, precio, tipoEps):
        self._tipo = tipo
        self._nombre = nombre
        self._precio = precio
        self._tipoEps = tipoEps
        self._agenda = []

        self._agenda.append(CitaVacuna("23 de Agosto de 2024. Hora 7:45 am", None, self))
        self._agenda.append(CitaVacuna("26 de Agosto de 2024. Hora 11:20 am", None, self))
        self._agenda.append(CitaVacuna("27 de Agosto de 2024. Hora 8:45 am", None, self))
        self._agenda.append(CitaVacuna("28 de Agosto de 2024. Hora 3:45 pm", None, self))
        self._agenda.append(CitaVacuna("29 de Agosto de 2024. Hora 12:30 pm", None, self))
        self._agenda.append(CitaVacuna("30 de Agosto de 2024. Hora 10:00 am", None, self))

    #Métodos.

    #Buscar los horarios disponibles para aplicarse una vacuna.
    def mostrarAgendaDisponible(self):
        agendaDisponible = []