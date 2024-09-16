# Clase Hospital que lleva el registro general de servicios y personas.
from src.baseDatos.Serializador import Serializador

class Hospital:
    #Atributo de clase.
    habitaciones = []

    #Inicializador.
    def __init__(self):
        #Deserializador aqui.
        self.listaDoctores = []
        self.listaPacientes = []
        self.listaMedicamentos = []
        self.listaVacunas = []
        Serializador.serializar(self)

    #Métodos.

    #Buscar doctores por especialidad.
    def buscarTipoDoctor(self, especialidad):
        doctoresDisponibles = []
        for doctor in self.listaDoctores:
            if doctor.especialidad == especialidad:
                doctoresDisponibles.append(doctor)
        return doctoresDisponibles

    #Buscar paciente con su número de cedula.
    def buscarPaciente(self, cedula):
        for paciente in self.listaPacientes:
            if paciente.getCedula() == cedula:
                return paciente
        return None # todo: Hacer el manejo de excepciones aca

    #Buscar doctor con la cédula.
    def buscarDoctor(self, cedula):
        for doctor in self.listaDoctores:
            if doctor.cedula == cedula:
                return doctor
        return None # todo: Hacer el manejo de excepciones aca

    #Buscar vacuna por el nombre.
    def buscarVacuna(self, nombre):
        for vacuna in self.listaVacunas:
            if vacuna.getNombre() == nombre:
                return vacuna
        return None # todo: Hacer el manejo de excepciones aca

    #Buscar medicamentos dispinibles.
    def medicamentosDisponibles(self):
        disponibles = []
        for medicamento in self.listaMedicamentos:
            if medicamento.cantidad > 0:
                disponibles.append(medicamento)
        return disponibles

    #Buscar vacunas por tipo.
    def buscarTipoVacuna(self, tipo):
        vacunasdisponibles = []
        for vacuna in self.listaVacunas:
            if vacuna.tipo == tipo:
                vacunasdisponibles.append(vacuna)
        return vacunasdisponibles

    #Setters y getters.
    def getListaDoctores(self):
        return self.listaDoctores

    def setListaDoctores(self, listaDoctores):
        self.listaDoctores = listaDoctores

    def getListaPacientes(self):
        return self.listaPacientes

    def setListaPacientes(self, listaPacientes):
        self.listaPacientes = listaPacientes

    def getListaMedicamentos(self):
        return self.listaMedicamentos

    def setListaMedicamentos(self, listaMedicamentos):
        self.listaMedicamentos = listaMedicamentos

    def getListaVacunas(self):
        return self.listaVacunas

    def setListaVacunas(self, listaVacunas):
        self.listaVacunas = listaVacunas

    @classmethod
    def getListaHabitaciones(cls):
        return cls.habitaciones

    @classmethod
    def setListaHabitaciones(cls, habitaciones):
        cls.habitaciones = habitaciones

    @property
    def listaPacientes(self):
        return self.listaPacientes

    @listaPacientes.setter
    def listaPacientes(self, value):
        self._listaPacientes = value

