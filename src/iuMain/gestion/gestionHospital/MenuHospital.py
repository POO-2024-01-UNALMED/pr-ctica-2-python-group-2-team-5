from baseDatos.Serializador import Serializador
from iuMain.gestion.gestionHospital.gestionHospital import gestionHospital


class MenuHospital:
    @staticmethod
    def menuGestionHospital(hospital):
        while True:
            print("\n───────── MENU GESTION DEL HOSPITAL ────────────")
            print("Por favor, elija una de las siguientes opciones: ")
            print("1. Construir Habitación")
            print("2. Ver lista de Habitaciones")
            print("3. Destruir Habitación")
            print("4. Agregar Medicamentos")
            print("5. Ver Inventario de medicamentos")
            print("6. Ver personas registradas en el hospital")
            print("7. Ver vacunas registradas en el hospital")
            print("8. --Regresar al menu anterior--")
            print("9. --Salir--")
            print("──────────────────────────────")
            opcion = input("Seleccione una opción: ")



            if opcion == "1":
                gestionHospital.construirHabitacion(hospital)
            elif opcion == "2":
                gestionHospital.verHabitacion(hospital)
            elif opcion == "3":
                gestionHospital.destruirHabitacion(hospital)
            elif opcion == "4":
                gestionHospital.agregarMedicamentos(hospital)
            elif opcion == "5":
                gestionHospital.verMedicamentos(hospital)
            elif opcion == "6":
                gestionHospital.verPersonasRegistradas(hospital)
            elif opcion == "7":
                gestionHospital.verVacunas(hospital)
            elif opcion == "8":
                return
            else:
                Serializador.serializar(hospital)
            print("Datos guardados.")