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

    def lecturaArchivos(self,ManejadorJugador):
            archivo = open('Equipos.csv')
            reader = csv.reader( archivo, delimiter = ',' )
            fila=next(reader)
            # print("Printeo de fila : ")
            # print(fila)
            bandera = True
            #print('Facultad')
            while bandera: # CARGA FACULTADES
                cod = int(fila[0])
                nom = str(fila[1])
                ciudad = str(fila[2])
                # print("\n")
                # print("Aca deberia de salir una facultad xdddd")
                # print("\n")
                # print('Carreras:')
                filaJugador=next(reader)
                listaaux = []
                while bandera and fila[0]==filaJugador[0]: #CARGA Jugador
                    #Carga Carreras
                    #print(filaCarrera)
                    codEquipo = int(filaJugador[0])
                    codJugador = int(filaJugador[1])
                    nombre = str(filaJugador[2])
                    dni = int(filaJugador[3])
                    ciudadNatal = str(filaJugador[4])
                    paisOrigen = str(filaJugador[5])
                    fechaNacimiento = str(filaJugador[6])
                    Jugad = Jugador(codEquipo,codJugador,nombre,dni,ciudadNatal,paisOrigen,fechaNacimiento)
                    #print(Carre)
                    
                    listaaux.append(Jugad)
                    #Facu.añadirCarrera(Carre)  # No se carga como corresponde
                    #Facu.__ListaCarrera.append(Carre) El atributo es privado, arigato
                    try:
                        filaJugador=next(reader) # Si no ha llegado a final de archivo
                    except StopIteration: # Solo si llego a final de archivo
                        bandera=False       # Termina con el while Principal
                fila=filaJugador
                # print("Monstrando las Carreras Cargadas En la lista Aux:")
                # for Carr in listaaux:
                #     print (Carr)
                # #Facu.MostrarCarreras()
                # print("Longitud de la lista aux : ",len(listaaux))
                Equi = Equipo(cod,nom,ciudad,listaaux)
                #Facu.MostrarCarreras()
                self.__arrayEquipos = np.append(self.__arrayEquipos,Equi)
            archivo.close()
    