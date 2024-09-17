from tkinter import messagebox

import tkinter as tk

from iuMain.gestion.FieldFrame import FieldFrame
from src.gestorAplicacion.personas.Doctor import Doctor
from src.manejoDeErrores.ErroresAplicacion import DatoDuplicado, TipoIncorrecto, CampoVacio


def imprimirTitulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text="Agregar doctor", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def agregarDoctor(hospital, frame):

    def verDoctor(cedula, nombre, tipo_eps, especialidad):
        imprimirTitulo(frame)

        info_doctor = tk.Label(frame, text=f"Informacion del doctor registrado", bg="white", font=("Helvetica", 12))
        info_doctor.pack(pady=10)

        frame_doctor = tk.Frame(frame, bg="white")
        frame_doctor.pack(padx=10, pady=10)

        label_cedula = tk.Label(frame_doctor, text="Cedula: ", bg="white", font=("Helvetica", 10, "bold"))
        label_cedula.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        label_cedula_doctor = tk.Label(frame_doctor, text=cedula, bg="white")
        label_cedula_doctor.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        label_doctor = tk.Label(frame_doctor, text="Doctor: ", bg="white", font=("Helvetica", 10, "bold"))
        label_doctor.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        label_nombre_doctor = tk.Label(frame_doctor, text=nombre, bg="white")
        label_nombre_doctor.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        label_tipo_eps = tk.Label(frame_doctor, text="Tipo de eps: ", bg="white", font=("Helvetica", 10, "bold"))
        label_tipo_eps.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        label_tipo_eps_doctor = tk.Label(frame_doctor, text=tipo_eps, bg="white")
        label_tipo_eps_doctor.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        label_especialidad = tk.Label(frame_doctor, text="Especialidad: ", bg="white", font=("Helvetica", 10, "bold"))
        label_especialidad.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        label_especialidad_doctor = tk.Label(frame_doctor, text=especialidad, bg="white")
        label_especialidad_doctor.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Se importa aca para evitar una referencia circula
        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        boton_regresar = tk.Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
        boton_regresar.pack()

    def agregarListaDoctores():
        cedula = fp.getValue(1)
        nombre = fp.getValue(2)
        tipoEps = fp.getValue(3)
        especialidad = fp.getValue(4)

        # Variable de control para verificar si hay errores
        Errores = False

        if len(cedula) != 0:
            try:
                cedula = int(fp.getValue(1))
                if hospital.buscarDoctor(cedula) is not None:
                    Errores = True
                    try:
                        raise DatoDuplicado()
                    except DatoDuplicado as e:
                        e.enviarMensaje()
            except ValueError:
                Errores = True
                TipoIncorrecto("en el campo cedula").enviarMensaje()

        if len(nombre) != 0:
            try:
                if nombre.isdigit():
                    Errores = True
                    raise ValueError
                else:
                    nombre = str(fp.getValue(2))
            except ValueError:
                Errores = True
                TipoIncorrecto("en el campo nombre").enviarMensaje()

        if len(tipoEps) != 0:
            try:
                if tipoEps != "Subsidiado" and tipoEps != "Contributivo" and tipoEps != "Particular":
                    Errores = True
                    raise ValueError
                else:
                    tipoEps = str(fp.getValue(3))
            except ValueError:
                Errores = True
                TipoIncorrecto("en el campo tipo de eps").enviarMensaje()

        if len(especialidad) != 0:
            try:
                if especialidad != "General" and especialidad != "Odontologia" and especialidad != "Oftalmologia":
                    Errores = True
                    raise ValueError
                else:
                    especialidad = str(fp.getValue(4))
            except ValueError:
                Errores = True
                TipoIncorrecto("en el campo especialidad").enviarMensaje()

        if not cedula or not nombre or not tipoEps or not especialidad:
            Errores = True
            try:
                raise CampoVacio()
            except CampoVacio as e:
                e.enviarMensaje()

        if not Errores:
            respuesta = tk.messagebox.askyesno("Confirmacion del doctor", "¿Estás seguro de agregar este doctor?")
            if respuesta:
                doctor = Doctor(cedula, nombre, tipoEps, especialidad)
                hospital.lista_doctores.append(doctor)
                messagebox.showinfo("Doctor agregado", "El doctor se ha agregado exitosamente")
                verDoctor(cedula, nombre, tipoEps, especialidad)
            else:
                messagebox.showinfo("Doctor no agregado", "No se ha agregado el doctor")
                # Se importa acá para evitar una referencia circular
                implementacionDefault(frame)


    def borrar_campos():
        for entry in fp.valores:
            entry.delete(0,tk.END)


    imprimirTitulo(frame)

    criterios = ["Cédula", "Nombre", "Tipo de eps (Subsidado, Contributivo o Particular)", "Especialidad (General, Oftalmologia u Odontologia)"]
    fp = FieldFrame(frame, "Criterio", criterios, "Valor", None, None)
    fp.pack()

    botones_frame = tk.Frame(frame, bg="white")
    botones_frame.pack()

    botonGuardar = tk.Button(botones_frame, text="Guardar", command=agregarListaDoctores)
    botonGuardar.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    boton_borrar = tk.Button(botones_frame, text="Borrar", command=borrar_campos)
    boton_borrar.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # Funcionalidad para regresar a la ventana principal

    # Se importa aca para evitar una referencia circular
    # Se importa aca para evitar una referencia circula
    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

    boton_regresar = tk.Button(frame, text="Regresar",command=lambda: implementacionDefault(frame))
    boton_regresar.pack()