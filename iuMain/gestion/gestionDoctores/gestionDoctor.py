from gestorAplicacion.administracionHospital.Hospital import *
from baseDatos.Serializador import *
from gestion.gestionDoctores import *


class GestionDoctor:


    @staticmethod
    def menu_gestion_doctor(hospital):
        while True:

            # Menu para gestionar la clase Doctor
            print("───────── MENU GESTION DE DOCTORES   ─────────")
            print("1. Registrar doctor")
            print("2. Eliminar doctor")
            print("3. Ver doctor")
            print("4. Agregar citas")
            print("5. Eliminar citas")
            print("6. --Regresar al menu anterior--")
            print("7. --Salir--")
            print("──────────────────────────────")
            opcion = input("Seleccione una opción: ")


            if opcion == "1":
                RegistrarDoctor.registrar_doctor(hospital)

            elif opcion == "2":
                EliminarDoctor.eliminar_doctor(hospital)

            elif opcion == "3":
                VerDoctor.ver_doctor(hospital)

            elif opcion == "4":
                AgregarEliminarCitas.agregar_citas(hospital)

            elif opcion == "5":
                AgregarEliminarCitas.eliminar_citas(hospital)

            elif opcion == "6":
                return

            elif opcion == "7":
                Serializador.serializar(hospital)
                exit(0)

            else:
                print("Opción Inválida")