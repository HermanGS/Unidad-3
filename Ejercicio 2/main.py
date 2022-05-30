
from re import M
from Menudos import Menudos as Menu
from ManejadorFlores import ManejadorFlores
from ManejadorRamos import ManejadorRamos
if __name__ == '__main__':
    print("hola loco")
    
    MF = ManejadorFlores()
    MF.IngresoArchivo()
    #MF.MostrarArreglo()
    MR = ManejadorRamos()
    MR.RegistrarRamo(MF)
    
    MR.MostrarListaDeRamos()
    MF.MostrarFloresPorFama()
    print("\n")
    MF.Mostrar5floresMasVendidas()
    #print("Mostrar2")
    #MR.MostrarRamos()
    print("\n")
    # MF.MostrarFloresPorFamaYGrande()


    print("\n")
    Menuc = Menu()
    op = -1
    while (op != 4):
        print("\n")
        Menuc.MientrasOP()
        op = int(input("Ingresar opcion : "))
        print("Opcion Elegida -> ",op)
        Menuc.ChoseOP(op,MF,MR)
        while op>4:
            print("\n")
            print("Opcion INCORRECTA (mayor a 4, elegir una opcion menor entre 1 y 4)")
            Menuc.MientrasOP()
            op = int(input("Ingresar opcion : "))

