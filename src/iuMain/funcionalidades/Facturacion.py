#Importar lo necesario...

from src.gestorAplicacion.administracionHospital import Hospital
from src.gestorAplicacion.servicios.Servicio import Servicio
from src.gestorAplicacion.servicios.Cita import Cita
from src.gestorAplicacion.servicios.CitaVacuna import CitaVacuna
from src.gestorAplicacion.servicios.Formula import Formula
from src.gestorAplicacion.servicios.Habitacion import Habitacion
from src.gestorAplicacion.personas import Paciente


class Facturacion:
    
    @staticmethod
    def facturacion(hospital):
        # Buscar paciente
        pacienteSeleccionado = None

        while pacienteSeleccionado is None:
            print("Ingrese la cédula del paciente:")
            cedula = int(input().strip())
            pacienteSeleccionado = hospital.buscarPaciente(cedula)

            if pacienteSeleccionado is None:
                print("Paciente no encontrado. ¿Desea intentar de nuevo? (s/n)")
                if input().strip().lower() == "n":
                    return

        # Buscar servicios pendientes por pago
        serviciosSinPagar = Servicio.obtenerServiciosSinPagar(pacienteSeleccionado)

        if not serviciosSinPagar:
            print("El paciente no tiene servicios pendientes de pago.")
            return

        print("El paciente tiene servicios pendientes de pago:")

        for servicio in serviciosSinPagar:
            print(servicio.descripcionServicio())

        # Seleccionar para pagar
        servicioSeleccionado = None
        print("Ingrese el número del servicio que va a pagar:")

        while servicioSeleccionado is None:
            idSeleccionada = int(input().strip())
            for servicio in serviciosSinPagar:
                if servicio.getIdServicio() == idSeleccionada:
                    servicioSeleccionado = servicio
                    break

            if servicioSeleccionado is None:
                print("Servicio no encontrado. ¿Desea intentar de nuevo? (s/n)")
                if input().strip().lower() == "n":
                    return

        # Calcular precios 
        # Hay ligadura dinámica
        precioServicioSeleccionado = 0
        if isinstance(servicioSeleccionado, Formula):
            precioServicioSeleccionado = pacienteSeleccionado.calcularPrecio(servicioSeleccionado)
        elif isinstance(servicioSeleccionado, CitaVacuna):
            precioServicioSeleccionado = pacienteSeleccionado.calcularPrecio(servicioSeleccionado)
        elif isinstance(servicioSeleccionado, Habitacion):
            precioServicioSeleccionado = pacienteSeleccionado.calcularPrecio(servicioSeleccionado)
        elif isinstance(servicioSeleccionado, Cita):
            precioServicioSeleccionado = pacienteSeleccionado.calcularPrecio(servicioSeleccionado)

        # el momneto mas duro de todos(pagar)
        print(f"Total a pagar: ${precioServicioSeleccionado}")
        print("¿Desea pagar? (s/n)")

        if input().strip().lower() == "s":
            servicioSeleccionado.validarPago(pacienteSeleccionado, servicioSeleccionado.getIdServicio())
            print("Pago realizado con éxito")
        else:
            print("Pago cancelado")

        # Limpiar la lista de servicios sin pagar
        serviciosSinPagar.clear()