from gestorAplicacion.administracionHospital.Hospital import Hospital
from gestorAplicacion.personas.Doctor import Doctor
from gestorAplicacion.servicios.Cita import Cita



def agregar_cita(hospital):
    cedula = int(input("Ingrese la cédula del doctor: "))
    doctor = hospital.buscar_doctor(cedula)
    if doctor is None:
        while True:
            print("El doctor no esta registrado.\n¿Desea registrarlo?")
            print("1. Si\n2. No \nElije sabiamente")
            opcion = input()
            if opcion == "1":
                doctor = Doctor(cedula)
                hospital.agregar_doctor(doctor)
                break
            elif opcion == "2":
                print("Bruh, Adios")
                return
            else:
                print("Opción Inválida")
