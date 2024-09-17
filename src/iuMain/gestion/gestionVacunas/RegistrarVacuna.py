import tkinter as tk
from tkinter import messagebox

from gestorAplicacion.administracionHospital.Vacuna import Vacuna
from iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
from manejoDeErrores.ErroresAplicacion import DatoDuplicado, TipoIncorrecto, CampoVacio


def registrarVacuna(hospital, frame_implementacion):

    def verVacunaRegistrada(tipo,nombre,precio):
        #Se limpia el frame
        for item in frame_implementacion.winfo_children():
            item.destroy()

        titulo = tk.Label(frame_implementacion, text="Registrar una vacuna", bg="white", font=("Helvetica", 16, "bold"))
        titulo.pack(pady=20)

        infoVacuna = tk.Label(frame_implementacion, text=f"Informacion de la vacuna registrada", bg="white", font=("Helvetica", 12))
        infoVacuna.pack(pady=10)

        frameVacuna = tk.Frame(frame_implementacion, bg="white")
        frameVacuna.pack(padx=10, pady=10)

        labelNombre = tk.Label(frameVacuna, text="Nombre: ", bg="white", font=("Helvetica", 10, "bold"))
        labelNombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        labelCedulaDoctor = tk.Label(frameVacuna, text=nombre, bg="white")
        labelCedulaDoctor.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        labelTipo = tk.Label(frameVacuna, text="Tipo: ", bg="white", font=("Helvetica", 10, "bold"))
        labelTipo.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        labelTipo = tk.Label(frameVacuna, text=tipo, bg="white")
        labelTipo.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        labelPrecio = tk.Label(frameVacuna, text="Precio: ", bg="white", font=("Helvetica", 10, "bold"))
        labelPrecio.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        labelPrecio = tk.Label(frameVacuna, text=precio, bg="white")
        labelPrecio.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        #Boton regresar

        botonRegresar = tk.Button(frame_implementacion, text="Regresar", command=lambda: implementacion_default(frame_implementacion))
        botonRegresar.pack(pady=5)


    def crearVacuna():

        nombre = fp.getValue(1)
        tipo = fp.getValue(2)
        tipoEps = str(fp.getValue(3)).split(",")
        precio = fp.getValue(4)

        # Variable de control para verificar si hay errores
        errores = False

        if len(nombre) != 0:
            try:
                if nombre.isdigit():
                    errores=True
                    raise ValueError
                else:
                    nombre=str(fp.getValue(1))
                    if hospital.buscarVacuna(nombre) is not None:
                        errores = True
                        try:
                            raise DatoDuplicado()
                        except DatoDuplicado as e:
                            e.enviarMensaje()
            except ValueError:
                errores = True
                TipoIncorrecto("en el campo nombre").enviarMensaje()

        if len(tipo) != 0:
            try:
                if tipo != "Obligatoria" and tipo != "No obligatoria":
                    errores = True
                    raise ValueError
                else:
                    tipo = str(fp.getValue(2))
            except ValueError:
                errores = True
                TipoIncorrecto("en el campo tipo").enviarMensaje()

        if tipoEps !=[""]:
            try:
                for eps in tipoEps:
                    if eps != "Subsidiado" and eps !="Contributivo" and eps !="Particular":
                        errores = True
                        raise ValueError
            except ValueError:
                errores = True
                TipoIncorrecto("en el campo eps").enviarMensaje()

        if len(precio) != 0:
            try:
                precio=float(fp.getValue(4))
            except ValueError:
                errores = True
                TipoIncorrecto("en el campo precio").enviarMensaje()

        if not nombre or not tipo or not precio or tipoEps==[""]:
            errores = True
            try:
                raise CampoVacio()
            except CampoVacio as e:
                e.enviarMensaje()

        if not errores:
            respuesta = tk.messagebox.askyesno("Confirmacion de la vacuna", "¿Estás seguro de agregar esta vacuna?")
            if respuesta:
                vacuna = Vacuna(tipo, nombre, tipoEps, precio)
                hospital.listaVacunas.append(vacuna)
                messagebox.showinfo("Vacuna agregada", "La vacuna se ha agregado exitosamente")
                verVacunaRegistrada(tipo, nombre, precio)
            else:
                messagebox.showinfo("Vacuna no agregada", "No se ha agregado la vacuna")
                # Se importa acá para evitar una referencia circular
                implementacionDefault(frame_implementacion)

    def borrarCampos():
        for entry in fp.valores:
            entry.delete(0,tk.END)


    # Titulo
    titulo = tk.Label(frame_implementacion, text="Registrar una vacuna", bg="white",font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

    #Formulario

    tituloIngresoCedula = tk.Label(frame_implementacion, text="Por favor llene cada uno de los campos:", bg="white", font=("Helvetica", 10, "bold"))
    tituloIngresoCedula.pack(pady=35)

    criterios= ["Nombre de la vacuna", "Ingrese el tipo de vacuna (Obligatoria, No obligatoria)",
                "Ingrese las eps a la que va a pertenecer (Subsidiado, Contributivo, Particular)",
                "Precio"]
    fp =FieldFrame(frame_implementacion,"Criterio", criterios, "Valor", None, None)
    fp.pack()

    #Botones
    botonesFrame=tk.Frame(frame_implementacion,bg="white")
    botonesFrame.pack(pady=10)


    #Guardar
    botonGuardarVacuna = tk.Button(botonesFrame, text="Guardar", command=crearVacuna, font=("Helvetica", 10, "bold"))
    botonGuardarVacuna.grid(row=0, column=0, padx=30, pady=10, sticky="w")

    #Borrar
    botonBorrar = tk.Button(botonesFrame, text="Borrar", command=borrarCampos, font=("Helvetica", 10, "bold"))
    botonBorrar.grid(row=0, column=1, padx=10, pady=30, sticky="w")


    # Funcionalidad para regresar a la ventana principal

    # Se importa aca para evitar una referencia circular

    botonRegresar = tk.Button(frame_implementacion, text="Regresar", command=lambda: implementacionDefault(frame_implementacion))
    botonRegresar.pack(pady=20)

