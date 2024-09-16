import tkinter as tk

from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault


def imprimirTitulo(frame_implementacion):
    # Limpia el frame
    for item in frame_implementacion.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame_implementacion, text="Ver pacientes del hospital", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def verPacientes(hospital, frame_implementacion):
    imprimirTitulo(frame_implementacion)

    tituloVerPacientes = tk.Label(frame_implementacion, text="Estos son todos los pacientes presentes en el hospital (Recuerda, si es necesario, desplazarse hacia abajo)",
    bg="white",font=("Helvetica", 10, "bold"))
    tituloVerPacientes.pack(pady=10)

    pacientesText = tk.Text(frame_implementacion, bg="white", font=("Helvetica", 14))
    pacientesText.pack(fill=tk.BOTH,expand=True)

    # Mostrar todas las vacunas presentes en el hospital
    for paciente in hospital.listaPacientes:
        nombre = paciente.nombre
        cedula = paciente.cedula
        tipoEps=paciente.tipoEps

        textoPaciente = f"Nombre: {nombre}\nCedula: {cedula}\nTipo eps: {tipoEps}\n\n"

        # Insertar el texto de la vacuna en el widget Text
        pacientesText.insert(tk.END, textoPaciente)

    pacientesText.config(padx=30)
    pacientesText.config(highlightthickness=5, highlightbackground="#4D5BE4")
    pacientesText.config(state="disabled")


    botonRegresar = tk.Button(frame_implementacion, text="Regresar",
                               command=lambda: implementacionDefault(frame_implementacion),
                               font=("Helvetica", 10, "bold"))
    botonRegresar.pack(pady=20)