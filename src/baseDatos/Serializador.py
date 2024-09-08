import pickle


class Serializador:

    archivoDoctores = open("src/baseDatos/temp/registroDoctores.pkl", "wb")
    archivoPaciente = open("src/baseDatos/temp/registroPacientes.pkl", "wb")
    archivoMedicamentos = open("src/baseDatos/temp/registroMedicamentos.pkl", "wb")
    archivoVacunas = open("src/baseDatos/temp/registroVacunas.pkl", "wb")
    archivoHabitaciones = open("src/baseDatos/temp/registroHabitaciones.pkl", "wb")
    archivoEnfermedades = open("src/baseDatos/temp/registroEnfermedades.pkl", "wb")

    @staticmethod
    def serializarDoctores(hospital, archivoDoctores):
        try: pickle.dump(hospital.getListaDoctores(), archivoDoctores)
        except: print("Error al serializar Doctores" )

    @staticmethod
    def serializarPacientes(hospital, archivoPacientes):
        try: pickle.dump(hospital.getListaPacientes(), archivoPacientes)
        except: print("Error al serializar Pacientes")

    @staticmethod
    def serializarMedicamentos(hospital, archivoMedicamentos):
        try: pickle.dump(hospital.getListaMedicamentos(), archivoMedicamentos)
        except: print("Error al serializar Medicamentos")

    @staticmethod
    def serializarVacunas(hospital, archivoVacunas):
        try: pickle.dump(hospital.getListaVacunas(), archivoVacunas)
        except: print("Error al serializar Vacunas")

    @staticmethod
    def serializarHabitaciones(hospital, archivoHabitaciones):
        try: pickle.dump(hospital.getListaHabitaciones(), archivoHabitaciones)
        except: print("Error en la serializacion Habitaciones")
    @staticmethod
    def serializarEnfermedades(hospital, archivoEnfermedades):
        try: pickle.dump(hospital.getListaEnfermedades(), archivoEnfermedades)
        except: print("Error en la serialization Enfermedades")



