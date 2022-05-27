import csv
from ast import While
from Facultad import Facultad
from Carrera import Carrera

class ManejadorFacultades:
    __ListaFacultades = []

    def __init__(self):
        self.__ListaFacultades = []

    
    def Prueba(self):
        Facultad()
        Carrera()
        Facu = Facultad()

    def Mostrar(self):
        for Facultad in self.__ListaFacultades:
            print(Facultad)
            for j in Facultad.retornaListaCarreras():
                print()

    def lecturaArchivos(self):
            archivo = open(r'C:\Users\HermanGS\Desktop\UNIVERSIDAD\Segundo año\Programación Orientada a Objetos\Unidad 3\Ejercicios\Ejercicio 1\Facultades.csv')
            reader = csv.reader( archivo, delimiter = ',' )
            fila=next(reader)
            bandera = True
            print('Facultad')
            while bandera: # CARGA FACULTADES
                #print(fila)
                print("\n")
                
                #Carga Facultades
                cod = int(fila[0])
                nombre = str(fila[1])
                direccion = str(fila[2])
                localidad = str(fila[3])
                telefono = str(fila[4])
                Facu = Facultad(cod,nombre,direccion,localidad,telefono)
                self.__ListaFacultades.append(Facu)
                print(Facu)
                print("\n")
                print('Carreras:')
                filaCarrera=next(reader)

                while bandera and fila[0]==filaCarrera[0]: #CARGA CARRERAS
                    #Carga Carreras
                    #print(filaCarrera)
                    print("\n")
                    cod = int(filaCarrera[1])
                    nombre = str(filaCarrera[2])
                    titulo = str(filaCarrera[3])
                    duracion = str(filaCarrera[4])
                    tipog = str(filaCarrera[5])
                    Carre = Carrera(cod,nombre,titulo,duracion,tipog)
                    print(Carre)
                    Facu.añadirCarrera(Carre)
                    #Facu.__ListaCarrera.append(Carre)
                    print("\n")
                    '''print("sexooooooooooooooooooooooooooooooooooooooooo")'''
                    try:
                        filaCarrera=next(reader)
                    except StopIteration:
                        bandera=False
                fila=filaCarrera
            archivo.close()