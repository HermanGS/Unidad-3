


import csv
from Jugador import Jugador

class ManejadorJugadores:
    __ListaJugadores : list


    def __init__(self):
        self.__ListaJugadores = []


    def AgregarJugador(self,jugador):
        self.__ListaJugadores.append(jugador)


    def IngresoArchivo(self):
        archivo = open(r'C:\Users\HermanGS\Desktop\Carpeta POO Compartiada\POO\Unidad 3\Ejercicios\Unidad-3-main\Ejercicio 3\Jugadores.csv')
        reader = csv.reader(archivo,delimiter=',')
        
        for fila in reader:
            nombre = str(fila[0])
            dni = int(fila[1])
            ciudadNatal = str(fila[2])
            paisOrigen = str(fila[3])
            fechaNacimiento = str(fila[4])
            Jugad = Jugador(nombre,dni,ciudadNatal,paisOrigen,fechaNacimiento)
            self.__ListaJugadores.append(Jugad)
        archivo.close()

    def MostrarListaJugadores(self):
        print("Lista De Jugadores : ")
        for i in self.__ListaJugadores:    
            print(i)
        
    def BuscarJugador(self,Nombre):
        valor = None
        i=0
        while i<len(self.__ListaJugadores) and Nombre != self.__ListaJugadores[i].getNombre():
            i=i+1
        if i<len(self.__ListaJugadores):
            valor = self.__ListaJugadores[i]
        return valor