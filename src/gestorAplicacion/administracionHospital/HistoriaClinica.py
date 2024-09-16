from src.gestorAplicacion.administracionHospital.Hospital import Hospital
from src.gestorAplicacion.personas import Paciente
from src.gestorAplicacion.servicios import Cita, CitaVacuna,Formula

# Clase HistoriaClinica: Revisar actividad del paciente dentro del hospital.

class HistoriaClinica:
    #Inicializador.
    def __init__(self, paciente: Paciente):
        self.PACIENTE = paciente
        self.historialCitas = []
        self.listaFormulas = []
        self.historialVacunas = []
        self.enfermedades = []

    #Métodos.

    #Buscar doctores por especialidad.
    def buscarCitaDoc(self, especialidad, hospital): #Hospital como parámetro?
        doctoresDisp = hospital.buscarTipoDoctor(especialidad)
        docCita = []
        for doc in doctoresDisp:
            for cita in self.historialCitas:
                if doc.getCedula() == cita.getDoctor().getCedula():
                    docCita.append(doc)
        return docCita

    #Agregar fórmulas al atributo de la clase.
    def agregarFormula(self, formulaPaciente):
        self.listaFormulas.append(formulaPaciente)


    def getEnfermedades(self):
        return self.enfermedades


    def setEnfermedades(self, value):
        self.enfermedades = value


    def getListaFormulas(self):
        return self.listaFormulas


    def getHistorialCitas(self):
        return self.historialCitas


    def getHistorialVacunas(self):
        return self.historialVacunas
