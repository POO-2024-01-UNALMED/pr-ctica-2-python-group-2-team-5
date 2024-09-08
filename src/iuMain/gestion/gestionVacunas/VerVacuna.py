from src.iuMain.gestion.gestionVacunas import RegistrarEliminarVacunas


class VerVacuna:

    @staticmethod
    def ver_vacuna(hospital):
        print("Ingrese el nombre de la vacuna. ")
        nombre_vacuna = input().strip()

        if not RegistrarEliminarVacunas.verificar_existencia_vacuna(nombre_vacuna, hospital):
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