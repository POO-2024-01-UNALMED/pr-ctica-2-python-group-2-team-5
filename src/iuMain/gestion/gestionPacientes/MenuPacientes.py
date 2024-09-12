from src.iuMain.gestion.gestionPacientes.GestionPaciente import GestionPaciente


class MenuPacientes:
    @staticmethod
    def mostrarMenuGestionPacientes(hospital):
        while True:
            print("MenuGestion Pacientes")
            print("1. Registrar paciente")
            print("2. Registrar enfermedad")
            print("3. Eliminar paciente")
            print("4. Ver paciente")
            print("5. Regresar al menú anterior")
            print("6. Salir")
            opcion = int(input("Opcion: "))

            if opcion == 1:
                GestionPaciente.registrarPaciente(hospital)
                break
            elif opcion == 2:
                GestionPaciente.reg
