import csv
from distutils import archive_util
from flores import flores
import numpy as np

class ManejadorFlores:
    __ArregloFLores = []

    def __init__(self):
        self.__ArregloFLores = np.empty(0,dtype=flores)


    def AgregarFlor(self,flor):
        self.__ArregloFLores = np.append(self.__ArregloFLores,flor)


    def IngresoArchivo(self):
        archivo = open(r'C:\Users\HermanGS\Desktop\UNIVERSIDAD\Segundo año\Programación Orientada a Objetos\Unidad 3\Ejercicios\Ejercicio 2\flores.csv')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            numero = int(fila[0])
            nombre = str(fila[1])
            color = str(fila[2])
            descripcion = str(fila[3])
            ObjetoFlores = flores(numero,nombre,color,descripcion)
            self.AgregarFlor(ObjetoFlores)
        archivo.close()

    def MostrarArreglo(self):
        for i in self.__ArregloFLores:
            print(i)