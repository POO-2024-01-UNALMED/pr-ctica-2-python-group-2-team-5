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

        fecha = input("Ingrese la fecha de la cita: ")
        doctor.agregar_cita(fecha)
        print("Listo! La cita ya ha sido agregada a la agenda del doctor correctamente!")
        print(doctor)
        print("Agenda: ")
        for i, cita in enumerate(doctor.agenda, start=1):
            print(f"{i}. {cita['fecha']}")



def eliminar_cita(hospital):
    cedula = int(input("Ingrese la cédula del doctor al que se le eliminará una cita: "))
    doctor = hospital.buscar_doctor(cedula)
    if doctor is None:
        while True:
            print("El doctor no esta registrado.\n¿Desea registrarlo?")
            print("1. Si\n2. No \nSeleccione una opción")
            opcion = input()
            if opcion == "1":
                doctor = Doctor(cedula)
                hospital.agregar_doctor(doctor)
                break
            elif opcion == "2":
                print("BRUH, Bye")
                return
            else:
                print("No entendiste verdad? OPCION INVALIDA")

    print("Seleccione la cita que desea eliminar, (solo se muestran las citas que no tienen un paciente asigando: ")
    agenda_disponible = doctor.mostrar_agenda_disponible()
    for i, cita in enumerate(agenda_disponible, start=1):
        print(f"{i}. {cita['fecha']}")
    numero_cita = int(input("Seleccione la cita que desea eliminar: "))
    while numero_cita < 1 or numero_cita > len(agenda_disponible):
        print("OPCION INVALIDA, te equivocate, por favor ingrese otra opción: ")
        numero_cita = int(input())
    doctor.eliminar_cita(agenda_disponible[numero_cita - 1]["fecha"])
    print("¡Cita ELIMINADA con exito!")
    print(doctor)
    print("Agenda: ")
    for i, cita in enumerate(doctor.agenda, start=1):
        print(f"{i}. {cita['fecha']}")


hospital = Hospital()
while True:
    print("1. Agregar cita\n2. Eliminar cita\n3. Salir")
    opcion = input()
    if opcion == "1":
        agregar_cita(hospital)
    elif opcion == "2":
        eliminar_cita(hospital)
    elif opcion == "3":
        break
    else:
        print("Opción inválida")