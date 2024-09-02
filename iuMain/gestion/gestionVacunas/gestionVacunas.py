def menu_gestion_vacunas(hospital):
    while True:
        print("───────── MENU DE GESTION DE VACUNAS ─────────")
        print("1. Registrar Vacuna")
        print("2. Eliminar Vacuna")
        print("3. Agregar cita de una vacuna")
        print("4. Eliminar cita de una vacuna")
        print("5. Ver informacion de una vacuna")
        print("6. Regresar al menu anterior")
        print("7. Salir")
        print("──────────────────────────────")
        opcion = input("Seleccione una opción: ")

        try:
            opcion = int(opcion)
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            continue
        
        if opcion == 1:
            registrar_vacuna(hospital)
        elif opcion == 2:
            eliminar_vacuna(hospital)
        elif opcion == 3:
            agregar_cita_vacuna(hospital)
        elif opcion == 4:
            eliminar_cita_vacuna(hospital)
        elif opcion == 5:
            ver_vacuna(hospital)
        elif opcion == 6:
            return  # Regresa al menú anterior
        elif opcion == 7:
            serializar(hospital)
            print("Datos guardados. Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")








