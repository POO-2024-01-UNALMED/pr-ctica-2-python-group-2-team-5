import tkinter as tk

from iuMain.interfazGrafica.VentanaPrincipalDelUsuario import FieldFrame
from manejoDeErrores.ErroresAplicacion import DatosFalsos, TipoIncorrecto, CampoVacio
from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault


def imprimirTitulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text="Ver doctor", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def verDoctor(hospital, frame):

    def elementosDoctor(doctor):
        imprimirTitulo(frame)
        infoDoctor = tk.Label(frame, text=f"Informacion del doctor", bg="white", font=("Helvetica", 12))
        infoDoctor.pack(pady=10)

        criterios = ["Cedula", "Nombre","Tipo de eps","Especialidad"]

        fp = FieldFrame(frame, "Criterio", criterios, "Valor",[doctor.cedula,
        doctor.nombre,doctor.tipoEps,doctor.especialidad],[False,False,False,False])
        fp.pack()

        botonRegresar = tk.Button(frame, text="Regresar",command=lambda: implementacionDefault(frame))
        botonRegresar.pack(pady=20)

    def busquedaDoctor():
        cedula = fp.getValue(1)

        if len(cedula) != 0:
            try:
                doctor = hospital.buscarDoctor(int(cedula))
                if doctor is not None:
                    elementosDoctor(doctor)
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

    tituloIngresoCedula = tk.Label(frame, text="Ingrese la cedula del doctor a ver:", bg="white",font=("Helvetica", 10, "bold"))
    tituloIngresoCedula.pack()

    criterios = ["Cedula"]
    fp = FieldFrame(frame, "", criterios, "", None, None)
    fp.pack()

    botonBuscarDoctor = tk.Button(frame, text="Buscar", command=busquedaDoctor)
    botonBuscarDoctor.pack(pady=5)


    botonRegresar = tk.Button(frame, text="Regresar",command=lambda: implementacionDefault(frame))
    botonRegresar.pack()