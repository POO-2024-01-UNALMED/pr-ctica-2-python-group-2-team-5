from iuMain.interfazGrafica.ventanaInicio import abrirVentanaInicio
from src.gestorAplicacion.administracionHospital.Hospital import Hospital


if __name__ == '__main__':
    hospitalAndino = Hospital()

    abrirVentanaInicio(hospitalAndino)