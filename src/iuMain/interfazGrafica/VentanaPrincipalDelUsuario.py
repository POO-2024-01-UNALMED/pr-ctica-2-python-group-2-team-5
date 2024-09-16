from tkinter import *
from tkinter import messagebox

# Ventana principal.
def abrirVentanaPrincipal(ventanaInicio):
    ventanaPrincipalDelUsuario = Toplevel()
    ventanaPrincipalDelUsuario.title("Ventana Principal del Usuario")
    ventanaPrincipalDelUsuario.geometry("600x500+400+90")

    ################## ZONA O ##################

    titulo = Label(ventanaPrincipalDelUsuario, text="HOSPITAL ANDINO", font=("Arial", 16))
    titulo.pack(padx=10, pady=10)

    ################## ZONA 1 ##################

    # Frame para los menus
    menuFrame = Frame(ventanaPrincipalDelUsuario, bd=2, relief="ridge")
    menuFrame.pack(padx=10, pady=10)

    class FieldFrame(Frame):
        def __init__(self, parent, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None):
            super().__init__(parent, bg="white")
            self.tituloCriterios = tituloCriterios
            self.criterios = criterios
            self.tituloValores = tituloValores
            self.valores = valores if valores is not None else ["" for _ in criterios]
            self.habilitado = habilitado if habilitado is not None else [True for _ in criterios]

            # Crear los títulos de las columnas
            Label(self, text=self.tituloCriterios, font=("Arial", 10), bg="white").grid(row=0, column=0, padx=10,
                                                                                        pady=5, sticky="w")
            Label(self, text=self.tituloValores, font=("Arial", 10), bg="white").grid(row=0, column=1, padx=10, pady=5,
                                                                                      sticky="e")

            # Crear etiquetas y campos de entrada para cada criterio
            self.entries = {}  # Diccionario para almacenar las entradas
            for i, criterio in enumerate(self.criterios):
                # Etiqueta del criterio
                label = Label(self, text=criterio, font=("Arial", 10), bg="white")
                label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")

                # Campo de entrada para el valor
                entry = Entry(self, width=30)
                entry.grid(row=i + 1, column=1, padx=10, pady=5)

                # Si tiene valor predeterminado, lo coloca
                if self.valores[i]:
                    entry.insert(0, self.valores[i])

                # Si el campo no está habilitado, lo desactiva
                if not self.habilitado[i]:
                    entry.config(state="disabled")

                # Guardar la referencia del campo de entrada
                self.entries[criterio] = entry

        def getValue(self, criterio):
            """Devuelve el valor ingresado en el campo del criterio dado."""
            return self.entries[criterio].get()

        def clearFields(self):
            """Limpia todos los campos de entrada."""
            for entry in self.entries.values():
                entry.delete(0, "end")

    # Eventos menu Archivo

    # Método para mostrar la info. básica de la aplicación al presionar el menú Archivo.
    # Configurar el mensaje para que sea más apropiado.
    def infoAplicacion():
        messagebox.showinfo("Información básica de la Aplicación","Con esta aplicación puedes gestionar tus tramites hospitalarios.")

    def salir():
        ventanaInicio.deiconify()
        ventanaPrincipalDelUsuario.destroy()

    # Método para mostrar los nombres de los autores de la aplicación.
    def acercaDe():
        messagebox.showinfo("Acerca de la aplicación.","Los autores de la aplicación son:\nJeronimo Zapata.\nJuan Pablo Vergara.\nHernando Montes.\nManuel Mera.\nSamuel Ramírez.")

    # Eventos menu Procesos y Consultas
    def actualizarFormulario():
        pass

    def asignarCita():
        pass

    def implementacionDefault(frame_implementacion):
        # Limpia el frame
        for widget in frame_implementacion.winfo_children():
            widget.destroy()

        # Ejecuta la implementacion por defecto
        texto_inicial = """
            Te encuentras en la ventana principal de la aplicación

            Tienes varias opciones:

            Archivo > Aplicacion: Muestra una descripcion de la aplicación
            Archivo > Salir: Regresa a la ventana inicial

            Procesos y consultas: Acá estan todos los servicios que permite gestionar la aplicación

            Ayuda > Acerca de: Muestra los creadores de la aplicación

            Seleccione una opcion para continuar
            """

        label_inicial = Label(frame_implementacion, text=texto_inicial, bg="white", font=("Helvetica", 14, "bold"))
        label_inicial.pack()
        label_inicial.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Frame adicional para la zona 1.

    framezona1 = Frame(menuFrame)
    framezona1.pack(fill="x")

    # menu Archivo
    menuArchivo = Menubutton(framezona1, text="Archivo")
    menuArchivo.pack(side="left", padx=(0, 2))

    archivoMenu = Menu(menuArchivo, tearoff=0)
    archivoMenu.add_command(label="Aplicación", command=infoAplicacion)

    archivoMenu.add_command(label="Salir", command = salir)
    menuArchivo.config(menu=archivoMenu)

    # menu Procesos y consultas
    menuProcesosConsultas = Menubutton(framezona1, text="Procesos y Consultas")
    menuProcesosConsultas.pack(side="left", padx=(0, 2))

    procesosMenu = Menu(menuProcesosConsultas, tearoff=0)
    procesosMenu.add_command(label="1. Agendar Citas", command=asignarCita)
    procesosMenu.add_command(label="2. Fórmula Médica")
    procesosMenu.add_command(label="3. Asignar Habitación")
    procesosMenu.add_command(label="4. Vacunación")
    procesosMenu.add_command(label="5. Facturación")
    menuProcesosConsultas.config(menu=procesosMenu)

    # menu Ayuda
    menuAyuda = Menubutton(framezona1, text="Ayuda")
    menuAyuda.pack(side="left", padx=(0, 2))

    ayudaMenu = Menu(menuAyuda, tearoff=0)
    ayudaMenu.add_command(label="Acerca de", command=acercaDe)
    menuAyuda.config(menu=ayudaMenu)

    ################## ZONA 2 ##################

    # Frame adicional pára la zona 2.

    frameZona2 = Frame(menuFrame)
    frameZona2.pack()

    tituloProceso = Label(frameZona2, text="Nombre del Proceso o Consulta", font=("Arial", 14), bg="white")
    tituloProceso.pack(padx=10, pady=10)

    descripcionProceso = Label(frameZona2, text="Descripción del detalle del proceso o la consulta", font=("Arial", 10),
                               bg="white")
    descripcionProceso.pack(padx=10, pady=10)

    formularioFrame = Frame(frameZona2, bg="white", bd=2, relief="ridge")
    formularioFrame.pack(padx=10, pady=10)

    fieldFrame = FieldFrame(formularioFrame, "Criterios", ["Nombre", "Fecha", "Doctor"], "Valores")
    fieldFrame.pack(padx=10, pady=10)

    # Frame adicional para los botones.

    frameBotones = Frame(frameZona2)
    frameBotones.pack(expand=True)

    # Botones para guardar los datos o limpiar los Entry.

    botonAceptar = Button(frameBotones, text="Aceptar")
    botonBorrar = Button(frameBotones, text="Borrar")
    botonAceptar.pack(padx=10, pady=10, side="left")
    botonBorrar.pack(padx=10, pady=10, side="left")

    ventanaPrincipalDelUsuario.mainloop()

