from gestorAplicacion.administracionHospital import Hospital, Vacuna
from gestorAplicacion.servicios import CitaVacuna
from iuMain.gestion.gestionVacunas import RegistrarEliminarVacunas

class AgregarEliminarCitaVacuna:

    @staticmethod
    def agregar_cita_vacuna(hospital):
        nombre_vacuna = input("Ingrese el nombre de la vacuna: ").strip()

        if not RegistrarEliminarVacunas.verificar_existencia_vacuna(nombre_vacuna, hospital):
            print("Esta vacuna no existe en el inventario del hospital.")
        else:
            vacuna = hospital.buscar_vacuna(nombre_vacuna)
            fecha_cita = input("Ingrese la fecha de la cita para la vacunación (Ejemplo: 28 de Agosto, 8:00 am): ").strip()

            vacuna.get_agenda().append(CitaVacuna(fecha_cita, None, None))
            print("Cita vacuna agregada con éxito")

            print("\nVacuna: " + vacuna.get_nombre())
            print("Agenda: ")
            for i, cita in enumerate(vacuna.get_agenda(), start=1):
                print(f"{i}. {cita.get_fecha()}")

    @staticmethod
    def eliminar_cita_vacuna(hospital):
        nombre_vacuna = input("Ingrese el nombre de la vacuna a la que se le eliminará su cita: ").strip()

        if not RegistrarEliminarVacunas.verificar_existencia_vacuna(nombre_vacuna, hospital):
            print("Esta vacuna no existe en el inventario del hospital.")
        else:
            vacuna = hospital.buscar_vacuna(nombre_vacuna)
            print("A continuación se muestran las citas de esta vacuna que no tienen paciente asignado:")
            agenda_disponible = vacuna.mostrar_agenda_disponible()

            if not agenda_disponible:
                print("No hay citas disponibles para eliminar.")
                return

            for i, cita in enumerate(agenda_disponible, start=1):
                print(f"{i}. {cita.get_fecha()}")

            numero_cita = int(input("Seleccione la cita que desea eliminar: ").strip())

            while numero_cita < 1 or numero_cita > len(agenda_disponible):
                numero_cita = int(input("Ingrese un número válido: ").strip())

            cita_a_eliminar = agenda_disponible[numero_cita - 1]

            vacuna.get_agenda().remove(cita_a_eliminar)
            print("Cita eliminada con éxito")

            print(f"\nVacuna: {vacuna.get_nombre()}")
            print("Agenda: ")
            for cita in vacuna.get_agenda():
                print(cita.get_fecha())
