import datetime

class Contrato:
    __jugador = None
    __equipo = None 
    __fechaInicio = ""
    __fechaFin = ""
    __pagoMensual = 0.0

    def __init__(self,jugador,equipo,fechaInicio,fechaFin,pagoMensual):
        self.__jugador = jugador
        self.__equipo = equipo
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__pagoMensual = pagoMensual

    def __str__(self):
        return "Jugador: {}, Equipo: {}, Fecha Inicio : {},Fecha Fin : {}, Pago Mensual : {}".format(self.__jugador,self.__equipo,self.__fechaInicio,self.__fechaFin,self.__pagoMensual)


    def getJugador(self):
        return self.__jugador

    def getEquipo(self):
        return self.__equipo

    def getFechaInicio(self):
        return self.__fechaInicio

    def getFechaFin(self):
        return self.__fechaFin

    def getPagoMensual(self):
        return self.__pagoMensual

    def mesesalvencimiento(self):
        mes=0
        fecha=self.getFechaFin().split("/")
        mesfin=int(fecha[1])
        actual=datetime.date.today()
        
        mesactual=int(actual.month)+12*(int(actual.year)-int(fecha[2]))

        mes=mesfin-mesactual
        return mes