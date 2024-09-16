import tkinter as tk

from iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault


def imprimirTitulo(frame_implementacion):
    # Limpia el frame
    for item in frame_implementacion.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame_implementacion, text="Ver vacunas del hospital", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def verVacunas(hospital, frame_implementacion):
    imprimirTitulo(frame_implementacion)

    tituloVerVacunas = tk.Label(frame_implementacion, text="Estas son todas las vacunas presentes en el hospital (Recuerda, si es necesario, desplazarse hacia abajo)",
    bg="white",font=("Helvetica", 10, "bold"))
    tituloVerVacunas.pack(pady=10)

    vacunasText = tk.Text(frame_implementacion, bg="white", font=("Helvetica", 14))
    vacunasText.pack(fill=tk.BOTH,expand=True)

    # Mostrar todas las vacunas presentes en el hospital
    for vacuna in hospital.listaVacunas:
        nombre = vacuna.nombre
        tipo = vacuna.tipo
        tipoEps =",".join(vacuna.tipoEps)
        fechas=[]
        for cita in vacuna.agenda:
            fechas.append(cita.fecha)
        agenda = ",".join(fechas)
        precio = vacuna.precio

        textoVacuna = f"Nombre: {nombre}\nTipo: {tipo}\nPrecio: {precio}\nEps a la que pertenece: {tipoEps}\nAgenda: {agenda}\n\n"

        # Insertar el texto de la vacuna en el widget Text
        vacunasText.insert(tk.END, textoVacuna)

    vacunasText.config(padx=30)
    vacunasText.config(highlightthickness=5, highlightbackground="#4D5BE4")
    vacunasText.config(state="disabled")


    botonRegresar = tk.Button(frame_implementacion, text="Regresar",
                               command=lambda: implementacionDefault(frame_implementacion),
                               font=("Helvetica", 10, "bold"))
    botonRegresar.pack(pady=20)