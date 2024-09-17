from tkinter import *
from tkinter import messagebox

from src.gestorAplicacion.servicios.Servicio import Servicio
from src.manejoDeErrores.ErroresAplicacion import DatosFalsos, TipoIncorrecto, CampoVacio, SinServicioSeleccionado
#from src.iuMain.gestion.FieldFrame import FieldFrame ---> TODO: Crear clase FieldFrame

# Mostrar el titulo de la funcionalidad.
def mostrarTitulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = Label(frame, text="Facturación", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def facturacion(hospital, frame):
    def validarListaServicios(paciente, listaServicios, opcion):
        if len(listaServicios) == 0:
            try:
                raise SinServicioSeleccionado()
            except SinServicioSeleccionado as s:
                s.enviarMensaje()
        else:
            if opcion == 1:
                calcularPrecio(paciente, listaServicios)
            elif opcion == 2:
                validarPago(paciente, listaServicios)

    def validarPago(paciente, servicios):
        respuesta = messagebox.askyesno("Confirmar pago", "¿Desea realizar el pago?")
        if respuesta:
            for servicio in servicios:
                servicio.validarPago(paciente, servicio.IDSERVICIO)
            messagebox.showinfo("Pago realizado!", "El pago se ha realizado exitosamente")
        else:
            messagebox.showinfo("Pago cancelado", "Usted ha decidido cancelar el pago")


        # Regresar a la presentacion principal
        # Lo importamos acá para evitar una referencia circular.
        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        implementacionDefault(frame)

    def calcularPrecio(paciente, servicios):
        def calcularPrecioServicio(servicio, labelServicios):
            # Permite editar la variable desde la funcion sin pasarla como argumento
            nonlocal precioTotal

            if servicio in labelServicios:
                servicios.remove(servicio)
                labelServicios.config(bg = "white")
                precioTotal -= paciente.calcularPrecio(servicio)
            else:
                servicios.append(servicio)
                labelServicios.config(bg = "lightblue")
                precioTotal += paciente.calcularPrecio(servicio)

                labelPrecioTotal.config(text=f"Precio total: ${precioTotal}")

        mostrarTitulo(frame)

        precioTotal = 0

        labelServicios = Label(frame, text="Confirme los servicios que va a pagar:", bg="white", font=("Helvetica", 10, "bold"))
        labelServicios.pack(pady = 10)

        servicios.sort(key=lambda servicio: servicio.IDSERVICIO)

        for servicio in servicios:
            precioServicio = paciente.calcularPrecio(servicio)
            precioTotal += precioServicio

            labelServicio = Label(frame, text=f"{servicio.descripcionServicio()} - "f"Precio: ${precioServicio}", bg="white")
            labelServicio.pack()
            labelServicio.config(bg = "lightblue")

            # Elegir el servicio haciendo click izquierdo.
            labelServicio.bind("<Button-1>", lambda event, s=servicio, ls= labelServicio: calcularPrecioServicio(s, ls))

        labelPrecioTotal = Label(frame, text=f"Precio total: ${precioTotal}", bg="white")
        labelPrecioTotal.pack(pady=10)

        botonPagar = Button(frame, text="Realizar pago", command=lambda: validarListaServicios(paciente, servicios, 2))
        botonPagar.pack(pady=10)

        # Boton para regresar a la ventana principal.

        # Lo importamos acá para evitar una referencia circular.
        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        botonRegresar = Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
        botonRegresar.pack()

        def obtenerServiciosSinPagar(paciente):
            def seleccionarServicio(servicio, labelServicio):
                if servicio in serviciosSeleccionados:
                    serviciosSeleccionados.remove(servicio)
                    labelServicio.config(bg = "white")
                else:
                    serviciosSeleccionados.append(servicio)
                    labelServicio.config(bg = "lightblue")

            listaServiciosSinPagar = Servicio.obtenerServiciosSinPagar(paciente)

            if len(listaServiciosSinPagar) == 0:
                messagebox.showinfo("Sin servicios pendientes", "Usted no tiene ningún servicios pendientes por pagar")
                # Regresar a la presentacion principal
                # Lo importamos acá para evitar una referencia circular.
                from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

                implementacionDefault(frame)
                return

            mostrarTitulo(frame)

            infoPaciente = Label(frame, text=f"{paciente.nombre} - CC: {paciente.cedula}", bg="white", font=("Helvetica", 12))
            infoPaciente.pack(pady=10)

            labelServicios = Label(frame, text="Lista de servicios sin pagar:", bg="white", font=("Helvetica", 10, "bold"))
            labelServicios.pack(pady=10)

            serviciosSeleccionados = []

            # Imprime cada servicio en un label.
            for servicio in listaServiciosSinPagar:
                labelServicio = Label(frame, text=servicio.descripcionServicio(), bg="white")
                labelServicio.pack()

                # Seleccionar el servicio al hacer click izquierdo
                labelServicio.bind("<Button-1>", lambda event, s = servicio, ls = labelServicio: seleccionarServicio(s, ls))

            botonPrecio = Button(frame, text="Continuar", command=lambda: validarListaServicios(paciente, serviciosSeleccionados, 1))
            botonPrecio.pack(pady=10)

            # Boton para regresar a la ventana principal.

            # Lo importamos acá para evitar una referencia circular.
            from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

            botonRegresar = Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
            botonRegresar.pack()

        # Se verifica que el paciente si exista en el sistema.
        def buscarPaciente():
            cedula = fieldPaciente.getValue(1)

            if len(cedula) != 0:
                try:
                    paciente = hospital.buscarPaciente(int(cedula))
                    obtenerServiciosSinPagar(paciente)

                except DatosFalsos as d:
                    d.enviarMensaje()
                except (ValueError, TypeError):
                    TipoIncorrecto().enviarMensaje()
            else:
                try:
                    raise CampoVacio()
                except CampoVacio as c:
                    c.enviarMensaje()

        mostrarTitulo(frame)

        # Pide la cedula del paciente.
        ingresoCedula = Label(frame, text="Ingrese la cédula del paciente:", bg="white", font=("Helvetica", 10, "bold"))
        ingresoCedula.pack()

        criterios = ["Cédula"]

        fieldPaciente = FieldFrame(frame, "", criterios, "", None, None)
        fieldPaciente.pack()

        # Botón para buscar paciente
        botonBuscarPaciente = Button(frame, text="Buscar", command=buscarPaciente())
        botonBuscarPaciente.pack(pady=10)

        # Botón para regresar a la presentación pincipal.
        # Se importa aca para evitar una referencia circular.
        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        botonRegresar = Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
        botonRegresar.pack(pady=5)
