from src.baseDatos.Serializador import Serializador
from src.iuMain.funcionalidades.AgendarCita import AgendarCita # --> TODO: Crear la clase.
from src.iuMain.funcionalidades.AsignarHabitacion import AsignarHabiatcion
from src.iuMain.funcionalidades.Facturacion import Facturacion
from src.iuMain.funcionalidades.FormulaMedica import FormulaMedica
from src.iuMain.funcionalidades.Vacunacion import Vacunacion


class MenuFuncionalidades:
    @staticmethod
    def menuFuncionalidades(hospital):
        print("Menu Funcionalidades")
        print("1. Agendar una cita medica")
        print("2. Generar fórmula médica")
        print("3. Asignar habitación a un paciente")
        print("4. Aplicarse una vacuna")
        print("5. Facturacion")
        print("6. --Regresar al menu inicial--")
        print("7. --Salir--")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            AgendarCita.agendarCita(hospital)

        elif opcion == 2:
            FormulaMedica.formulaMedica(hospital)

        elif opcion == 3:
            AsignarHabiatcion.asignarHabitacion(hospital)
        elif opcion == 4:
            Vacunacion.vacunacion(hospital)
        elif opcion == 5:
            Facturacion.facturacion(hospital)
        elif opcion == 6:
            Serializador.serializar(hospital)
            return hospital
        elif opcion == 7:
            Serializador.serializar(hospital)
            return SystemExit