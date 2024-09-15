from tkinter import messagebox

class ErroresAplicacion(Exception):
    def __init__(self, mensaje):
        self.mensaje = f"Manejo de errores de la aplicacion\n{mensaje}"
        super().__init__(self.mensaje)

    def enviarMensaje(self):
        messagebox.showerror("ErroresAplicacion", self.mensaje)


class IngresoErroneo(ErroresAplicacion):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(f"Ingreso Erróneo: {self.mensaje}")

class ErrorAdministrativo(ErroresAplicacion):
    def __init__(self, mensaje):
        self.mensaje = mensaje

        super().__init__(f"Error Administrativo: {self.mensaje}")

class DatosFalsos(IngresoErroneo):
    def __init__(self):
        super().__init__("NO se encuentra el dato que intenta ingresar")


class TipoIncorrecto(IngresoErroneo):
    def __init__(self, mensaje = ""):
        super().__init__(f"Ingrese el dato de forma CORRECTA, por favor {mensaje}")

class CampoVacio(IngresoErroneo):
    def __init__(self):
        super().__init__("Uno o mas campos se encuentran VACIOS")

class DatoDuplicado(IngresoErroneo):
    def __init__(self):
        super().__init__("El dato que intenta ingresar se encuentra DUPLICADO")

class SinDoctores(ErrorAdministrativo):
    def __init__(self):
        super().__init__("NO hay doctores")


class SinAgenda(ErrorAdministrativo):
    def __init__(self):
        super().__init__("NO existen citas disponibles")


class SinCitaPrevia(ErrorAdministrativo):
    def __init__(self):
        super().__init__("Agende una cita con un DOCTOR primero")


class SinMedicamentos(ErrorAdministrativo):
    def __init__(self):
        super().__init__("Su medicamento NO se encuentra disponible")


class SinVacunas(ErrorAdministrativo):
    def __init__(self):
        super().__init__("NO tiene vacunas disponibles")


class SinServicioSeleccionado(ErrorAdministrativo):
    def __init__(self):
        super().__init__("Seleccione ALMENOS un servicio")


class EstaHospitalizado(ErrorAdministrativo):
    def __init__(self):
        super().__init__("Usted ya se encuentra OCUPANDO una habitacion")
