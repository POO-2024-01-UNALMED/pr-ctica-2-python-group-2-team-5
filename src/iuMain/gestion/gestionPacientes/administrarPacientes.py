from tkinter import messagebox

import tkinter as tk

from iuMain.gestion.FieldFrame import FieldFrame
from manejoDeErrores.ErroresAplicacion import TipoIncorrecto, CampoVacio, DatosFalsos


def imprimirTitulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text="Administrar paciente", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)



def administrarPaciente(hospital, frame):

    def borrar(paciente):
        respuesta = tk.messagebox.askyesno("Confirmar eliminacion", "¿Estas seguro de eliminar este paciente?")
        if respuesta:
            hospital.listaPacientes.remove(paciente)
            messagebox.showinfo("Paciente eliminado", "El paciente se ha eliminado exitosamente")
            # Se importa aca para evitar una referencia circular
            from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

            implementacionDefault(frame)
        else:
            messagebox.showinfo("Eliminacion cancelada", "El paciente no ha sido eliminado")
            # Se importa aca para evitar una referencia circula
            from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
            implementacionDefault(frame)

    def verPaciente(paciente):

        imprimirTitulo(frame)

        infoPaciente = tk.Label(frame, text=f"Informacion del paciente registrado", bg="white", font=("Helvetica", 12))
        infoPaciente.pack(pady=10)

        framePaciente = tk.Frame(frame, bg="white")
        framePaciente.pack(padx=10, pady=10)

        labelCedula = tk.Label(framePaciente, text="Cedula: ", bg="white", font=("Helvetica", 10, "bold"))
        labelCedula.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        labelCedulaDoctor = tk.Label(framePaciente, text=paciente.cedula, bg="white")
        labelCedulaDoctor.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        labelPaciente = tk.Label(framePaciente, text="Paciente: ", bg="white", font=("Helvetica", 10, "bold"))
        labelPaciente.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        labelNombreDoctor = tk.Label(framePaciente, text=paciente.nombre, bg="white")
        labelNombreDoctor.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        labelTipoEps = tk.Label(framePaciente, text="Tipo de eps: ", bg="white", font=("Helvetica", 10, "bold"))
        labelTipoEps.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        labelTipoEpsPaciente = tk.Label(framePaciente, text=paciente.tipoEps, bg="white")
        labelTipoEpsPaciente.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Se importa aca para evitar una referencia circula
        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        botonRegresar = tk.Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
        botonRegresar.pack()

    def actualizarPaciente(fp, paciente):
        nombre = fp.getValue(2)
        error = False
        if nombre != "":
            try:
                if nombre.isdigit():
                    error = True
                    raise ValueError
                else:
                    nombre = str(nombre)
            except ValueError:
                TipoIncorrecto().enviar_mensaje()
        else:
            try:
                error = True
                raise CampoVacio()
            except CampoVacio as e:
                e.enviar_mensaje()
        if error is not True:
            respuesta = tk.messagebox.askyesno("Confirmacion de cambio", "¿Estas seguro deseas cambiar el nombre?")
            if respuesta:
                paciente.nombre = nombre
                messagebox.showinfo("Cambio hecho", "El nombre se ha cambiado exitosamente")
                verPaciente(paciente)
            else:
                messagebox.showinfo("Cambio cancelado", "El nombre no se ha cambiado")
                # Se importa aca para evitar una referencia circula
                from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                implementacionDefault(frame)



    def habilitarEntrys(fp, paciente, boton, boton2):
        boton2.destroy()
        boton.destroy()
        fp.habilitarEntry(2, True)
        guardar_cambios = tk.Button(frame, text="Guardar", command=lambda: actualizarPaciente(fp, paciente))
        guardar_cambios.pack()





    def administracionPaciente(paciente):
        imprimirTitulo(frame)
        infoDoctor = tk.Label(frame, text=f"Informacion del paciente", bg="white", font=("Helvetica", 12))
        infoDoctor.pack(pady=10)

        criterios = ["Cedula", "Nombre", "Tipo de eps"]

        fp = FieldFrame(frame, "Criterio", criterios, "Valor", [paciente.cedula, paciente.nombre, paciente.tipoEps],[False, False, False, False])
        fp.pack()

        botonEditar = tk.Button(frame, text="Editar", command=lambda: habilitarEntrys(fp, paciente, botonEditar, botonBorrar))
        botonEditar.pack(pady=10)
        botonBorrar = tk.Button(frame, text="Borrar", command=lambda: borrar(paciente))
        botonBorrar.pack(pady=10)


    def buscarPaciente():
        cedula = fp.getValue(1)
        if len(cedula) != 0:
            try:
                paciente = hospital.buscarPaciente(int(cedula))
                administracionPaciente(paciente)
            except DatosFalsos as e:
                e.enviar_mensaje()
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

    botonBuscarPaciente = tk.Button(frame, text="Buscar", command=buscarPaciente)
    botonBuscarPaciente.pack()
