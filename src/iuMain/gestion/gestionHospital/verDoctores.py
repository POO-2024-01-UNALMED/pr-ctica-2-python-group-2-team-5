import tkinter as tk
from iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault


def imprimirTitulo(frame_implementacion):
    # Limpia el frame
    for item in frame_implementacion.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame_implementacion, text="Ver doctores del hospital", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def verDoctores(hospital, frame_implementacion):
    imprimirTitulo(frame_implementacion)

    tituloVerDoctores = tk.Label(frame_implementacion, text="Estos son todos los doctores presentes en el hospital (Recuerda, si es necesario, desplazarse hacia abajo)",
    bg="white",font=("Helvetica", 10, "bold"))
    tituloVerDoctores.pack(pady=10)

    doctoresText = tk.Text(frame_implementacion, bg="white", font=("Helvetica", 14))
    doctoresText.pack(fill=tk.BOTH,expand=True)

    # Mostrar todas las vacunas presentes en el hospital
    for doctor in hospital.lista_doctores:
        nombre = doctor.nombre
        cedula = doctor.cedula
        especialidad = doctor.especialidad
        tipo_eps= doctor.tipoEps
        fechas=[]
        for cita in doctor.agenda:
            fechas.append(cita.fecha)
        agenda = ",".join(fechas)

        textoDoctor = f"Nombre: {nombre}\nCedula: {cedula}\nEspecialidad: {especialidad}\nTipo de eps: {tipo_eps}\nAgenda: {agenda}\n\n"

        # Insertar el texto de la vacuna en el widget Text
        doctoresText.insert(tk.END, textoDoctor)

    doctoresText.config(padx=30)
    doctoresText.config(highlightthickness=5, highlightbackground="#4D5BE4")
    doctoresText.config(state="disabled")


    botonRegresar = tk.Button(frame_implementacion, text="Regresar",
                               command=lambda: implementacionDefault(frame_implementacion),
                               font=("Helvetica", 10, "bold"))
    botonRegresar.pack(pady=20)