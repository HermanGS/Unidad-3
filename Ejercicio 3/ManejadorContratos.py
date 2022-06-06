import numpy as np
from Contrato import Contrato 
from ManejadorEquipos import Manejador_Equipos
from ManejadorJugadores import ManejadorJugadores
import csv

class ManejadorContratos:
    __arrayContratos : list

    def __init__(self):
        self.__arrayContratos = np.empty(0,dtype=Contrato)

    def AgregarContrato(self,contrato):
            self.__arrayContratos = np.append(self.__arrayContratos,contrato)

    def MostrarContratos(self):
        print("\nLongitud Arreglo Contratos : ",len(self.__arrayContratos))
        print("LISTA de TODOS LOS CONTRATOS: \n")
        for i in self.__arrayContratos:
            print("\n")
            print(i)


    def BuscarInfoJugadorDNI(self,DNI):
        i=0
        valor = None
        while i<len(self.__arrayContratos) and DNI != self.__arrayContratos[i].getJugador().getDNI():
            i=i+1
        if i<len(self.__arrayContratos):
            print("Equipo del Jugador con DNI : ",DNI)
            print(self.__arrayContratos[i].getEquipo())
            print("Fecha de Vencimiento del Contrato : {}".format(self.__arrayContratos[i].getFechaFin()))
        else:
            print("No se encontro ningun Jugador con ese DNI")

    def Repetir_Busqueda_DNI(self):
        i=0
        while i!=0:
            i=int(input(""))
        pass

    def Archivo(self):
        archivo = open('ArchivoGenerado.csv','w',newline='')
        writer = csv.writer(archivo,delimiter=',')
        listadelista =[]
        for i in range(len(self.__arrayContratos)):
            dniJugador = self.__arrayContratos[i].getJugador().getDNI()
            nombreEquipo = self.__arrayContratos[i].getEquipo().getNombre()
            FechaInicio = self.__arrayContratos[i].getFechaInicio()
            FechaFin =  self.__arrayContratos[i].getFechaFin()
            PagoMensual = self.__arrayContratos[i].getPagoMensual()
            fila = ",,,,".split(',')
            fila[0] = dniJugador
            fila[1] = nombreEquipo
            fila[2] = FechaInicio
            fila[3] = FechaFin
            fila[4] = PagoMensual
            listadelista.append(fila)
            #print(fila)
        writer.writerows(listadelista)