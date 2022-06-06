
class Jugador:
    __nombre = ""
    __dni = 0
    __ciudad_natal = ""
    __pais_origen = ""
    __fechaNacimiento = ""


    def __init__(self,nombre,dni,ciudad_natal,pais_origen,fechaNacimiento):
        self.__nombre = nombre
        self.__dni = dni
        self.__ciudad_natal = ciudad_natal
        self.__pais_origen = pais_origen
        self.__fechaNacimiento = fechaNacimiento

    def __str__(self) -> str:
        return "Nombre : {},Dni : {},Ciudad Natal : {},Pais Origen : {},Fecha Nacimiento : {}".format(self.__nombre,self.__dni,self.__ciudad_natal,self.__pais_origen,self.__fechaNacimiento)

    def getNombre(self):
        return self.__nombre
    
    def getDNI(self):
        return self.__dni