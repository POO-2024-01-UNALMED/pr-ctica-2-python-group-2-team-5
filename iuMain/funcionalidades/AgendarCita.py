#Importar lo necesario...
from gestorAplicacion.administracionHospital.Hospital import Hospital
from gestorAplicacion.personas.Doctor import Doctor
from gestorAplicacion.personas.Paciente import Paciente
from gestorAplicacion.servicios.Cita import Cita

#Clase Agendar cita, que corresponde a la funcionalidad 1.
class AgendarCita:
    #Métodos.

    #Buscar doctores por la EPS.
    @classmethod
    def agendarCita(cls, hospital):
        #Buscar paciente con el número de cédula.
        numeroCedula = int(input("Por favor, ingrese su número de identificación: "))
        pacienteCita = hospital.buscarPaciente(numeroCedula)

        #Verificar si se encontró un paciente que coincida con la cédula.
        if pacienteCita == None:
            while True:
                print("El paciente no está registrado")