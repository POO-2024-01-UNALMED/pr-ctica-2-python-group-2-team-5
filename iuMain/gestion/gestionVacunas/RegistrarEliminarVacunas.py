from gestorAplicacion.administracionHospital import Hospital, Vacuna

class RegistrarEliminarVacunas:

    @staticmethod
    def verificar_existencia_vacuna(nombre, hospital):
        for vacuna in hospital.get_lista_vacunas():
            if nombre == vacuna.get_nombre():
                return True
        return False

    @staticmethod
    def registrar_vacuna(hospital):
        nombre = input("A continuación ingrese la información de la nueva vacuna:\nNombre de la vacuna (Debe iniciar con mayúscula): ").strip()

        if RegistrarEliminarVacunas.verificar_existencia_vacuna(nombre, hospital):
            print("La vacuna ya existe en el sistema.")
            return

        tipo = input("Ingrese el tipo de la vacuna (Obligatoria, No obligatoria): ").strip()

        tipo_eps = []
        while True:
            eps = input("Ingrese el tipo de la EPS a la que va a estar disponible la vacuna (Subsidiado, Contributivo o Particular): ").strip()
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

        if not RegistrarEliminarVacunas.verificar_existencia_vacuna(nombre_vacuna, hospital):
            print("Esta vacuna no existe en el inventario del hospital.")
        else:
            for vacuna in hospital.get_lista_vacunas():
                if vacuna.get_nombre() == nombre_vacuna:
                    print(f"{vacuna.get_nombre()} fue eliminada exitosamente.")
                    hospital.get_lista_vacunas().remove(vacuna)
                    break