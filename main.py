from src.gestor_aplicacion.administracion.hospital import Hospital
from src.ui_main.ventana_inicial import ventana_inicial

if __name__ == '__main__':
    hospitalAndino = Hospital()

    ventana_inicial(hospitalAndino)
