from tkinter import *

from iuMain.interfazGrafica.ventanaInicio import ventanaInicio

# Ventana Principal
ventanaPrincipalDelUsuario = Tk()
ventanaPrincipalDelUsuario.title("Ventana Principal del Usuario (Zona 0) ")
ventanaPrincipalDelUsuario.geometry("600x400")

titulo = Label(ventanaPrincipalDelUsuario, text="Hospital Andino", font=("Arial", 16))
titulo.grid()

ventanaPrincipalDelUsuario.mainloop()