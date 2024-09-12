from iuMain.gestion.gestionPacientes.MenuPacientes import MenuPacientes
from iuMain.gestion.gestionPacientes.gestionPaciente import GestionPaciente


class MenuGestion:
    @staticmethod
    def menuGestion(hospital):
        print("MenuGestion")

        print("\n─────────   MENU GESTION GENERAL   ─────────")
        print("1. Gestionar Pacientes")
        print("2. Gestionar apartado de vacunas")
        print("3. Gestionar Doctores")
        print("4. Gestionar Hospital")
        print("5. --Regresar al menu inicial--")
        print("6. --Salir--")
        opcion = int(input("Seleccione una opcion: "))


        if opcion == 1:
            MenuPacientes.mostrar