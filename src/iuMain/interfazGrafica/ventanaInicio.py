from tkinter import *  # ---> Importamos todo por ahora.
from PIL import Image, ImageTk
from iuMain.interfazGrafica.VentanaPrincipalDelUsuario import abrirVentanaPrincipal
# Primeras pruebas interfaz gráfica python.

# Variables de apoyo
mensajeBienvenida = ""
hvDesarrolladores = []
hojasDeVida = []
indice = 0
imgsFunc = []
indiceFunc = 0

# Label para ubicar las imagemes.

labelImg1 = Label()
labelImg2 = Label()
labelImg3 = Label()
labelImg4 = Label()

def abrirVentanaInicio():
    global mensajeBienvenida, hvDesarrolladores, hojasDeVida, indice, imgsFunc, indiceFunc
    # Ventana de inicio (Tamaño: 600x600, en una ubicación de x: 400px, y: 40px de la pantalla)

    ventanaInicio = Tk()
    ventanaInicio.title("Ventana de Inicio")
    ventanaInicio.geometry("600x600+400+40")

    #Cambiar el icono.

    #ventanaInicio.wm_iconbitmap("imagenes/hospital-building.ico")

    # ------------ EVENTOS -------------------

    # Eventos del menú, muestra la descripción del programa al dar click en descripcion sistema.

    def descripcionSistema():
        global mensajeBienvenida
        mensajeBienvenida.config(text = "Con este programa podrá pedir citas, generar fórmulas médicas, reservar habitaciones, agendar citas de vacunación y realizar los pagos por los servicios recibidos, además de administrar de forma general todos los componentes que hacen parte del sistema hospitalario.", font = ("Arial", 11))

    # Método para volver a mostrar el mensaje de bienvenida (Quitar la descripción).
    def quitarDescripcion(event):
        mensajeBienvenida.config(text = "Bienvenido al Sistema de Información Hospitalario!", font = ("Arial", 15))

    # Métodos para cargar las imagenes.

    # Para el FrameP6.

    def cargarImagen(ruta, tamano = (120, 160)):
        img1 = Image.open(ruta)
        img1 = img1.resize(tamano)
        return ImageTk.PhotoImage(img1)

    # Para el FrameP4.

    def cargarImagenP4(ruta, tamano = (260, 340)):
        img1 = Image.open(ruta)
        img1 = img1.resize(tamano)
        return ImageTk.PhotoImage(img1)

    # Evento para cambiar el texto en las hojas de vida, Frame P5.

    def mostrarHV(event):
        # Para mostrar las hojas de vida.

        global hojasDeVida, indice, hvDesarrolladores
        hvDesarrolladores.config(text = hojasDeVida[indice])
        indice = (indice + 1) % len(hojasDeVida)

        # Para cambiar las imagenes del frameP6.

        global indiceImgs, labelImg1, labelImg2, labelImg3, labelImg4, listaImgs
        # Cambiar las imágenes de cada label.
        labelImg1.config(image = listaImgs[indiceImgs][0])
        labelImg2.config(image = listaImgs[indiceImgs][1])
        labelImg3.config(image = listaImgs[indiceImgs][2])
        labelImg4.config(image = listaImgs[indiceImgs][3])

        # Siguiente grupo de imagenes.

        indiceImgs = (indiceImgs + 1) % len(listaImgs)

    # Método para cambiar las imagenes del FrameP4 al pasar el ratón.

    def imagenesP4(event):
        global imgsFunc, btnImgsFunc, indiceFunc
        btnImgsFunc.config(image = imgsFunc[indiceFunc])
        indiceFunc = (indiceFunc + 1) % len(imgsFunc)

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

    # ------------------- Frames P1 y P2 -----------------------------------------

    frameP1 = Frame(ventanaInicio, bg = "black")
    frameP1.pack(side = "left", expand = True, fill = "both", padx = (10, 5), pady = 10)

    frameP2 = Frame(ventanaInicio, bg = "black")
    frameP2.pack(side = "right", expand = True, fill = "both", padx = (5, 10), pady = 10)

    # ----------------------------- Frame P3 --------------------------------------

    frameP3 = Frame(frameP1, bg = "white", height = 200)
    frameP3.pack_propagate(False)
    frameP3.pack(fill = "both", padx = 10, pady = (10, 5))

    # Mensaje de bienvenida en el Frame 3.

    mensajeBienvenida = Label(frameP3, text = "Bienvenido al Sistema de Información Hospitalario!", wraplength = 250, font = ("Arial", 15), justify = "left")
    mensajeBienvenida.pack(expand = True, fill = "both")
    mensajeBienvenida.bind("<Button-1>", quitarDescripcion)

    # ------------------------------- Frame P4 -------------------------------------

    frameP4 = Frame(frameP1, bg = "white", height = 440)
    frameP4.pack_propagate(False)
    frameP4.pack(fill = "both", padx = 10, pady = (5, 10))

    # Imagenes para ubicar en el Label del FrameP4

    imgsFunc = [cargarImagenP4("imagenes/fun1.jpg"),
                cargarImagenP4("imagenes/fun2.jpg"),
                cargarImagenP4("imagenes/fun3.jpg"),
                cargarImagenP4("imagenes/fun4.jpg"),
                cargarImagenP4("imagenes/fun5.jpg")]

    indiceFunc = 0

    # Botón para ubicar las imagenes relacionadas al sistema de hospital.

    btnImgsFunc = Button(frameP4, text = "Pase el mouse por aquí para ver las imagenes relacionadas al sistema, o de click izquierdo para abrir la ventana principal!", command = lambda: abrirVentanaInicio(), wraplength = 250, justify = "left", font = ("Arial", 12))
    btnImgsFunc.pack(expand = True, fill = "both", padx = 5, pady = 5)
    btnImgsFunc.bind("<Enter>", imagenesP4)

    # ------------------------------ Frame P5 -----------------------------

    frameP5 = Frame(frameP2, bg = "white", height = 200)
    frameP5.pack_propagate(False)
    frameP5.pack(fill = "both", padx = 10, pady = (10, 5))

    # Hojas de vidas de los desarrolladores en el Frame 5.

    hojasDeVida = [
        "Hojas de Vida de los Desarrolladores",
        "Nombre: Nombre1\nEdad: Edad1\nVive en: Lugar1\nEstudia: Ingeniería de Sistemas\nEn: Universidad Nacional de Colombia\nSede: Medellin\nCorreo: correoinst@unal.edu.co",
        "Nombre: Nombre2\nEdad: Edad2\nVive en: Lugar2\nEstudia: Ingeniería de Sistemas\nEn: Universidad Nacional de Colombia\nSede: Medellin\nCorreo: correoinst@unal.edu.co",
        "Nombre: Nombre3\nEdad: Edad3\nVive en: Lugar3\nEstudia: Ingeniería de Sistemas\nEn: Universidad Nacional de Colombia\nSede: Medellin\nCorreo: correoinst@unal.edu.co",
        "Nombre: Nombre4\nEdad: Edad4\nVive en: Lugar4\nEstudia: Ingeniería de Sistemas\nEn: Universidad Nacional de Colombia\nSede: Medellin\nCorreo: correoinst@unal.edu.co"
    ]
    indice = 0

    hvDesarrolladores = Label(frameP5, text = "Click aquí!", justify = "left", font = ("Arial", 11), wraplength = 250)
    hvDesarrolladores.pack(expand = True,fill = "both")
    hvDesarrolladores.bind("<Button-1>", mostrarHV)

    # ---------------------------- Frame P6 --------------------------------------

    frameP6 = Frame(frameP2, bg = "white", height = 440)
    frameP6.grid_propagate(False)
    frameP6.pack(fill = "both", padx = 10, pady = (5, 10))

    # Cargar la imagen para ubicar en el Frame P6.

    img1Tk = cargarImagen("imagenes/img2.jpg")
    img2Tk = cargarImagen("imagenes/img2.jpg")
    img3Tk = cargarImagen("imagenes/img3.jpg")
    img4Tk = cargarImagen("imagenes/img4.jpg")

    # Lista imagenes para mostrar en el Frame P6.

    listaImgs = [
        [cargarImagen("imagenes/img2.jpg"), cargarImagen("imagenes/img3.jpg"), cargarImagen("imagenes/img4.jpg"), cargarImagen("imagenes/img5.jpg")],
        [cargarImagen("imagenes/img2.jpg"), cargarImagen("imagenes/img7.jpg"), cargarImagen("imagenes/img8.jpg"), cargarImagen("imagenes/img1.jpg")]
    ]

    indiceImgs = 0

    # Label para ubicar las imagemes.

    labelImg1 = Label(frameP6, image = img1Tk, background = "blue")
    labelImg1.grid(row = 0, column = 0, padx = (6, 2), pady = (8, 2))

    labelImg2 = Label(frameP6, image = img2Tk, background = "blue")
    labelImg2.grid(row = 0, column = 1, padx = (3, 5), pady = (8, 2))

    labelImg3 = Label(frameP6, image = img3Tk, background = "blue")
    labelImg3.grid(row = 1, column = 0, padx = (6, 2), pady = (5, 5))

    labelImg4 = Label(frameP6, image = img4Tk, background = "blue")
    labelImg4.grid(row = 1, column = 1, padx = (3, 5), pady = (5, 5))

    # -------------------------- Método mainloop ----------------------------------

    ventanaInicio.mainloop()