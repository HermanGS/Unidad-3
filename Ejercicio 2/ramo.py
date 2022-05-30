from flores import flores

class ramos:
    __tamaño = 0
    __tipo_de_tamaño = ""
    __ListaDeFlores = []

    def __init__(self,tamaño,flor =  None):
        self.__tamaño = tamaño
        if self.__tamaño == 1 or self.__tamaño == 2:
            self.__tipo_de_tamaño = 'Chico'
        if self.__tamaño == 3:
            self.__tipo_de_tamaño = 'Mediano'
        if self.__tamaño == 4:
            self.__tipo_de_tamaño = 'Grande'
        self.__ListaDeFlores = []

    def AgregarFlor(self,flor):
        self.__ListaDeFlores.append(flor)
    
    def __str__(self):
        return "Tamaño : {}".format(self.__tamaño)

    def str2(self):
        return "Tamaño : {} \n Lista De Flores :  \n{}".format(self.__tamaño,self.MostrarListaDeFlores())

    def getTamaño(self):
        return self.__tamaño

    def MostrarListaDeFlores(self):
        for i in self.__ListaDeFlores:
            print(i)
        