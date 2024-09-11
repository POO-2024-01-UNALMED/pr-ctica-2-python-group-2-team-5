#Importar las clases necesarias...
from baseDatos import Deserializador
from gestorAplicacion.personas import Doctor, Paciente
from gestorAplicacion.servicios import Habitacion
from gestorAplicacion.administracionHospital import Vacuna, Medicamento

#Clase Hospital que lleva el registro general de servicios y personas.
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

    #Métodos.

    #Buscar doctores por especialidad.
    def buscarTipoDoctor(self, especialidad):
        doctoresDisponibles = []
        for i in range(1, len(self.listaDoctores)):
            if self.listaDoctores[i - 1].getEspecialidad() == especialidad:
                doctoresDisponibles.append(self.listaDoctores[i - 1])
        return doctoresDisponibles

    #Buscar paciente con su número de cedula.
    def buscarPaciente(self, cedula):
        for paciente in self.listaPacientes:
            if paciente.getCedula() == cedula:
                return paciente
        return None

    #Buscar doctor con la cédula.
    def buscarDoctor(self, cedula):
        for doctor in self.listaDoctores:
            if doctor.getCedula() == cedula:
                return doctor
        return None

    #Buscar vacuna por el nombre.
    def buscarVacuna(self, nombre):
        for vacuna in self.listaVacunas:
            if vacuna.getNombre() == nombre:
                return vacuna
        return None

    #Buscar medicamentos dispinibles.
    def medicamentosDisponibles(self):
        medicamentos = []
        for i in range(len(self.listaMedicamentos)):
            if self.listaMedicamentos[i].getCantidad() > 0:
                medicamentos.append(self.listaMedicamentos[i])
        return medicamentos

    #Buscar vacunas por tipo.
    def buscarTipoVacuna(self, tipo):
        vacunas = []
        for i in range(1, len(self.listaVacunas)):
            if self.listaVacunas[i - 1].getTipo() == tipo:
                vacunas.append(self.listaVacunas[i - 1])
        return vacunas

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

