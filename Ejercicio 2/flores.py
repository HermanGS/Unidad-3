


class flores:
    __numero = 0
    __nombre = ""
    __color = ""
    __descripcion =  ""

    def __init__(self,numero,nombre,color,descripcion):
        #self.__numero = numero
        self.__numero = self.getNumeroFlor()
        self.__nombre = nombre
        self.__color = color
        self.__descripcion = descripcion
        self.__ContadorFama = 0
        # self.__VendidaEnGrande = False
        


    def __str__(self) -> str:
        return "{}, {}, {}, {}".format(self.__numero,self.__nombre,self.__color,self.__descripcion)

    def MostrarfloresVersionFama(self):
        print("{}, {}, {}, {}, Veces que se ha vendido : {}".format(self.__numero,self.__nombre,self.__color,self.__descripcion,self.__ContadorFama))

    # def MostrarfloresFamaYGrande(self):
    #     print("{}, {}, {}, {}, Veces que se ha vendido : {} , Se ha vendido en un Ramo de 4 : {}".format(self.__numero,self.__nombre,self.__color,self.__descripcion,self.__ContadorFama,self.__VendidaEnGrande))

    @classmethod
    def getNumeroFlor(cls):
        cls.__numero = cls.__numero + 1
        return cls.__numero
    
    def getNombre(self):
        return self.__nombre
    
    def getColor(self):
        return self.__color

    def getDescripcion(self):
        return self.__descripcion

    def ContarFlorVendida(self):
        self.__ContadorFama = self.__ContadorFama + 1
        
    def getFama(self):
        return self.__ContadorFama

    # def setGrandeTrue(self):
    #     self.__VendidaEnGrande = True
    
    # def getBoolGrande(self):
    #     return self.__VendidaEnGrande