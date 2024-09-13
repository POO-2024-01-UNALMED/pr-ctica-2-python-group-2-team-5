from tkinter import *  # ---> Importamos todo por ahora.
from PIL import Image, ImageTk

# Primeras pruebas interfaz gráfica python.

# TODO: Añadir los command a los menús.

# Ventana de inicio (Tamaño: 600x600, en una ubicación de x: 400px, y: 40px de la pantalla)

ventanaInicio = Tk()
ventanaInicio.title("Ventana de Inicio")
ventanaInicio.geometry("600x600+400+40")

# ------------ EVENTOS (PRUEBAS) -------------------

# Eventos del menú.

def descripcionSistema():
    global mensajeBienvenida
    mensajeBienvenida.config(text = "Puede pedir citas, generar fórmulas y reservar habitaciones...")

# Evento para cambiar el texto en las hojas de vida, Frame P5.

def mostrarHV(event):
    # Para mostrar las hojas de vida.

    global hojasDeVida, indice, descripcionDesarrollador
    descripcionDesarrollador.config(text = hojasDeVida[indice])
    indice = (indice + 1) % len(hojasDeVida)

    # Para cambiar las imagenes del frameP6.

    global img1, indiceImgs, labelImg1, labelImg2, labelImg3, labelImg4, listaImgs, nDimension, img1Tk
    img1 = Image.open(listaImgs[indiceImgs])
    nDimension = img1.resize((120, 160))
    img1Tk = ImageTk.PhotoImage(nDimension)
    labelImg1.config(image = img1Tk)
    labelImg2.config(image = img1Tk)
    labelImg3.config(image = img1Tk)
    labelImg4.config(image = img1Tk)
    indiceImgs = (indiceImgs + 1) % len(listaImgs)

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

mensajeBienvenida = Label(frameP3, text = "Bienvenido al Sistema de Información Hospitalario!", wraplength = 250, font = ("Arial", 15))
mensajeBienvenida.pack(expand = True, fill = "both")

# Frame P4.

frameP4 = Frame(frameP1, bg = "white", height = 440)
frameP4.pack_propagate(False)
frameP4.pack(fill = "both", padx = 10, pady = (5, 10))

# Frame P5.

frameP5 = Frame(frameP2, bg = "white", height = 200)
frameP5.pack_propagate(False)
frameP5.pack(fill = "both", padx = 10, pady = (10, 5))

# Hojas de vidas de los desarrolladores en el Frame 5.

hojasDeVida = [
    "Hojas de Vida de los Desarrolladores",
    "Nombre: Nombre1\nEdad: Edad1\nVive en: Lugar1\nEstudia: Ing. de Sistemas\nEn la Universidad: Nacional de Colombia\nSede: Medellin",
    "Nombre: Nombre2\nEdad: Edad2\nVive en: Lugar2\nEstudia: Ing. de Sistemas\nEn la Universidad: Nacional de Colombia\nSede: Medellin",
    "Nombre: Nombre3\nEdad: Edad3\nVive en: Lugar3\nEstudia: Ing. de Sistemas\nEn la Universidad: Nacional de Colombia\nSede: Medellin",
    "Nombre: Nombre4\nEdad: Edad4\nVive en: Lugar4\nEstudia: Ing. de Sistemas\nEn la Universidad: Nacional de Colombia\nSede: Medellin"
]
indice = 0

descripcionDesarrollador = Label(frameP5, text = "Click!", justify = "left")
descripcionDesarrollador.pack(expand = True,fill = "both")
descripcionDesarrollador.bind("<Button-1>", mostrarHV)

# Frame P6.

frameP6 = Frame(frameP2, bg = "white", height = 440)
frameP6.grid_propagate(False)
frameP6.pack(fill = "both", padx = 10, pady = (5, 10))

# Cargar la imagen para ubicar en el Frame P6.

img1 = Image.open("imagenes/img1.jpg")
nDimension = img1.resize((120, 160))
img1Tk = ImageTk.PhotoImage(nDimension)

# Lista imagenes para mostrar en el Frame P6.

listaImgs = ["imagenes/img2.jpg", "imagenes/img3.jpg", "imagenes/img4.jpg", "imagenes/img5.jpg", "imagenes/img6.jpg", "imagenes/img7.jpg", "imagenes/img8.jpg"]
indiceImgs = 0

# Label para ubicar la imagem.

labelImg1 = Label(frameP6, image = img1Tk, background = "blue")
labelImg1.grid(row = 0, column = 0, padx = (5, 2), pady = (5, 2))

labelImg2 = Label(frameP6, image = img1Tk, background = "blue")
labelImg2.grid(row = 0, column = 1, padx = (2, 5), pady = (5, 2))

labelImg3 = Label(frameP6, image = img1Tk, background = "blue")
labelImg3.grid(row = 1, column = 0, padx = (5, 2), pady = (2, 5))

labelImg4 = Label(frameP6, image = img1Tk, background = "blue")
labelImg4.grid(row = 1, column = 1, padx = (2, 5), pady = (2, 5))

# Método mainloop.

ventanaInicio.mainloop()