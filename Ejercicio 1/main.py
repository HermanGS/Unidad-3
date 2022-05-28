from ast import While
from operator import imod
from ManejadorFacultades import ManejadorFacultades
from Menu import Menu

if __name__ == '__main__':
    MF = ManejadorFacultades()
    Menuc = Menu()
    print("-------------------------------------------------------------------------------------------")
    print("Ingreso De datos del Archivo ... INICIO")
    print("-------------------------------------------------------------------------------------------")
    MF.lecturaArchivos()

    
    print("-------------------------------------------------------------------------------------------")
    print("Ingreso De datos del Archivo ... TERMINADO")
    print("-------------------------------------------------------------------------------------------")

    print("\n")
    print("-------------------------------------------------------------------------------------------")
    print("Manejo de Datos ya desde las estructuras Cargadas: \n Lista de Facultad y Lista de Carreras de cada Facultad:")
    print("-------------------------------------------------------------------------------------------")
    
    MF.MostrarFacultadesyYyCarreras()
    print("\n")
    
    MF.MostrarFacuEinfo(1)
    print("\n")
    
    
    
    
    name = "Ingenieria Civil"
    MF.MostrarCarreraPorNombreDos(name)
    print("\n")
    MF.MostrarCarreraPorNombre(name)
    print("\n")
    MF.MostrarCarreraPorNombreTres(name)
    
    print("\n")
    op=int(-1)
    while op !=3:
        print("\n")
        Menuc.MientrasOP() 
        op = int(input("Ingrese la opcion Elegida : "))
        Menuc.ChoseOp(op,MF)
        while op>3 or op<1:
            print("\n")
            print("-------------------------------------------------------------------------------------------")
            print("DATO INGRESADO INCORRECTO ELIJA DE NUEVO POR FAVOR (ENTRE 1,2 Y 3)")
            print("-------------------------------------------------------------------------------------------")
            Menuc.MientrasOP()
            op = int(input("Ingrese la opcion Elegida : ")) 

        
        



















