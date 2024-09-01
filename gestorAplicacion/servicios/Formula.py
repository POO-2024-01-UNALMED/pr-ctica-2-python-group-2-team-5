#Importar lo necesario...
from gestorAplicacion.servicios.Servicio import Servicio
from gestorAplicacion.administracionHospital.Medicamento import Medicamento
from gestorAplicacion.personas.Doctor import Doctor
from gestorAplicacion.personas.Paciente import Paciente

#Clase Formula, permite recetanle los medicamentos necesarios a los pácientes según sus enfermedades a tratar.
class Formula(Servicio):
    #Inicializador.
    def __init__(self, listaMedicamentos, doctor, paciente):
        self._listaMedicamentos = listaMedicamentos
        self._doctor = doctor
        super().__init__(paciente)

    #Sobrecarga de constructor. Terminar
    #def __int__(self):
    #    pass

    #Métodos.

    #Métodos implementados de la clase Servicio.
    def validarPago(self, paciente, idServicio):
        for formula in paciente.getHistoriaClinica().getListaFormulas():
            if formula.getIdServicio() == idServicio:
                formula.setEstadoPago(True)

    def descripcionServicio(self):
        return f"{self._IDSERVICIO} - Fórmula prescrita por: {self._doctor.getNombre()}"

    def __str__(self):
        return f"Hola {self._paciente.getNombre}\nEstos son tus medicamentos formulados:\n{self._listaMedicamentos}"

    #Setters y getters.
    def getListaMedicamentos(self):
        return self._listaMedicamentos

    def setListaMedicamentos(self, listaMedicamentos):
        self._listaMedicamentos = listaMedicamentos

    def getDoctor(self):
        return self._doctor

    def setDoctor(self, doctor):
        self._doctor = doctor