from Carrera import Carrera

class Facultad:
    __Codigo = None
    __Nombre = None
    __Direccion = None
    __Localidad = None
    __telefono = None
    __ListaCarreras = []

    def __init__(self,codigo = None, Nombre = None, Direccion = None, Localidad = None, telefono = None,listaAuxCarreras = None):
        self.__Codigo = codigo
        self.__Nombre = Nombre
        self.__Direccion = Direccion
        self.__Localidad = Localidad
        self.__telefono = telefono
        self.__ListaCarreras = []
        for i in range(len(listaAuxCarreras)):
            #print("Printeo del i en el __init__ : {}".format(i)) Esto era para verificar si el init cargaba
            self.__ListaCarreras.append(listaAuxCarreras[i])
        
        # Version alternativa de la copia de listas a ver :  Funciona igual por ahora
        #self.__ListaCarreras = listaAuxCarreras.copy() 

        
    def MostrarCarreras(self):
        for i in self.__ListaCarreras:
            print(i)          

    def MostrarCarrerasNOMyDURA(self):
        for i in self.__ListaCarreras:
            print(i.getInfoRapida())

    def RetornaListaCarreras(self):
        return self.__ListaCarreras

    def añadirCarrera(self,Carrera):
        if(type(Carrera)==Carrera):
            self.__ListaCarreras.append(Carrera)

    def __str__(self):
        return  ("({}),{},{},{},{}".format(self.__Codigo,self.__Nombre,self.__Direccion,self.__Localidad,self.__telefono))

    def getNombre(self):
        return self.__Nombre

    def getCodigo(self):
        return self.__Codigo

    def getLocalidad(self):
        return self.__Localidad