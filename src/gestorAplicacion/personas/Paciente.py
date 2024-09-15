from gestorAplicacion.servicios.Cita import Cita
from src.gestorAplicacion.administracionHospital.CategoriaHabitacion import CategoriaHabitacion
from src.gestorAplicacion.administracionHospital.HistoriaClinica import HistoriaClinica
from src.gestorAplicacion.administracionHospital.Hospital import Hospital
from src.gestorAplicacion.administracionHospital.Pago import Pago
from src.gestorAplicacion.personas.Persona import Persona
from src.gestorAplicacion.servicios.CitaVacuna import CitaVacuna
from src.gestorAplicacion.servicios.Formula import Formula
from src.gestorAplicacion.servicios.Habitacion import Habitacion


class Paciente(Persona, Pago):


    # Constructor
    def __init__(self, cedula, nombre, tipoEps):
        super().__init__(cedula, nombre, tipoEps)
        self.habitacionAsignada = None
        self.historiaClinica = HistoriaClinica(self)



    def medEnfermedad(self, enfermedad, hospital):
        medicamentos = hospital.medicamentosDisponibles()
        medEnfermedades = []

        for med in medicamentos:
            if med.enfermedad.nombre == enfermedad.nombre and med.enfermedad.tipologia == enfermedad.tipologia:
                medEnfermedades.append(med)

        return medEnfermedades

    def buscarDoctorEps(self, especialidad , hospital):
        doctoresPorEspecialidad = hospital.buscarTipoDoctor(especialidad)
        doctoresDisponibles = [doctor for doctor in doctoresPorEspecialidad if doctor.tipoEps == self.tipoEps]
        return doctoresDisponibles

    def actualizarHistorialCitas(self, citaAsignada: Cita):
        self.historiaClinica.historialCitas.append(citaAsignada)

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
