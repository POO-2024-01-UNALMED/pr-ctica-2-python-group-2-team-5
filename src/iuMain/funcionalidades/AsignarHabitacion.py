from tkinter import *
from tkinter import ttk, messagebox

from src.gestorAplicacion.servicios.Habitacion import Habitacion
from src.manejoDeErrores.ErroresAplicacion import DatosFalsos, TipoIncorrecto, CampoVacio, EstaHospitalizado
#from src.iuMain.gestion.FieldFrame import FieldFrame TODO: Crear la clase FieldFrame


def mostraTitulo(frame):
    # Limpiar el Frame.
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = Label(frame, text="Asignar Habitación", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)


def asignarHabitacion(hospital, frame):
    def mostrarAsignacion(paciente):
        # cuando se confirma se muestra en pantalla el resumen de la asignacion
        mostraTitulo(frame)
        labelPaciente = Label(frame, text="Resumen asignación de habitación del Paciente:", bg="white", font=("Helvetica", 12))
        labelPaciente.pack(pady=10)

        infoHabitacion = Text(frame, bg="white", font=("Helvetica", 14))
        infoHabitacion.pack(fill="both", expand=True)

        textoInfo = f"Nombre: {paciente.nombre}\nCedula: {paciente.cedula}\nNumero de habitación: {paciente.habitacion_asignada.numero}\nCategoria de Habitacion:  {paciente.habitacion_asignada.categoria.name}\n"
        infoHabitacion.insert("end", textoInfo)
        infoHabitacion.config(padx=30, highlightthickness=5, highlightbackground="#4D5BE4", state="disabled")

        # Se importa aca para evitar una referencia circular
        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        botonRegresar = Button(frame, text="Regresar", command = lambda: implementacionDefault(frame))
        botonRegresar.pack()

    # Ingreso de datos para asignar habitación.
    def ingresarDatosHabitacion(paciente):
        # Se pide confirmar la asignacion y se actualiza la lista de habitaciones
        def confirmarHabitacion():
            eleccion = entry.get()
            if eleccion:
                resultado = messagebox.askyesno("Confirmar habitación","¿Está seguro de que desea elegir esta habitación?")
                if resultado:
                    numeroHabitacion, categoriaHabitacion = cboxElegirHabitacion.get().split(" - ")
                    for i, habitacion in enumerate(hospital.habitaciones):
                        if habitacion.numero == int(numeroHabitacion) and habitacion.categoria == categoriaHabitacion:
                            habitacion.ocupada = True
                            habitacion.dias = int(entry.get())
                            habitacion.paciente = paciente
                            paciente.habitacionAsignada = habitacion
                            break
                    messagebox.showinfo("Habitación asignada!", "La habitación se ha asignado exitosamente!")
                    mostrarAsignacion(paciente)

                else:
                    messagebox.showinfo("Asignación cancelada", "Usted ha decidido cancelar la elección de habitación")
                    # Se importa aca para evitar una referencia circular
                    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                    implementacionDefault(frame)

            else:
                try:
                    raise CampoVacio()
                except CampoVacio as c:
                    c.enviarMensaje()

        def obtenerCategorias(paciente):
            # Código para obtener las categorías disponibles según la EPS del usuario
            if paciente.tipoEps == "Subsidiado":
                return ["CAMILLA", "OBSERVACION", "UCI"]
            elif paciente.tipoEps == "Contributivo":
                return ["INDIVIDUAL", "DOBLE", "OBSERVACION", "UCI", "UCC"]
            else:
                return ["CAMILLA", "UCI"]

        def obtenerHabitaciones(categoria):
            # Código para obtener las habitaciones disponibles para la categoría seleccionada
            habitacionesDisponibles = []
            for habitacion in hospital.habitaciones:
                if habitacion.categoria == categoria:
                    if not habitacion.ocupada:
                        habitacionesDisponibles.append(habitacion)
            return habitacionesDisponibles

        mostraTitulo(frame)

        infoPaciente = Label(frame, text=f"{paciente.nombre} - CC: {paciente.cedula}", bg="white", font=("Helvetica", 12))
        infoPaciente.pack(pady=10)

        frame1 = Frame(frame, bg="white")
        frame1.pack()

        def limpiarEntry():
            entry.delete("0", "end")

        # Habilitar el combobox de habitaciones.
        def habilitarElegirHabitacion(event):
            eleccion = cboxTipoCategoria.get()
            cboxElegirHabitacion.set("")
            limpiarEntry()
            entry.config(state='disabled')
            if eleccion:
                habitacionesDisponibles = obtenerHabitaciones(eleccion)
                if habitacionesDisponibles:
                    cboxElegirHabitacion['state'] = 'readonly'
                    cboxElegirHabitacion['values'] = [f"{habitacion.numero} - {habitacion.categoria}" for habitacion in habitacionesDisponibles]
                else:
                    # No hay habitaciones disponibles para la categoría seleccionada
                    respuesta = messagebox.askquestion("No hay habitaciones disponibles","No hay habitaciones disponibles para la categoría seleccionada. ¿Desea cambiar de categoría?")
                    if respuesta == 'yes':
                        # Aquí puedes implementar la lógica para cambiar la categoría
                        nuevaCategoria = Habitacion.BuscarOtraCategoria(cboxTipoCategoria.get())  # Función para obtener la nueva categoría
                        if nuevaCategoria:
                            cboxTipoCategoria.set(str(nuevaCategoria))  # Establecer la nueva categoría en el Combobox
                            habilitarElegirHabitacion(None)  # Llamar nuevamente a la función para habilitar las habitaciones

                    else:

                        cboxElegirHabitacion['state'] = 'disabled'
            else:
                cboxElegirHabitacion['state'] = 'disabled'

        # Codigo para habilitar el entry de dias estimados
        def habilitarIngresoDias(event):
            eleccion = cboxElegirHabitacion.get()
            limpiarEntry()
            if eleccion:
                entry.config(state='normal')
                entry.update()  # Agregar esta línea para actualizar el estado del Entry
            else:
                entry.config(state='disabled')
                limpiarEntry()

        # Labels y Combobox necesarios para llenar la informacion para asignar la habitacion
        tipoCategoria = Label(frame1, text="Seleccione el tipo de categoria:", bg="white", font=("Helvetica", 10, "bold"))
        tipoCategoria.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        valorPorDefecto1 = StringVar()

        cboxTipoCategoria = ttk.Combobox(frame1, values=obtenerCategorias(paciente), textvariable=valorPorDefecto1, state="readonly")
        cboxTipoCategoria.bind("<<ComboboxSelected>>", habilitarElegirHabitacion)
        cboxTipoCategoria.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        ElegirHabitacion = Label(frame1, text="Seleccione la habitación de su preferencia:", bg="white", font=("Helvetica", 10, "bold"))
        ElegirHabitacion.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        valorPorDefecto2 = StringVar()

        cboxElegirHabitacion = ttk.Combobox(frame1, textvariable=valorPorDefecto2, state="disabled")
        cboxElegirHabitacion.bind("<<ComboboxSelected>>", habilitarIngresoDias)
        cboxElegirHabitacion.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        labelEntry = Label(frame1, text="Ingrese los dias:", bg="white", font=("Helvetica", 10, "bold"))
        labelEntry.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        entry = Entry(frame1, state='disabled')
        entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Boton para aceptar e ir a la confirmacion de la asignacion
        botonAceptar = Button(frame, text="Aceptar", command=confirmarHabitacion)
        botonAceptar.pack(pady=5)

        # Se importa aca para evitar una referencia circular
        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
        # Boton para regresar a la ventana principal
        boton_regresar = tk.Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
        boton_regresar.pack(pady=5)

    # Aca se verifica que el paciente exista, que no tenga ya una habitacion asignada y que no hubieron errores al ingresarlo
    def buscarPaciente():
        cedula = framePaciente.getValue(1)

        if len(cedula) != 0:
            try:
                paciente = hospital.buscarPaciente((int(cedula)))
                if paciente.habitacionAsignada is None:
                    ingresarDatosHabitacion(paciente)
                else:
                    try:
                        raise EstaHospitalizado()
                    except EstaHospitalizado as e:
                        e.enviarMensaje()
            except DatosFalsos as d:
                d.enviarMensaje()
            except ValueError:
                TipoIncorrecto().enviarMensaje()
        else:
            try:
                raise CampoVacio()
            except CampoVacio as c:
                c.enviarMensaje()

    mostraTitulo(frame)

    # Pide la cedula del paciente

    ingresoCedula = Label(frame, text="Ingrese la cédula del paciente:", bg="white", font=("Helvetica", 10, "bold"))
    ingresoCedula.pack()

    criterios = ["Cédula"]

    framePaciente = FieldFrame(frame, "", criterios, "", None, None)
    framePaciente.pack()

    botonBuscarPaciente = Button(frame, text="Buscar", command=buscarPaciente())
    botonBuscarPaciente.pack(pady=10)

    # Funcionalidad para regresar a la ventana principal

    # Se importa aca para evitar una referencia circular
    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

    botonRegresar = Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
    botonRegresar.pack()