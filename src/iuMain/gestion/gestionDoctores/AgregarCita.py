from tkinter import messagebox
import tkinter as tk

from src.gestorAplicacion.administracionHospital.Hospital import Hospital
from src.gestorAplicacion.personas.Doctor import Doctor
from src.gestorAplicacion.servicios.Cita import Cita
from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import fieldFrame, FieldFrame, implementacionDefault
from src.manejoDeErrores.ErroresAplicacion import DatosFalsos, TipoIncorrecto, CampoVacio


def imprimirTitulo(frame):
    for item in frame.winfo_children():
        item.destroy()

    titulo = tk.label(frame, text="Agregar Cita", bg="White", font=("Helvetica", 20, "bold"))
    titulo.pack(pady=20)


def agregarCita(hospital, frame):
    def verCitaDoctor(doctor):

        imprimirTitulo(frame)

        infoDoctor = tk.label(frame, text=f"Citas en la agenda de {doctor.nombre} - CC {doctor.cedula}", bg="White",
                              font=("Helvetica", 12, "bold"))
        infoDoctor.pack(pady=10)

        agendaText = tk.Text(frame, bg="white", font=("Helvetica", 14))
        agendaText.pack(fill=tk.BOTH, expand=True)

        for cita in doctor.agendaDoctor:
            fecha = cita.fecha

            textoAgenda = f"Fecha: {fecha} \n \n"

            agendaText.insert(tk.END, textoAgenda)

        agendaText.config(padx=30)
        agendaText.config(highlightbackground="#4D5BE4", highlightthickness=5)
        agendaText.config(state="disabled")

        botonRegresar = tk.Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
        botonRegresar.pack()

    def agregarFechaCita(doctor):
        def confirmarCita():
            respuesta = tk.messagebox.askyesno("Confirmar cita", "¿Esta seguro de agregar esta cita?")
            if respuesta:
                fecha = str(fp2.getValue(1))

                cita = Cita(None, doctor, fecha)
                doctor.agendaDoctor.append(cita)

                messagebox.showinfo("Cita Agregado", "Cita agregada Correctamente")

                verCitaDoctor(doctor)
            else:
                messagebox.showinfo("Cita cancelada", "La cita no ha sido agregada")
                implementacionDefault(frame)

        imprimirTitulo(frame)

        infoDoctor = tk.Label(frame, text=f"{doctor.getNombre()} - CC: {doctor.cedula}", bg="White",
                              font=("Helvetica", 12))
        infoDoctor.pack(pady=10)

        criterios = ["Fecha de la cita. Por Ejemplo: '17 de Noviembre, 11:00 am"]

        fp2 = FieldFrame(frame, "", criterios, "", None, None)
        fp2.pack()

        botonGuardar = tk.Button(frame, text="Guardar", command=confirmarCita)

        botonRegresar = tk.Button(frame, text="Regresar", command=implementacionDefault(frame))
        botonGuardar.pack()

        def busquedaDoctor():
            cedula = fp1.getValue(1)

            if len(cedula) != 0:

                try:
                    doctor = hospital.buscarDoctor(cedula)
                    if doctor is not None:
                        agregarCita(doctor)


                    else:
                        raise DatosFalsos
                except DatosFalsos as e:
                    e.enviarMensaje()
                except ValueError:
                    TipoIncorrecto().enviarMensaje()
            else:
                try:
                    raise CampoVacio()
                except CampoVacio as e:
                    e.enviarMensaje()

        imprimirTitulo(frame)

        tituloIngresoCedula = tk.Label(frame, text="Ingrese la cedula del doctor al que se le agregara la cita:",
                                       bg="white", font=("Helvetica", 10, "bold"))
        tituloIngresoCedula.pack()

        criterios = ["Cedula"]

        fp1 = FieldFrame(frame, "", criterios, "", None, None)
        fp1.pack()

        botonBuscarDoctor = tk.Button(frame, text="Buscar", command=busquedaDoctor)
        botonBuscarDoctor.pack(pady=5)

        botonRegresar = tk.Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
        botonRegresar.pack()