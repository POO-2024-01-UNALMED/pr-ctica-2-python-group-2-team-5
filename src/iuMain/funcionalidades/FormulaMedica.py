from tkinter import *
from tkinter import ttk, messagebox
from gestorAplicacion.servicios.Formula import Formula
from manejoDeErrores.ErroresAplicacion import *
from iuMain.gestion.FieldFrame import FieldFrame

def mostratTitulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = Label(frame, text="Formular Medicamentos", bg="white", font=("Helvetica", 10, "bold"))
    titulo.pack()

def formulaMedica(hospital, frame):
    def doctorFormula(paciente):
        def habilitarDoctor(event):
            global valorPorDefecto1
            indiceSeleccionado = cboxEnfermedades.current()
            objetoSeleccionado = paciente.HISTORIACLINICA.enfermedades[indiceSeleccionado]
            valorPorDefecto1 = objetoSeleccionado.nombre + objetoSeleccionado.tipologia
            eleccion = cboxEnfermedades.get()
            listaDocEnf = paciente.HISTORIACLINICA.buscarCitaDoc(objetoSeleccionado.especialidad, hospital)
            cboxElegirDoctor.set("")
            if len(listaDocEnf) != 0:
                if eleccion:
                    cboxElegirDoctor['state'] = 'readonly'
                    cboxElegirDoctor['values'] = listaDocEnf
                else:
                    cboxElegirDoctor['state'] = 'disabled'

                indiceEnfermedad = cboxEnfermedades.current()
                enfObjeto = paciente.HISTORIACLINICA.enfermedades[indiceEnfermedad]

                if len(paciente.HISTORIACLINICA.buscarCitaDoc(enfObjeto.especialidad, hospital)) != 0:
                    formulaPaciente = Formula(paciente)
                    for widget in frame.winfo_children():
                        if isinstance(widget, Button) and widget.cget("text") == "Seleccionar medicamentos":
                            widget.destroy()

                    # Crear nuevo botón.
                    botonSeleccionar = Button(frame, text="Seleccionar medicamentos", command=lambda: seleccionMedicamentos(enfObjeto, formulaPaciente, cboxElegirDoctor.get()))
                    botonSeleccionar.pack()

                else:
                    try:
                        raise SinCitaPrevia()
                    except SinCitaPrevia as s:
                        s.enviarMensaje()
                        # Se importa aca para evitar una referencia circular
                        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                        implementacionDefault(frame)
            else:
                try:
                    raise SinCitaPrevia()
                except SinCitaPrevia as s:
                    s.enviarMensaje()
                    cboxElegirDoctor['state'] = 'disabled'
                    # Se importa aca para evitar una referencia circular
                    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                    implementacionDefault(frame)

        mostratTitulo(frame)

        # Mostrar la informacion del paciente.
        infoPaciente = Label(frame, text = f"{paciente.nombre} - CC: {paciente.cedula}", bg = "white")
        infoPaciente.pack

        # Widgets necesarios para la funcionalidad.

        # Frames que los contiene.
        frameDatos = Frame(frame)
        frameDatos.pack()

        # Label con indicaciones y ComboBox
        enfermedadTratar = Label(frameDatos, text="Seleccione la enfermedad a tratar: ", bg = "white")
        enfermedadTratar.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        valorPorDefecto1 = StringVar()

        cboxEnfermedades = ttk.Combobox(frameDatos, values=paciente.HISTORIACLINICA.enfermedades, textvariable=valorPorDefecto1, state = 'readonly')
        cboxEnfermedades.bind("<<ComboboxSelected>>", habilitarDoctor)
        cboxEnfermedades.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Label para pedir ingreso de doctor y ComboBox.
        elegirDoctor = Label(frameDatos, text="Seleccione el doctor que hará la formula:", bg="white")
        elegirDoctor.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        valorPorDefecto2 = StringVar()

        cboxElegirDoctor = ttk.Combobox(frameDatos, textvariable=valorPorDefecto2, state="disabled", width=30)
        cboxElegirDoctor.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        def seleccionMedicamentos(enfermedad, formula, doctor):
            if doctor != "":
                # Nuevo frame para seleccion de medicamentos.
                mostratTitulo(frame)
                frameSeleccion = Frame(frame, bg="white")
                frameSeleccion.pack(fill="both", expand=True)
                medicamentosDisponibles = paciente.medEnfermedad(enfermedad, hospital)

                if len(medicamentosDisponibles) != 0:
                    # Titulo seleccion medicamentos.
                    tituloSeleccion = Label(frameSeleccion, text="Seleccione los medicamentos", bg="white")
                    tituloSeleccion.pack()

                    # Listbox para eleccion de medicamentos.
                    listBoxMedicamentos = Listbox(frameSeleccion, selectmode="multiple", bg = "whte")
                    listBoxMedicamentos.pack(fill="both", expand=True)

                    # Agregar los elementos al listbox.
                    for med in medicamentosDisponibles:
                        listBoxMedicamentos.insert("end", med)

                    # Finalizar la selección.
                    botonFinalizar = Button(frameSeleccion, text = "Finalizar selección", command=lambda: obtenerSeleccion(listBoxMedicamentos.curselection(), medicamentosDisponibles, formula, doctor))
                    botonFinalizar.pack()
                else:
                    try:
                        raise SinMedicamentos()
                    except SinMedicamentos as s:
                        s.enviarMensaje()
                        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                        implementacionDefault(frame)
            else:
                try:
                    raise ValueError
                except ValueError:
                    IngresoErroneo("No ha elegido ningún doctor").enviarMensaje()
                    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                    implementacionDefault(frame)

        def obtenerSeleccion(seleccion, disponibles, formula, doctor):
            mostratTitulo(frame)

            # Indices seleccionados en el listbox.
            indicesSeleccionados = seleccion

            # Ver los medicamentos usando los indices.
            medicamentosSeleccionados = [disponibles[indice] for indice in indicesSeleccionados]
            if len(medicamentosSeleccionados) != 0:
                frameMedicamentosSeleccionados = Frame(frame)
                frameMedicamentosSeleccionados.pack(fill="both", expand=True)

                labelMedicamentosSeleccionados = Label(frameMedicamentosSeleccionados, text="Estos son sus medicamentos:", bg="white")
                labelMedicamentosSeleccionados.pack()

                formula.listaMedicamentos = medicamentosSeleccionados

                for med in medicamentosSeleccionados:
                    stringInformacion = med.mostrarInfo()
                    labelMedicamento = Label(frameMedicamentosSeleccionados, text=stringInformacion, bg="white")
                    labelMedicamento.pack()

                botonGenerarFormula = Button(frameMedicamentosSeleccionados, text=stringInformacion, bg="white")
                botonGenerarFormula.pack()
            else:
                try:
                    raise ValueError
                except ValueError:
                    IngresoErroneo("No ingresó ningún medicamento.").enviarMensaje()
                    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                    implementacionDefault(frame)

            def generarFormula(formulaPaciente, doctor):
                respuesta = messagebox.askyesno("Confirmar Fórmula", "¿Está seguro que desea generar esta formula?")
                if respuesta:
                    for med in formulaPaciente.listaMedicamentos:
                        med.eliminarCantidad()

                    for doc in hospital.listaDoctores:
                        if doc.nombre == doc.split(" ")[0]:
                            formulaPaciente.doctor = doc
                            paciente.HISTORIACLINICA.listaFormulas.append(formulaPaciente)
                            messagebox.showinfo("Formula Generada!", "La formula se ha generado exitosamente!")
                            mostrarHistorial(paciente)
                else:
                    messagebox.showinfo("Formula cancelada", "Usted ha decidido cancelar la fórmula")
                    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                    implementacionDefault(frame)
    def mostrarHistorial(paciente):
        mostratTitulo(frame)
        frameFormulas = Frame(frame)
        frameFormulas.pack(fill="both", expand=True)

        labelFormulas = Label(frameFormulas, text="Historial de formulas", bg="white")
        labelFormulas.pack(fill="both")

        for formula in paciente.HISTORIACLINICA.listaFormulas:
            label = Label(frameFormulas, text= formula.descripcionServicio())
            label.pack(fill="both", expand=True)

        # Botón para regresar a la presentación pincipal.
        # Se importa aca para evitar una referencia circular.
        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        botonRegresar = Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
        botonRegresar.pack(pady=5)

    def buscarPaciente():
        cedula = framePaciente.getValue(1)

        if len(cedula) != 0:
            try:
                paciente = hospital.buscarPaciente(int(cedula))
                doctorFormula(paciente)
            except DatosFalsos as d:
                d.enviarMensaje()
            except ValueError:
                TipoIncorrecto().enviarMensaje()
        else:
            try:
                raise CampoVacio()
            except CampoVacio as c:
                c.enviarMensaje()

    mostratTitulo(frame)

    # Se pide la cedula del paciente.
    ingresoCedula = Label(frame, text="Ingrese la cédula del paciente:", bg="white")
    ingresoCedula.pack()

    criterios = ["Cédula"]

    framePaciente = FieldFrame(frame, "", criterios, "", None, None)
    framePaciente.pack()

    # Botón para buscar paciente
    botonBuscarPaciente = Button(frame, text="Buscar", command=buscarPaciente)
    botonBuscarPaciente.pack(pady=10)

    # Botón para regresar a la presentación pincipal.
    # Se importa aca para evitar una referencia circular.
    from iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

    botonRegresar = Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
    botonRegresar.pack(pady=5)