from src.gestorAplicacion.administracionHospital.Vacuna import Vacuna
from src.gestorAplicacion.servicios.CitaVacuna import CitaVacuna


class gestionVacunas:
    @staticmethod
    def agregar_cita_vacuna(hospital):
        nombre_vacuna = input("Ingrese el nombre de la vacuna: ").strip()

        if not gestionVacunas.verificar_existencia_vacuna(nombre_vacuna, hospital):
            print("Esta vacuna no existe en el inventario del hospital.")
        else:
            vacuna = hospital.buscar_vacuna(nombre_vacuna)
            fecha_cita = input(
                "Ingrese la fecha de la cita para la vacunación (Ejemplo: 28 de Agosto, 8:00 am): ").strip()

            vacuna.get_agenda().append(Cita_Vacuna(fecha_cita, None, None))
            print("Cita vacuna agregada con éxito")

            print("\nVacuna: " + vacuna.get_nombre())
            print("Agenda: ")
            for i, cita in enumerate(vacuna.get_agenda(), start=1):
                print(f"{i}. {cita.get_fecha()}")

    @staticmethod
    def eliminar_cita_vacuna(hospital):
        nombre_vacuna = input("Ingrese el nombre de la vacuna a la que se le eliminará su cita: ").strip()

        if not gestionVacunas.verificar_existencia_vacuna(nombre_vacuna, hospital):
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

    @staticmethod
    def verificar_existencia_vacuna(nombre, hospital):
        for vacuna in hospital.get_lista_vacunas():
            if nombre == vacuna.get_nombre():
                return True
        return False

    @staticmethod
    def registrar_vacuna(hospital):
        nombre = input(
            "A continuación ingrese la información de la nueva vacuna:\nNombre de la vacuna (Debe iniciar con mayúscula): ").strip()

        if gestionVacunas.verificar_existencia_vacuna(nombre, hospital):
            print("La vacuna ya existe en el sistema.")
            return

        tipo = input("Ingrese el tipo de la vacuna (Obligatoria, No obligatoria): ").strip()

        tipo_eps = []
        while True:
            eps = input(
                "Ingrese el tipo de la EPS a la que va a estar disponible la vacuna (Subsidiado, Contributivo o Particular): ").strip()
            tipo_eps.append(eps)

            while True:
                letra = input("¿Desea agregar otro tipo de EPS? (s/n): ").strip().lower()
                if letra in ['s', 'n']:
                    respuesta = letra == 's'
                    break
                else:
                    print("Respuesta inválida, por favor ingrese 's' o 'n'.")

            if not respuesta:
                break

        precio = float(input("Ingrese el precio de la vacuna: ").strip())

        vacuna_nueva = Vacuna(tipo, nombre, tipo_eps, precio)
        print("¡La vacuna ha sido registrada con éxito!")

        hospital.get_lista_vacunas().append(vacuna_nueva)
        print("\nInformación general de la nueva vacuna registrada:")
        print(f"Nombre de la vacuna: {vacuna_nueva.get_nombre()}")
        print(f"Tipo de la vacuna: {vacuna_nueva.get_tipo()}")
        print(f"Precio de la vacuna: {vacuna_nueva.get_precio()}")

    @staticmethod
    def eliminar_vacuna(hospital):
        nombre_vacuna = input("Ingrese el nombre de la vacuna que desea eliminar: ").strip()

        if not gestionVacunas.verificar_existencia_vacuna(nombre_vacuna, hospital):
            print("Esta vacuna no existe en el inventario del hospital.")

        else:
            for vacuna in hospital.get_lista_vacunas():
                if vacuna.get_nombre() == nombre_vacuna:
                    print(f"{vacuna.get_nombre()} fue eliminada exitosamente.")
                    hospital.get_lista_vacunas().remove(vacuna)
                    break

    @staticmethod
    def ver_vacuna(hospital):
        print("Ingrese el nombre de la vacuna. ")
        nombre_vacuna = input().strip()

        if not gestionVacunas.verificar_existencia_vacuna(nombre_vacuna, hospital):
            print("Esta vacuna no existe en el inventario del hospital.")
        else:
            for vacuna in hospital.get_lista_vacunas():
                if vacuna.get_nombre() == nombre_vacuna:
                    print(f"\nNombre: {vacuna.get_nombre()}")
                    print(f"Tipo: {vacuna.get_tipo()}")
                    print("Eps a la que está disponible:")
                    for i, eps in enumerate(vacuna.get_tipo_eps(), start=1):
                        print(f"{i}. {eps}")
                    print(f"Precio: {vacuna.get_precio()}")