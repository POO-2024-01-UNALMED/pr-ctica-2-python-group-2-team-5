import tkinter as tk
from tkinter import messagebox

from gestorAplicacion.servicios.CitaVacuna import CitaVacuna
from manejoDeErrores.ErroresAplicacion import DatosFalsos, TipoIncorrecto, CampoVacio


def imprimirTtiulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text="Agregar cita a vacuna", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)
def agregarCitaVacuna(hospital, frame):

    def verCitasVacuna(vacuna):
        imprimirTtiulo(frame)
        infoHistorial = tk.Label(frame, text=f"Agenda de la vacuna {vacuna.nombre} - Tipo: {vacuna.tipo}",
                                  bg="white", font=("Helvetica", 12))
        infoHistorial.pack(pady=10)

        agendaVacunaText = tk.Text(frame, bg="white", font=("Helvetica", 14))
        agendaVacunaText.pack(fill=tk.BOTH, expand=True)

        # Mostrar todas las vacunas que tiene el usuario


        for cita in vacuna.agenda:
            fecha = cita.fecha

            texto_vacuna = f"~~ {fecha}\n\n"

            # Insertar el texto de la vacuna en el widget Text
            agendaVacunaText.insert(tk.END, texto_vacuna)

        agendaVacunaText.config(padx=30, pady=5)
        agendaVacunaText.config(highlightthickness=5, highlightbackground="#4D5BE4")
        agendaVacunaText.config(state="disabled")

        # Se importa aca para evitar una referencia circula
        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        botonRegresar = tk.Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
        botonRegresar.pack()

    def agregarFechaVacuna(vacuna):
        def confirmarCita():
            respuesta = tk.messagebox.askyesno("Confirmar cita", "¿Estas seguro de agregar esta cita?")
            if respuesta:
                fecha = str(fp2.getValue(1))

                cita = CitaVacuna(fecha, None, vacuna)
                vacuna.agenda.append(cita)
                messagebox.showinfo("Cita agregada", "La cita se ha agregado exitosamente a esta vacuna")
                verCitasVacuna(vacuna)
            else:
                messagebox.showinfo("Cita cancelada", "La cita no ha sido agregada")
                # Se importa aca para evitar una referencia circula
                from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                implementacionDefault(frame)

        imprimirTtiulo(frame)

        infoDoctor = tk.Label(frame, text=f"{vacuna.nombre} - Tipo: {vacuna.tipo}", bg="white",font=("Helvetica", 12))
        infoDoctor.pack(pady=10)

        criterios = ["Fecha de la cita (ejm: 25 de Junio, 10:00 am)"]
        fp2 = FieldFrame(frame, "", criterios, "", None, None,25)
        fp2.pack()

        botonGuardar = tk.Button(frame, text="Guardar", command=lambda: confirmarCita())
        botonGuardar.pack(pady=5)

        # Se importa aca para evitar una referencia circula
        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        botonRegresar = tk.Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
        botonRegresar.pack()


    def busquedaVacuna():
        nombre = fp.getValue(1)

        if len(nombre) != 0:
            try:
                if nombre.isdigit():
                    raise ValueError
                else:
                    vacuna = hospital.buscarVacuna(nombre)
                    if vacuna is not None:
                        agregarFechaVacuna(vacuna)
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

    imprimirTtiulo(frame)
    tituloIngresoNombre = tk.Label(frame, text="Ingrese el nombre de la vacuna a ver:", bg="white", font=("Helvetica", 10, "bold"))
    tituloIngresoNombre.pack()

    criterios = ["Nombre"]
    fp = FieldFrame(frame, "", criterios, "", None, None)
    fp.pack()

    botonBuscarVacuna = tk.Button(frame, text="Buscar", command=busquedaVacuna, font=("Helvetica", 10, "bold"))
    botonBuscarVacuna.pack(pady=5)

    # Se importa aca para evitar una referencia circula
    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

    botonRegresar = tk.Button(frame, text="Regresar", command=lambda: implementacionDefault(frame),font=("Helvetica", 10, "bold"))
    botonRegresar.pack(pady=20)