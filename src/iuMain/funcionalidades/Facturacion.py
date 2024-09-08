#Importar lo necesario...
from src.gestorAplicacion import Cita, Formula, Habitacion
from src.gestorAplicacion.servicios import Servicio


class Facturacion:
    
    @staticmethod
    def facturacion(hospital):
        # Buscar paciente
        paciente_seleccionado = None

        while paciente_seleccionado is None:
            print("Ingrese la cédula del paciente:")
            cedula = int(input().strip())
            paciente_seleccionado = hospital.buscar_paciente(cedula)

            if paciente_seleccionado is None:
                print("Paciente no encontrado. ¿Desea intentar de nuevo? (s/n)")
                if input().strip().lower() == "n":
                    return

        # Buscar servicios pendientes por pago
        servicios_sin_pagar = Servicio.obtener_servicios_sin_pagar(paciente_seleccionado)

        if not servicios_sin_pagar:
            print("El paciente no tiene servicios pendientes de pago.")
            return

        print("El paciente tiene servicios pendientes de pago:")

        for servicio in servicios_sin_pagar:
            print(servicio.descripcion_servicio())

        # Seleccionar para pagar
        servicio_seleccionado = None
        print("Ingrese el número del servicio que va a pagar:")

        while servicio_seleccionado is None:
            id_seleccionada = int(input().strip())
            for servicio in servicios_sin_pagar:
                if servicio.get_id_servicio() == id_seleccionada:
                    servicio_seleccionado = servicio
                    break

            if servicio_seleccionado is None:
                print("Servicio no encontrado. ¿Desea intentar de nuevo? (s/n)")
                if input().strip().lower() == "n":
                    return

        # Calcular precios 
        # Hay ligadura dinámica
        precio_servicio_seleccionado = 0
        if isinstance(servicio_seleccionado, Formula):
            precio_servicio_seleccionado = paciente_seleccionado.calcular_precio(servicio_seleccionado)
        elif isinstance(servicio_seleccionado, CitaVacuna):
            precio_servicio_seleccionado = paciente_seleccionado.calcular_precio(servicio_seleccionado)
        elif isinstance(servicio_seleccionado, Habitacion):
            precio_servicio_seleccionado = paciente_seleccionado.calcular_precio(servicio_seleccionado)
        elif isinstance(servicio_seleccionado, Cita):
            precio_servicio_seleccionado = paciente_seleccionado.calcular_precio(servicio_seleccionado)

        # el momneto mas duro de todos(pagar)
        print(f"Total a pagar: ${precio_servicio_seleccionado}")
        print("¿Desea pagar? (s/n)")

        if input().strip().lower() == "s":
            servicio_seleccionado.validar_pago(paciente_seleccionado, servicio_seleccionado.get_id_servicio())
            print("Pago realizado con éxito")
        else:
            print("Pago cancelado")

        # Limpiar la lista de servicios sin pagar
        servicios_sin_pagar.clear()