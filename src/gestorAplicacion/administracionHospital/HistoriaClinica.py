#Importar las clases necesarias...
from Hospital import Hospital
from src.gestorAplicacion.personas import Paciente, Doctor
from gestorAplicacion.servicios import Cita, CitaVacuna,Formula
from baseDatos import Serializador


#Clase HistoriaClinica: Revisar actividad del paciente dentro del hospital.

class HistoriaClinica(Serializador):
    #Inicializador.
    def __init__(self, paciente: Paciente):
        self.paciente = paciente
        self.historialCitas = []
        self.listaFormulas = []
        self.historialVacunas = []
        self.enfermedades = []

    #Métodos.

    #Buscar doctores por especialidad.
    def buscarCitaDoc(self, especialidad): #Hospital como parámetro?
        doctoresDisp = Hospital.buscarTipoDoctor(especialidad)
        docCita = []
        for doc in doctoresDisp:
            for cita in self.historialCitas:
                if doc.getCedula() == cita.getDoctor().getCedula():
                    docCita.append(doc)
        return docCita

    #Agregar fórmulas al atributo de la clase.
    def agregarFormula(self, formulaPaciente):
        self.listaFormulas.append(formulaPaciente)

    #Setters y getters.
    def getPaciente(self):
        return self.paciente

    def getHistorialCitas(self):
        return self.historialCitas

    def setHistorialCitas(self, historialCitas):
        self.historialCitas = historialCitas

    def getListaFormulas(self):
        return self.listaFormulas

    def setListaFormulas(self, listaFormulas):
        self.listaFormulas = listaFormulas

    def getHistorialVacunas(self):
        return self.historialVacunas

    def setHistorialVacunas(self, historialVacunas):
        self.historialVacunas = historialVacunas

    def getEnfermedades(self):
        return self.enfermedades

    def setEnfermedades(self, enfermedades):
        self.enfermedades = enfermedades
