from gestorAplicacion.administracionHospital.Hospital import Hospital
from gestorAplicacion.personas import Paciente
from gestorAplicacion.servicios import Cita, CitaVacuna,Formula



#Clase HistoriaClinica: Revisar actividad del paciente dentro del hospital.

class HistoriaClinica:
    #Inicializador.
    def __init__(self, paciente: Paciente):
        self.paciente = paciente
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


    def enfermedades(self):
        return self.enfermedades


    def getEnfermedades(self, value):
        self.enfermedades = value


    def lista_formulas(self):
        return self.listaFormulas


    def historial_citas(self):
        return self.historialCitas


    def historial_vacunas(self):
        return self.historialVacunas
