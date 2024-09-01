#Importar lo necesario...
from gestorAplicacion.administracionHospital import Hospital, Vacuna
from gestorAplicacion.personas import Paciente
from gestorAplicacion.servicios import CitaVacuna
#from uiMain.gestion.gestionPaciente import RegistrarPaciente

class Vacunacion:

    @staticmethod
    def vacunacion(hospital):
        print("Ingrese la cédula del paciente: ")

        numero_cedula = int(input())
        paciente_asignado = hospital.buscar_paciente(numero_cedula)

        if paciente_asignado is None:
            while True:
                print("El paciente no está registrado.\n¿Desea registrarlo?")
                print("1. Si\n2. No \nSeleccione una opción")
                opcion = int(input())
                if opcion == 1:
                    #registrar_paciente(hospital)
                    return
                elif opcion == 2:
                    print("Adiós")
                    return
                else:
                    print("Opción Inválida")

        print(paciente_asignado.bienvenida())

        print("\nSeleccione el tipo de vacuna que requiere")
        print("1. Obligatoria")
        print("2. No obligatoria")
        print("Ingrese una opción: ")
        
        tipo_vacuna = int(input())

        while tipo_vacuna < 1 or tipo_vacuna > 2:
            print("Opción fuera de rango, por favor ingrese otro número: ")
            tipo_vacuna = int(input())

        print("Vacunas Disponibles")

        vacunas_disponibles = []

        if tipo_vacuna == 1:
            vacunas_disponibles = paciente_asignado.buscar_vacuna_por_eps("Obligatoria", hospital)
            if not vacunas_disponibles:
                print("No hay vacunas disponibles para usted de tipo obligatoria")
                return
            for i, vacuna in enumerate(vacunas_disponibles, 1):
                print(f"{i}. {vacuna.get_nombre()}")

        elif tipo_vacuna == 2:
            vacunas_disponibles = paciente_asignado.buscar_vacuna_por_eps("No obligatoria", hospital)
            if not vacunas_disponibles:
                print("No hay vacunas disponibles para usted de tipo no obligatoria")
                return
            for i, vacuna in enumerate(vacunas_disponibles, 1):
                print(f"{i}. {vacuna.get_nombre()}")

        print("\nSeleccione la vacuna que requiere aplicarse: ")
        numero_vacuna = int(input())

        verificar_vacuna = False

        while True:
            while numero_vacuna < 1 or numero_vacuna > len(vacunas_disponibles):
                print("Opción fuera de rango, por favor ingrese otro número: ")
                numero_vacuna = int(input())

            for i, historial in enumerate(paciente_asignado.get_historia_clinica().get_historial_vacunas()):
                if historial.get_vacuna().get_nombre() == vacunas_disponibles[numero_vacuna - 1].get_nombre():
                    verificar_vacuna = True
                    print("Usted ya se puso esta vacuna, por favor ingrese otra opción o ingrese el número 0 para terminar el proceso: ")
                    numero_vacuna = int(input())
                    if numero_vacuna == 0:
                        return
                    break
                else:
                    verificar_vacuna = False

            if not verificar_vacuna:
                break

        agenda_disponible = vacunas_disponibles[numero_vacuna - 1].mostrar_agenda_disponible()

        if not agenda_disponible:
            print("No hay citas disponibles para esta vacuna")
            return

        print("\nCitas disponibles: ")
        for i, cita in enumerate(agenda_disponible, 1):
            print(f"{i}. {cita.get_fecha()}")

        print("\nSeleccione la cita de su preferencia: ")
        numero_cita = int(input())

        cita_asignada = vacunas_disponibles[numero_vacuna - 1].actualizar_agenda(paciente_asignado, numero_cita, agenda_disponible)

        print("\nCita asignada correctamente, puede acudir al centro asistencial con la siguiente información: ")
        paciente_asignado.actualizar_historial_vacunas(cita_asignada)

        print("\nResumen de su cita: ")
        print(f"Fecha: {cita_asignada.get_fecha()}")
        print(f"Paciente: {cita_asignada.get_paciente().get_nombre()}")
        print(f"Vacuna: {cita_asignada.get_vacuna().get_nombre()}")
        print("Asistente médico: Enfermera")

        agenda_disponible.clear()
        vacunas_disponibles.clear()

        print("\nEste es el historial de vacunas aplicadas del paciente seleccionado: ")
        for i, historial in enumerate(paciente_asignado.get_historia_clinica().get_historial_vacunas(), 1):
            print(f"{i}. Vacuna: {historial.get_vacuna().get_nombre()}")

        print(f"\n{paciente_asignado.despedida(cita_asignada)}")