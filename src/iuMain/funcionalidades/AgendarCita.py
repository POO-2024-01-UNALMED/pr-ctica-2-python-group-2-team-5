#Importar lo necesario...
from src.iuMain.gestion.gestionPacientes.gestionPaciente import GestionPaciente

#Clase Agendar cita, que corresponde a la funcionalidad 1.
class AgendarCita:
    #Métodos.

    #Buscar doctores por la EPS.
    @classmethod
    def doctoresEps(cls, doctores, paciente):
        if len(doctores) != 0:
            print("Los doctores disponibles para la EPS " + paciente.getTipoEps() + " son:")
            for i in range(1, len(doctores)):
                print(i + ". " + doctores.get[i - 1].getNombre())
        else:
            print("\nLo sentimos! En este momento no hay doctores disponibles para la EPS " + paciente.getTipoEps() + ".\nPuede elegir otra opción si lo desea.")


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
                    GestionPaciente.registrarPaciente(hospital)
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
            opcion = int(input("1. General.\n2. Odontología.\n3. Oftalmología.\n4. Regresar al menú"))

            #Casos de error.
            while opcion < 1 or opcion > 4:
                print("Opción no válida. Intente de nuevo.")
                opcion = int(input())

            #Búsqueda de doctores según la especialidad elegida y que coincidan con la EPS del paciente
            if opcion == 1:
                doctoresDisponibles = pacienteCita.buscarDoctorEps("General", hospital)
                AgendarCita.doctoresEps(doctoresDisponibles, pacienteCita)
                break
            elif opcion == 2:
                doctoresDisponibles = pacienteCita.buscarDoctorEps("Odontología", hospital)
                AgendarCita.doctoresEps(doctoresDisponibles, pacienteCita)
                break
            elif opcion == 3:
                doctoresDisponibles = pacienteCita.buscarDoctorEps("Oftalmología", hospital)
                AgendarCita.doctoresEps(doctoresDisponibles, pacienteCita)
                break
            else:
                return

        #Agenda del doctor escogido.
        agendaDoctor = []

        #Si el doctor no tiene citas escogidas.
        while len(agendaDoctor) == 0:
            # Elegir lista doctoresDisponibles.
            eleccion = int(input("\nPor favor, elija el doctor por el que desea ser atendido: "))

            # Casos de error.
            while eleccion < 1 or eleccion > len(doctoresDisponibles) + 1:
                print("Opción no válida. Intente de nuevo.")
                eleccion = int(input())

            if eleccion == len(doctoresDisponibles) + 1:
                return

            doctorElegido = doctoresDisponibles[eleccion - 1]
            agendaDoctor = doctorElegido.mostrarAgenda()

            if len(agendaDoctor) != 0:
                #Mostar agenda del doctor.
                print("\nLas citas disponibles para el/la Doctor(a) " + doctorElegido.getNombre() + " son:")
                for i in range(1, len(agendaDoctor)):
                    print(i + ". " + agendaDoctor[i-1].getFecha())

                #Elegir entre los horarios disponibles.
                eleccionCita = int(input("Por favor, elija el horario de la cita que el paciente quiere tomar: "))

                #Casos de error.
                while eleccionCita < 1 or eleccionCita > len(agendaDoctor):
                    print("Opción no válida. Intente de nuevo")
                    eleccionCita = input()

                #Actualizar la agenda del doctor.
                cita = doctorElegido.actualizarAgenda(pacienteCita, eleccionCita, agendaDoctor)

                print("Se ha asignado su cita!")

                #Historial de citas del paciente.
                pacienteCita.actualizarHistorialCitas(cita)

                print("Información de su cita:\nFecha: " + cita.getFecha() + "\nDoctor: " + cita.getDoctor().getNombre())

                #Limpiar arrays.
                agendaDoctor.clear()
                doctoresDisponibles.clear()

                print("\n" + pacienteCita.despedida(cita))
                break
            else:
                print("Lo sentimos! El doctor elegido no tiene citas disponibles en su agenda. Puede intentar elegir otro Doctor.")
