import os
import pickle

from src.gestorAplicacion.administracionHospital.Enfermedad import Enfermedad
from src.gestorAplicacion.administracionHospital.Hospital import *

class Serializador:
    @staticmethod
    def serializar(hospital):
        with open(os.path.abspath("src/base_datos/temp/registro_doctores.pickle"), "wb") as file:
            file.truncate()
            pickle.dump(hospital.listaDoctores, file)
        with open(os.path.abspath("src/base_datos/temp/registro_pacientes.pickle"), "wb") as file:
            file.truncate()
            pickle.dump(hospital.listaPacientes, file)
        with open(os.path.abspath("src/base_datos/temp/registro_medicamentos.pickle"), "wb") as file:
            file.truncate()
            pickle.dump(hospital.listaMedicamentos, file)
        with open(os.path.abspath("src/base_datos/temp/registro_vacunas.pickle"), "wb") as file:
            file.truncate()
            pickle.dump(hospital.listaVacunas, file)
        with open(os.path.abspath("src/base_datos/temp/registro_enfermedades.pickle"), "wb") as file:
            file.truncate()
            pickle.dump(Enfermedad._enfermedades_registradas, file)
        with open(os.path.abspath("src/base_datos/temp/registro_habitaciones.pickle"), "wb") as file:
            file.truncate()
            pickle.dump(hospital.habitaciones, file)

