from tkinter import *
from tkinter import ttk, messagebox
from src.gestorAplicacion.servicios.Formula import Formula
from src.manejoDeErrores.ErroresAplicacion import *
from src.iuMain.gestion.FieldFrame import FieldFrame

def mostratTitulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = Label(frame, text="Formular Medicamentos", bg="white", font=("Helvetica", 10, "bold"))
    titulo.pack()

def formulaMedica(hospital, frame):
    def doctorFormula(paciente):
        def habilitarDoctor(event):
            global valorPorDefecto1
            indiceSeleccionado = cboxEnfermedades.current()
            objetoSeleccionado = paciente.HISTORIACLINICA.enfermedades[indiceSeleccionado]
            valorPorDefecto1 = objetoSeleccionado.nombre + objetoSeleccionado.tipologia
            eleccion = cboxEnfermedades.get()
            listaDocEnf = paciente.HISTORIACLINICA.buscarCitaDoc(objetoSeleccionado.especialidad, hospital)
            cboxElegirDoctor.set("")
            if len(listaDocEnf) != 0:
                if eleccion:
                    cboxElegirDoctor['state'] = 'readonly'
                    cboxElegirDoctor['values'] = listaDocEnf
                else:
                    cboxElegirDoctor['state'] = 'disabled'

                indiceEnfermedad = cboxEnfermedades.current()
                enfObjeto = paciente.HISTORIACLINICA.enfermedades[indiceEnfermedad]

                if len(paciente.HISTORIACLINICA.buscarCitaDoc(enfObjeto.especialidad, hospital)) != 0:
                    formulaPaciente = Formula(paciente)
                    for widget in frame.winfo_children():
                        if isinstance(widget, Button) and widget.cget("text") == "Seleccionar medicamentos":
                            widget.destroy()

                    # Crear nuevo botón.
                    botonSeleccionar = Button(frame, text="Seleccionar medicamentos", command=lambda: seleccionMedicamentos(enfObjeto, formulaPaciente, cboxElegirDoctor.get()))
                    botonSeleccionar.pack()

                else:
                    try:
                        raise SinCitaPrevia()
                    except SinCitaPrevia as s:
                        s.enviarMensaje()
                        # Se importa aca para evitar una referencia circular
                        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                        implementacionDefault(frame)
            else:
                try:
                    raise SinCitaPrevia()
                except SinCitaPrevia as s:
                    s.enviarMensaje()
                    cboxElegirDoctor['state'] = 'disabled'
                    # Se importa aca para evitar una referencia circular
                    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
                    implementacionDefault(frame)

        mostratTitulo(frame)
        ## TERMINAR FUNCIONALIDAD FORMULA MÉDICA ##
        ## LINEA 67 ARCHIVO PYTHON ##