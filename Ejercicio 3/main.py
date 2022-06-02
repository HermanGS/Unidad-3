from joblib import PrintTime
from ManejadorEquipos import Manejador_Equipos
from ManejadorJugadores import ManejadorJugadores
from ManejadorContratos import ManejadorContratos

if __name__ == '__main__':

    ME = Manejador_Equipos()
    MJ = ManejadorJugadores()
    MC = ManejadorContratos()


    ME.lecturaArchivos()
    ME.MostrarArreglo()
    print("\n")
    MJ.IngresoArchivo()
    MJ.MostrarListaJugadores()


