from array import ArrayType
from Equipo import Equipo
from Jugador import Jugador
from ManejadorJugadores import ManejadorJugadores
import csv
import numpy as np


class Manejador_Equipos:
    __arrayEquipos = ArrayType

    def __init__(self):
        self.__arrayEquipos = np.empty(0,dtype=Equipo)


    def prueba(self):
        jug = Jugador()

    def lecturaArchivos(self):
        archivo = open('Equipos.csv')
        reader = csv.reader( archivo, delimiter = ',' )
        fila=next(reader)
        print("Fila cero : ",fila)
        for fila in range(int(fila)):
            cod = int(fila[0])
            nom = str(fila[1])
            ciudad = str(fila[2])
            Equi = Equipo(cod,nom,ciudad)

            self.__arrayEquipos = np.append(self.__arrayEquipos,Equi)

        archivo.close()


    def MostrarArreglo(self):
        for i in self.__arrayEquipos:
            print(i)
    
    