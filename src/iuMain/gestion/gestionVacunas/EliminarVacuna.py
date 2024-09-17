from tkinter import messagebox

import tkinter as tk

from iuMain.gestion.FieldFrame import FieldFrame
from manejoDeErrores.ErroresAplicacion import DatosFalsos, TipoIncorrecto, CampoVacio


def imprimirTitulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text="Eliminar vacuna", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def eliminarVacuna(hospital, frame):

    def eliminacionVacuna(vacuna):
        respuesta = tk.messagebox.askyesno("Confirmar eliminacion", "¿Estas seguro de eliminar esta vacuna?")
        if respuesta:
            hospital.listaVacunas.remove(vacuna)
            messagebox.showinfo("Vacuna eliminada", "La vacuna se ha eliminado exitosamente")
            # Se importa aca para evitar una referencia circula
            from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

            implementacionDefault(frame)
        else:
            messagebox.showinfo("Eliminacion cancelada", "La vacuna no ha sido eliminada")
            # Se importa aca para evitar una referencia circula
            from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
            implementacionDefault(frame)

    def elementosVacuna(vacuna):
        imprimirTitulo(frame)
        infoVacuna = tk.Label(frame, text=f"Información de la vacuna", bg="white", font=("Helvetica", 12))
        infoVacuna.pack(pady=10)
        criterios = ["Nombre de la vacuna", "Tipo de vacuna", "Eps a las que pertenece", "Precio"]
        cadenaTipoEps = ",".join(vacuna.tipoEps)

        fp = FieldFrame(frame, "Criterio", criterios, "Valor", [vacuna.nombre,vacuna.tipo,
        cadenaTipoEps,vacuna.precio],[False, False, False, False], 34)

        fp.pack()

        #Boton de eliminar

        botonEliminar = tk.Button(frame, text="Eliminar", command=lambda: eliminacionVacuna(vacuna),font=("Helvetica", 10, "bold"))
        botonEliminar.pack(pady=10)

        # Se importa aca para evitar una referencia circula
        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        #Boton de regresar
        botonRegresar = tk.Button(frame, text="Regresar",
                                   command=lambda: implementacionDefault(frame),
                                   font=("Helvetica", 10, "bold"))
        botonRegresar.pack(pady=20)



    def busquedaVacuna():
        nombre= fp.getValue(1)

        if len(nombre) != 0:
            try:
                if nombre.isdigit():
                    raise ValueError
                else:
                    vacuna = hospital.buscarVacuna(nombre)
                    if vacuna is not None:
                        elementosVacuna(vacuna)
                    else:
                        raise DatosFalsos
            except ValueError:
                TipoIncorrecto().enviarMensaje()
            except DatosFalsos as e:
                e.enviarMensaje()

        else:
            try:
                raise CampoVacio()
            except CampoVacio as e:
                e.enviarMensaje()


    imprimirTitulo(frame)

    tituloIngresoCedula = tk.Label(frame, text="Ingrese el nombre de la vacuna a eliminar:", bg="white",
                                     font=("Helvetica", 10, "bold"))
    tituloIngresoCedula.pack()

    criterios = ["Nombre"]
    fp = FieldFrame(frame, "", criterios, "", None, None)
    fp.pack()

    botonBuscarDoctor = tk.Button(frame, text="Buscar", command=busquedaVacuna,font=("Helvetica", 10, "bold"))
    botonBuscarDoctor.pack(pady=5)

    # Se importa aca para evitar una referencia circula
    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

    botonRegresar = tk.Button(frame, text="Regresar", command=lambda: implementacionDefault(frame),font=("Helvetica", 10, "bold"))
    botonRegresar.pack()