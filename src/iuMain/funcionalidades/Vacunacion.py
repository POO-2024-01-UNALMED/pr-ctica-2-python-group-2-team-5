from tkinter import *
from tkinter import ttk, messagebox
from gestorAplicacion.administracionHospital import Hospital, Vacuna
from gestorAplicacion.servicios import CitaVacuna
from gestorAplicacion.personas import Paciente
from iuMain.gestion.gestionPacientes import administrarPacientes, registrarPacientes
from manejoDeErrores.ErroresAplicacion import DatosFalsos, TipoIncorrecto, CampoVacio, SinDoctores, SinAgenda, SinVacunas
from iuMain.gestion.FieldFrame import FieldFrame

def mostrarTitulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = Label(frame, text="Vacunación", bg="white",font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def vacunacion(hospital, frame):
    def mostrarHistorialVacunas(paciente):
        mostrarTitulo(frame)
        informacionHospital = Label(frame, text=f"Historial de vacunas de {paciente.nombre} - CC: {paciente.cedula}", bg="white")
        informacionHospital.pack(pady=10)

        textHistorialVacunas = Text(frame, bg="white")
        textHistorialVacunas.pack(fill = "both", expand = True)

        # Mostrar todas las vacunas que tiene el usuario.

        vacunasPaciente = []

        for cita in paciente.HISTORIACLINICA.historialVacunas:
            vacunasPaciente.append(cita.vacuna)

        for vacuna in vacunasPaciente:
            nombre = vacuna.nombre
            tipo = vacuna.tipo
            precio = vacuna.precio

            textoVacuna = f"Nombre: {nombre}\nTipo: {tipo}\nPrecio: {precio}\n"

            # Ubicar en el text Historial Vacunas.
            textHistorialVacunas.insert("end", textoVacuna)

        textHistorialVacunas.config(padx=30, highlightthickness=5, highlightbackground="#4D5BE4", state="disabled")

        # Botón para regresar a la presentación pincipal.
        # Se importa aca para evitar una referencia circular.
        from iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        botonRegresar = Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
        botonRegresar.pack(pady=5)

    def agendarVacuna(paciente):
        def confirmarCita():
            eleccion = cboxElegirCita.get()
            if eleccion:
                respuesta = messagebox.askyesno("Confirmar cita de vacuna", "¿Está seguro que desea agendar esta cita?")
                if respuesta:
                    for vacuna in paciente.buscarVacunaEps(cboxTipoVacuna.get(), hospital):
                        if vacuna.nombre == cboxElegirVacuna.get():
                            citaAgendada = vacuna.actualizarAgenda(paciente, cboxElegirCita.current() + 1, vacuna.mostrarAgendaDisponible())
                            paciente.actualizarHistorialVacunas(citaAgendada)
                    messagebox.showinfo("Vacuna agendada!", "La cita de vacunación se ha agendado exitosamente!")
                    mostrarHistorialVacunas(paciente)
                else:
                    messagebox.showinfo("Vacuna cancelada", "Usted ha decidido cancelar la cita de vacunación")
                    # Importamos aca para evitar referencia circular.
                    from iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                    implementacionDefault(frame)
            else:
                try:
                    raise CampoVacio()
                except CampoVacio as c:
                    c.enviarMensaje()
        def listarCitas():
            listaCitas = []
            try:
                for vacuna in paciente.buscarVacunaEps(cboxTipoVacuna, hospital):
                    if vacuna.nombre == cboxElegirVacuna.get():
                        for cita in vacuna.mostrarAgendaDisponible():
                            listaCitas.append(cita.fecha)
                return listaCitas

            except SinAgenda as s:
                s.enviarMensaje()
                cboxElegirCita['state'] = 'disabled'

        def habilitarElegirCita(event):
            eleccion = cboxElegirVacuna.get()
            cboxElegirCita.set("")
            if eleccion:
                cboxElegirCita['state'] = 'readonly'
                cboxElegirCita['values']= listarCitas()
            else:
                cboxElegirCita['state'] = 'disabled'

        def listarVacunas():
            listavacunas = []
            for vacuna in paciente.buscarVacunaEps(cboxTipoVacuna.get(), hospital):
                listavacunas.append(vacuna.nombre)
            return listavacunas

        def habilitarElegirVacuna(event):
            eleccion = cboxTipoVacuna.get()
            cboxElegirVacuna.set("")
            cboxElegirCita.set("")
            cboxElegirCita['state'] = 'disabled'
            if eleccion:
                cboxElegirVacuna['state'] = 'readonly'
                todasLasVacunas = listarVacunas()

                # Deshabilitar las vacunas ya se ha aplicado
                vacunasAplicadas = []
                for citaVacuna in paciente.HISTORIACLINICA.historialVacunas:
                    vacunasAplicadas.append(citaVacuna.vacuna.nombre)

                # Se filtran las ya se ha aplicado
                opcionesLibres = list(filter(lambda vacuna: vacuna not in vacunasAplicadas, todasLasVacunas))

                if len(opcionesLibres) != 0:
                    cboxElegirVacuna['values'] = opcionesLibres
                else:
                    try:
                        raise SinVacunas()
                    except SinVacunas as s:
                        s.enviarMensaje()
                        cboxElegirVacuna['state'] = 'disabled'

        mostrarTitulo(frame)

        infoPaciente = Label(frame, text=f"{paciente.nombre} - CC: {paciente.cedula}", bg="white")
        infoPaciente.pack(pady=20)

        frame1 = Frame(frame, bg = "white")
        frame1.pack()

        tipoVacuna = Label(frame1, text="Seleccione el tipo de vacuna: ")
        tipoVacuna.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        valorPorDefecto1 = StringVar()

        cboxTipoVacuna = ttk.Combobox(frame1, values=["Obligatoria", "No obligatoria"], textvariable=valorPorDefecto1, state="readonly")
        cboxTipoVacuna.bind("<<ComboboxSelected>>", habilitarElegirVacuna)
        cboxTipoVacuna.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        elegirVacuna = Label(frame1, text="Seleccione la vacuna de su preferencia:", bg="white")
        elegirVacuna.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        valorPorDefecto2 = StringVar()

        cboxElegirVacuna = ttk.Combobox(frame1, textvariable=valorPorDefecto2, state="disabled")
        cboxElegirVacuna.bind("<<ComboboxSelected>>", habilitarElegirCita)
        cboxElegirVacuna.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        elegirCita = Label(frame1, text="Seleccione una fecha para su cita en enfermería:", bg="white")
        elegirCita.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        valorPorDefecto3 = StringVar()

        cboxElegirCita = ttk.Combobox(frame1, textvariable=valorPorDefecto3, state="disabled")
        cboxElegirCita.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        botonAceptar = Button(frame, text="Aceptar", command=confirmarCita)
        botonAceptar.pack(pady=5)

        # Botón para regresar a la presentación pincipal.
        # Se importa aca para evitar una referencia circular.
        from iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        botonRegresar = Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
        botonRegresar.pack(pady=5)

    def buscarPaciente():
        cedula = framePaciente.getValue(1)
        if len(cedula) != 0:
            try:
                paciente = hospital.buscarPaciente(int(cedula))
                agendarVacuna(paciente)
            except DatosFalsos as d:
                d.enviarMensaje()
            except ValueError:
                TipoIncorrecto().enviarMensaje()
        else:
            try:
                raise CampoVacio()
            except CampoVacio as c:
                c.enviarMensaje()

    mostrarTitulo(frame)

    # Se pide la cedula del paciente

    ingresoCedula = Label(frame, text="Ingrese la cédula del paciente:", bg="white")
    ingresoCedula.pack()

    criterios = ["Cédula"]

    framePaciente = FieldFrame(frame,"", criterios, "", None, None)
    framePaciente.pack()

    botonBuscarPaciente = Button(frame, text="Buscar", command=buscarPaciente)
    botonBuscarPaciente.pack(pady=5)

    # Botón para regresar a la presentación pincipal.
    # Se importa aca para evitar una referencia circular.
    from iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

    botonRegresar = Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
    botonRegresar.pack(pady=5)