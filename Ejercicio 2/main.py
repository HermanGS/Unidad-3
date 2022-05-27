from re import M
from Menudos import Menudos
from ManejadorFlores import ManejadorFlores
if __name__ == '__main__':
    print("hola loco")
    
    MF = ManejadorFlores()
    MF.IngresoArchivo()
    MF.MostrarArreglo()

    print("\n")
    Menuc = Menudos()
    op = -1
    while (op != 4):
        print("\n")
        Menuc.MientrasOP()
        op = int(input("Ingresar opcion : "))
        Menuc.ChoseOP(op)
        while op>4:
            print("\n")
            print("Opcion INCORRECTA (mayor a 4, elegir una opcion menor entre 1 y 4)")
            Menuc.MientrasOP()
            op = int(input("Ingresar opcion : "))

