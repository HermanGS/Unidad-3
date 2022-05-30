
class Jugador:
    __codEquipo : int
    __codJugador : int 
    __nombre = ""
    __dni = 0
    __ciudad_natal = ""
    __pais_origen = ""
    __fechaNacimiento = ""


    def __init__(self,codEquipo,codJugador,nombre,dni,ciudad_natal,pais_origen,fechaNacimiento):
        self.__codEquipo = codEquipo
        self.__codJugador = codJugador
        self.__nombre = nombre
        self.__dni = dni
        self.__ciudad_natal = ciudad_natal
        self.__pais_origen = pais_origen
        self.__fechaNacimiento = fechaNacimiento

    def __str__(self) -> str:
        return "CodigoEquipo : {}, CodigoJugador : {} ,Nombre : {},Dni : {},Ciudad Natal : {},Pais Origen : {},Fecha Nacimiento : {}".format(self.__codEquipo,self.__codJugador,self.__nombre,self.__dni,self.__ciudad_natal,self.__pais_origen,self.__fechaNacimiento)
