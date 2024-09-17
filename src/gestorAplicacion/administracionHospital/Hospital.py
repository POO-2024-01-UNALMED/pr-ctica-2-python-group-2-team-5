# Clase Hospital que lleva el registro general de servicios y personas.
import os
import pickle

from gestorAplicacion.administracionHospital.Enfermedad import Enfermedad
from manejoDeErrores.ErroresAplicacion import DatosFalsos

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
        self.deserializar()

    #Métodos.


    #Buscar paciente con su número de cedula.
    def buscarPaciente(self, cedula):
        for paciente in self.listaPacientes:
            if paciente.getCedula() == cedula:
                return paciente
        raise DatosFalsos()

    #Buscar doctor con la cédula.
    def buscarDoctor(self, cedula):
        for doctor in self.listaDoctores:
            if doctor.cedula == cedula:
                return doctor
        return None

    def medicamentosDisponibles(self):
        disponibles = []
        for medicamento in self.listaMedicamentos:
            if medicamento.cantidad > 0:
                disponibles.append(medicamento)
        return disponibles

    #Buscar doctores por especialidad.
    def buscarTipoDoctor(self, especialidad):
        doctoresDisponibles = []
        for doctor in self.listaDoctores:
            if doctor.especialidad == especialidad:
                doctoresDisponibles.append(doctor)
        return doctoresDisponibles

    #Buscar vacunas por tipo.
    def buscarTipoVacuna(self, tipo):
        vacunasdisponibles = []
        for vacuna in self.listaVacunas:
            if vacuna.tipo == tipo:
                vacunasdisponibles.append(vacuna)
        return vacunasdisponibles

    def buscarVacuna(self, nombre):
        vacunaSeleccionada = None
        for vacuna in self.listaVacunas:
            if vacuna.nombre == nombre:
                vacunaSeleccionada = vacuna
        return vacunaSeleccionada

    def serializar(self):
        serializarDoctores = open("src/baseDatos/temp/registro_doctores.pickle", "wb")
        pickle.dump(self.listaDoctores, serializarDoctores)
        serializarDoctores.close()
        serializarPacientes =  open("src/baseDatos/temp/registro_pacientes.pickle", "wb")
        pickle.dump(self.listaPacientes, serializarPacientes)
        serializarPacientes.close()
        serializarMedicamento =  open("src/baseDatos/temp/registro_medicamentos.pickle", "wb")
        pickle.dump(self.listaMedicamentos, serializarMedicamento)
        serializarMedicamento.close()
        serializarVacunas = open("src/baseDatos/temp/registro_vacunas.pickle", "wb")
        pickle.dump(self.listaVacunas, serializarVacunas)
        serializarVacunas.close()
        serializarEnfermedades = open("src/baseDatos/temp/registro_enfermedades.pickle", "wb")
        pickle.dump(Enfermedad.enfermedadesRegistradas, serializarEnfermedades)
        serializarEnfermedades.close()
        serializarHabitaciones =  open("src/baseDatos/temp/registro_habitaciones.pickle", "wb")
        pickle.dump(self.habitaciones, serializarHabitaciones)
        serializarHabitaciones.close()

    def deserializar(self):
        deserealizarDoctores = open("src/base_datos/temp/registro_doctores.pickle", "rb")
        self.listaDoctores = pickle.load(deserealizarDoctores)
        deserealizarPacientes = open("src/base_datos/temp/registro_pacientes.pickle", "rb")
        self.listaPacientes = pickle.load(deserealizarPacientes)
        deserealizarMedicamentos =  open("src/base_datos/temp/registro_medicamentos.pickle", "rb")
        self.listaMedicamentos = pickle.load(deserealizarMedicamentos)
        deserealizarVacunas = open("src/base_datos/temp/registro_vacunas.pickle", "rb")
        self.listaVacunas = pickle.load(deserealizarVacunas)
        deserealizarEnfermedades =  open("src/base_datos/temp/registro_enfermedades.pickle", "rb")
        Enfermedad.enfermedadesRegistradas = pickle.load(deserealizarEnfermedades)
        deserealizarHabitaciones = open("src/base_datos/temp/registro_habitaciones.pickle", "rb")
        self.habitaciones = pickle.load(deserealizarHabitaciones)



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

