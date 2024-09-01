from gestorAplicacion.administracionHospital import CategoriaHabitacion, Habitacion, HistoriaClinica, Hospital, Pago
from gestorAplicacion.servicios import Cita, CitaVacuna, Formula, Enfermedad
from gestorAplicacion.personas import Persona

class Paciente(Persona, Pago):

    # Constructor
    def __init__(self, cedula: int, nombre: str, tipo_eps: str, categoria_habitacion: CategoriaHabitacion = None):
        super().__init__(cedula, nombre, tipo_eps)
        self.historia_clinica = HistoriaClinica(self)
        self.categoria_habitacion = categoria_habitacion
        self.habitacion_asignada = None

    # Método encargado de realizar la búsqueda de medicamentos disponibles
    def med_enfermedad(self, enfermedad: Enfermedad, hospital: Hospital):
        medicamentos = hospital.medicamentos_disponibles()
        med_enfermedades = [med for med in medicamentos if enfermedad.nombre == med.enfermedad.nombre and enfermedad.tipologia == med.enfermedad.tipologia]
        return med_enfermedades

    # Método encargado de buscar doctores por especialidad y tipo de EPS
    def buscar_doctor_eps(self, especialidad: str, hospital: Hospital):
        doctores_por_especialidad = hospital.buscar_tipo_doctor(especialidad)
        doctores_disponibles = [doctor for doctor in doctores_por_especialidad if doctor.tipo_eps == self.tipo_eps]
        return doctores_disponibles

    # Método encargado de actualizar la historia clínica
    def actualizar_historial_citas(self, cita_asignada: Cita):
        self.historia_clinica.historial_citas.append(cita_asignada)

    # Sobrecarga de métodos con calcular precio de los distintos servicios
    def calcular_precio_formula(self, formula: Formula):
        precio = sum(med.precio * (0.8 if self.tipo_eps == "Contributivo" else 0.7 if self.tipo_eps == "Subsidiado" else 1) for med in formula.lista_medicamentos)
        return precio * (1 + self.IVA)

    def calcular_precio_cita(self, cita_asignada: Cita):
        especialidad_precios = {
            "General": 5000,
            "Oftalmologia": 7000,
            "Odontologia": 10000
        }
        eps_precios = {
            "Contributivo": 2000,
            "Subsidiado": 500,
            "Particular": 10000
        }
        precio_total = especialidad_precios.get(cita_asignada.doctor.especialidad, 0)
        precio_total += eps_precios.get(self.tipo_eps, 0)
        return precio_total * (1 + self.IVA)

    def calcular_precio_cita_vacuna(self, cita_asignada: CitaVacuna):
        tipo_vacuna_precios = {
            "Obligatoria": 1000,
            "No obligatoria": 3000
        }
        eps_precios = {
            "Contributivo": 2000,
            "Subsidiado": 500,
            "Particular": 10000
        }
        precio_total = cita_asignada.vacuna.precio + tipo_vacuna_precios.get(cita_asignada.vacuna.tipo, 0)
        precio_total += eps_precios.get(self.tipo_eps, 0)
        return precio_total * (1 + self.IVA)

    def calcular_precio_habitacion(self, habitacion_asignada: Habitacion):
        if self.tipo_eps == "Subsidiado":
            precio = 0
        elif self.tipo_eps == "Contributivo":
            precio = (habitacion_asignada.categoria.valor / 2) * habitacion_asignada.dias
        else:
            precio = habitacion_asignada.categoria.valor * habitacion_asignada.dias
        return precio * (1 + self.IVA)

    # Método que busca las vacunas por tipo ingresado, invocando el método de hospital, y filtrándolas por EPS del paciente
    def buscar_vacuna_por_eps(self, tipo: str, hospital: Hospital):
        vacunas_por_tipo = hospital.buscar_tipo_vacuna(tipo)
        vacunas_disponibles = [vacuna for vacuna in vacunas_por_tipo if self.tipo_eps in vacuna.tipo_eps]
        return vacunas_disponibles

    # Método de bienvenida del Doctor
    def mensaje_doctor(self, doctor: Persona):
        return f"{doctor.bienvenida()}\nPor favor selecciona los medicamentos que vas a formularle a: {self.nombre}"

    # Método que agrega una cita a la lista de citas de la historia clínica del paciente
    def actualizar_historial_vacunas(self, cita_asignada: CitaVacuna):
        self.historia_clinica.historial_vacunas.append(cita_asignada)

    # to string
    def __str__(self):
        return f"---------------------------\nNombre: {self.nombre}\nCédula: {self.cedula}\nTipo de EPS: {self.tipo_eps}\n---------------------------"

    # Método de despedida
    def despedida(self, cita_asignada: Cita):
        return f"¡Adiós {self.nombre}! {cita_asignada.mensaje()}"