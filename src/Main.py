from gestorAplicacion.administracionHospital.Hospital import Hospital
from iuMain.funcionalidades.MenuFuncionalidades import MenuFuncionalidades


def mostrarMenuInicial(hospital)
    while True:
        print("MENU INICIAL")
        print("1. Servicios para Paciente")
        print("2. Gestionara registros")
        print("3. Salir")

        opcionSeleccionada = int(input("Seleccione una opcion: "))
        if opcionSeleccionada == 1:
            MenuFuncionalidades.menuFuncionalidades(hospital)

        elif opcionSeleccionada == 2:
            MenuGes






if __name__ == '__main__':
    hospital = Hospital()
    mostrarMenuInicial(hospital)



