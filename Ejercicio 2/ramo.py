
class ramo:
    __tamaño = ""

    def __init__(self,tamaño):
        self.__tamaño = tamaño
        

    def __str__(self):
        return "Tamaño : {}".format(self.__tamaño)

    def getTamaño(self):
        return self.__tamaño