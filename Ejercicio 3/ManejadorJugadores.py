


class ManejadorJugadores:
    __ListaJugadores : list


    def __init__(self):
        self.__ListaJugadores = []


    def AgregarJugador(self,jugador):
        self.__ListaJugadores.append(jugador)
    