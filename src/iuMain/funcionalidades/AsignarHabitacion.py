from src.gestorAplicacion import CategoriaHabitacion


class AsignarHabiatcion:

    @staticmethod
    def disponibilidadHabitacion(habitaciones, paciente):
        if habitaciones:
            print(f"Las habitaciones para la categoría {paciente.getCategoriaHabitacion()} son:")

            for i, Habitacion in enumerate(habitaciones, start = 1):
                print(f"{i}. ID habitación: {Habitacion.getNumero()}:")

            eleccion = int(input("Escoja la habitación de su preferencia: "))

            # casos  de error:
            while eleccion < 1 or eleccion > len(habitaciones):
                print("Elija una opción válida")
                eleccion = int(input("Escoja la habitación de su preferencia: "))

            auxiliarHbitaciones = habitaciones.pop(eleccion - 1 )

            # Devolvemos la opcion elegida:
            return auxiliarHbitaciones
        return None

    @staticmethod
    def asignarHabitacion(Hospital):
        #buscar paciente
        nIdentificacion = int(input("Por favor, ingrese el número de identidicación del paciente"))
        paciente = Hospital.buscarPaciente(nIdentificacion)

        #el paciente no puede tener una habitacion asignada previamente

        if paciente:
            if not paciente.getHabitacionAsignada():
                Habitacion =  None

                #Revision del tipo de eps del paciente para mostrar habitaciones disponibles
                if paciente.getTipoEps() == "Subsidiado":
                    eleccion = None
                    while eleccion not in {1, 2, 3}:
                        print("Seleccione el tipo de habitacion que necesite. Recuerde que el precio a  pagar se determina pr el tipo de la habitación.")
                        print("1. Camilla. \n2. Observación. \n3. Uci")
                        eleccion = int(input())

                        if eleccion == 1:
                            paciente.setCategoriaHabitacion(CategoriaHabitacion.CAMILLA)

                        elif eleccion == 2:
                            paciente.setCategoriaHabitacion(CategoriaHabitacion.OBSERVACION)

                        elif eleccion == 3:
                            paciente.setCategoriaHabitacion(CategoriaHabitacion.UCI)

                        else:
                            print("Elija una opción válida")

                        if eleccion in {1, 2, 3}:
                            hDisponibles = Habitacion.buscarHabitacionDisponible(paciente.getCategoriaHabitacion())
                            Habitacion = AsignarHabiatcion.disponibilidadHabitacion(hDisponibles, paciente)

                elif paciente.getTipoEps() == "Contributivo":
                    eleccion = None
                    while eleccion not in {1, 2, 3}:
                        print("Seleccione el tipo de habitacion que necesite. Recuerde que el precio a pagar se determina pr el tipo de la habitación.")
                        print("1. Individual. \n2. Doble. \n3. Onservación. \n4. Uci. \n5. Ucc")
                        eleccion = int(input())

                        if eleccion == 1:
                            paciente.setCategoriaHabitacion(CategoriaHabitacion.INDIVIDUAL)

                        elif eleccion == 2:
                            paciente.setCategoriaHabitacion(CategoriaHabitacion.DOBLE)

                        elif eleccion == 3:
                            paciente.setCategoriaHabitacion(CategoriaHabitacion.OBSERVACION)

                        elif eleccion == 4:
                            paciente.setCategoriaHabitacion(CategoriaHabitacion.UCI)

                        elif eleccion == 5:
                            paciente.setCategoriaHabitacion(CategoriaHabitacion.UCC)

                        else:
                            print("Elija una opción válida")

                        if eleccion in {1, 2, 3, 4, 5}:
                            hDisponibles = Habitacion.buscarHabitacionDisponible(paciente.getCategoriaHabitacion())
                            Habitacion = AsignarHabiatcion.disponibilidadHabitacion(hDisponibles, paciente)


                else:
                    eleccion = None
                    while eleccion not in {1, 2}:
                        print("Seleccione el tipo de habitacion que necesite. Recuerde que el precio a pagar se determina pr el tipo de la habitación.")
                        print("1. Camilla. \n2. Uci.")
                        eleccion = int(input())

                        if eleccion == 1:
                            paciente.setCategoriaHabitacion(CategoriaHabitacion.CAMILLA)
                        
                        elif eleccion == 2:
                            paciente.setCategoriaHabitacion(CategoriaHabitacion.UCI)

                        else:
                            print("Elija una opción válida")

                        if eleccion in {1,2}:
                            hDisponibles = Habitacion.buscarHabitacionDisponible(paciente.getCategoriaHabitacion())
                            Habitacion = AsignarHabiatcion.disponibilidadHabitacion(hDisponibles, paciente)

                if Habitacion:
                    # la habitacion ahora esta ocupada:
                    Habitacion.setOcupada(True)

                    #Asignar habitacion al paciente y viceversa:
                    Habitacion.setPacinete(paciente)
                    paciente.setHabitacionAsignada(Habitacion)

                    #Informacion de la habitacion asignada:
                    print("\nSe le ha asignado una habitacion! A continuación está la información de su reserva:")
                    print(f"Cédula del Paciente: {paciente.getCedula()}")
                    print(f"Nombre del Paciente: {paciente.getNombre()}")
                    print(f"Número de Id del la habitación: {Habitacion.getNumero()}")
                    print(f"Categoría de la habitacion: {Habitacion.getCategoria()}")

                else:
                    print(f"Que pena me da!, Latin Brothers. No hay habitaciones disponibles en este momento para la categoría {paciente.getCategoriaHabitacion()}")
                    eleccion = input("¿Desea elegir una habitación de otra categoría (S/N)? ").strip().upper()

                    if eleccion == "S":
                        categoria = Habitacion.buscarOtracategoria(paciente.getCategoriaHabitacion())
                        otraHabitacionDisponibles = Habitacion.buscarHabitacionDisponible(categoria)
                        otraHabitacion = AsignarHabiatcion.disponibilidadHabitacion(otraHabitacionDisponibles, paciente)

                        if otraHabitacion:
                            # la habitacion ahora esta ocupada:
                            otraHabitacion.setOcupada(True)
                            #Asignar habitacion al paciente y viceversa:
                            otraHabitacion.setPacinete(paciente)
                            paciente.setHabitacionAsignada(otraHabitacion)

                            #Días de uso:
                            dias = int(input("¿Cuántos días estima que hará uso de la habitación? "))
                            paciente.getHabitacionAsignada().setDias(dias)

                            #Informacion de la habitación asignada:
                            print("\nSe le ha asignado una habitación! A continuación está la información de su reserva:")
                            print(f"Cédula del Paciente: {paciente.getcedula()}")
                            print(f"Nombre del Paciente: {paciente.getNombre()}")
                            print(f"Número de Id del la habitación: {otraHabitacion.getNumero()}")
                            print(f"Categoría de la habitación: {otraHabitacion.getCategoria()}")

                        else:
                            print(f"Lo siento, no hay habitaciones disponibles en este momento para ninguna de las categoría.")

                    else:
                        print("operación cancelada por el usuario.")

            else:
                print("El paciente ya tiene una habitación reservada.")
        else:
            print(f"El paciente con identificación {nIdentificacion} no está registrado en el sistema.")

            






