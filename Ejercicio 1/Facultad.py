from Carrera import Carrera

class Facultad:
    __Codigo = None
    __Nombre = None
    __Direccion = None
    __Localidad = None
    __telefono = None
    __ListaCarrera = []

    def __init__(self,codigo = None, Nombre = None, Direccion = None, Localidad = None, telefono = None,listaCarreras = []):
        self.__Codigo = codigo
        self.__Nombre = Nombre
        self.__Direccion = Direccion
        self.__Localidad = Localidad
        self.__telefono = telefono
        
        self.__ListaCarrera = []

        
        
             

    def RetornaListaCarreras(self):
        return self.__ListaCarrera

    def añadirCarrera(self,Carrera):
        if(type(Carrera)==Carrera):
            self.__ListaCarrera.append(Carrera)

    def __str__(self):
        return  ("({}),{},{},{},{}".format(self.__Codigo,self.__Nombre,self.__Direccion,self.__Localidad,self.__telefono))



