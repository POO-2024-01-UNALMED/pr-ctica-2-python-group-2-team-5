#Importar lo necesario...
from gestorAplicacion.administracionHospital.Hospital import Hospital
from gestorAplicacion.personas.Doctor import Doctor
from gestorAplicacion.personas.Paciente import Paciente
from gestorAplicacion.servicios.Cita import Cita

#Clase Agendar cita, que corresponde a la funcionalidad 1.
class AgendarCita:
    #Métodos.

    #Buscar doctores por la EPS.
    @classmethod
    def agendarCita(cls, hospital):
        #Buscar paciente con el número de cédula.
        numeroCedula = int(input("Por favor, ingrese su número de identificación: "))
        pacienteCita = hospital.buscarPaciente(numeroCedula)

        #Verificar si se encontró un paciente que coincida con la cédula.
        if pacienteCita == None:
            while True:
                print("El paciente no está registrado\nDesea registrarlo?: ")
                opcion = int(input("\n1. Si\n2. No"))

                if opcion == 1:
                    RegistrarPaciente.registrarPaciente(hospital)
                    return
                elif opcion == 2:
                    print("Regresando al menú principal...")
                    return
                else:
                    print("Opción no valida. Intente de nuevo.")

        #Bienveida.
        print(pacienteCita.bienvenida())

        #Array de doctores para uso posterior.
        doctoresDisponibles = []

        #Si no hay doctores por el tipo de EPS buscada.
        while len(doctoresDisponibles) == 0:
            print("\nPor favor, seleccione el tipo de cita que requiere: ")
            opcion = int(input("1. General.\n2. Odontología.\n3. Oftanmología.\n4. Regresar al menú"))

            #Casos de error.
            while opcion < 1 or opcion > 4:
                print("Opción no válida. Intente de nuevo.")
                opcion = int(input())

            #Búsqueda de doctores según la especialidad elegida y que coincidan con la EPS del paciente
            if opcion == 1:
                doctoresDisponibles = pacienteCita.buscarDoctorEps("General", hospital)
                doctoresEps(doctoresDisponibles, pacienteCita)
                break
            elif opcion == 2:
                doctoresDisponibles = pacienteCita.buscarDoctorEps("Odontología", hospital)
                doctoresEps(doctoresDisponibles, pacienteCita)
                break
            elif opcion == 3:
                doctoresDisponibles = pacienteCita.buscarDoctorEps("Oftalmología", hospital)
                doctoresEps(doctoresDisponibles, pacienteCita)
                break
            else:
                return

        #Agenda del doctor escogido.
        agendaDoctor = []

        #Si el doctor no tiene citas escogidas.
        while len(agendaDoctor) == 0:
