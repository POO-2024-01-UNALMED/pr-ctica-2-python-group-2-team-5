from tkinter import *
from PIL import Image, ImageTk
import VentanaPrincipalDelUsuario


def abrirVentanaInicio(Hospital):
    # Ventana de inicio
    ventanaInicio = Tk()
    ventanaInicio.title("Ventana de Inicio")
    ventanaInicio.geometry("600x600+400+40")

    # ------------ EVENTOS -------------------

    def descripcionSistema():
        mensajeBienvenida.config(text="Con este programa podrá pedir citas, generar fórmulas médicas, reservar habitaciones, agendar citas de vacunación y realizar los pagos por los servicios recibidos, además de administrar de forma general todos los componentes que hacen parte del sistema hospitalario.", font=("Arial", 11))

    def quitarDescripcion(event):
        mensajeBienvenida.config(text="Bienvenido al Sistema de Información Hospitalario, HOSPITAL ANDINO!", font=("Arial", 15))

    def cargarImagen(ruta, tamano=(120, 160)):
        img = Image.open(ruta)
        img = img.resize(tamano)
        return ImageTk.PhotoImage(img)

    def cargarImagenP4(ruta, tamano=(260, 340)):
        img = Image.open(ruta)
        img = img.resize(tamano)
        return ImageTk.PhotoImage(img)

    def mostrarHV(event):
        global indice
        hvDesarrolladores.config(text=hojasDeVida[indice])
        indice = (indice + 1) % len(hojasDeVida)

        # Cambiar las imágenes del frameP6
        global indiceImgs
        labelImg1.config(image=listaImgs[indiceImgs][0])
        labelImg1.image = listaImgs[indiceImgs][0]  # Mantener referencia
        labelImg2.config(image=listaImgs[indiceImgs][1])
        labelImg2.image = listaImgs[indiceImgs][1]
        labelImg3.config(image=listaImgs[indiceImgs][2])
        labelImg3.image = listaImgs[indiceImgs][2]
        labelImg4.config(image=listaImgs[indiceImgs][3])
        labelImg4.image = listaImgs[indiceImgs][3]

        indiceImgs = (indiceImgs + 1) % len(listaImgs)

    def imagenesP4(event):
        global indiceFunc
        btnImgsFunc.config(image=imgsFunc[indiceFunc])
        btnImgsFunc.image = imgsFunc[indiceFunc]  # Mantener referencia
        indiceFunc = (indiceFunc + 1) % len(imgsFunc)

    def abrirVentPrincipal():
        ventanaInicio.withdraw()
        VentanaPrincipalDelUsuario.abrirVentanaPrincipal(ventanaInicio)

    # ------------------------------------------------------------

    # Barra de menú
    barraMenu = Menu(ventanaInicio)
    ventanaInicio.config(menu=barraMenu)
    menuInicio = Menu(barraMenu, tearoff=0)
    barraMenu.add_cascade(label="Inicio", menu=menuInicio)
    menuInicio.add_command(label="Descripcion del sistema", command=descripcionSistema)
    menuInicio.add_separator()
    menuInicio.add_command(label="Salir", command=ventanaInicio.destroy)

    # ------------------- Frames P1 y P2 -----------------------------------------
    frameP1 = Frame(ventanaInicio, bg="black")
    frameP1.pack(side="left", expand=True, fill="both", padx=(10, 5), pady=10)
    frameP2 = Frame(ventanaInicio, bg="black")
    frameP2.pack(side="right", expand=True, fill="both", padx=(5, 10), pady=10)

    # ----------------------------- Frame P3 --------------------------------------
    frameP3 = Frame(frameP1, bg="white", height=200)
    frameP3.pack_propagate(False)
    frameP3.pack(fill="both", padx=10, pady=(10, 5))
    mensajeBienvenida = Label(frameP3, text="Bienvenido al Sistema de Información Hospitalario, HOSPITAL ANDINO!", wraplength=250, font=("Arial", 15), justify="left")
    mensajeBienvenida.pack(expand=True, fill="both")
    mensajeBienvenida.bind("<Button-1>", quitarDescripcion)

    # ------------------------------- Frame P4 -------------------------------------
    frameP4 = Frame(frameP1, bg="white", height=440)
    frameP4.pack_propagate(False)
    frameP4.pack(fill="both", padx=10, pady=(5, 10))

    # Imagenes para ubicar en el Label del FrameP4
    global imgsFunc, btnImgsFunc, indiceFunc
    imgsFunc = [cargarImagenP4("src/iuMain/interfazGrafica/imagenes/fun1.jpg"),
                cargarImagenP4("src/iuMain/interfazGrafica/imagenes/fun2.jpg"),
                cargarImagenP4("src/iuMain/interfazGrafica/imagenes/fun3.jpg"),
                cargarImagenP4("src/iuMain/interfazGrafica/imagenes/fun4.jpg"),
                cargarImagenP4("src/iuMain/interfazGrafica/imagenes/fun5.jpg")]
    indiceFunc = 0
    btnImgsFunc = Button(frameP4, text="Pase el mouse por aquí para ver las imagenes relacionadas al sistema, o de click izquierdo para abrir la ventana principal!", command = abrirVentPrincipal, wraplength=250, justify="left", font=("Arial", 12))
    btnImgsFunc.pack(expand=True, fill="both", padx=5, pady=5)
    btnImgsFunc.bind("<Enter>", imagenesP4)

    # ------------------------------ Frame P5 -----------------------------
    frameP5 = Frame(frameP2, bg="white", height=200)
    frameP5.pack_propagate(False)
    frameP5.pack(fill="both", padx=10, pady=(10, 5))

    # Hojas de vidas
    global hojasDeVida, indice
    hojasDeVida = [
        "Hojas de Vida de los Desarrolladores",
        "Nombre: Juan Pablo Jimenez Vergara\nCarrera: Ingeniería de Sistemas\nInstitución: Universidad Nacional de Colombia\nSede: Medellin\nCorreo: juanjimenezve@unal.edu.co",
        "Nombre: Jerónimo Zapata Quiroz\nCarrera: Ingeniería de Sistemas\nInstitución: Universidad Nacional de Colombia\nSede: Medellin\nCorreo: jzapataq@unal.edu.co",
        "Nombre: Hernando Montes Gonzales\nCarrera: Ingeniería de Sistemas\nInstitución: Universidad Nacional de Colombia\nSede: Medellin\nCorreo: hmontesg@unal.edu.co",
        "Nombre: Manuel Mera Mera\nCarrera: Ingeniería de Sistemas\nInstitución: Universidad Nacional de Colombia\nSede: Medellin\nCorreo: mmeram@unal.edu.co",
        "Nombre: Samuel Ramirez Muñoz\nCarrera: Ingeniería de Sistemas\nInstitución: Universidad Nacional de Colombia\nSede: Medellin\nCorreo: sramirezmu@unal.edu.co"
    ]
    indice = 0
    hvDesarrolladores = Label(frameP5, text="Click aquí!", justify="left", font=("Arial", 11), wraplength=250)
    hvDesarrolladores.pack(expand=True, fill="both")
    hvDesarrolladores.bind("<Button-1>", mostrarHV)

    # ---------------------------- Frame P6 --------------------------------------
    frameP6 = Frame(frameP2, bg="white", height=440)
    frameP6.grid_propagate(False)
    frameP6.pack(fill="both", padx=10, pady=(5, 10))

    # Cargar imagenes y mantener referencias globales
    global img1Tk, img2Tk, img3Tk, img4Tk, listaImgs, indiceImgs
    img1Tk = cargarImagen("src/iuMain/interfazGrafica/imagenes/img2.jpg")
    img2Tk = cargarImagen("src/iuMain/interfazGrafica/imagenes/img2.jpg")
    img3Tk = cargarImagen("src/iuMain/interfazGrafica/imagenes/img3.jpg")
    img4Tk = cargarImagen("src/iuMain/interfazGrafica/imagenes/img4.jpg")

    listaImgs = [
        [cargarImagen("src/iuMain/interfazGrafica/imagenes/img2.jpg"), cargarImagen("src/iuMain/interfazGrafica/imagenes/img3.jpg"), cargarImagen("src/iuMain/interfazGrafica/imagenes/img4.jpg"), cargarImagen("src/iuMain/interfazGrafica/imagenes/img5.jpg")],
        [cargarImagen("src/iuMain/interfazGrafica/imagenes/img2.jpg"), cargarImagen("src/iuMain/interfazGrafica/imagenes/img7.jpg"), cargarImagen("src/iuMain/interfazGrafica/imagenes/img8.jpg"), cargarImagen("src/iuMain/interfazGrafica/imagenes/img1.jpg")]
    ]

    indiceImgs = 0

    labelImg1 = Label(frameP6, image=img1Tk, background="blue")
    labelImg1.grid(row=0, column=0, padx=(6, 2), pady=(8, 2))
    labelImg2 = Label(frameP6, image=img2Tk, background="blue")
    labelImg2.grid(row=0, column=1, padx=(3, 5), pady=(8, 2))
    labelImg3 = Label(frameP6, image=img3Tk, background="blue")
    labelImg3.grid(row=1, column=0, padx=(6, 2), pady=(5, 5))
    labelImg4 = Label(frameP6, image=img4Tk, background="blue")
    labelImg4.grid(row=1, column=1, padx=(3, 5), pady=(5, 5))

    ventanaInicio.mainloop()
