class gestionHospital:
    @staticmethod
    def agregar_medicamentos(hospital):
        import sys

        def leer_entero():
            return int(input())

        def leer_flotante():
            return float(input())

        def leer_string():
            return input().strip()

        anadir_otro = True
        while anadir_otro:
            print("¡Bienvenido! ¿Deseas aumentar el stock de un medicamento existente (1) o añadir uno nuevo (2)?")
            print("1. Aumentar el stock de un medicamento existente.")
            print("2. Ingresar un nuevo medicamento.")

            lista_medicamentos = hospital.get_lista_medicamentos()
            opcion = leer_entero()

            if opcion == 1:
                while True:
                    VerMedicamentos.ver_medicamentos(hospital)
                    opcion_med = leer_entero()

                    if opcion_med <= 0 or opcion_med > len(lista_medicamentos):
                        print("Opción no válida. Intente de nuevo.")
                    else:
                        escogido = lista_medicamentos[opcion_med - 1]
                        print("Ingrese la nueva cantidad del medicamento:")
                        cantidad = leer_entero()
                        escogido.set_cantidad(cantidad)
                        print("Se ha actualizado el medicamento:")
                        print(escogido)
                        break
                continue

            elif opcion == 2:
                print("Por favor, ingrese el nombre del nuevo medicamento:")
                nombre = leer_string()

                enfermedades = Enfermedad.get_enfermedades_registradas()
                while True:
                    print("¿Qué enfermedad trata este medicamento?")
                    print("0. Registrar una nueva enfermedad")
                    for i, enf in enumerate(enfermedades):
                        print(f"{i + 1}. {enf}")

                    opcion_enf = leer_entero()

                    if opcion_enf == 0:
                        print("Por favor, ingrese el nombre de la nueva enfermedad:")
                        n_enfermedad = leer_string()
                        print("Por favor, ingrese la tipología de la enfermedad:")
                        t_enfermedad = leer_string()
                        print("Por favor, ingrese la especialidad que trata dicha enfermedad:")
                        e_enfermedad = leer_string()
                        nueva_enfermedad = Enfermedad(e_enfermedad, n_enfermedad, t_enfermedad)
                        print("¡Se ha registrado la nueva enfermedad en el sistema!")
                    elif opcion_enf <= 0 or opcion_enf > len(enfermedades):
                        print("Opción no válida. Por favor intente de nuevo.")
                    else:
                        enfermedad = enfermedades[opcion_enf - 1]
                        break

                print("Por favor, ingrese una descripción para el medicamento:")
                d_medicamento = leer_string()
                print("Por favor, ingrese la cantidad de unidades del medicamento:")
                c_medicamento = leer_entero()
                print("Por favor, ingrese el precio del medicamento:")
                p_medicamento = leer_flotante()

                nuevo_medicamento = Medicamento(nombre, enfermedad, d_medicamento, c_medicamento, p_medicamento)
                hospital.get_lista_medicamentos().append(nuevo_medicamento)
            else:
                print("Opción no válida. Por favor intente de nuevo.")

            while True:
                print("¿Desea añadir un nuevo medicamento? (s/n)")
                confirmar = leer_string().lower()

                if confirmar in ['s', 'n']:
                    anadir_otro = confirmar == 's'
                    break
                else:
                    print("Opción no válida. Por favor intente de nuevo.")

        print("¡Se han actualizado los medicamentos!")


    @staticmethod
    def verPersonasRegistradas(hospital):
        listaDoctores = hospital.getListaDoctores()
        listaPacientes = hospital.getListaPacientes()
        print("Doctores: ")
        for i, doc in enumerate(listaDoctores):
            print(f"{i + 1}. {doc}")
        print("Paciente: ")
        for i, doc in enumerate(listaPacientes):
            print(f"{i + 1}. {doc}")
    @staticmethod
    def construirHabitacion(hospital):

        print("Por favor, ingrese la informacion de la nueva habitacion: ")
        print("ingrese el NUMERO de la habitacion")
        habitacion =