
from Contrato import Contrato

class Equipo:
    __nombre = ""
    __ciudad = ""
    __ListaContratos = []

    def __init__(self,nombre,ciudad):
        self.__nombre = nombre
        self.__ciudad =ciudad

    def __str__(self):
        return "Nombre : {}, Ciudad : {}".format(self.__nombre,self.__ciudad)


    def getNombre(self):
        return self.__nombre
    
    def FirmarContrato(self,jugador,fechaInicio,fechaFin,pagoMensual):
        ContratoTemp = Contrato(jugador,self,fechaInicio,fechaFin,pagoMensual)
        self.__ListaContratos.append(ContratoTemp)
        return ContratoTemp

    def ListarVencimientos(self):
        for contrato in self.__ListaContratos:
            if contrato.mesesalvencimiento()<=6:
                print(contrato.getJugador())

    def CalculoImporte(self):
        sumaimporte = 0.0
        for i in range(len(self.__ListaContratos)):
            sumaimporte = sumaimporte + self.__ListaContratos[i].getPagoMensual()
        return sumaimporte

