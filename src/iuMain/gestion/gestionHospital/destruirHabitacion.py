from tkinter import messagebox

import tkinter as tk

from iuMain.gestion.FieldFrame import FieldFrame
from manejoDeErrores.ErroresAplicacion import DatosFalsos, CampoVacio


def imprimirTitulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text="Destruir habitacion", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def destruirHabitacion(hospital, frame):

    def destruccionHabitacion(habitacion):
        respuesta = tk.messagebox.askyesno("Confirmar destrucción", "¿Estas seguro de destruir esta habitacion?")
        if respuesta:
            hospital.habitaciones.remove(habitacion)
            messagebox.showinfo("Habitación Destruida", "La habitación se ha destruido exitosamente")
            # Se importa aca para evitar una referencia circula
            from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

            implementacionDefault(frame)
        else:
            messagebox.showinfo("Destrución cancelada", "La habitacion no ha sido eliminado")
            # Se importa aca para evitar una referencia circula
            from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
            implementacionDefault(frame)

    def elementosHabitacion(habitacion):
        imprimirTitulo(frame)
        infoDoctor = tk.Label(frame, text=f"Información de la Habitacion", bg="white", font=("Helvetica", 12))
        infoDoctor.pack(pady=10)

        criterios = ["Numero", "Tipo de Categoria (CAMILLA, INDIVIDUAL, DOBLE, OBSERVACION, UCI o UCC)","Estado","Paciente Asignado", "Disas Establecido el Paciente"]
        if habitacion.ocupada==False:
            fp = FieldFrame(frame, "Criterio", criterios, "Valor", [habitacion.numero, habitacion.categoria.name,"Desocupada","Libre", habitacion.dias],[False, False, False, False, False])
            fp.pack()
            botonEliminar = tk.Button(frame, text="Eliminar", command=lambda: destruccionHabitacion(habitacion))
            botonEliminar.pack(pady=10)
        else:
            fp = FieldFrame(frame, "Criterio", criterios, "Valor",[habitacion.numero, habitacion.categoria.name, "Ocupada", habitacion.paciente.nombre,habitacion.dias], [False, False, False, False, False])
            fp.pack()

        # Se importa aca para evitar una referencia circula
        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        boton_regresar = tk.Button(frame, text="Regresar",command=lambda: implementacionDefault(frame))
        boton_regresar.pack(pady=10)

    def busquedaHabitacion():
        numero = fp.getValue(1)
        categoria = fp.getValue(2)

        if len(numero) != 0 and categoria != "":
            for i, habitacion in enumerate(hospital.habitaciones):
                if habitacion.numero == int(numero) and habitacion.categoria.name == categoria:
                    if habitacion:
                        elementosHabitacion(habitacion)
                    else:
                        try:
                            raise DatosFalsos
                        except DatosFalsos as e:
                            e.enviarMensaje()
        else:
            try:
                raise CampoVacio()
            except CampoVacio as e:
                e.enviarMensaje()

    imprimirTitulo(frame)

    tituloIngresoNumero = tk.Label(frame, text="Ingrese el numero y categoria de la habitacion a destruir:", bg="white",font=("Helvetica", 10, "bold"))
    tituloIngresoNumero.pack()


    criterios = ["Numero", "Tipo de Categoria (CAMILLA, INDIVIDUAL, DOBLE, OBSERVACION, UCI o UCC)"]
    fp = FieldFrame(frame, "", criterios, "", None, None)
    fp.pack()

    botonBuscarDoctor = tk.Button(frame, text="Buscar", command=busquedaHabitacion)
    botonBuscarDoctor.pack(pady=5)

    # Se importa aca para evitar una referencia circula
    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

    botonRegresar = tk.Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
    botonRegresar.pack()