import tkinter as tk
from tkinter import messagebox
from tkinter import *
from src.ui_main.funcionalidades import agendar_citas, formula_medica, asignar_habitacion, vacunacion, \
    facturacion
from src.ui_main.gestion.gestion_doctores import agregar_doctor, ver_doctor, eliminar_doctor, agregar_cita
from src.ui_main.gestion.gestion_pacientes import registrar_paciente, administrar_paciente, registrar_enfermedad
from src.ui_main.gestion.gestion_vacunas import registrar_vacuna, ver_vacuna, eliminar_vacuna,agregar_cita_vacuna
from src.ui_main.gestion.gestion_hospital import ver_vacunas, ver_pacientes, ver_doctores, agregar_medicamento, \
    ver_medicamentos, construir_habitacion, destruir_habitacion

def cambiar_contenido(opcion, hospital, frame_implementacion):
    # Limpia el frame
    for widget in frame_implementacion.winfo_children():
        widget.destroy()

    # Ejecuta la funcionalidad
    opciones = {
        "cita": agendar_citas.agendar_citas,
        "formula": formula_medica.formula_medica,
        "habitacion": asignar_habitacion.asignar_habitacion,
        "vacuna": vacunacion.vacunacion,
        "pago": facturacion.facturacion,

        # Gestion hospital
        "ver_vacunas": ver_vacunas.ver_vacunas,
        "ver_pacientes": ver_pacientes.ver_pacientes,
        "ver_doctores": ver_doctores.ver_doctores,
        "construir-habitacion": construir_habitacion.construir_habitacion,
        "destruir-habitacion": destruir_habitacion.destruir_habitacion,
        "agregar-medicamento": agregar_medicamento.agregar_medicamento,
        "ver-medicamentos": ver_medicamentos.ver_medicamentos,

        # Gestion vacunas
        "registrar_vacuna": registrar_vacuna.registrar_vacuna,
        "ver_vacuna": ver_vacuna.ver_vacuna,
        "eliminar_vacuna": eliminar_vacuna.eliminar_vacuna,
        "agregar_cita_vacuna": agregar_cita_vacuna.agregar_cita_vacuna,

        # Gestion Doctores
        "agregar_doctor": agregar_doctor.agregar_doctor,
        "ver_doctor": ver_doctor.ver_doctor,
        "eliminar_doctor": eliminar_doctor.eliminar_doctor,
        "agregar_cita": agregar_cita.agregar_cita,

        # Gestion pacientes
        "registrar-paciente": registrar_paciente.registrar_paciente,
        "administrar-paciente": administrar_paciente.administrar_paciente,
        "registrar-enfermedad": registrar_enfermedad.registrar_enfermedad,

    }

    if opcion in opciones:
        opciones[opcion](hospital, frame_implementacion)


def implementacion_default(frame_implementacion):
    # Limpia el frame
    for widget in frame_implementacion.winfo_children():
        widget.destroy()

    # Ejecuta la implementacion por defecto
    texto_inicial = "Bienvenido al sistema"


    label_inicial = tk.Label(frame_implementacion, text=texto_inicial, bg="white", font=("Helvetica", 14, "bold"), justify="left")
    label_inicial.pack()
    label_inicial.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


def ventana_principal(hospital):
    def acerca_de():
       
        messagebox.showinfo("Acerca de la aplicación.","Los autores de la aplicación son:\nJeronimo Zapata.\nJuan Pablo Vergara.\nHernando Montes.\nManuel Mera.\nSamuel Ramírez.")



    def descripcion_aplicacion():
        
        texto_descripcion = """
        HOSPITAL ANDINO

        Es una aplicacion enfocada en la gestion eficiente de los servicios que ofrece el hospital.

        La aplicacion cuenta con varias funcionalidades:

        1. Citas médicas: Se encarga de agendar citas de oftalmología, odontología o medicina general al paciente
        2. Formulas médicas: Se encarga de generar las formulas con los medicamentos para tratar la enfermedad del paciente.
        3. Asignar habitación: Se encarga de la gestion para asignar una habitacion al paciente en caso de hospitalizacion.
        4. Vacunacion: Se encarga de la gestion para asignar una cita de vacunacion al paciente.
        5. Facturacion: Se encarga de la gestion del pago de los servicios prestados al paciente.
        6. Gestion: Se encarga de procesos como agregar pacientes, agregar vacunas, agregar medicamentos, etc...
        """

        messagebox.showinfo("Descripcion aplicacion", texto_descripcion)
    

    
    ventana = tk.Tk()
    ventana.title("HOSPITAL ANDINO")
    ventana.geometry("800x600+400+40")
    ventana.protocol("WM_DELETE_WINDOW", hospital.serializar())

    titulo = Label(ventana, text="HOSPITAL ANDINO", font=("Verdana", 16))
    titulo.pack(padx=10, pady=10)

    # Menu de opciones (Zona 1)

    menuFrame = Frame(ventana, bd=2, relief="ridge")
    menuFrame.pack(padx=10, pady=10)

    barra_menu = tk.Menu(menuFrame)
    ventana.config(menu=barra_menu)
    

    opcion_archivo = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Archivo", menu=opcion_archivo)
    opcion_archivo.add_command(label="Aplicacion", command=descripcion_aplicacion)

    # Se importa aca para evitar una referencia circular
    from main import ventana_inicial

    opcion_archivo.add_command(label="Salir",
                               command=lambda: [ventana.destroy(), ventana_inicial(hospital)])

    opcion_funcionalidades = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Procesos y Consultas", menu=opcion_funcionalidades)
    opcion_funcionalidades.add_command(label="Agendar citas",
                                       command=lambda: cambiar_contenido("cita", hospital, frame_implementacion))
    opcion_funcionalidades.add_command(label="Generar formula medica",
                                       command=lambda: cambiar_contenido("formula", hospital, frame_implementacion))
    opcion_funcionalidades.add_command(label="Asignar habitacion",
                                       command=lambda: cambiar_contenido("habitacion", hospital, frame_implementacion))
    opcion_funcionalidades.add_command(label="Aplicarse una vacuna",
                                       command=lambda: cambiar_contenido("vacuna", hospital, frame_implementacion))
    opcion_funcionalidades.add_command(label="Facturacion",
                                       command=lambda: cambiar_contenido("pago", hospital, frame_implementacion))
    opcion_funcionalidades.add_separator()

    # Gestión hospital con un submenú
    opcion_gestion_hospital = tk.Menu(opcion_funcionalidades, tearoff=0)
    opcion_funcionalidades.add_cascade(label="Gestión hospital", menu=opcion_gestion_hospital)
    opcion_gestion_hospital.add_command(label="Vacunas del hospital",
                                        command=lambda: cambiar_contenido("ver_vacunas", hospital,
                                                                          frame_implementacion))
    opcion_gestion_hospital.add_command(label="Pacientes del hospital",
                                        command=lambda: cambiar_contenido("ver_pacientes", hospital,
                                                                          frame_implementacion))
    opcion_gestion_hospital.add_command(label="Doctores del hospital",
                                        command=lambda: cambiar_contenido("ver_doctores", hospital,
                                                                          frame_implementacion))
    opcion_gestion_hospital.add_command(label="Construir habitación",
                                        command=lambda: cambiar_contenido("construir-habitacion", hospital,
                                                                          frame_implementacion))
    opcion_gestion_hospital.add_command(label="Destruir habitación",
                                        command=lambda: cambiar_contenido("destruir-habitacion", hospital,
                                                                          frame_implementacion))
    opcion_gestion_hospital.add_command(label="Agregar medicamento",
                                        command=lambda: cambiar_contenido("agregar-medicamento", hospital,
                                                                          frame_implementacion))
    opcion_gestion_hospital.add_command(label="Ver medicamentos",
                                        command=lambda: cambiar_contenido("ver-medicamentos", hospital,
                                                                          frame_implementacion))

    # Gestion vacunas con un submenú
    opcion_gestion_vacuna = tk.Menu(opcion_funcionalidades, tearoff=0)
    opcion_funcionalidades.add_cascade(label="Gestión vacunas", menu=opcion_gestion_vacuna)
    opcion_gestion_vacuna.add_command(label="Registrar Vacuna",
                                      command=lambda: cambiar_contenido("registrar_vacuna", hospital,
                                                                        frame_implementacion))
    opcion_gestion_vacuna.add_command(label="Ver vacuna",
                                      command=lambda: cambiar_contenido("ver_vacuna", hospital, frame_implementacion))
    opcion_gestion_vacuna.add_command(label="Eliminar vacuna",
                                      command=lambda: cambiar_contenido("eliminar_vacuna", hospital,
                                                                        frame_implementacion))
    opcion_gestion_vacuna.add_command(label="Agregar Cita a vacuna",
                                      command=lambda: cambiar_contenido("agregar_cita_vacuna", hospital,
                                                                        frame_implementacion))

    # Gestión doctores con un submenú
    opcion_gestion_doctores = tk.Menu(opcion_funcionalidades, tearoff=0)
    opcion_funcionalidades.add_cascade(label="Gestión doctores", menu=opcion_gestion_doctores)
    opcion_gestion_doctores.add_command(label="Agregar doctor",
                                        command=lambda: cambiar_contenido("agregar_doctor", hospital,
                                                                          frame_implementacion))
    opcion_gestion_doctores.add_command(label="Ver doctor",
                                        command=lambda: cambiar_contenido("ver_doctor", hospital, frame_implementacion))
    opcion_gestion_doctores.add_command(label="Eliminar doctor",
                                        command=lambda: cambiar_contenido("eliminar_doctor", hospital,
                                                                          frame_implementacion))
    opcion_gestion_doctores.add_command(label="Agregar cita",
                                        command=lambda: cambiar_contenido("agregar_cita", hospital,
                                                                          frame_implementacion))

    # Gestion pacientes submenu
    opcion_gestion_pacientes = tk.Menu(opcion_funcionalidades, tearoff=0)
    opcion_funcionalidades.add_cascade(label="Gestión pacientes", menu=opcion_gestion_pacientes)
    opcion_gestion_pacientes.add_command(label="Registrar paciente",
                                         command=lambda: cambiar_contenido("registrar-paciente", hospital,
                                                                           frame_implementacion))
    opcion_gestion_pacientes.add_command(label="Administrar paciente",
                                         command=lambda: cambiar_contenido("administrar-paciente", hospital,
                                                                           frame_implementacion))
    opcion_gestion_pacientes.add_command(label="Registrar enfermedad",
                                         command=lambda: cambiar_contenido("registrar-enfermedad", hospital,
                                                                           frame_implementacion))

    opcion_ayuda = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Ayuda", menu=opcion_ayuda)
    opcion_ayuda.add_command(label="Acerca de", command=acerca_de)

    # Implementacion de las funcionalidades (Zona 2)

    frame_implementacion = tk.Frame(ventana)
    frame_implementacion.pack(fill=tk.BOTH, expand=True)
    frame_implementacion.configure(bg="white")

    implementacion_default(frame_implementacion)

    ventana.mainloop()
