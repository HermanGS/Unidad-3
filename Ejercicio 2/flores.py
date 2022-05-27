


class flores:
    __numero = 0
    __nombre = ""
    __color = ""
    __descripcion =  ""

    def __init__(self,numero,nombre,color,descripcion):
        self.__numero = numero
        self.__nombre = nombre
        self.__color = color
        self.__descripcion = descripcion

    def __str__(self) -> str:
        return "{}, {}, {}, {}".format(self.__numero,self.__nombre,self.__color,self.__descripcion)

    def getNumero(self):
        return self.__numero
    
    def getNombre(self):
        return self.__nombre
    
    def getColor(self):
        return self.__color

    def getDescripcion(self):
        return self.__descripcion

        