
class Equipo:
    __nombre = ""
    __ciudad = ""
    

    def __init__(self,nombre,ciudad):
        self.__nombre = nombre
        self.__ciudad =ciudad

    def __str__(self):
        return "Nombre : {}, Ciudad : {}".format(self.__nombre,self.__ciudad)
    
    
