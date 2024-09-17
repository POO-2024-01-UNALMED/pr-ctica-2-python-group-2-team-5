from tkinter import messagebox, ttk


import tkinter as tk

from iuMain.gestion.FieldFrame import FieldFrame
from src.gestorAplicacion.administracionHospital.Enfermedad import Enfermedad
from src.gestorAplicacion.administracionHospital.Medicamento import Medicamento
from src.manejoDeErrores.ErroresAplicacion import TipoIncorrecto, DatoDuplicado, CampoVacio


def imprimirTitulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text="Agregar Medicamento", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)


def agregarMedicamento(hospital, frame):
    def agregarListaMedicamentos():
        nombre = fp.getValue(1)
        descripcion = fp.getValue(2)
        cantidad = fp.getValue(3)
        precio = fp.getValue(4)
        error = False
        if nombre != "" and descripcion != "" and cantidad != "" and precio != "" and combo_enfermedades.get() != "":
            try:
                if nombre.isdigit():
                    error = True
                    raise ValueError
                else:
                    nombre = str(nombre)
            except ValueError:
                TipoIncorrecto("en el campo nombre").enviarMensaje()
            try:
                if descripcion.isdigit():
                    error = True
                    raise ValueError
                else:
                    descripcion = str(descripcion)
            except ValueError:
                TipoIncorrecto("en el campo descripcion").enviarMensaje()
            try:
                cantidad = int(cantidad)
                if cantidad == 0:
                    error = True
                    raise ValueError
            except ValueError:
                TipoIncorrecto("en el campo cantidad").enviarMensaje()
            try:
                precio = float(precio)
                if precio == 0:
                    error = True
                    raise ValueError
            except ValueError:
                TipoIncorrecto("en el campo precio").enviarMensaje()
            try:
                for med in hospital.lista_medicamentos:
                    if nombre == med.nombre:
                        error = True
                        raise DatoDuplicado()
            except DatoDuplicado as e:
                e.enviarMensaje()
        else:
            try:
                raise CampoVacio()
            except CampoVacio as e:
                e.enviarMensaje()
                error = True
        if error is not True:
            respuesta = tk.messagebox.askyesno("Confirmacion de medicamento", "¿Estas seguro de agregar este medicamento?")
            if respuesta:
                indiceEnfermedad = combo_enfermedades.current()
                enf_objeto = Enfermedad.getEnfermedadesRegistradas()[indiceEnfermedad]

                medicamento = Medicamento(nombre, descripcion, enf_objeto, cantidad, precio)
                hospital.lista_medicamentos.append(medicamento)
                messagebox.showinfo("Medicamento agregado", "El medicamento se ha agregado exitosamente")
                # Se importa aca para evitar una referencia circular
                implementacionDefault(frame)
            else:
                messagebox.showinfo("Medicamento no agregado", "No se ha agregado el medicamento")
                # Se importa aca para evitar una referencia circular
                implementacionDefault(frame)

    def borrarCampos():
        for entry in fp.valores:
            entry.delete(0, tk.END)

    imprimirTitulo(frame)

    criterios = ["Nombre", "Descripcion", "Cantidad", "Precio"]
    fp = FieldFrame(frame, "Criterio", criterios, "Valor", None, None)
    fp.pack()
    enf_frame = tk.Frame(frame, bg="white")
    enf_frame.pack()
    label_enf = tk.Label(enf_frame, text="Enfermedad que trata", bg="white", font=("Helvetica", 10, "bold"))
    label_enf.grid(row=0, column=0, sticky="w")
    combo_enfermedades = ttk.Combobox(enf_frame, values=Enfermedad.getEnfermedadesRegistradas(), state="readonly")
    combo_enfermedades.grid(row=0, column=1, sticky="w")
    boton_agregar = tk.Button(frame, text="Guardar", command=agregarListaMedicamentos)
    boton_agregar.pack(pady=10)
    boton_borrar = tk.Button(frame, text="Borrar", command=borrarCampos)
    boton_borrar.pack(pady=10)

    # Funcionalidad para regresar a la ventana principal

    # Se importa aca para evitar una referencia circula
    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

    boton_regresar = tk.Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
    boton_regresar.pack(pady=10)
