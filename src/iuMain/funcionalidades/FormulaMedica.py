#Importar lo necesario...
from src.gestorAplicacion import Formula
from src.iuMain.gestion.gestionPacientes.gestionPaciente import GestionPaciente

class FormulaMedica:
    def __init__(self, hospital):
        self.hospital = hospital
        self.sc = None  # Simulación de entrada (esto debería manejarse mejor en un entorno real)

    def formula_medica(self):
        paciente = self.select_patient()
        if not paciente:
            return

        enfermedad_tratar = self.select_disease(paciente)
        if not enfermedad_tratar:
            return

        doctor_escogido = self.select_doctor(paciente, enfermedad_tratar)
        if not doctor_escogido:
            return

        formula_paciente = self.create_formula(paciente, doctor_escogido, enfermedad_tratar)
        if formula_paciente:
            paciente.historia_clinica.agregar_formula(formula_paciente)
            print(formula_paciente)

    def select_patient(self):
        cedula = input("Ingrese la cédula del paciente: ")
        paciente = self.hospital.buscar_paciente(int(cedula))
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

    def select_disease(self, paciente):
        if not paciente.historia_clinica.enfermedades:
            print("No hay enfermedades registradas, por favor diríjase a la sección de registrar enfermedades.")
            return None
        while True:
            print("¿Qué enfermedad deseas tratar?")
            for i, enfermedad in enumerate(paciente.historia_clinica.enfermedades):
                print(f"{i + 1}. {enfermedad}")
            opc_enf = input()
            if opc_enf.isdigit() and 0 < int(opc_enf) <= len(paciente.historia_clinica.enfermedades):
                return paciente.historia_clinica.enfermedades[int(opc_enf) - 1]
            else:
                print("Opción Inválida")

    def select_doctor(self, paciente, enfermedad_tratar):
        doctores_cita = paciente.historia_clinica.buscar_cita_doc(enfermedad_tratar.especialidad, self.hospital)
        if not doctores_cita:
            print("Ahora no contamos con doctores para tratar esta enfermedad. Lo sentimos mucho.")
            return None
        while True:
            print(f"Los doctores que lo han atendido y están disponibles para formular {enfermedad_tratar.nombre} {enfermedad_tratar.tipologia} son:")
            for i, doctor in enumerate(doctores_cita):
                print(f"{i + 1}. {doctor.nombre}")
            opc_doc = input()
            if opc_doc.isdigit() and 0 < int(opc_doc) <= len(doctores_cita):
                return doctores_cita[int(opc_doc) - 1]
            else:
                print("Opción inválida")

    def create_formula(self, paciente, doctor, enfermedad_tratar):
        list_medicamento = []
        formula_paciente = Formula(paciente)
        formula_paciente.doctor = doctor

        while True:
            print(paciente.mensaje_doctor(doctor))

            disponible_enf = paciente.med_enfermedad(enfermedad_tratar, self.hospital)
            if not disponible_enf:
                print("No hay más medicamentos disponibles")
                break

            while True:
                for i, medicamento in enumerate(disponible_enf):
                    print(f"{i + 1}. {medicamento}, Cantidad: {medicamento.cantidad}, Precio: {medicamento.precio}")
                opc_med = input()
                if opc_med.isdigit() and 0 < int(opc_med) <= len(disponible_enf):
                    medicamento_escogido = disponible_enf[int(opc_med) - 1]
                    medicamento_escogido.eliminar_cantidad()
                    list_medicamento.append(medicamento_escogido)
                    break
                else:
                    print("Opción inválida")

            formula_paciente.lista_medicamentos = list_medicamento
            print(f"Esta es tu lista actual de medicamentos: {list_medicamento}")

            for i, medicamento in enumerate(list_medicamento):
                print(f"{i + 1}. {medicamento}")

            agregar_otro = input("¿Desea agregar otro medicamento? (s/n): ")
            if agregar_otro.lower() != 's':
                break

        if not list_medicamento:
            return None

        return formula_paciente