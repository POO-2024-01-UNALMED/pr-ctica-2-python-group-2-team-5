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
        try:
            with open(os.path.abspath("src/baseDatos/temp/registro_doctores"), "wb") as file:
                file.truncate()
                pickle.dump(self.listaDoctores, file)
            with open(os.path.abspath("src/baseDatos/temp/registro_pacientes.pickle"), "wb") as file:
                file.truncate()
                pickle.dump(self.listaPacientes, file)
            with open(os.path.abspath("src/baseDatos/temp/registro_medicamentos.pickle"), "wb") as file:
                file.truncate()
                pickle.dump(self.listaMedicamentos, file)
            with open(os.path.abspath("src/baseDatos/temp/registro_vacunas.pickle"), "wb") as file:
                file.truncate()
                pickle.dump(self.listaVacunas, file)
            with open(os.path.abspath("src/baseDatos/temp/registro_enfermedades.pickle"), "wb") as file:
                file.truncate()
                pickle.dump(Enfermedad.enfermedadesRegistradas, file)
            with open(os.path.abspath("src/baseDatos/temp/registro_habitaciones.pickle"), "wb") as file:
                file.truncate()
                pickle.dump(self.habitaciones, file)
        except FileNotFoundError as e:
            print(f"Archivo no encontrado: {e}")
        except pickle.UnpicklingError as e:
            print(f"Error al deserializar: {e}")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    def deserializar(self):
        try:
            with open(os.path.abspath("src/baseDatos/temp/registro_doctores"), "rb") as file:
                self.listaDoctores = pickle.load(file)
            with open(os.path.abspath("src/baseDatos/temp/registro_pacientes.pickle"), "rb") as file:
                self.listaPacientes = pickle.load(file)
            with open(os.path.abspath("src/baseDatos/temp/registro_medicamentos.pickle"), "rb") as file:
                self.listaMedicamentos = pickle.load(file)
            with open(os.path.abspath("src/baseDatos/temp/registro_vacunas.pickle"), "rb") as file:
                self.listaVacunas = pickle.load(file)
            with open(os.path.abspath("src/baseDatos/temp/registro_enfermedades.pickle"), "rb") as file:
                Enfermedad.enfermedadesRegistradas = pickle.load(file)
            with open(os.path.abspath("src/baseDatos/temp/registro_habitaciones.pickle"), "rb") as file:
                self.habitaciones = pickle.load(file)
        except FileNotFoundError as e:
            print(f"Archivo no encontrado: {e}")
        except pickle.UnpicklingError as e:
            print(f"Error al deserializar: {e}")
        except Exception as e:
            print(f"Ocurrió un error: {e}")


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

