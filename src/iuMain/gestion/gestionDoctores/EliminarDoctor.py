from tkinter import messagebox

from iuMain.gestion.FieldFrame import FieldFrame
from src.manejoDeErrores.ErroresAplicacion import DatosFalsos, TipoIncorrecto, CampoVacio
import tkinter as tk

def imprimirTitulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text="Eliminar doctor", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def eliminarDoctor(hospital, frame):

    def eliminacionDoctor(doctor):
        respuesta = tk.messagebox.askyesno("Confirmar eliminacion", "¿Estas seguro de eliminar este doctor?")
        if respuesta:
            hospital.listaDoctores.remove(doctor)
            messagebox.showinfo("Doctor eliminado", "El doctor se ha eliminado exitosamente")
            # Se importa aca para evitar una referencia circula
            from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

            implementacionDefault(frame)
        else:
            messagebox.showinfo("Eliminacion cancelada", "El doctor no ha sido eliminado")
            # Se importa aca para evitar una referencia circula
            from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
            implementacionDefault(frame)

    def elementosDoctor(doctor):
        imprimirTitulo(frame)
        info_doctor = tk.Label(frame, text=f"Información del doctor", bg="white", font=("Helvetica", 12))
        info_doctor.pack(pady=10)

        criterios = ["Cedula", "Nombre","Tipo de eps","Especialidad"]

        fp = FieldFrame(frame, "Criterio", criterios, "Valor",[doctor.cedula,
        doctor.nombre,doctor.tipoEps,doctor.especialidad],[False,False,False,False])
        fp.pack()

        botonEliminar = tk.Button(frame, text="Eliminar", command=lambda:eliminacionDoctor(doctor))
        botonEliminar.pack(pady=10)
        # Se importa aca para evitar una referencia circula
        from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

        botonRegresar = tk.Button(frame, text="Regresar",command=lambda: implementacionDefault(frame))
        botonRegresar.pack(pady=10)

    def busquedaDoctor():
        cedula = fp.getValue(1)

        if len(cedula) != 0:
            try:
                doctor = hospital.buscar_doctor(int(cedula))
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

    tituloIngresoCedula = tk.Label(frame, text="Ingrese la cedula del doctor a eliminar:", bg="white",font=("Helvetica", 10, "bold"))
    tituloIngresoCedula.pack()

    criterios = ["Cedula"]
    fp = FieldFrame(frame, "", criterios, "", None, None)
    fp.pack()

    botonBuscarDoctor = tk.Button(frame, text="Buscar", command=busquedaDoctor)
    botonBuscarDoctor.pack(pady=5)

    # Se importa aca para evitar una referencia circula
    from src.iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault

    botonRegresar = tk.Button(frame, text="Regresar", command=lambda: implementacionDefault(frame))
    botonRegresar.pack()