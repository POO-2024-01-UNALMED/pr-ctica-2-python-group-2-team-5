from tkinter import *
from tkinter import ttk, messagebox
from manejoDeErrores.ErroresAplicacion import DatosFalsos, TipoIncorrecto, CampoVacio, SinDoctores, SinAgenda
from iuMain.gestion.FieldFrame import FieldFrame

# Mostrar el titulo de la funcionalidad.
def mostarTitulo(frame):
    # Limpiar el Frame.
    for item in frame.winfo_children():
        item.destroy()

        # Imprime el titulo
        titulo = Label(frame, text="Agendar citas", bg="white", font=("Arial", 16, "bold"))
        titulo.pack(padx = 10, pady=10)

def agendarCitas(hospital, frame):

    #Mostrar historial citas.
    def mostrarHistorialCitas(paciente):
        mostarTitulo(frame)
        informacionHistorial = Label(frame, text=f"Historial de citas de {paciente.nombre} - CC: {paciente.cedula}", bg="white",font=("Helvetica", 12))
        informacionHistorial.pack(pady=10)

        textHistorialCitas = Text(frame, bg="white", font=("Arial", 14))
        textHistorialCitas.pack(fill="both", expand=True)

        for cita in paciente.HISTORIACLINICA.historialCitas:
            tipoCita = cita.doctor.especialidad
            nombreDoctor = cita.doctor.nombre
            fecha = cita.fecha

            textCita = f"Tipo de cita: {tipoCita}\nDoctor: {nombreDoctor}\nFecha: {fecha}\n"
            textHistorialCitas.insert("end", textCita)

        textHistorialCitas.config(padx = 30, state = "disabled")

        # Boton para regresar a la ventana principal.

        # Lo importamos acá para evitar una referencia circular.
        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        botonRegresar = Button(frame, text = "Regresar", command = lambda: implementacionDefault(frame))
        botonRegresar.pack()

    # Ingresar datos para agendar una cita.
    def ingresarDatosCita(paciente):
        # Se le pregunta si desea confirmar la cita.
        def confirmarCita():
            eleccion = cboxElegirCita.get()

            if eleccion:
                resultado = messagebox.askyesno("Confirmar cita", "¿Está seguro de que desea agendar esta cita?")
                if resultado:
                    for doctor in paciente.buscarDoctorEps(cboxTipoCita.get(), hospital):
                        if doctor.nombre == cboxElegirDoctor.get():
                            citaAgendada = doctor.actualizarAgenda(paciente, cboxElegirCita.current() + 1, doctor.mostrarAgendaDisponible())
                            paciente.actualizarHistorialCitas(citaAgendada)
                    messagebox.showinfo("Cita agendada!", "La cita se agendó exitosamente!")
                    mostrarHistorialCitas(paciente)
                else:
                    messagebox.showinfo("Cita cancelada!", "Usted ha decidido cancelar la cita")
                    # Importamos de nuevo la presentacion de inicio (para evitar referencia circular la importamos acá)
                    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                    implementacionDefault(frame)
            else:
                try:
                    raise CampoVacio()
                except CampoVacio as c:
                    c.enviarMensaje()

        def listarCitas():
            listaCitas = []
            try:
                for doctor in paciente.buscarDoctorEps(cboxTipoCita.get(), hospital):
                    if doctor.nombre == cboxElegirDoctor.get():
                        for cita in doctor.mostrarAgendaDisponible():
                            listaCitas.append(cita.fecha)
                return listaCitas

            except SinAgenda as s:
                s.enviarMensaje()
                cboxElegirCita['state'] = 'disabled'

        def habilitarEleccionCita(event):
            eleccion = cboxElegirDoctor.get()
            cboxElegirCita.set("")
            if eleccion:
                cboxElegirCita['state'] = 'readonly'
                cboxElegirCita['values'] = listarCitas()
            else:
                cboxElegirCita['state'] = 'disabled'

        # Busca los doctores de la especialidad seleccionada y del tipo de eps del paciente
        def listarDoctores():
            listaDoctores = []
            try:
                for doctor in paciente.buscarDoctorEps(cboxTipoCita.get(), hospital):
                    listaDoctores.append(doctor.nombre)
                return listaDoctores
            except SinDoctores as s:
                s.enviarMensaje()
                cboxElegirDoctor['state'] = 'disabled'

        def habilitarElegirDoctor(event):
            eleccion = cboxTipoCita.get()
            cboxElegirDoctor.set("")
            cboxElegirCita.set("")
            cboxElegirCita['state'] = 'disabled'
            if eleccion:
                cboxElegirDoctor['state'] = 'readonly'
                cboxElegirDoctor['values'] = listarDoctores()
            else:
                cboxElegirDoctor['state'] = 'disabled'

        mostarTitulo(frame)

        infoPaciente = Label(frame, text=f"{paciente.nombre} - CC: {paciente.cedula}", bg="white", font=("Arial", 12))
        infoPaciente.pack(pady=10)

        frame1 = Frame(frame, bg="white")
        frame1.pack()

        # Creamos los widgets que permitan llenar la información.

        # Para elegir el tipo de cita.
        tipoCita = Label(frame1, text="Seleccione el tipo de cita:", bg="white", font=("Arial", 10, "bold"))
        tipoCita.grid(row=0,column=0,padx=10,pady=10,sticky="w")

        valorPorDefecto1 = StringVar()

        cboxTipoCita = ttk.Combobox(frame1, values=["General", "Odontologia", "Oftalmologia"], textvariable=valorPorDefecto1, state="readonly")
        cboxTipoCita.bind("<<ComboboxSelected>>", habilitarElegirDoctor)
        cboxTipoCita.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Para elegir el doctor.
        elegirDoctor = Label(frame1, text="Seleccione el doctor de su preferencia:", bg="white", font=("Helvetica", 10, "bold"))
        elegirDoctor.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        valorPorDefecto2 = StringVar()

        cboxElegirDoctor = ttk.Combobox(frame1, textvariable=valorPorDefecto2, state="disabled")
        cboxElegirDoctor.bind("<<ComboboxSelected>>", habilitarEleccionCita)
        cboxElegirDoctor.grid(row=1,column=1,padx=10,pady=10,sticky="w")

        # Para elegir la cita en si.
        elegirCita = Label(frame1, text="Seleccione una fecha para su cita:", bg="white", font=("Helvetica", 10, "bold"))
        elegirCita.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        valorPorDefecto3 = StringVar()

        cboxElegirCita = ttk.Combobox(frame1, textvariable=valorPorDefecto3, state="disabled")
        cboxElegirCita.grid(row=2,column=1,padx=10,pady=10,sticky="w")

        # Botón para continuar y preguntar por la confirmación de la cita.
        botonContinuar = Button(frame, text="Continuar", command = confirmarCita)
        botonContinuar.pack(pady=5)

        # Botón para regresar a la presentación pincipal.
        # Se importa aca para evitar una referencia circular.
        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        botonRegresar = Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
        botonRegresar.pack(pady=5)
    
    # Se verifica que el paciente si exista en el sistema.
    def buscarPaciente():
        cedula = fieldPaciente.getValue(1)

        if len(cedula) != 0:
            try:
                paciente = hospital.buscarPaciente(int(cedula))

                # Si el paciente existe, llamamos a la función que permite agendar citas.
                ingresarDatosCita(paciente)
            except DatosFalsos as d:
                d.enviarMensaje()
            except ValueError:
                TipoIncorrecto.enviarMensaje()
        else:
            try:
                raise CampoVacio()
            except CampoVacio as c:
                c.enviarMensaje()

    mostarTitulo(frame)

    # Pide la cedula del paciente.
    ingresoCedula = Label(frame, text="Ingrese la cédula del paciente:", bg="white",font=("Helvetica", 10, "bold"))
    ingresoCedula.pack()

    criterios = ["Cédula"]

    fieldPaciente = FieldFrame(frame, "", criterios, "", None, None)
    fieldPaciente.pack()

    # Botón para buscar paciente
    botonBuscarPaciente = Button(frame, text="Buscar", command=buscarPaciente)
    botonBuscarPaciente.pack(pady=10)

    # Botón para regresar a la presentación pincipal.
    # Se importa aca para evitar una referencia circular.
    from iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

    botonRegresar = Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
    botonRegresar.pack(pady=5)