
class Contrato:
    __fechaInicio = ""
    __fechaFin = ""
    __pagoMensual = 0.0

    def __init__(self,fechaInicio,fechaFin,pagoMensual):
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__pagoMensual = pagoMensual

    def __str__(self):
        return "Fecha Inicio : {},Fecha Fin : {}, Pago Mensual : {}".format(self.__fechaInicio,self.__fechaFin,self.__pagoMensual)