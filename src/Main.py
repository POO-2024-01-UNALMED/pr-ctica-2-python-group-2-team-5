import pickle

from gestorAplicacion.administracionHospital.Hospital import Hospital
from iuMain.interfazGrafica.ventanaInicio import abrirVentanaInicio

if __name__ == '__main__':

    serializarDoctores = open("../../baseDatos/temp/registro_doctores.pickle", "wb")
    pickle.dump(None, serializarDoctores)
    serializarDoctores.close()
    serializarPacientes = open("../../baseDatos/temp/registro_pacientes.pickle", "wb")
    pickle.dump(None, serializarPacientes)
    serializarPacientes.close()
    serializarMedicamento = open("../../baseDatos/temp/registro_medicamentos.pickle", "wb")
    pickle.dump(None, serializarMedicamento)
    serializarMedicamento.close()
    serializarVacunas = open("../../baseDatos/temp/registro_vacunas.pickle", "wb")
    pickle.dump(None, serializarVacunas)
    serializarVacunas.close()
    serializarEnfermedades = open("../../baseDatos/temp/registro_enfermedades.pickle", "wb")
    pickle.dump(None, serializarEnfermedades)
    serializarEnfermedades.close()
    serializarHabitaciones = open("../../baseDatos/temp/registro_habitaciones.pickle", "wb")
    pickle.dump(None, serializarHabitaciones)
    serializarHabitaciones.close()