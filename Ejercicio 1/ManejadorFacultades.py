import csv
import re
from traceback import print_tb
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

    def MostrarFacultadesyYyCarreras(self):
        for Facultad in self.__ListaFacultades:
            print(Facultad)
            print("Carreras : \n")
            Facultad.MostrarCarreras()
            print("\n")

    def lecturaArchivos(self):
            archivo = open('Facultades.csv')
            reader = csv.reader( archivo, delimiter = ',' )
            fila=next(reader)
            # print("Printeo de fila : ")
            # print(fila)
            bandera = True
            #print('Facultad')
            while bandera: # CARGA FACULTADES
                cod = int(fila[0])
                nom = str(fila[1])
                direccion = str(fila[2])
                localidad = str(fila[3])
                telefono = str(fila[4])
                # print("\n")
                # print("Aca deberia de salir una facultad xdddd")
                # print("\n")
                # print('Carreras:')
                filaCarrera=next(reader)
                listaaux = []
                while bandera and fila[0]==filaCarrera[0]: #CARGA CARRERAS
                    #Carga Carreras
                    #print(filaCarrera)
                    codFacultad = int(filaCarrera[0])
                    codCarrera = int(filaCarrera[1])
                    nombre = str(filaCarrera[2])
                    titulo = str(filaCarrera[3])
                    duracion = str(filaCarrera[4])
                    tipog = str(filaCarrera[5])
                    Carre = Carrera(codFacultad,codCarrera,nombre,titulo,duracion,tipog)
                    #print(Carre)
                    listaaux.append(Carre)
                    #Facu.añadirCarrera(Carre)  # No se carga como corresponde
                    #Facu.__ListaCarrera.append(Carre) El atributo es privado, arigato
                    try:
                        filaCarrera=next(reader) # Si no ha llegado a final de archivo
                    except StopIteration: # Solo si llego a final de archivo
                        bandera=False       # Termina con el while Principal
                fila=filaCarrera
                # print("Monstrando las Carreras Cargadas En la lista Aux:")
                # for Carr in listaaux:
                #     print (Carr)
                # #Facu.MostrarCarreras()
                # print("Longitud de la lista aux : ",len(listaaux))
                Facu = Facultad(cod,nom,direccion,localidad,telefono,listaaux)
                #Facu.MostrarCarreras()
                self.__ListaFacultades.append(Facu)
            archivo.close()

    def BuscarFacu(self,cod):  #Funciona pero es For
        indice = None
        for i in self.__ListaFacultades:
            #print("Codigo que se esta comparando : ",i.getCodigo(),"Codigo Ingresado : ",cod)
            if(i.getCodigo() == cod):
                indice = cod
                return indice
        
    def BuscarFacuDos(self,cod):  #Funciona pero este While es igual al For
        indice = None
        i=0
        while i in range(len(self.__ListaFacultades)):
            if (self.__ListaFacultades[i].getCodigo() == cod):
                indice = cod
            i=i+1
        return indice

    def BuscarFacuTres(self,cod): # Funciona Genial y es Mejor que el While que imita al For
        indice = None
        i=0
        while i in range(len(self.__ListaFacultades)) and self.__ListaFacultades[i].getCodigo() != cod:
            i=i+1
        if i<len(self.__ListaFacultades):
            indice = cod
        return indice

    def MostrarFacuEinfo(self,codigodeFacu):
        print("printeo codigo : ",codigodeFacu)
        if (codigodeFacu >= 1 and codigodeFacu <=2):
            indice  = self.BuscarFacuTres(codigodeFacu)
            if indice == None:
                print("No se encontro ninguna Facultad con Codigo : ({})".format(codigodeFacu))
            else:    
                print("Nombre de la Facultad Encontrada: ",self.__ListaFacultades[indice-1].getNombre())
                print("Carreras:")
                self.__ListaFacultades[indice-1].MostrarCarrerasNOMyDURA()
        else:
            print("Codigo Incorrecto")


    def MostrarCarreraPorNombreDos(self,nombre): #Ineficiente
        for i in range(len(self.__ListaFacultades)):
            for j in range(len(self.__ListaFacultades[i].RetornaListaCarreras())):
                print("Nombre de afuera : ",nombre,"nombre de la facultad que se esta comparando : ",self.__ListaFacultades[i].RetornaListaCarreras()[j].getNombre())
                if nombre == self.__ListaFacultades[i].RetornaListaCarreras()[j].getNombre():
                        print("De la Carrera con Nombre : {} \nCodigo de la Facultad / Carrera : ({},{})\n Nombre de la Facultad : {} \n Localidad de la Facultad : {}".format(nombre,self.__ListaFacultades[i].RetornaListaCarreras()[j].getCodigoFacultad(),self.__ListaFacultades[i].RetornaListaCarreras()[j].getCodigoCarrera(),self.__ListaFacultades[i].getNombre(),self.__ListaFacultades[i].getLocalidad()))
            

    
    def MostrarCarreraPorNombre(self,nombre):   #Ineficiente
        i=0
        while i<len(self.__ListaFacultades):
            j=0
            while j<len(self.__ListaFacultades[i].RetornaListaCarreras()):
                print("Nombre de afuera : ",nombre,"nombre de la facultad que se esta comparando : ",self.__ListaFacultades[i].RetornaListaCarreras()[j].getNombre())
                if nombre == self.__ListaFacultades[i].RetornaListaCarreras()[j].getNombre():
                        print("De la Carrera con Nombre : {} \nCodigo de la Facultad / Carrera : ({},{})\n Nombre de la Facultad : {} \n Localidad de la Facultad : {}".format(nombre,self.__ListaFacultades[i].RetornaListaCarreras()[j].getCodigoFacultad(),self.__ListaFacultades[i].RetornaListaCarreras()[j].getCodigoCarrera(),self.__ListaFacultades[i].getNombre(),self.__ListaFacultades[i].getLocalidad()))
                j=j+1
            i=i+1
        pass

    def MostrarCarreraPorNombreTres(self,nombre): #Eficiente Cumple con mis expectativas
        bandera = True
        indice = None
        i=0
        while i in range(len(self.__ListaFacultades)) and bandera == True:
            j=0
            while j in range(len(self.__ListaFacultades[i].RetornaListaCarreras())) and self.__ListaFacultades[i].RetornaListaCarreras()[j].getNombre() != nombre:
                #print("Nombre de afuera : ",nombre,"nombre de la facultad que se esta comparando : ",self.__ListaFacultades[i].RetornaListaCarreras()[j].getNombre())
                j=j+1
            if j<len(self.__ListaFacultades[i].RetornaListaCarreras()):
                bandera = False
                print("De la Carrera con Nombre : {} \nCodigo de la Facultad / Carrera : ({},{})\n Nombre de la Facultad : {} \n Localidad de la Facultad : {}".format(nombre,self.__ListaFacultades[i].RetornaListaCarreras()[j].getCodigoFacultad(),self.__ListaFacultades[i].RetornaListaCarreras()[j].getCodigoCarrera(),self.__ListaFacultades[i].getNombre(),self.__ListaFacultades[i].getLocalidad()))
            else:    
                i=i+1
        
            
        
        return indice
