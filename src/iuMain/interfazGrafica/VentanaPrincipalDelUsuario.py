from tkinter import *
from tkinter import ttk

################# HAY QUE IMPORTAR VENTANAINICIO ########################
#from ventanaInicio import ventanaInicio

# Ventana Principal
ventanaPrincipalDelUsuario = Tk()
ventanaPrincipalDelUsuario.title("Ventana Principal del Usuario")
ventanaPrincipalDelUsuario.geometry("600x500")

################## ZONA O ##################

titulo = Label(ventanaPrincipalDelUsuario, text="Hospital Andino", font=("Arial", 16))
titulo.grid(row=0, column=0, columnspan=1, pady=10)

################## ZONA 1 ##################

#Frame para los menus 
menuFrame = Frame(ventanaPrincipalDelUsuario, bg="white", bd=2, relief="ridge")
menuFrame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)



from tkinter import *

class FieldFrame(Frame):
    def __init__(self, parent, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None):
        super().__init__(parent, bg="white")
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.tituloValores = tituloValores
        self.valores = valores if valores is not None else ["" for _ in criterios]
        self.habilitado = habilitado if habilitado is not None else [True for _ in criterios]

        # Crear los títulos de las columnas
        Label(self, text=self.tituloCriterios, font=("Arial", 10), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        Label(self, text=self.tituloValores, font=("Arial", 10), bg="white").grid(row=0, column=1, padx=10, pady=5, sticky="e")

        # Crear etiquetas y campos de entrada para cada criterio
        self.entries = {}  # Diccionario para almacenar las entradas
        for i, criterio in enumerate(self.criterios):
            # Etiqueta del criterio
            label = Label(self, text=criterio, font=("Arial", 10), bg="white")
            label.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

            # Campo de entrada para el valor
            entry = Entry(self, width=30)
            entry.grid(row=i+1, column=1, padx=10, pady=5)
            
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
            entry.delete(0, END)


#Eventos menu Archivo

def aplicacion():
    ventanaInfo = Toplevel(ventanaPrincipalDelUsuario)
    ventanaInfo.title("Información de la Aplicación")
    ventanaInfo.geometry("400x200")
    labelInfo = Label(ventanaInfo, text="Esta aplicación es un sistema de gestión para el Hospital Andino.")
    labelInfo.pack()

"""
########## ESTO NO DA (que vuelva a ventanaInicial) ########### 
def salir():
    ventanaPrincipalDelUsuario.withdraw()
    ventanaInicio.deiconify()

"""

def acercaDe():
    ventanaAcercaDe = Toplevel(ventanaPrincipalDelUsuario)
    ventanaAcercaDe.title("Acerca de")
    ventanaAcercaDe.geometry("300x200")
    labelAcercaDe = Label(ventanaAcercaDe, text="Autores:\nJerónimo\n...")
    labelAcercaDe.pack()

#Eventos menu Procesos y Consultas
def actualizarFormulario():
    pass

def asignarCita():
    pass





#menu Archivo
menuArchivo = Menubutton(menuFrame, text="Archivo")
menuArchivo.grid(row=0, column=0, sticky="w", padx=5)

archivoMenu = Menu(menuArchivo, tearoff=0)
archivoMenu.add_command(label="Aplicación", command=aplicacion)
archivoMenu.add_command(label="Salir" """,command=salir""")
menuArchivo.config(menu=archivoMenu)

#menu Procesos y consultas 
menuProcesosConsultas = Menubutton(menuFrame, text="Procesos y Consultas")
menuProcesosConsultas.grid(row=0, column=1,)

procesosMenu = Menu(menuProcesosConsultas, tearoff=0)
procesosMenu.add_command(label="1. Agendar Citas", command=asignarCita)
procesosMenu.add_command(label="2. Fórmula Médica")
procesosMenu.add_command(label="3. Asignar Habitación")
procesosMenu.add_command(label="4. Vacunación")
procesosMenu.add_command(label="5. Facturación")
menuProcesosConsultas.config(menu=procesosMenu)

#menu Ayuda
menuAyuda = Menubutton(menuFrame, text="Ayuda")
menuAyuda.grid(row=0, column=2, )

ayudaMenu = Menu(menuAyuda, tearoff=0)
ayudaMenu.add_command(label="Acerca de", command= acercaDe)
menuAyuda.config(menu=ayudaMenu)


################## ZONA 2 ##################

tituloProceso = Label(menuFrame, text="Nombre del Proceso o Consulta", font=("Arial", 14), bg="white")
tituloProceso.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

descripcionProceso= Label(menuFrame, text="Descripción del detalle del proceso o la consulta", font=("Arial", 10), bg="white")
descripcionProceso.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

formularioFrame= Frame(menuFrame, bg="white", bd=2, relief="ridge")
formularioFrame.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="ew")


fieldFrame = FieldFrame(formularioFrame, "Criterios", ["Nombre", "Fecha", "Doctor"], "Valores")
fieldFrame.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

botonAceptar = Button(formularioFrame, text="Aceptar")
botonBorrar = Button(formularioFrame, text="Borrar")
botonAceptar.grid(row=5, column=0, padx=50, pady=10, sticky="w")
botonBorrar.grid(row=5, column=1, padx=50, pady=10, sticky="e")


ventanaPrincipalDelUsuario.mainloop()