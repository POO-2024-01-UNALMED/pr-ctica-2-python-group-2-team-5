from gestorAplicacion.personas import Paciente, Doctor
from gestorAplicacion.administracionHospital import Medicamento
from gestorAplicacion.servicios import Servicio


#Clase Formula, permite recetanle los medicamentos necesarios a los pácientes según sus enfermedades a tratar.
class Formula(Servicio):
    #Inicializador.
    def __init__(self, listaMedicamentos, doctor, paciente):
        super().__init__(paciente)
        self.listaMedicamentos = listaMedicamentos
        self.doctor = doctor
        

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
        return f"{self.idServicio} - Fórmula prescrita por: {self.doctor.getNombre()}"

    def __str__(self):
        return f"Hola {self.paciente.getNombre}\nEstos son tus medicamentos formulados:\n{self.listaMedicamentos}"

    #Setters y getters.
    def getListaMedicamentos(self):
        return self.listaMedicamentos

    def setListaMedicamentos(self, listaMedicamentos):
        self.listaMedicamentos = listaMedicamentos

    def getDoctor(self):
        return self.doctor

    def setDoctor(self, doctor):
        self.doctor = doctor