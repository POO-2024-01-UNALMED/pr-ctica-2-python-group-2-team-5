from gestorAplicacion.administracionHospital.Hospital import *
from gestorAplicacion.personas.Doctor import Doctor


class RegistrarDoctor:

    @staticmethod
    
    def registrar_doctor(hospital):
        print("Por favor introduce la información del doctor para su registro")
        nombre = input("Ingrese el nombre del doctor: ")
        id = int(input("Ingrese el número de cédula: "))

        if hospital.buscar_doctor(id) is not None:
            print("Este doctor ya esta registrado")
            return

        eps = input("Ingrese su tipo de EPS 'Subsidiado','Contributivo' o 'Particular': ")
        especialidad = input("Ingrese su especialidad 'General', 'Odontologia' o 'Oftalmologia': ")

        doctor = Doctor(id, nombre, eps, especialidad)
        print("¡El doctor ha sido registrado con éxito!")
        hospital.doctores.append(doctor)
        print(doctor)