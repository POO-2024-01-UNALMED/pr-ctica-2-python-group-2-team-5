import tkinter as tk

from iuMain.interfazGrafica.VentanaPrincipalDelUsuario import implementacionDefault
from manejoDeErrores.ErroresAplicacion import DatosFalsos, TipoIncorrecto, CampoVacio


def imprimirTitulo(frame_implementacion):
    # Limpia el frame
    for item in frame_implementacion.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame_implementacion, text="Ver una vacuna", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def verVacuna(hospital, frame_implementacion):

    def elementosVacuna(vacuna):
        imprimirTitulo(frame_implementacion)
        criterios = ["Nombre de la vacuna", "Tipo de vacuna",
                     "Eps a las que pertenece",
                     "Precio"]
        cadenaTipoEps=",".join(vacuna.tipo_eps)

        fp = FieldFrame(frame_implementacion, "Criterio", criterios, "Valor",[vacuna.nombre,
        vacuna.tipo,cadenaTipoEps,vacuna.precio],[False,False,False,False],34)
        fp.pack()

        botonRegresar = tk.Button(frame_implementacion, text="Regresar", command=lambda: implementacion_default(frame_implementacion),font=("Helvetica", 10, "bold"))
        botonRegresar.pack(pady=20)


    def busquedaVacuna():
        nombre = fp.getValue(1)

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

    imprimirTitulo(frame_implementacion)
    tituloIngresoNombre = tk.Label(frame_implementacion, text="Ingrese el nombre de la vacuna a ver:", bg="white",font=("Helvetica", 10, "bold"))
    tituloIngresoNombre.pack()

    criterios = ["Nombre"]
    fp = FieldFrame(frame_implementacion, "", criterios, "", None, None)
    fp.pack()

    botonBuscarVacuna = tk.Button(frame_implementacion, text="Buscar", command=busquedaVacuna, font=("Helvetica", 10, "bold"))
    botonBuscarVacuna.pack(pady=5)


    botonRegresar = tk.Button(frame_implementacion, text="Regresar", command=lambda: implementacionDefault(frame_implementacion),font=("Helvetica", 10, "bold"))
    botonRegresar.pack(pady=20)
