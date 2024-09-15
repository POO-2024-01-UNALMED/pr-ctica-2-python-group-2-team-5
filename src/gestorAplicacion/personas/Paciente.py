from gestorAplicacion.servicios.Cita import Cita
from src.gestorAplicacion.administracionHospital.CategoriaHabitacion import CategoriaHabitacion
from src.gestorAplicacion.administracionHospital.Enfermedad import Enfermedad
from src.gestorAplicacion.administracionHospital.HistoriaClinica import HistoriaClinica
from src.gestorAplicacion.administracionHospital.Hospital import Hospital
from src.gestorAplicacion.administracionHospital.Pago import Pago
from src.gestorAplicacion.personas.Persona import Persona
from src.gestorAplicacion.servicios.CitaVacuna import CitaVacuna
from src.gestorAplicacion.servicios.Formula import Formula
from src.gestorAplicacion.servicios.Habitacion import Habitacion


class Paciente(Persona, Pago):


    # Constructor
    def __init__(self, cedula: int, nombre: str, tipoEps: str, categoriaHabitacion: CategoriaHabitacion):
        super().__init__(cedula, nombre, tipoEps)
        self.historiaClinica: HistoriaClinica
        self.categoriaHabitacion: CategoriaHabitacion = categoriaHabitacion
        self.habitacionAsignada: Habitacion

    def medEnfermedad(self, enfermedad: Enfermedad, hospital: Hospital):
        medicamentos = hospital.medicamentosDisponibles()
        medEnfermedades = [med for med in medicamentos if enfermedad.nombre == med.enfermedad.nombre and enfermedad.tipologia == med.enfermedad.tipologia]
        return medEnfermedades

    def buscarDoctorEps(self, especialidad: str, hospital: Hospital):
        doctoresPorEspecialidad = hospital.buscarTipoDoctor(especialidad)
        doctoresDisponibles = [doctor for doctor in doctoresPorEspecialidad if doctor.tipoEps == self.tipoEps]
        return doctoresDisponibles

    def actualizarHistorialCitas(self, citaAsignada: Cita):
        self.historiaClinica.historialCitas.append(citaAsignada)

    def calcularPrecioFormula(self, formula: Formula):
        precio = sum(med.precio * (0.8 if self.tipoEps == "Contributivo" else 0.7 if self.tipoEps == "Subsidiado" else 1) for med in formula.listaMedicamentos)
        return precio * (1 + self.IVA)

    def calcularPrecioCita(self, citaAsignada: Cita):
        especialidadPrecios = {
            "General": 5000,
            "Oftalmologia": 7000,
            "Odontologia": 10000
        }
        epsPrecios = {
            "Contributivo": 2000,
            "Subsidiado": 500,
            "Particular": 10000
        }
        precioTotal = especialidadPrecios.get(citaAsignada.doctor.especialidad, 0)
        precioTotal += epsPrecios.get(self.tipoEps, 0)
        return precioTotal * (1 + self.IVA)

    def calcularPrecioCitaVacuna(self, citaAsignada: CitaVacuna):
        tipoVacunaPrecios = {
            "Obligatoria": 1000,
            "No obligatoria": 3000
        }
        epsPrecios = {
            "Contributivo": 2000,
            "Subsidiado": 500,
            "Particular": 10000
        }
        precioTotal = citaAsignada.vacuna.precio + tipoVacunaPrecios.get(citaAsignada.vacuna.tipo, 0)
        precioTotal += epsPrecios.get(self.tipoEps, 0)
        return precioTotal * (1 + self.IVA)

    def calcularPrecioHabitacion(self, habitacionAsignada: Habitacion):
        
        if self.tipoEps == "Subsidiado":
            precio = 0

        elif self.tipoEps == "Contributivo":
            precio = (habitacionAsignada.categoria.valor / 2) * habitacionAsignada.dias

        else:
            precio = habitacionAsignada.categoria.valor * habitacionAsignada.dias

        return precio * (1 + self.IVA)


    def buscarVacunaPorEps(self, tipo: str, hospital: Hospital):
        vacunasPorTipo = hospital.buscarTipoVacuna(tipo)
        vacunasDisponibles = [vacuna for vacuna in vacunasPorTipo if self.tipoEps in vacuna.tipoEps]
        return vacunasDisponibles

    def mensajeDoctor(self, doctor: Persona):
        return f"{doctor.bienvenida()}\nPor favor selecciona los medicamentos que vas a formularle a: {self.nombre}"

    def actualizarHistorialVacunas(self, citaAsignada: CitaVacuna):
        self.historiaClinica.historialVacunas.append(citaAsignada)

    def __str__(self):
        return f"---------------------------\nNombre: {self.nombre}\nCédula: {self.cedula}\nTipo de EPS: {self.tipoEps}\n---------------------------"

    def despedida(self, citaAsignada: Cita):
        return f"¡Adiós {self.nombre}! {citaAsignada.mensaje()}"


    def getHistoriaClinica(self):
        return self.historiaClinica
    
    def getCategoriaHabitacion(self):
        return self.categoriaHabitacion
    
    def getHabitacion(self):
        return self.habitacion
    
    def setCategoriaHabitacion(self, habitacion: CategoriaHabitacion):
        self.categoriaHabitacion = habitacion

    def setHabitacionAsignada(self, habitacion: Habitacion):
        self.habitacionAsignada = habitacion
