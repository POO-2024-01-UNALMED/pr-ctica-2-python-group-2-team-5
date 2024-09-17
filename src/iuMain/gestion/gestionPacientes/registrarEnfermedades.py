from tkinter import messagebox, ttk

import tkinter as tk

from gestorAplicacion.administracionHospital.Enfermedad import Enfermedad
from iuMain.gestion.FieldFrame import FieldFrame
from manejoDeErrores.ErroresAplicacion import DatosFalsos, TipoIncorrecto, CampoVacio, DatoDuplicado


def imprimirTitulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text="Registrar nueva enfermedad a un paciente", bg="white",
                      font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)


def registrarEnfermedad(hospital, frame):
    def nuevaEnfermedad(paciente):
        def borrarCampos():
            for entry in fp.valores:
                entry.delete(0, tk.END)

        def crearEnfermedad():
            nombre = fp.getValue(1)
            tipologia = fp.getValue(2)
            especialidad = fp.getValue(3)
            error = False
            if nombre != "" and tipologia != "" and especialidad != "":
                try:
                    if nombre.isdigit():
                        error = True
                        raise ValueError
                    else:
                        nombre = str(nombre)
                except ValueError:
                    TipoIncorrecto("en el campo nombre").enviarMensaje()
                try:
                    if tipologia.isdigit():
                        error = True
                        raise ValueError
                    else:
                        tipologia = str(tipologia)
                except ValueError:
                    TipoIncorrecto("en el campo tipologia").enviarMensaje()
                try:
                    if especialidad != "General" and especialidad != "Oftalmologia" and especialidad != "Odontologia":
                        error = True
                        raise ValueError
                    else:
                        especialidad = str(especialidad)
                except ValueError:
                    TipoIncorrecto("en el campo especialidad").enviarMensaje()
                try:
                    for enf in Enfermedad.getEnfermedadesRegistradas():
                        if nombre == enf.nombre and tipologia == enf.tipologia:
                            error = True
                            raise DatoDuplicado()
                except DatoDuplicado as e:
                    e.enviarMensaje()
            else:
                try:
                    raise CampoVacio()
                except CampoVacio as e:
                    e.enviar_mensaje()
                    error = True

            if error is not True:
                respuesta = tk.messagebox.askyesno("Confirmacion Enfermedad",
                                                   "¿Estas seguro de agregar esta enfermedad?")
                if respuesta:
                    enf = Enfermedad(nombre, tipologia, especialidad)
                    paciente.historiaClinica.enfermedades.append(enf)
                    messagebox.showinfo("Enfermedad agregada", "La enfermedad se ha agregado exitosamente")
                    # Se importa aca para evitar una referencia circula
                    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                    implementacionDefault(frame)

                else:
                    messagebox.showinfo("Enfermedad no agregada", "No se ha agregado la enfermedad")
                    # Se importa aca para evitar una referencia circula
                    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                    implementacionDefault(frame)

        imprimirTitulo(frame)
        criterios = ["Nombre", "Tipologia", "Especialidad que la trata(General, Oftalmologia u Odontologia)"]
        fp = FieldFrame(frame, "Criterio", criterios, "Valor", None, None)
        fp.pack()

        botonesFrame = tk.Frame(frame, bg="white")
        botonesFrame.pack()

        botonGuardar = tk.Button(botonesFrame, text="Guardar", command=crearEnfermedad)
        botonGuardar.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        botonBorrar = tk.Button(botonesFrame, text="Borrar", command=borrarCampos)
        botonBorrar.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    def agregarEnfermedad(paciente, combo):
            indice = combo.current()
            objetoSeleccionado = Enfermedad.getEnfermedadesRegistradas()[indice]
            error = False
            if objetoSeleccionado in paciente.historiaClinica.enfermedades:
                try:
                    error = True
                    raise DatoDuplicado()
                except DatoDuplicado as e:
                    e.enviarMensaje()
            if error is not True:
                respuesta = tk.messagebox.askyesno("Confirmar registro", "¿Estas seguro de agregar esta enfermedad?")
                if respuesta:

                    paciente.historiaClinica.agregarEnfermedades(objetoSeleccionado)
                    messagebox.showinfo("Enfermedad agregada", "La enfermedad se ha agregado exitosamente")
                    # Se importa aca para evitar una referencia circula
                    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                    implementacionDefault(frame)
                else:
                    messagebox.showinfo("Agregar enfermedad cancelada", "No se ha agregado la enfermedad")
                    # Se importa aca para evitar una referencia circula
                    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                    implementacionDefault(frame)

    def registrarEnfermedad(paciente):
        imprimirTitulo(frame)

        labelEnfermedad = tk.Label(frame, text="Enfermedades actuales", bg="white", font=("Helvetica", 12, "bold"))
        labelEnfermedad.pack(pady=10)
        frameEnfermedad = tk.Frame(frame, bg="white")
        frameEnfermedad.pack()
        for enf in paciente.historiaClinica.enfermedades:
            enf_label = tk.Label(frameEnfermedad, text=enf, font=("Helvetica", 10), bg="white")
            enf_label.pack()

        labelOpcion = tk.Label(frame, text="Elija que enfermedad registrar", font=("Helvetica", 12, "bold"),
                                bg="white")
        labelOpcion.pack()
        comboEnfermedades = ttk.Combobox(frame, values=Enfermedad.getEnfermedadesRegistradas(), state="readonly")
        comboEnfermedades.pack()
        botonAgregar = tk.Button(frame, text="Agregar", command=lambda: agregarEnfermedad(paciente, comboEnfermedades))
        botonAgregar.pack(pady=10)
        botonRegistrar = tk.Button(frame, text="Registrar enfermedad nueva", command=lambda: nuevaEnfermedad(paciente))
        botonRegistrar.pack()

    def buscarPaciente():
        cedula = fp.getValue(1)
        if len(cedula) != 0:
            try:
                paciente = hospital.buscarPaciente(int(cedula))
                registrarEnfermedad(paciente)
            except DatosFalsos as e:
                e.enviarMensaje()
            except ValueError:
                TipoIncorrecto().enviarMensaje()
        else:
            try:
                raise CampoVacio()
            except CampoVacio as e:
                e.enviarMensaje()

    imprimirTitulo(frame)

    # Pide la cedula del paciente
    labelIngresoCedula = tk.Label(frame, text="Ingrese la cédula del paciente:", bg="white",
                                    font=("Helvetica", 10, "bold"))
    labelIngresoCedula.pack()

    criterios = ["Cédula"]
    fp = FieldFrame(frame, "", criterios, "", None, None)
    fp.pack()

    botonBuscaPaciente = tk.Button(frame, text="Buscar", command=buscarPaciente)
    botonBuscaPaciente.pack()
