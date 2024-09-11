import pickle


class Serializador:

    @staticmethod
    def serializar(hospital):
        hospital.serializarDoctores(hospital, archivoDoctores = open("src/baseDatos/temp/registroDoctores.pkl", "wb"))
        hospital.serializarPacientes(hospital, archivoPaciente = open("src/baseDatos/temp/registroPacientes.pkl", "wb"))
        hospital.serializarMedicamentos(hospital, archivoMedicamentos = open("src/baseDatos/temp/registroMedicamentos.pkl", "wb"))
        hospital.serializarVacunas(hospital,  archivoVacunas = open("src/baseDatos/temp/registroVacunas.pkl", "wb"))
        hospital.serializarHabitaciones(hospital, archivoHabitaciones = open("src/baseDatos/temp/registroHabitaciones.pkl", "wb"))
        hospital.serializarEnfermedades(hospital, archivoEnfermedades = open("src/baseDatos/temp/registroEnfermedades.pkl", "wb"))

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



