#Importar lo necesario...
from gestorAplicacion import Formula
from gestorAplicacion.administracionHospital import Hospital, Medicamento, Enfermedad
from gestorAplicacion.personas import Doctor, Paciente
from iuMain.gestion.gestionPacientes.gestionPaciente import GestionPaciente

class FormulaMedica:
    def __init__(self, hospital):
        self.hospital = hospital
        self.sc = None  # Simulación de entrada (esto debería manejarse mejor en un entorno real)

    def formulaMedica(self):
        paciente = self.selectPatient()
        if not paciente:
            return

        enfermedadTratar = self.selectDisease(paciente)
        if not enfermedadTratar:
            return

        doctorEscogido = self.selectDoctor(paciente, enfermedadTratar)
        if not doctorEscogido:
            return

        formulaPaciente = self.createFormula(paciente, doctorEscogido, enfermedadTratar)
        if formulaPaciente:
            paciente.historiaClinica.agregarFormula(formulaPaciente)
            print(formulaPaciente)

    def selectPatient(self):
        cedula = input("Ingrese la cédula del paciente: ")
        paciente = self.hospital.buscarPaciente(int(cedula))
        if not paciente:
            while True:
                opcion = input("El paciente no está registrado.\n¿Desea registrarlo?\n1. Sí\n2. No\nSeleccione una opción: ")
                if opcion == '1':
                    GestionPaciente.registrarPaciente(self.hospital)
                    return None
                elif opcion == '2':
                    print("Adiós")
                    return None
                else:
                    print("Opción Inválida")
        return paciente

    def selectDisease(self, paciente):
        if not paciente.historiaClinica.getEnfermedades:
            print("No hay enfermedades registradas, por favor diríjase a la sección de registrar enfermedades.")
            return None
        while True:
            print("¿Qué enfermedad deseas tratar?")
            for i, enfermedad in enumerate(paciente.historiaClinica.getEnfermedades):
                print(f"{i + 1}. {enfermedad}")
            opcEnf = input()
            if opcEnf.isdigit() and 0 < int(opcEnf) <= len(paciente.historiaClinica.getEnfermedades):
                return paciente.historiaClinica.getEnfermedades[int(opcEnf) - 1]
            else:
                print("Opción Inválida")

    def selectDoctor(self, paciente, enfermedadTratar):
        doctoresCita = paciente.historiaClinica.buscarCitaDoc(enfermedadTratar.especialidad, self.hospital)
        if not doctoresCita:
            print("Ahora no contamos con doctores para tratar esta enfermedad. Lo sentimos mucho.")
            return None
        while True:
            print(f"Los doctores que lo han atendido y están disponibles para formular {enfermedadTratar.nombre} {enfermedadTratar.tipologia} son:")
            for i, doctor in enumerate(doctoresCita):
                print(f"{i + 1}. {doctor.nombre}")
            opcDoc = input()
            if opcDoc.isdigit() and 0 < int(opcDoc) <= len(doctoresCita):
                return doctoresCita[int(opcDoc) - 1]
            else:
                print("Opción inválida")

    def createFormula(self, paciente, doctor, enfermedadTratar):
        listMedicamento = []
        formulaPaciente = Formula(paciente)
        formulaPaciente.doctor = doctor

        while True:
            print(paciente.mensajeDoctor(doctor))

            disponibleEnf = paciente.medEnfermedad(enfermedadTratar, self.hospital)
            if not disponibleEnf:
                print("No hay más medicamentos disponibles")
                break

            while True:
                for i, medicamento in enumerate(disponibleEnf):
                    print(f"{i + 1}. {medicamento}, Cantidad: {medicamento.cantidad}, Precio: {medicamento.precio}")
                opcMed = input()
                if opcMed.isdigit() and 0 < int(opcMed) <= len(disponibleEnf):
                    medicamentoEscogido = disponibleEnf[int(opcMed) - 1]
                    medicamentoEscogido.eliminarCantidad()
                    listMedicamento.append(medicamentoEscogido)
                    break
                else:
                    print("Opción inválida")

            formulaPaciente.listaMedicamentos = listMedicamento
            print(f"Esta es tu lista actual de medicamentos: {listMedicamento}")

            for i, medicamento in enumerate(listMedicamento):
                print(f"{i + 1}. {medicamento}")

            agregarOtro = input("¿Desea agregar otro medicamento? (s/n): ")
            if agregarOtro.lower() != 's':
                break

        if not listMedicamento:
            return None

        return formulaPaciente