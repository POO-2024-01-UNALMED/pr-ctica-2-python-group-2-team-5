from gestorAplicacion.administracionHospital import Hospital, Vacuna
from gestorAplicacion.servicios import CitaVacuna
from gestorAplicacion.personas import Paciente
from iuMain.gestion.gestionPacientes import administrarPacientes


class Vacunacion:

    @staticmethod
    def vacunacion(hospital):
        print("Ingrese la cédula del paciente: ")

        numeroCedula = int(input())
        pacienteAsignado = hospital.buscarPaciente(numeroCedula)

        if pacienteAsignado is None:
            while True:
                print("El paciente no está registrado.\n¿Desea registrarlo?")
                print("1. Si\n2. No \nSeleccione una opción")
                opcion = int(input())
                if opcion == 1:
                    gestionPaciente.registrarPaciente(hospital)
                    return
                elif opcion == 2:
                    print("Adiós")
                    return
                else:
                    print("Opción Inválida")

        print(pacienteAsignado.bienvenida())

        print("\nSeleccione el tipo de vacuna que requiere")
        print("1. Obligatoria")
        print("2. No obligatoria")
        print("Ingrese una opción: ")
        
        tipoVacuna = int(input())

        while tipoVacuna < 1 or tipoVacuna > 2:
            print("Opción fuera de rango, por favor ingrese otro número: ")
            tipoVacuna = int(input())

        print("Vacunas Disponibles")

        vacunasDisponibles = []

        if tipoVacuna == 1:
            vacunasDisponibles = pacienteAsignado.buscarVacunaPorEps("Obligatoria", hospital)
            if not vacunasDisponibles:
                print("No hay vacunas disponibles para usted de tipo obligatoria")
                return
            for i, vacuna in enumerate(vacunasDisponibles, 1):
                print(f"{i}. {vacuna.getNombre()}")

        elif tipoVacuna == 2:
            vacunasDisponibles = pacienteAsignado.buscarVacunaPorEps("No obligatoria", hospital)
            if not vacunasDisponibles:
                print("No hay vacunas disponibles para usted de tipo no obligatoria")
                return
            for i, vacuna in enumerate(vacunasDisponibles, 1):
                print(f"{i}. {vacuna.getNombre()}")

        print("\nSeleccione la vacuna que requiere aplicarse: ")
        numeroVacuna = int(input())

        verificarVacuna = False

        while True:
            while numeroVacuna < 1 or numeroVacuna > len(vacunasDisponibles):
                print("Opción fuera de rango, por favor ingrese otro número: ")
                numeroVacuna = int(input())

            for i, historial in enumerate(pacienteAsignado.getHistoriaClinica().getHistorialVacunas()):
                if historial.getVacuna().getNombre() == vacunasDisponibles[numeroVacuna - 1].getNombre():
                    verificarVacuna = True
                    print("Usted ya se puso esta vacuna, por favor ingrese otra opción o ingrese el número 0 para terminar el proceso: ")
                    numeroVacuna = int(input())
                    if numeroVacuna == 0:
                        return
                    break
                else:
                    verificarVacuna = False

            if not verificarVacuna:
                break

        agendaDisponible = vacunasDisponibles[numeroVacuna - 1].mostrarAgendaDisponible()

        if not agendaDisponible:
            print("No hay citas disponibles para esta vacuna")
            return

        print("\nCitas disponibles: ")
        for i, cita in enumerate(agendaDisponible, 1):
            print(f"{i}. {cita.getFecha()}")

        print("\nSeleccione la cita de su preferencia: ")
        numeroCita = int(input())

        citaAsignada = vacunasDisponibles[numeroVacuna - 1].actualizarAgenda(pacienteAsignado, numeroCita, agendaDisponible)

        print("\nCita asignada correctamente, puede acudir al centro asistencial con la siguiente información: ")
        pacienteAsignado.actualizarHistorialVacunas(citaAsignada)

        print("\nResumen de su cita: ")
        print(f"Fecha: {citaAsignada.getFecha()}")
        print(f"Paciente: {citaAsignada.getPaciente().getNombre()}")
        print(f"Vacuna: {citaAsignada.getVacuna().getNombre()}")
        print("Asistente médico: Enfermera")

        agendaDisponible.clear()
        vacunasDisponibles.clear()

        print("\nEste es el historial de vacunas aplicadas del paciente seleccionado: ")
        for i, historial in enumerate(pacienteAsignado.getHistoriaClinica().getHistorialVacunas(), 1):
            print(f"{i}. Vacuna: {historial.getVacuna().getNombre()}")

        print(f"\n{pacienteAsignado.despedida(citaAsignada)}")