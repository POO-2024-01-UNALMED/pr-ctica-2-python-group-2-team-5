from src.gestorAplicacion import CategoriaHabitacion, HistoriaClinica, Hospital, Pago, Enfermedad
from src.gestorAplicacion import Cita, Cita_Vacuna, Formula, Habitacion
from src.gestorAplicacion import Persona

class Paciente(Persona, Pago):


    # Constructor
    def __init__(self, cedula: int, nombre: str, tipoEps: str, categoria_habitacion: CategoriaHabitacion):
        super().__init__(cedula, nombre, tipoEps)
        self._historiaClinica: HistoriaClinica
        self._categoriaHabitacion: CategoriaHabitacion = categoria_habitacion
        self._habitacionAsignada: Habitacion

    def med_enfermedad(self, enfermedad: Enfermedad, hospital: Hospital):
        medicamentos = hospital.medicamentos_disponibles()
        med_enfermedades = [med for med in medicamentos if enfermedad.nombre == med.enfermedad.nombre and enfermedad.tipologia == med.enfermedad.tipologia]
        return med_enfermedades

    def buscar_doctor_eps(self, especialidad: str, hospital: Hospital):
        doctores_por_especialidad = hospital.buscar_tipo_doctor(especialidad)
        doctores_disponibles = [doctor for doctor in doctores_por_especialidad if doctor.tipo_eps == self.tipo_eps]
        return doctores_disponibles

    def actualizar_historial_citas(self, cita_asignada: Cita):
        self.historia_clinica.historial_citas.append(cita_asignada)

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

    def calcular_precio_cita_vacuna(self, cita_asignada: Cita_Vacuna):
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


    def buscar_vacuna_por_eps(self, tipo: str, hospital: Hospital):
        vacunas_por_tipo = hospital.buscar_tipo_vacuna(tipo)
        vacunas_disponibles = [vacuna for vacuna in vacunas_por_tipo if self.tipo_eps in vacuna.tipo_eps]
        return vacunas_disponibles

    def mensaje_doctor(self, doctor: Persona):
        return f"{doctor.bienvenida()}\nPor favor selecciona los medicamentos que vas a formularle a: {self.nombre}"

    def actualizar_historial_vacunas(self, cita_asignada: Cita_Vacuna):
        self.historia_clinica.historial_vacunas.append(cita_asignada)

    def __str__(self):
        return f"---------------------------\nNombre: {self.nombre}\nCédula: {self.cedula}\nTipo de EPS: {self.tipo_eps}\n---------------------------"

    def despedida(self, cita_asignada: Cita):
        return f"¡Adiós {self.nombre}! {cita_asignada.mensaje()}"


    def getHistoriaClinica(self):
        return self._historiaClinica
    def getCategoriaHabitacion(self):
        return self._categoriaHabitacion
    def getHabitacion(self):
        return self._habitacion
    def setCategoriaHabitacion(self, habitacion: CategoriaHabitacion):
        self._categoriaHabitacion = habitacion
    def setHabitacionAsignada(self, habitacion: Habitacion):
        self._habitacionAsignada = habitacion
