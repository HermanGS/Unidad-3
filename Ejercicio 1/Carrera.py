
class Carrera:
    __Codigo_Facultad = None
    __Codigo_Carrera = None
    __Nombre = None
    __Titulo = None
    __Duracion = None
    __TipoGrado = None

    def __init__(self,codigoFacultad,codigoCarrera,nombre,titulo,duracion,tipogrado):
        self.__Codigo_Facultad = codigoFacultad
        self.__Codigo_Carrera = codigoCarrera
        self.__Nombre = nombre
        self.__Titulo = titulo
        self.__Duracion = duracion
        self.__TipoGrado = tipogrado

    def __str__(self) -> str:
        return "{},{},{},{},{},{}".format(self.__Codigo_Facultad,self.__Codigo_Carrera,self.__Nombre,self.__Titulo,self.__Duracion,self.__TipoGrado)

    def getInfoRapida(self):
        return "Nombre : {:7}   /   Duracion : {:7}".format(self.__Nombre,self.__Duracion)

    def getCodigoFacultad(self):
        return self.__Codigo_Facultad

    def getCodigoCarrera(self):
        return self.__Codigo_Carrera
    
    def getNombre(self):
        return self.__Nombre