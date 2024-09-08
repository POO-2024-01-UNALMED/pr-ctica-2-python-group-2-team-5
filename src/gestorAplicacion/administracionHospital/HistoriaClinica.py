#Importar las clases necesarias...
from Hospital import Hospital
from src.gestorAplicacion import Paciente


#Clase HistoriaClinica: Revisar actividad del paciente dentro del hospital.

class HistoriaClinica:
    #Inicializador.
    def __init__(self, paciente: Paciente):
        self.paciente = paciente
        self._historialCitas = []
        self._listaFormulas = []
        self._historialVacunas = []
        self._enfermedades = []

    #Métodos.

    #Buscar doctores por especialidad.
    def buscarCitaDoc(self, especialidad): #Hospital como parámetro?
        doctoresDisp = Hospital.buscarTipoDoctor(especialidad)
        docCita = []
        for doc in doctoresDisp:
            for cita in self._historialCitas:
                if doc.getCedula() == cita.getDoctor().getCedula():
                    docCita.append(doc)
        return docCita

    #Agregar fórmulas al atributo de la clase.
    def agregarFormula(self, formulaPaciente):
        self._listaFormulas.append(formulaPaciente)

    #Setters y getters.
    def getPaciente(self):
        return self.paciente

    def getHistorialCitas(self):
        return self._historialCitas

    def setHistorialCitas(self, historialCitas):
        self._historialCitas = historialCitas

    def getListaFormulas(self):
        return self._listaFormulas

    def setListaFormulas(self, listaFormulas):
        self._listaFormulas = listaFormulas

    def getHistorialVacunas(self):
        return self._historialVacunas

    def setHistorialVacunas(self, historialVacunas):
        self._historialVacunas = historialVacunas

    def getEnfermedades(self):
        return self._enfermedades

    def setEnfermedades(self, enfermedades):
        self._enfermedades = enfermedades
