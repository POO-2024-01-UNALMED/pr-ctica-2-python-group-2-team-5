from tkinter import messagebox

import tkinter as tk

from iuMain.gestion.FieldFrame import FieldFrame
from gestorAplicacion.administracionHospital.CategoriaHabitacion import CategoriaHabitacion
from gestorAplicacion.servicios.Habitacion import Habitacion
from manejoDeErrores.ErroresAplicacion import DatoDuplicado


def imprimirTitulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text="Contruir Habitación", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def construirHabitacion(hospital, frame):

    def verHabitacion(numero, categoria):
        imprimirTitulo(frame)

        informacionHabitacion = tk.Label(frame, text=f"Informacion de la habitación construida", bg="white", font=("Helvetica", 12))
        informacionHabitacion.pack(pady=10)

        frameHabitacion = tk.Frame(frame, bg="white")
        frameHabitacion.pack(padx=10, pady=10)

        labelNum = tk.Label(frameHabitacion, text="Numero: ", bg="white", font=("Helvetica", 10, "bold"))
        labelNum.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        labelNumHabitacion = tk.Label(frameHabitacion, text=numero, bg="white")
        labelNumHabitacion.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        labelCategoria = tk.Label(frameHabitacion, text="Categoria: ", bg="white", font=("Helvetica", 10, "bold"))
        labelCategoria.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        labelCategoriaHabitacion = tk.Label(frameHabitacion, text=categoria, bg="white")
        labelCategoriaHabitacion.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        labelOcupado = tk.Label(frameHabitacion, text="Estado: ", bg="white", font=("Helvetica", 10, "bold"))
        labelOcupado.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        labelOcupadoHabitacion = tk.Label(frameHabitacion, text="Desocupada", bg="white")
        labelOcupadoHabitacion.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        labelPaciente = tk.Label(frameHabitacion, text="Disponibilidad: ", bg="white", font=("Helvetica", 10, "bold"))
        labelPaciente.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        labelPacienteHabitacion = tk.Label(frameHabitacion, text="Disponible para pacientes", bg="white")
        labelPacienteHabitacion.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        botonRegresar = tk.Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
        botonRegresar.pack()

    def agregarHabitaciones():
        respuesta = tk.messagebox.askyesno("Confirmacion de construcion", "¿Estas seguro de construir esta habitación?")

        if respuesta:
            numero = int(fp.getValue(1))
            categoria = str(fp.getValue(2))

            Error = False

            for i, habitacion in enumerate(hospital.habitaciones):
                if habitacion.numero == numero and habitacion.categoria.name ==categoria:
                    try:
                        raise DatoDuplicado
                    except DatoDuplicado as e:
                        Error = True
                        e.enviarMensaje()

            if Error == False:
                if categoria == CategoriaHabitacion.CAMILLA.name:
                    habitacion_nueva = Habitacion(numero, CategoriaHabitacion.CAMILLA, False, None, 0)
                    hospital.habitaciones.append(habitacion_nueva)

                elif categoria == CategoriaHabitacion.INDIVIDUAL.name:
                    habitacion_nueva = Habitacion(numero, CategoriaHabitacion.INDIVIDUAL, False, None, 0)
                    hospital.habitaciones.append(habitacion_nueva)

                elif categoria == CategoriaHabitacion.DOBLE.name:
                    habitacion_nueva = Habitacion(numero, CategoriaHabitacion.DOBLE, False, None, 0)
                    hospital.habitaciones.append(habitacion_nueva)

                elif categoria == CategoriaHabitacion.OBSERVACION.name:
                    habitacion_nueva = Habitacion(numero, CategoriaHabitacion.OBSERVACION, False, None, 0)
                    hospital.habitaciones.append(habitacion_nueva)

                elif categoria == CategoriaHabitacion.UCI.name:
                    habitacion_nueva = Habitacion(numero, CategoriaHabitacion.UCI, False, None, 0)
                    hospital.habitaciones.append(habitacion_nueva)

                elif categoria == CategoriaHabitacion.UCC.name:
                    habitacion_nueva = Habitacion(numero, CategoriaHabitacion.UCC, False, None, 0)
                    hospital.habitaciones.append(habitacion_nueva)

                messagebox.showinfo("Habitación Construida", "La habitación se ha construido exitosamente")
                verHabitacion(numero, categoria)

        else:
            messagebox.showinfo("Habitación no construida", "No se ha construido la habitación")
            # Se importa aca para evitar una referencia circular
            implementacionDefault(frame)

    def borrarCampos():
        for entry in fp.valores:
            entry.delete(0,tk.END)


    imprimirTitulo(frame)

    criterios = ["Numero", "Tipo de Categoria (CAMILLA, INDIVIDUAL, DOBLE, OBSERVACION, UCI o UCC)"]
    fp = FieldFrame(frame, "Criterio", criterios, "Valor", None, None)
    fp.pack()

    botonesFrame = tk.Frame(frame, bg="white")
    botonesFrame.pack()

    botonGuardar = tk.Button(botonesFrame, text="Guardar", command=agregarHabitaciones)
    botonGuardar.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    botonBorrar = tk.Button(botonesFrame, text="Borrar", command=borrarCampos)
    botonBorrar.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # Funcionalidad para regresar a la ventana principal

    # Se importa aca para evitar una referencia circula
    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

    botonRegresar = tk.Button(frame, text="Regresar",command=lambda: implementacionDefault(frame))
    botonRegresar.pack()