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

# Método para cargar las imagenes.

def cargarImagen(ruta, tamaño = (120, 160)):
    img1 = Image.open(ruta)
    img1 = img1.resize(tamaño)
    return ImageTk.PhotoImage(img1)

def cargarImagenP4(ruta):
    img1 = Image.open(ruta)
    img1 = img1.resize(tamaño)
    return ImageTk.PhotoImage(img1)

# Evento para cambiar el texto en las hojas de vida, Frame P5.

def mostrarHV(event):
    # Para mostrar las hojas de vida.

    global hojasDeVida, indice, hvDesarrolladores
    hvDesarrolladores.config(text = hojasDeVida[indice])
    indice = (indice + 1) % len(hojasDeVida)

    # Para cambiar las imagenes del frameP6.

    global indiceImgs, labelImg1, labelImg2, labelImg3, labelImg4, listaImgs
    # Cambiar las imágenes de cada label independientemente
    labelImg1.config(image=listaImgs[indiceImgs][0])
    labelImg2.config(image=listaImgs[indiceImgs][1])
    labelImg3.config(image=listaImgs[indiceImgs][2])
    labelImg4.config(image=listaImgs[indiceImgs][3])

    # Avanzar al siguiente conjunto de imágenes
    indiceImgs = (indiceImgs + 1) % len(listaImgs)

def imagenesP4(event):
    global imgsFunc, labelImgsFunc, indiceFunc
    img1 = Image.open(imgsFunc[indiceFunc])
    #img1 = img1.resize()
    imgTk = ImageTk.PhotoImage(img1)
    labelImgsFunc.config(image = imgTk)

    print("Cambiando imgs")

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

# Imagenes para ubicar en el Label del FrameP4.

imgsFunc = ["imagenes/fun1.jpg",
            "imagenes/fun2.jpg",
            "imagenes/fun3.jpg",
            "imagenes/fun4.jpg",
            "imagenes/fun5.jpg"]

indiceFunc = 0

# Label para ubicar las imagenes relacionadas al sistema de hospital.

labelImgsFunc = Label(frameP4, bg = "green")
labelImgsFunc.pack(expand = True, fill = "both", padx = 5, pady = 5)
labelImgsFunc.bind("<Enter>", imagenesP4)

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

hvDesarrolladores = Label(frameP5, text = "Click!", justify = "left")
hvDesarrolladores.pack(expand = True,fill = "both")
hvDesarrolladores.bind("<Button-1>", mostrarHV)

# Frame P6.

frameP6 = Frame(frameP2, bg = "white", height = 440)
frameP6.grid_propagate(False)
frameP6.pack(fill = "both", padx = 10, pady = (5, 10))

# Cargar la imagen para ubicar en el Frame P6.

img1 = Image.open("imagenes/img1.jpg")
nDimension = img1.resize((120, 160))
img1Tk = ImageTk.PhotoImage(nDimension)

# Lista imagenes para mostrar en el Frame P6.

listaImgs = [
    [cargarImagen("imagenes/img2.jpg"), cargarImagen("imagenes/img3.jpg"), cargarImagen("imagenes/img4.jpg"), cargarImagen("imagenes/img5.jpg")],
    [cargarImagen("imagenes/img6.jpg"), cargarImagen("imagenes/img7.jpg"), cargarImagen("imagenes/img8.jpg"), cargarImagen("imagenes/img1.jpg")]
]

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