from Equipo import Equipo
from Jugador import Jugador
from ManejadorJugadores import ManejadorJugadores
import csv
import numpy as np


class Manejador_Equipos:
    __arrayEquipos = []

    def __init__(self):
        self.__arrayEquipos = np.empty(0,dtype=Equipo)


    def prueba(self):
        jug = Jugador()

    def lecturaArchivos(self):
        archivo = open(r'C:\Users\HermanGS\Desktop\Carpeta POO Compartiada\POO\Unidad 3\Ejercicios\Unidad-3-main\Ejercicio 3\Equipos.csv')
        reader = csv.reader( archivo, delimiter = ',' )
        fila=next(reader)
        cantidad = int(fila[0])
        print("Ingreso de Datos del Archivo ...")
        print("Cantidad de Equipos: ",cantidad)
        print("\n")
        i=0
        while i<cantidad:
                fila = next(reader)
                nom = str(fila[0])
                ciudad = str(fila[1])
                Equi = Equipo(nom,ciudad)
                self.__arrayEquipos = np.append(self.__arrayEquipos,Equi)
                i=i+1
        archivo.close()

    def Espacio(self):
        print("\n")
        print("\n")
        print("\n")

    
    def MostrarArreglo(self):
        print("Equipos :")
        for i in self.__arrayEquipos:
            print(i)
    

    def BuscarEquipo(self,Nombre):
        valor = None
        i=0
        while i<len(self.__arrayEquipos) and Nombre != self.__arrayEquipos[i].getNombre():
            i=i+1
        if i<len(self.__arrayEquipos):
            valor = self.__arrayEquipos[i]
        return valor


    def BuscarEquipoIndice(self,NombreEquipo):
        valor = None
        i=0
        while i<len(self.__arrayEquipos) and NombreEquipo != self.__arrayEquipos[i].getNombre():
            i=i+1
        if i<len(self.__arrayEquipos):
            valor = i
            return valor


    def VencimientosEquipo(self,NombreEquipo):
        indice = self.BuscarEquipoIndice(NombreEquipo)
        if indice != None:
            print("Equipo Encontrado:   {}".format(self.__arrayEquipos[indice]))
            self.__arrayEquipos[indice].ListarVencimientos()
        else:
            print("No se encontró el nombre del Equipo Buscado por Teclado")

    def Calcular_ImporteTotal(self,NombreEquipo):
        indice = self.BuscarEquipoIndice(NombreEquipo)
        if indice != None:
            print("Equipo Encontrado:   {}".format(self.__arrayEquipos[indice]))
            importeTotal = self.__arrayEquipos[indice].CalculoImporte()
            print("Importe Total de los Contratos que Posee Con los Jugadores : {} ".format(importeTotal))
        else:
            print("No se encontró el nombre del Equipo Buscado por Teclado")

