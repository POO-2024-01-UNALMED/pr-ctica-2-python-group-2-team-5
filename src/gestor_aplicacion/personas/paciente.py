from src.gestor_aplicacion.administracion.historia_clinica import HistoriaClinica
from src.gestor_aplicacion.personas.persona import Persona
from src.gestor_aplicacion.servicios.cita import Cita
from src.gestor_aplicacion.servicios.cita_vacuna import CitaVacuna
from src.gestor_aplicacion.servicios.formula import Formula
from src.gestor_aplicacion.servicios.habitacion import Habitacion
from src.manejo_errores.error_aplicacion import SinDoctores


# Clase destinada a crear pacientes
class Paciente(Persona):

    # Atributos y constructor
    def __init__(self, cedula, nombre, tipo_eps):
        super().__init__(cedula, nombre, tipo_eps)
        self._habitacion_asignada = None
        self._HISTORIA_CLINICA = HistoriaClinica(self)

    # Metodos

    # Metodo que calcula el precio de un servicio, recibe un objeto de la clase Servicio
    # y devuelve un entero dependiendo la clase que sea servicio
    def calcular_precio(self, servicio):
        if isinstance(servicio, Formula):
            IVA = 1.19
            precio_total = 0
            for med in servicio.lista_meds:
                if self._tipo_eps == "Subsidiado":
                    precio_total += med.precio * 1.3
                if self._tipo_eps == "Contributivo":
                    precio_total += med.precio * 1.2
                if self._tipo_eps == "Particular":
                    precio_total += med.precio
            return precio_total * IVA
        elif isinstance(servicio, CitaVacuna):
            IVA = 0.19
            precio_total = servicio.vacuna.precio

            if servicio.vacuna.tipo == "Obligatoria":
                precio_total += 1000
            elif servicio.vacuna.tipo == "No obligatoria":
                precio_total += 3000

            tipo_eps = servicio.paciente.tipo_eps
            if tipo_eps == "Contributivo":
                precio_total += 2000
            elif tipo_eps == "Subsidiado":
                precio_total += 500
            elif tipo_eps == "Particular":
                precio_total += 10000

            precio_total *= (1 + IVA)
            return precio_total
        elif isinstance(servicio, Habitacion):
            IVA = 0.19
            precio_total = 0
            if self.tipo_eps == "Subsidiado":
                precio_total = self._habitacion_asignada.categoria.valor * 0
            elif self.tipo_eps == "Contributivo":
                precio_total = (self._habitacion_asignada.categoria.valor / 2) * self._habitacion_asignada.dias
            else:
                precio_total = self._habitacion_asignada.categoria.valor * self._habitacion_asignada.dias
            precio_total *= (1 + IVA)
            return precio_total

        elif isinstance(servicio, Cita):
            IVA = 0.19
            precio_total = 0
            tipo_eps = servicio.paciente.tipo_eps
            especialidad = servicio.doctor.especialidad

            if especialidad == "General":
                precio_total += 5000
            if especialidad == "Odontologia":
                precio_total += 10000
            if especialidad == "Oftalmologia":
                precio_total += 7000
            if tipo_eps == "Contributivo":
                precio_total += 2000
            if tipo_eps == "Subsidiado":
                precio_total += 500
            if tipo_eps == "Particular":
                precio_total += 10000

            precio_total *= (1 + IVA)
            return precio_total

    # Método que se encarga de buscar los medicamentos disponibles y posteriormente busca los medicamentos
    # que traten la enfermedad ingresada como parámetro. Recibe un objeto de clase Enfermedad, uno de clase
    # Hospital y retorna una lista de objetos de Medicamento
    def med_enfermedad(self, enfermedad, hospital):
        meds = hospital.meds_disponibles()
        med_enfermedades = []
        for med in meds:
            if med.enfermedad.nombre == enfermedad.nombre and med.enfermedad.tipologia == enfermedad.tipologia:
                med_enfermedades.append(med)
        return med_enfermedades

    # Método que busca los doctores por especialidad y por el tipo de eps del paciente
    # Recibe un string, y un objeto de clase Hospital. Retorna una lista de objetos de Doctor
    def buscar_doctor_por_eps(self, especialidad, hospital):
        doctores_por_especialidad = hospital.buscar_tipo_doctor(especialidad)
        doctores_disponibles = []

        for doctor in doctores_por_especialidad:
            if doctor.tipo_eps == self.tipo_eps:
                doctores_disponibles.append(doctor)
        if len(doctores_disponibles) != 0:
            return doctores_disponibles
        else:
            raise SinDoctores()

    # Método que busca las vacunas por tipo ingresada en el parámetro, invocando el método
    # de hospital, y con el for filtrandolas por eps del paciente
    # Recibe un string, un objeto de clase Hospital y devuelve una lista de
    # objetos de Vacuna
    def buscar_vacuna_por_eps(self, tipo, hospital):
        vacunas_por_tipo = hospital.buscar_tipo_vacuna(tipo)
        vacunas_disponibles = []

        for vacuna in vacunas_por_tipo:
            for eps in vacuna.tipo_eps:
                if eps == self.tipo_eps:
                    vacunas_disponibles.append(vacuna)
        return vacunas_disponibles

    # Método que agrega una cita a la lista de citas de la historia clínica del paciente
    # recibe un objeto de tipo Cita y modifica el atributo _historia_clinica de paciente
    def actualizar_historial_citas(self, cita_seleccionada):
        self.historia_clinica.historial_citas.append(cita_seleccionada)

    # Método que agrega una Cita_Vacuna a la lista de citas de la historia clínica del paciente
    # recibe un objeto de tipo Cita_Vacuna y modifica el atributo _historia_clinica de paciente
    def actualizar_historial_vacunas(self, cita_asignada):
        self.historia_clinica.historial_vacunas.append(cita_asignada)

    @property
    def habitacion_asignada(self):
        return self._habitacion_asignada

    @property
    def historia_clinica(self):
        return self._HISTORIA_CLINICA

    @habitacion_asignada.setter
    def habitacion_asignada(self, hab):
        self._habitacion_asignada = hab
