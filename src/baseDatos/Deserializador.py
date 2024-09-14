import os
import pickle

from src.gestorAplicacion.administracionHospital.Enfermedad import Enfermedad


class Deserializador:
    @staticmethod
    def deserializar(hospital):
        with open(os.path.abspath("src/base_datos/temp/registro_doctores.pickle"), "rb") as file:
            hospital.listaDoctores = pickle.load(file)
        with open(os.path.abspath("src/base_datos/temp/registro_pacientes.pickle"), "rb") as file:
            hospital.listaPacientes = pickle.load(file)
        with open(os.path.abspath("src/base_datos/temp/registro_medicamentos.pickle"), "rb") as file:
            hospital.listaMedicamentos = pickle.load(file)
        with open(os.path.abspath("src/base_datos/temp/registro_vacunas.pickle"), "rb") as file:
            hospital.listaVacunas = pickle.load(file)
        with open(os.path.abspath("src/base_datos/temp/registro_enfermedades.pickle"), "rb") as file:
            Enfermedad._enfermedades_registradas = pickle.load(file)
        with open(os.path.abspath("src/base_datos/temp/registro_habitaciones.pickle"), "rb") as file:
            hospital.habitaciones = pickle.load(file)