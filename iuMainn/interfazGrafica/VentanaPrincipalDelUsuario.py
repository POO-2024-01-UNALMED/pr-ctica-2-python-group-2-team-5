from tkinter import *



# Ventana Principal
ventanaPrincipalDelUsuario = Tk()
ventanaPrincipalDelUsuario.title("Ventana Principal del Usuario (Zona 0) ")
ventanaPrincipalDelUsuario.geometry("600x400")

titulo = Label(ventanaPrincipalDelUsuario, text="Hospital Andino", font=("Arial", 16))
titulo.grid(row=0, column=0, columnspan=4)

#Eventos menu 

def aplicacion():
    ventanaInfo = Toplevel(ventanaPrincipalDelUsuario)
    ventanaInfo.title("Información de la Aplicación")
    ventanaInfo.geometry("400x200")
    labelInfo = Label(ventanaInfo, text="Esta aplicación es un sistema de gestión para el Hospital Andino.")
    labelInfo.pack()
    
"""
def salir():
    ventanaPrincipalDelUsuario.destroy()
    ventanaInicio.deicoinfy()
"""

#Frame para los menus 
menuFrame = Frame(ventanaPrincipalDelUsuario, bg="white", bd=2, relief="ridge")
menuFrame.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

ventanaPrincipalDelUsuario.rowconfigure(1, weight=1) 
ventanaPrincipalDelUsuario.columnconfigure(0, weight=1)

#menu Archivo
menuArchivo = Menubutton(menuFrame, text="Archivo")
menuArchivo.grid(row=0, column=0)

archivoMenu = Menu(menuArchivo, tearoff=0)
archivoMenu.add_command(label="Aplicación", command=aplicacion)
archivoMenu.add_command(label="Salir")
menuArchivo.config(menu=archivoMenu)

#menu Procesos y consultas 
menuProcesosConsultas = Menubutton(menuFrame, text="Procesos y Consultas")
menuProcesosConsultas.grid(row=0, column=1)

procesosMenu = Menu(menuProcesosConsultas, tearoff=0)
procesosMenu.add_command(label="1. Agendar Citas")
procesosMenu.add_command(label="2. Fórmula Médica")
procesosMenu.add_command(label="3. Asignar Habitación")
procesosMenu.add_command(label="4. Vacunación")
procesosMenu.add_command(label="5. Facturación")
menuProcesosConsultas.config(menu=procesosMenu)

#menu Ayuda
menuAyuda = Menubutton(menuFrame, text="Ayuda")
menuAyuda.grid(row=0, column=2)

ayudaMenu = Menu(menuAyuda, tearoff=0)
ayudaMenu.add_command(label="Acerca de")
menuAyuda.config(menu=ayudaMenu)





ventanaPrincipalDelUsuario.mainloop()