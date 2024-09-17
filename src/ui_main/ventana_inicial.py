import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from src.ui_main.ventana_principal import ventana_principal

imagen_seleccionada = 0
desarrollador = 0


def ventana_inicial(hospital):
    def desarrollador4():
        global tk_foto1_nueva, tk_foto2_nueva, tk_foto3_nueva, tk_foto4_nueva

        nombre.config(text="Samuel Ramirez Muños", font=("Helvetica", 12))
        email.config(text="sramirezmu@unal.edu.co", font=("Helvetica", 12))
        github.config(text="github.com/SamuelRamirezM", font=("Helvetica", 12))
        carrera.config(text="Ingeniería de Sistemas e Informática", font=("Helvetica", 12))

        foto1_nueva = lista_fotos[desarrollador][0]
        foto2_nueva = lista_fotos[desarrollador][1]
        foto3_nueva = lista_fotos[desarrollador][2]
        foto4_nueva = lista_fotos[desarrollador][3]
        tk_foto1_nueva = ImageTk.PhotoImage(foto1_nueva.resize((foto00.winfo_width(), foto00.winfo_height())))
        tk_foto2_nueva = ImageTk.PhotoImage(foto2_nueva.resize((foto01.winfo_width(), foto01.winfo_height())))
        tk_foto3_nueva = ImageTk.PhotoImage(foto3_nueva.resize((foto10.winfo_width(), foto10.winfo_height())))
        tk_foto4_nueva = ImageTk.PhotoImage(foto4_nueva.resize((foto11.winfo_width(), foto11.winfo_height())))
        foto00.create_image(0, 0, image=tk_foto1_nueva, anchor="nw")
        foto01.create_image(0, 0, image=tk_foto2_nueva, anchor="nw")
        foto10.create_image(0, 0, image=tk_foto3_nueva, anchor="nw")
        foto11.create_image(0, 0, image=tk_foto4_nueva, anchor="nw")

    def desarrollador3():
        global tk_foto1_nueva, tk_foto2_nueva, tk_foto3_nueva, tk_foto4_nueva

        nombre.config(text="Hernando Montes Gonzalez", font=("Helvetica", 12))
        email.config(text="hmontesg@unal.edu.co", font=("Helvetica", 12))
        github.config(text="github.com/HernandoMontes", font=("Helvetica", 12))
        carrera.config(text="Ingeniería de Sistemas e Informática", font=("Helvetica", 12))

        foto1_nueva = lista_fotos[desarrollador][0]
        foto2_nueva = lista_fotos[desarrollador][1]
        foto3_nueva = lista_fotos[desarrollador][2]
        foto4_nueva = lista_fotos[desarrollador][3]
        tk_foto1_nueva = ImageTk.PhotoImage(foto1_nueva.resize((foto00.winfo_width(), foto00.winfo_height())))
        tk_foto2_nueva = ImageTk.PhotoImage(foto2_nueva.resize((foto01.winfo_width(), foto01.winfo_height())))
        tk_foto3_nueva = ImageTk.PhotoImage(foto3_nueva.resize((foto10.winfo_width(), foto10.winfo_height())))
        tk_foto4_nueva = ImageTk.PhotoImage(foto4_nueva.resize((foto11.winfo_width(), foto11.winfo_height())))
        foto00.create_image(0, 0, image=tk_foto1_nueva, anchor="nw")
        foto01.create_image(0, 0, image=tk_foto2_nueva, anchor="nw")
        foto10.create_image(0, 0, image=tk_foto3_nueva, anchor="nw")
        foto11.create_image(0, 0, image=tk_foto4_nueva, anchor="nw")

    def desarrollador2():
        global tk_foto1_nueva, tk_foto2_nueva, tk_foto3_nueva, tk_foto4_nueva

        nombre.config(text="Manuel Mera Mera", font=("Helvetica", 12))
        email.config(text="MmeraM@unal.edu.co", font=("Helvetica", 12))
        github.config(text="github.com/Manuelmera", font=("Helvetica", 12))
        carrera.config(text="Ingeniería de Sistemas e Informática", font=("Helvetica", 12))

        foto1_nueva = lista_fotos[desarrollador][0]
        foto2_nueva = lista_fotos[desarrollador][1]
        foto3_nueva = lista_fotos[desarrollador][2]
        foto4_nueva = lista_fotos[desarrollador][3]
        tk_foto1_nueva = ImageTk.PhotoImage(foto1_nueva.resize((foto00.winfo_width(), foto00.winfo_height())))
        tk_foto2_nueva = ImageTk.PhotoImage(foto2_nueva.resize((foto01.winfo_width(), foto01.winfo_height())))
        tk_foto3_nueva = ImageTk.PhotoImage(foto3_nueva.resize((foto10.winfo_width(), foto10.winfo_height())))
        tk_foto4_nueva = ImageTk.PhotoImage(foto4_nueva.resize((foto11.winfo_width(), foto11.winfo_height())))
        foto00.create_image(0, 0, image=tk_foto1_nueva, anchor="nw")
        foto01.create_image(0, 0, image=tk_foto2_nueva, anchor="nw")
        foto10.create_image(0, 0, image=tk_foto3_nueva, anchor="nw")
        foto11.create_image(0, 0, image=tk_foto4_nueva, anchor="nw")

    def desarrollador1():
        global tk_foto1_nueva, tk_foto2_nueva, tk_foto3_nueva, tk_foto4_nueva

        nombre.config(text="Juan Pablo Jimenez Vergara", font=("Helvetica", 12))
        email.config(text="juajimenezve@unal.edu.co", font=("Helvetica", 12))
        github.config(text="github.com/PabloJimenez028", font=("Helvetica", 12))
        carrera.config(text="Ingenieria de Sistemas e Informática", font=("Helvetica", 12))

        foto1_nueva = lista_fotos[desarrollador][0]
        foto2_nueva = lista_fotos[desarrollador][1]
        foto3_nueva = lista_fotos[desarrollador][2]
        foto4_nueva = lista_fotos[desarrollador][3]
        tk_foto1_nueva = ImageTk.PhotoImage(foto1_nueva.resize((foto00.winfo_width(), foto00.winfo_height())))
        tk_foto2_nueva = ImageTk.PhotoImage(foto2_nueva.resize((foto01.winfo_width(), foto01.winfo_height())))
        tk_foto3_nueva = ImageTk.PhotoImage(foto3_nueva.resize((foto10.winfo_width(), foto10.winfo_height())))
        tk_foto4_nueva = ImageTk.PhotoImage(foto4_nueva.resize((foto11.winfo_width(), foto11.winfo_height())))
        foto00.create_image(0, 0, image=tk_foto1_nueva, anchor="nw")
        foto01.create_image(0, 0, image=tk_foto2_nueva, anchor="nw")
        foto10.create_image(0, 0, image=tk_foto3_nueva, anchor="nw")
        foto11.create_image(0, 0, image=tk_foto4_nueva, anchor="nw")

    def desarrollador0():
        global tk_foto1_nueva, tk_foto2_nueva, tk_foto3_nueva, tk_foto4_nueva

        nombre.config(text="Nombre: Jeronimo Zapata Quiroz", font=("Helvetica", 12))
        email.config(text="jzapataq@unal.edu.co", font=("Helvetica", 12))
        github.config(text="github.com/jerozapata", font=("Helvetica", 12))
        carrera.config(text="Ingeniería de Sistemas e Informática", font=("Helvetica", 12))

        foto1_nueva = lista_fotos[desarrollador][0]
        foto2_nueva = lista_fotos[desarrollador][1]
        foto3_nueva = lista_fotos[desarrollador][2]
        foto4_nueva = lista_fotos[desarrollador][3]
        tk_foto1_nueva = ImageTk.PhotoImage(foto1_nueva.resize((foto00.winfo_width(), foto00.winfo_height())))
        tk_foto2_nueva = ImageTk.PhotoImage(foto2_nueva.resize((foto01.winfo_width(), foto01.winfo_height())))
        tk_foto3_nueva = ImageTk.PhotoImage(foto3_nueva.resize((foto10.winfo_width(), foto10.winfo_height())))
        tk_foto4_nueva = ImageTk.PhotoImage(foto4_nueva.resize((foto11.winfo_width(), foto11.winfo_height())))
        foto00.create_image(0, 0, image=tk_foto1_nueva, anchor="nw")
        foto01.create_image(0, 0, image=tk_foto2_nueva, anchor="nw")
        foto10.create_image(0, 0, image=tk_foto3_nueva, anchor="nw")
        foto11.create_image(0, 0, image=tk_foto4_nueva, anchor="nw")

    def cambiar_hoja_de_vida(event):
        global desarrollador

        desarrollador = (desarrollador + 1) % 5

        if desarrollador == 0:
            desarrollador0()
        elif desarrollador == 1:
            desarrollador1()
        elif desarrollador == 2:
            desarrollador2()
        elif desarrollador == 3:
            desarrollador3()
        elif desarrollador == 4:
            desarrollador4()

    def cambiar_imagen_aplicacion(event):
        global tk_cambio_aplicacion
        global imagen_seleccionada

        width = canvas_imagenes_aplicacion.winfo_width()
        height = canvas_imagenes_aplicacion.winfo_height()

        imagen_seleccionada = (imagen_seleccionada + 1) % len(lista_imagenes)

        imagen_aplicacion_nueva = lista_imagenes[imagen_seleccionada]

        tk_cambio_aplicacion = ImageTk.PhotoImage(imagen_aplicacion_nueva.resize((width, height)))

        canvas_imagenes_aplicacion.create_image(0, 0, image=tk_cambio_aplicacion, anchor="nw")

    def acomodar_foto4(event):
        global tk_foto4

        width = event.width
        height = event.height

        foto4 = lista_fotos[desarrollador][3]
        tk_foto4 = ImageTk.PhotoImage(foto4.resize((width, height)))

        foto11.create_image(0, 0, image=tk_foto4, anchor="nw")

    def acomodar_foto3(event):
        global tk_foto3

        width = event.width
        height = event.height

        foto3 = lista_fotos[desarrollador][2]
        tk_foto3 = ImageTk.PhotoImage(foto3.resize((width, height)))

        foto10.create_image(0, 0, image=tk_foto3, anchor="nw")

    def acomodar_foto2(event):
        global tk_foto2

        width = event.width
        height = event.height

        foto2 = lista_fotos[desarrollador][1]
        tk_foto2 = ImageTk.PhotoImage(foto2.resize((width, height)))

        foto01.create_image(0, 0, image=tk_foto2, anchor="nw")

    def acomodar_foto1(event):
        global tk_foto1

        width = event.width
        height = event.height

        foto1 = lista_fotos[desarrollador][0]
        tk_foto1 = ImageTk.PhotoImage(foto1.resize((width, height)))

        foto00.create_image(0, 0, image=tk_foto1, anchor="nw")

    def acomodar_imagen_aplicacion(event):
        global tk_aplicacion

        width = event.width
        height = event.height

        imagen_aplicacion_nueva = lista_imagenes[imagen_seleccionada].resize((width, height))
        tk_aplicacion = ImageTk.PhotoImage(imagen_aplicacion_nueva)

        canvas_imagenes_aplicacion.create_image(0, 0, image=tk_aplicacion, anchor="nw")

    def descripcion():
        descripcion_texto = "HOSPITAL ANDINO es una aplicacion que se encarga de gestionar " \
                          "los servicios de salud que ofrece su hospital"
        messagebox.showinfo("Descripcion", descripcion_texto)

    ventana = tk.Tk()
    ventana.title("HOSPITAL ANDINO - Sistema de gestion hospitalaria")
    ventana.geometry("600x600+400+40")
    ventana.protocol("WM_DELETE_WINDOW", hospital.serializar())

    # Menu inicio
    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu)
    opcion_archivo = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=opcion_archivo)
    opcion_archivo.add_command(label="Descripcion", command=descripcion)
    opcion_archivo.add_command(label="Salir", command=lambda: [hospital.serializar(), ventana.destroy()])

    # Frames principales
    frame_p1 = ttk.Frame(ventana, width=200)
    frame_p2 = ttk.Frame(ventana)

    # Mensaje de bienvenida
    frame_p3 = ttk.Frame(frame_p1)
    bienvenida = ttk.Label(frame_p3, text="Bienvenido al sistema de informacion hospitalario, HOSPITAL ANDINO", anchor="center", font=("Arial", 12), wraplength=200)

    # Imagenes de la aplicacion
    frame_p4 = ttk.Frame(frame_p1)
    p4_imagenes = ttk.Frame(frame_p4)
    p4_imagenes.configure(borderwidth=7, relief="solid", padding=0)
    canvas_imagenes_aplicacion = tk.Canvas(p4_imagenes)
    lista_imagenes = [Image.open("src/ui_main/imagenes/fun1.jpg").resize((400, 400)),
                      Image.open("src/ui_main/imagenes/fun2.jpg").resize((400, 400)),
                      Image.open("src/ui_main/imagenes/fun3.jpg").resize((400, 400)),
                      Image.open("src/ui_main/imagenes/fun4.jpg").resize((400, 400)),
                      Image.open("src/ui_main/imagenes/fun5.jpg").resize((400, 400))]

    # Boton para continuar
    p4_continuar = ttk.Frame(frame_p4)
    style = ttk.Style()
    style.configure("My.TButton.TButton", foreground="black", background="#4D5BE4", font=("Helvetica", 10, "bold"))

    continuar = ttk.Button(p4_continuar, text="Ingresar a la aplicación", style="My.TButton.TButton", command=lambda: [ventana.destroy(), ventana_principal(hospital)])

    # Hoja de vida desarrolladores
    frame_p5 = ttk.Frame(frame_p2)
    nombre = ttk.Label(frame_p5, anchor="center")
    email = ttk.Label(frame_p5, anchor="center")
    github = ttk.Label(frame_p5, anchor="center")
    carrera = ttk.Label(frame_p5, anchor="center")

    nombre.config(text="Nombre: Jeronimo Zapata Quiroz", font=("Helvetica", 12))
    email.config(text="Correo: jzapataq@unal.edu.co", font=("Helvetica", 12))
    github.config(text="github.com/jerozapata", font=("Helvetica", 12))
    carrera.config(text="Carrera: Ingeniería de Sistemas e Informática", font=("Helvetica", 12))

    # Fotos desarrolladores
    frame_p6 = ttk.Frame(frame_p2)
    lista_fotos = [[Image.open("src/ui_main/imagenes/jero1.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/jero2.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/jero3.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/jero4.jpg").resize((1000, 1000))],

                   [Image.open("src/ui_main/imagenes/juan1.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/juan2.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/juan3.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/juan4.jpg").resize((1000, 1000))],

                   [Image.open("src/ui_main/imagenes/manuel1.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/manuel2.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/manuel3.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/manuel4.jpg").resize((1000, 1000))],

                   [Image.open("src/ui_main/imagenes/hernando1.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/hernando2.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/hernando3.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/hernando4.jpg").resize((1000, 1000))],

                   [Image.open("src/ui_main/imagenes/samuel1.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/samuel2.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/samuel3.jpg").resize((1000, 1000)),
                    Image.open("src/ui_main/imagenes/samuel4.jpg").resize((1000, 1000))],
                   ]

    foto00 = tk.Canvas(frame_p6)
    foto01 = tk.Canvas(frame_p6)
    foto10 = tk.Canvas(frame_p6)
    foto11 = tk.Canvas(frame_p6)

    # Diseño
    frame_p1.pack(side="left", fill="both")
    frame_p2.pack(side="left", fill="both")

    frame_p3.pack(fill="both")
    bienvenida.pack(expand=True, fill="both", ipady=10, padx=10, pady=10)

    frame_p4.pack(expand=True, fill="both")
    p4_imagenes.pack(expand=True, fill="both")
    canvas_imagenes_aplicacion.pack(expand=True, fill="both")
    canvas_imagenes_aplicacion.bind("<Configure>", acomodar_imagen_aplicacion)
    canvas_imagenes_aplicacion.bind("<Enter>", cambiar_imagen_aplicacion)

    p4_continuar.pack(fill="both")
    continuar.pack(expand=True, fill="both", ipady=10, padx=10, pady=10)


    frame_p5.pack(fill="both")
    nombre.pack(expand=True, fill="both", ipady=5)
    email.pack(expand=True, fill="both")
    github.pack(expand=True, fill="both")
    carrera.pack(expand=True, fill="both")
    nombre.bind("<Button-1>", cambiar_hoja_de_vida)
    email.bind("<Button-1>", cambiar_hoja_de_vida)
    github.bind("<Button-1>", cambiar_hoja_de_vida)
    carrera.bind("<Button-1>", cambiar_hoja_de_vida)

    frame_p6.pack(expand=True, fill="both")
    frame_p6.columnconfigure(0, weight=1, uniform="fotos")
    frame_p6.columnconfigure(1, weight=1, uniform="fotos")
    frame_p6.rowconfigure(0, weight=1)
    frame_p6.rowconfigure(1, weight=1)
    foto00.grid(row=0, column=0, sticky="nsew")
    foto01.grid(row=0, column=1, sticky="nsew")
    foto10.grid(row=1, column=0, sticky="nsew")
    foto11.grid(row=1, column=1, sticky="nsew")
    foto00.bind("<Configure>", acomodar_foto1)
    foto01.bind("<Configure>", acomodar_foto2)
    foto10.bind("<Configure>", acomodar_foto3)
    foto11.bind("<Configure>", acomodar_foto4)

    ventana.mainloop()
