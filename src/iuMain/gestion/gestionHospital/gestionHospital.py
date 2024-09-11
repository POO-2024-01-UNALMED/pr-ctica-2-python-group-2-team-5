from gestorAplicacion.administracionHospital.CategoriaHabitacion import CategoriaHabitacion
from gestorAplicacion.administracionHospital.Enfermedad import Enfermedad
from gestorAplicacion.administracionHospital.Medicamento import Medicamento
from gestorAplicacion.servicios.Habitacion import Habitacion


class gestionHospital:
    @staticmethod
    def agregarMedicamentos(hospital):
        import sys

        def leerEntero():
            return int(input())

        def leerFlotante():
            return float(input())

        def leerString():
            return input().strip()

        anadir_otro = True
        while anadir_otro:
            print("¡Bienvenido! ¿Deseas aumentar el stock de un medicamento existente (1) o añadir uno nuevo (2)?")
            print("1. Aumentar el stock de un medicamento existente.")
            print("2. Ingresar un nuevo medicamento.")

            lista_medicamentos = hospital.get_lista_medicamentos()
            opcion = leerEntero()

            if opcion == 1:
                while True:
                    VerMedicamentos.ver_medicamentos(hospital)
                    opcion_med = leerEntero()

                    if opcion_med <= 0 or opcion_med > len(lista_medicamentos):
                        print("Opción no válida. Intente de nuevo.")
                    else:
                        escogido = lista_medicamentos[opcion_med - 1]
                        print("Ingrese la nueva cantidad del medicamento:")
                        cantidad = leerEntero()
                        escogido.set_cantidad(cantidad)
                        print("Se ha actualizado el medicamento:")
                        print(escogido)
                        break
                continue

            elif opcion == 2:
                print("Por favor, ingrese el nombre del nuevo medicamento:")
                nombre = leerString()

                enfermedades = Enfermedad.getEnfermedadesRegistradas()
                while True:
                    print("¿Qué enfermedad trata este medicamento?")
                    print("0. Registrar una nueva enfermedad")
                    for i, enf in enumerate(enfermedades):
                        print(f"{i + 1}. {enf}")

                    opcion_enf = leerEntero()

                    if opcion_enf == 0:
                        print("Por favor, ingrese el nombre de la nueva enfermedad:")
                        n_enfermedad = leerString()
                        print("Por favor, ingrese la tipología de la enfermedad:")
                        t_enfermedad = leerString()
                        print("Por favor, ingrese la especialidad que trata dicha enfermedad:")
                        e_enfermedad = leerString()
                        nueva_enfermedad = Enfermedad(e_enfermedad, n_enfermedad, t_enfermedad)
                        print("¡Se ha registrado la nueva enfermedad en el sistema!")
                    elif opcion_enf <= 0 or opcion_enf > len(enfermedades):
                        print("Opción no válida. Por favor intente de nuevo.")
                    else:
                        enfermedad = enfermedades[opcion_enf - 1]
                        break

                print("Por favor, ingrese una descripción para el medicamento:")
                d_medicamento = leerString()
                print("Por favor, ingrese la cantidad de unidades del medicamento:")
                c_medicamento = leerEntero()
                print("Por favor, ingrese el precio del medicamento:")
                p_medicamento = leerFlotante()

                nuevo_medicamento = Medicamento(nombre, enfermedad, d_medicamento, c_medicamento, p_medicamento)
                hospital.get_lista_medicamentos().append(nuevo_medicamento)
            else:
                print("Opción no válida. Por favor intente de nuevo.")

            while True:
                print("¿Desea añadir un nuevo medicamento? (s/n)")
                confirmar = leerString().lower()

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

        global habitacionOcupada

        print("Por favor, ingrese la informacion de la nueva habitacion: ")
        numerohabitacion = int(input("ingrese el NUMERO de la habitacion"))
        categoriahabitacion = None

        print("Por favor elija el tip de habitacion que desea construir\n1. CAMILLA\n2. INDIVIDUAL\n3. DOBLE\n4. OBSERVACION\n5. UCI\n6. UCC")
        eleccion = int(input("Escoja una de las opciones: "))

        if eleccion == 1:
            categoriahabitacion = CategoriaHabitacion.CAMILLA
        elif eleccion == 2:
            categoriahabitacion = CategoriaHabitacion.INDIVIDUAL
        elif eleccion == 3:
            categoriahabitacion = CategoriaHabitacion.DOBLE
        elif eleccion == 4:
            categoriahabitacion = CategoriaHabitacion.OBSERVACION
        elif eleccion == 5:
            categoriahabitacion = CategoriaHabitacion.UCI
        elif eleccion == 6:
            categoriahabitacion = CategoriaHabitacion.UCC
        else:
            print("opcion no valida")
            return
        while eleccion != 1 or eleccion != 2 or eleccion != 3 or eleccion != 4 or eleccion != 5 or eleccion != 6:
            habitacionOcupada = False

        dias = 0

        for habitacion in hospital.habitaciones:
            if (habitacion.numero == numerohabitacion and habitacion.categoria == categoriahabitacion) :
                print("La habitacion que desea construir ya existe")
                return
        nuevahabitacion = Habitacion(numerohabitacion, categoriahabitacion, habitacionOcupada, None, dias)
        hospital.get_habitaciones().append(nuevahabitacion)
        print("Se ha construido la habitacion exitosamente\n-Número de ID de la habitación: " + nuevahabitacion.getNumero()+ " " + "Categoría de la habitacion: " + nuevahabitacion.getCategoria())

    @staticmethod
    def destruirHabitacion(hospital):
            print("Por favor introduzca la informacion de la habitacion que desea destruir")
            nhabitacion = int(input("ingrese el NUMERO de la habitacion"))

            categoria = str(input("¿Qué tipo de habitación desea destruir?\n'CAMILLA', 'INDIVIDUAL', 'DOBLE', 'OBSERVACION', 'UCI', 'UCC': "))
            if categoria == "CAMILLA":
                hEscogida = CategoriaHabitacion.CAMILLA
            elif categoria == "INDIVIDUAL":
                hEscogida = CategoriaHabitacion.INDIVIDUAL
            elif categoria == "DOBLE":
                hEscogida = CategoriaHabitacion.DOBLE
            elif categoria == "OBSERVACION":
                hEscogida = CategoriaHabitacion.OBSERVACION
            elif categoria == "UCI":
                hEscogida = CategoriaHabitacion.UCI
            elif categoria == "UCC":
                hEscogida = CategoriaHabitacion.UCC
            else:
                print("opcion no valida")
                return
            for habitacion1 in hospital.habitaciones:
                if habitacion1.getNumero() == nhabitacion and habitacion1.getCategoria() == hEscogida:
                    if habitacion1.isOcupada():
                        hospital.get_habitaciones().remove(habitacion1)
                        print("Se ha destruido la habitacion exitosamente")
                    else:
                        print("La habitacion esta en uso y no puede ser destruida")
                        return


            print("La habitacion que desea destruir no existe")

