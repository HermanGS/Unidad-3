
class Carrera:
    __Codigo = None
    __Nombre = None
    __Titulo = None
    __Duracion = None
    __TipoGrado = None

    def __init__(self,codigo,nombre,titulo,duracion,tipogrado):
        self.__Codigo = codigo
        self.__Nombre = nombre
        self.__Titulo = titulo
        self.__Duracion = duracion
        self.__TipoGrado = tipogrado

    def __str__(self) -> str:
        return "{},{},{},{},{}".format(self.__Codigo,self.__Nombre,self.__Titulo,self.__Duracion,self.__TipoGrado)
