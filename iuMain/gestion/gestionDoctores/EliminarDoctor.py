from gestorAplicacion.administracionHospital.Hospital import *
from gestorAplicacion.personas.Doctor import *



class EliminarDoctor:
    @staticmethod
    def eliminar_doctor(hospital):
        cedula = int(input("Ingrese la cédula del doctor que se ELIMINARA: "))
        doctor = hospital.buscar_doctor(cedula)
        if doctor is None:
            print("No puedo eliminar algo que no existe asi que...")
            while True:
                print("El doctor no esta registrado.\n¿Desea registrarlo?")
                print("1. Si\n2. No \nSeleccione una opción")
                opcion = input()
                if opcion == "1":
                    
                    return
                elif opcion == "2":
                    print(">:( Adios")
                    return
                else:
                    print("Opción Inválida")
        hospital.doctores.remove(doctor)
        print("¡DOCTOR ASESINADO! digo eliminado")