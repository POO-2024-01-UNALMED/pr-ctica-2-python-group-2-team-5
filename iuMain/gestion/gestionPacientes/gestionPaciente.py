
from gestorAplicacion.administracionHospital.Hospital import *
from gestorAplicacion.personas.Paciente import Paciente



class gestionPaciente:
    @staticmethod
    def eliminarPaciente(self, hospital: Hospital):
        #Crear el Scanner
        cedula = str(print("Ingrese la cedula del paciente a eliminar"))
        paciente = hospital.buscarPaciente(cedula)

        if paciente is None:
            print("El paciente NO EXISTE / Se encuentra ELIMINADO")
        else:
            hospital.listaPacientes.remove(paciente)
            print("El paciente ha sido ELIMINADO con éxito")

    @staticmethod
    def registrarPaciente(self, hospital: Hospital):
        print("Por favor introduzca la informacion del Paciente")

        nombre = str(input("Ingrese el nombre del paciente: "))

        cedula = int(input("Ingrese la cedula del paciente: "))

        if (hospital.buscarPaciente(cedula)) is not None:
            print("El paciente ya se encuentra registrado")
            return

        eps = str(print("Ingrese su tipo de EPS 'Subsidiado', 'Contributivo', 'Particular'"))

        if eps != "Subsidiado" or "Contributivo" or "Particular":
            print("La EPS ingresada no es correcta")
            return

        paciente = Paciente(cedula, nombre, eps)
        hospital.getListaPacientes().append(paciente)

        print("El paciente ha sido registrado con Éxito, recuerde que la Historia Clínica se encuentra VACIA")
        print(paciente)

    def mostrarInformacionPaciente(self, hospital: Hospital):
        cedula = int(input("Ingrese la cedula del paciente: "))

        paciente = hospital.buscarPaciente(cedula)


        if paciente is None:
            while (True):
                print("El paciente no esta registrado. \n ¿Desea Registrarlo?")
                opcion = int(input("1. Sí \n2. No \nSeleccione una opción: "))

                if opcion == 1:
                    gestionPaciente.registrarPaciente(self, hospital)
                    print("El paciente ha sido registrado")
                    return
                elif opcion == 2:
                    print("Adios :D ")
                    return
                else:
                    print("Ha seleccionado una opcion inválida.")
                    return #Si saca error aca, esto esta mal

        print("\n---INFORMACION DEL PACIENTE---")
        print(paciente)
        print("\n---HISTORIA CLINICA---")
        print("\nEnfermedades: ")
        for i in (paciente.getHistorialClinica().getEnfermedad()):
            print(i)
        print("\nFormulas: ")
        for i in (paciente.getHistorialClinica().getFormulas()):
            print(i)
        print("\nCitas: ")
        for cita in (paciente.getHistorialClinica().getHistorialCitas()):
            print("Fecha: " + cita.getFecha())
            print("Doctor: " + cita.getDoctor().getNombre())
        print("\nHistorial Vacunas: ")
        for vacuna in paciente.getHistoriaClinica().getHistoriaVacunas():
            print(vacuna.getVacuna.getNombre())









