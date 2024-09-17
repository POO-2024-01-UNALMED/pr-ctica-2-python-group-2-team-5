from tkinter import *
from tkinter import ttk, messagebox
from gestorAplicacion.servicios.Formula import Formula
from manejoDeErrores.ErroresAplicacion import *
from iuMain.gestion.FieldFrame import FieldFrame

def mostratTitulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = Label(frame, text="Formular Medicamentos", bg="white", font=("Helvetica", 10, "bold"))
    titulo.pack()

def formulaMedica(hospital, frame):
    pass