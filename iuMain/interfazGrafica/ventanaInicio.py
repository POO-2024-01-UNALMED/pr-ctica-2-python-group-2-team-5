from tkinter import *  # ---> Importamos todo por ahora.

# Primeras pruebas interfaz gráfica python.

# TODO: Añadir los command a los menús.

# Ventana de inicio (Tamaño: 600x600, en una ubicación de x: 400px, y: 40px de la pantalla)

ventanaInicio = Tk()
ventanaInicio.title("Ventana de Inicio")
ventanaInicio.geometry("600x600+400+40")

# ------------ EVENTOS (PRUEBAS) -------------------

#Eventos del menú.

def descripcionSistema():
    global mensajeBienvenida
    mensajeBienvenida.config(text = "Puede pedir citas, generar fórmulas y reservar habitaciones...")

# --------------------------------------------------

# Barra de menú.

barraMenu = Menu(ventanaInicio)
ventanaInicio.config(menu = barraMenu)

# Menú Inicio (tearoff para dejar el menú estático en su lugar).

menuInicio = Menu(barraMenu, tearoff = 0)
barraMenu.add_cascade(label = "Inicio", menu = menuInicio)

# Agregar las opciones al Menú de Inicio.

menuInicio.add_command(label = "Descripcion del sistema", command = descripcionSistema)
menuInicio.add_separator()
menuInicio.add_command(label = "Salir", command = ventanaInicio.destroy)

# Frames P1 y P2.

frameP1 = Frame(ventanaInicio, bg = "black")
frameP1.pack(side = "left", expand = True, fill = "both", padx = (10, 5), pady = 10)

frameP2 = Frame(ventanaInicio, bg = "black")
frameP2.pack(side = "right", expand = True, fill = "both", padx = (5, 10), pady = 10)

# Frame P3.

frameP3 = Frame(frameP1, bg = "white", height = 200)
frameP3.pack_propagate(False)
frameP3.pack(fill = "both", padx = 10, pady = (10, 5))

# Mensaje de bienvenida en el Frame 3.

mensajeBienvenida = Label(frameP3, text = "Bienvenido al Sistema de Información Hospitalario!")
mensajeBienvenida.place(y = 80)

# Frame P4.

frameP4 = Frame(frameP2, bg = "white", height = 200)
frameP4.pack(fill = "both", padx = 10, pady = (10, 5))

# Frame P5.

frameP5 = Frame(frameP1, bg = "white")
frameP5.pack(expand = True, fill = "both", padx = 10, pady = (5, 10))

# Frame P6.

frameP6 = Frame(frameP2, bg = "white")
frameP6.pack(expand = True, fill = "both", padx = 10, pady = (5, 10))

# Método mainloop.

ventanaInicio.mainloop()