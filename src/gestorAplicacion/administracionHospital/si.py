import pickle

from gestorAplicacion.administracionHospital.Enfermedad import Enfermedad


def serializar(self):
    serializarDoctor = open("../../baseDatos/temp/registro_doctores.pickle", "wb")
    pickle.dump(self.listaDoctores, serializarDoctor)
    serializarDoctor.close()

    serializarPaciente = open("../../baseDatos/temp/registro_pacientes.pickle", "wb")
    pickle.dump(self.listaPacientes, serializarPaciente)
    serializarPaciente.close()

    serializarMedicamentos = open("../../baseDatos/temp/registro_medicamentos.pickle", "wb")
    pickle.dump(self.listaMedicamentos, serializarMedicamentos)
    serializarMedicamentos.close()

    serializarVacunas = open("../../baseDatos/temp/registro_vacunas.pickle", "wb")
    pickle.dump(self.listaVacunas, serializarVacunas)
    serializarVacunas.close()

    serializarEnfermedades = open("../../baseDatos/temp/registro_enfermedads.pickle", "wb")
    pickle.dump(Enfermedad.enfermedadesRegistradas, serializarEnfermedades)
    serializarEnfermedades.close()

    serializarHabitaciones = open("../../baseDatos/temp/registro_habitables.pickle", "wb")
    pickle.dump(self.habitaciones, serializarHabitaciones)
    serializarHabitaciones.close()


if __name__ == '__main__':

    serializar()