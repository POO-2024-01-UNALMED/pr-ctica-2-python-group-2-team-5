from tkinter import *
from tkinter import messagebox

import sys
sys.path.append("src")

from iuMain.funcionalidades import AgendarCita,AsignarHabitacion,Vacunacion,Facturacion,FormulaMedica
from iuMain.gestion.gestionHospital import verPacientes,verMedicamentos,verDoctores,verVacunas,agregarMedicamentos,construirHabitacion,destruirHabitacion

def cambiarContenido(opcion, Hospital, frame_implementacion):

    #limpiar frame
    for widget in frame_implementacion.winfo_children():
        widget.destroy()

    # Cambios con funcionalidades
    opciones={
        "agendarCita": AgendarCita.agendarCitas,
        "asignarHabitacion": AsignarHabitacion.asignarHabitacion,
        "vacunacion": Vacunacion.Vacunacion,
        "pago": Facturacion.Facturacion,
       # "formulaMedica": FormulaMedica.FormulaMedica,

        #Gestion Hospital
        "verPacientes": verPacientes.verPacientes,
        "verDoctores": verDoctores.verDoctores,
        "verMedicamentos": verMedicamentos.verMedicamentos,
        "verVacunas": verVacunas.verVacunas,
        "agregarMedicamentos": agregarMedicamentos.agregarMedicamento,
        "construirHabitacion": construirHabitacion.construirHabitacion,
        "destruirHabitacion": destruirHabitacion.destruirHabitacion,

        
        


    }

    if opcion in opciones:
        opciones[opcion](Hospital, frame_implementacion)

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

# Presentacion antes de la ventana principal.

def implementacionDefault(frame_implementacion):
    # Limpia el frame
    for widget in frame_implementacion.winfo_children():
        widget.destroy()

    # Ejecuta la implementacion por defecto
    textoInicial = """
        Te encuentras en la ventana principal de la aplicación

        Tienes varias opciones:

        Archivo > Aplicacion: Muestra una descripcion de la aplicación
        Archivo > Salir: Regresa a la ventana inicial

        Procesos y consultas: Acá estan todos los servicios que permite gestionar la aplicación

        Ayuda > Acerca de: Muestra los creadores de la aplicación

        Seleccione una opcion para continuar
        """

    labelInicial = Label(frame_implementacion, text=textoInicial, bg="white", font=("Helvetica", 14, "bold"))
    labelInicial.pack()
    labelInicial.place(relx=0.5, rely=0.5, anchor="center")

# Ventana principal.
def abrirVentanaPrincipal(hospital):

    def infoAplicacion():
        messagebox.showinfo("Información básica de la Aplicación","Con esta aplicación puedes gestionar tus tramites hospitalarios.")



    # Método para mostrar los nombres de los autores de la aplicación.
    def acercaDe():
        messagebox.showinfo("Acerca de la aplicación.","Los autores de la aplicación son:\nJeronimo Zapata.\nJuan Pablo Vergara.\nHernando Montes.\nManuel Mera.\nSamuel Ramírez.")


    # Eventos menu Procesos y Consultas
    def actualizarFormulario():
        pass

    def asignarCita():
        pass


    ventanaPrincipalDelUsuario = Toplevel()
    ventanaPrincipalDelUsuario.title("Ventana Principal del Usuario")
    ventanaPrincipalDelUsuario.geometry("600x500+400+90")
#    ventanaPrincipalDelUsuario.protocol("WM_DELETE_WINDOW", hospital.serializar())

    ################## ZONA O ##################

    titulo = Label(ventanaPrincipalDelUsuario, text="HOSPITAL ANDINO", font=("Verdana", 16))
    titulo.pack(padx=10, pady=10)

    ################## ZONA 1 ##################

    # Frame para los menus
    menuFrame = Frame(ventanaPrincipalDelUsuario, bd=2, relief="ridge")
    menuFrame.pack(padx=10, pady=10)
    class FieldFrame(Frame):

        def __init__(self, frame,tituloCriterios, criterios, tituloValores, valores, habilitado,ancho_entry=20):
            super().__init__(frame,bg="white")

            self.valores=[]

            #Etiquetas para los títulos de las columnas
            Label(self, text=tituloCriterios,bg="white",font=("Helvetica", 12, "bold")).grid(row=0, column=0)
            Label(self, text=tituloValores,bg="white",font=("Helvetica", 12, "bold")).grid(row=0, column=1)

            # Etiquetas y campos de entrada para cada criterio
            for i, criterio in enumerate(criterios, start=1):
                Label(self, text=criterio,bg="white", font=("Helvetica", 10, "bold")).grid(row=i, column=0, padx=20, pady=5, sticky="w")
                entry = Entry(self,width=ancho_entry)
                entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
                # Se inserta los valores por defecto que queramos
                if valores is not None:
                    #el número 0 indica que se inserta desde el inicio del string
                    entry.insert(0, valores[i - 1])
                #Para deshabilitar el entry
                if habilitado is not None and not habilitado[i - 1]:
                    entry.config(state='readonly')

                #Se guarda la referencia de ese entry
                self.valores.append(entry)

        def habilitarEntry(self, indice, habilitar):
            if habilitar:
                return self.valores[indice - 1].config(state="normal")
            else:
                return self.valores[indice - 1].config(state="readonly")

        def getValue(self, criterio):
            return self.valores[criterio-1].get()



    # Eventos menu Archivo

    # Método para mostrar la info. básica de la aplicación al presionar el menú Archivo.
    # Configurar el mensaje para que sea más apropiado.



    # Frame adicional para la zona 1.

    framezona1 = Frame(menuFrame)
    framezona1.pack(fill="x")

    # menu Archivo
    menuArchivo = Menubutton(framezona1, text="Archivo")
    menuArchivo.pack(side="left", padx=(0, 2))

    archivoMenu = Menu(menuArchivo, tearoff=0)
    archivoMenu.add_command(label="Aplicación", command=infoAplicacion)

    from ventanaInicio import abrirVentanaInicio

    archivoMenu.add_command(label="Salir", command = lambda: [ventanaPrincipalDelUsuario.destroy(), abrirVentanaInicio(hospital="rr")])
    menuArchivo.config(menu=archivoMenu)

    # menu Procesos y consultas
    menuProcesosConsultas = Menubutton(framezona1, text="Procesos y Consultas")
    menuProcesosConsultas.pack(side="left", padx=(0, 2))

    procesosMenu = Menu(menuProcesosConsultas, tearoff=0)
    procesosMenu.add_command(label="1. Agendar Citas", command=lambda: cambiarContenido("agendarCita", hospital, frame_implementacion))
    procesosMenu.add_command(label="2. Fórmula Médica", command=lambda: cambiarContenido("formualMedica", hospital, frame_implementacion) )
    procesosMenu.add_command(label="3. Asignar Habitación", command=lambda: cambiarContenido("asignarHabitacion", hospital, frame_implementacion))
    procesosMenu.add_command(label="4. Vacunación", command=lambda: cambiarContenido("vacunacion", hospital, frame_implementacion))
    procesosMenu.add_command(label="5. Facturación", command=lambda: cambiarContenido("pago", hospital, frame_implementacion))

    procesosMenu.add_separator()



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

    frame_implementacion = Frame(ventanaPrincipalDelUsuario)
    frame_implementacion.pack(fill="both", expand=True)
    frame_implementacion.configure(bg="white")

    implementacionDefault(
        frame_implementacion
    )

    ventanaPrincipalDelUsuario.mainloop()

