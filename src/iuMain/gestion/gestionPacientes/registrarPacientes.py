from tkinter import messagebox

import tkinter as tk

from gestorAplicacion.personas.Paciente import Paciente
from manejoDeErrores.ErroresAplicacion import DatoDuplicado, TipoIncorrecto, CampoVacio


def imprimirTitulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text="Agregar paciente", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)


def registrarPaciente(hospital, frame):
    def verPaciente(cedula, nombre, tipo_eps):
        imprimirTitulo(frame)

        infoPaciente = tk.Label(frame, text=f"Informacion del paciente registrado", bg="white", font=("Helvetica", 12))
        infoPaciente.pack(pady=10)

        framePaciente = tk.Frame(frame, bg="white")
        framePaciente.pack(padx=10, pady=10)

        labelCedula = tk.Label(framePaciente, text="Cedula: ", bg="white", font=("Helvetica", 10, "bold"))
        labelCedula.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        labelCedulaDoctor = tk.Label(framePaciente, text=cedula, bg="white")
        labelCedulaDoctor.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        labelPaciente = tk.Label(framePaciente, text="Paciente: ", bg="white", font=("Helvetica", 10, "bold"))
        labelPaciente.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        labelNombreDoctor = tk.Label(framePaciente, text=nombre, bg="white")
        labelNombreDoctor.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        labelTipoEps = tk.Label(framePaciente, text="Tipo de eps: ", bg="white", font=("Helvetica", 10, "bold"))
        labelTipoEps.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        labelTipoEpsPaciente = tk.Label(framePaciente, text=tipo_eps, bg="white")
        labelTipoEpsPaciente.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Se importa aca para evitar una referencia circula
        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        botonRegresar = tk.Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
        botonRegresar.pack()

    def agregarListaPacientes():
        cedula = fp.getValue(1)
        nombre = fp.getValue(2)
        tipoEps = fp.getValue(3)
        error = False
        if cedula != "" and nombre != "" and tipoEps != "":
            try:
                cedula = int(cedula)
                for pac in hospital.listaPacientes:
                    if cedula == pac.cedula:
                        error = True
                        raise DatoDuplicado()
            except DatoDuplicado as e:
                e.enviarMensaje()
            except ValueError:
                TipoIncorrecto("en el campo cedula").enviarMensaje()
            try:
                if nombre.isdigit():
                    error = True
                    raise ValueError
                else:
                    nombre = str(nombre)
            except ValueError:
                TipoIncorrecto("en el campo nombre").enviarMensaje()
            try:
                if tipoEps != "Subsidiado" and tipoEps != "Contributivo" and tipoEps != "Particular":
                    error = True
                    raise ValueError
                else:
                    nombre = str(nombre)
            except ValueError:
                TipoIncorrecto("en el campo tipo eps").enviarMensaje()
        else:
            try:
                error = True
                raise CampoVacio()
            except CampoVacio as e:
                e.enviarMensaje()

        if error is not True:
            respuesta = tk.messagebox.askyesno("Confirmacion del paciente", "¿Estas seguro de registrar este paciente?")

            if respuesta:

                paciente = Paciente(cedula, nombre, tipoEps)
                hospital.listaPacientes.append(paciente)
                messagebox.showinfo("Paciente registrado", "El paciente se ha registrado exitosamente")
                verPaciente(cedula, nombre, tipoEps)
            else:
                messagebox.showinfo("Paciente no registrado", "No se ha registrado el paciente")
                # Se importa aca para evitar una referencia circula
                from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                implementacionDefault(frame)

    def borrarCampos():
        for entry in fp.valores:
            entry.delete(0, tk.END)

    imprimirTitulo(frame)

    criterios = ["Cédula", "Nombre", "Tipo de eps (Subsidado, Contributivo o Particular)"]
    fp = FieldFrame(frame, "Criterio", criterios, "Valor", None, None)
    fp.pack()

    botonesFrame = tk.Frame(frame, bg="white")
    botonesFrame.pack()

    botonGuardar = tk.Button(botonesFrame, text="Guardar", command=agregarListaPacientes)
    botonGuardar.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    botonBorrar = tk.Button(botonesFrame, text="Borrar", command=borrarCampos)
    botonBorrar.grid(row=0, column=1, padx=10, pady=10, sticky="w")
