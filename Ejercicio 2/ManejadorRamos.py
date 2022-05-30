from ramo import ramos
from ManejadorFlores import ManejadorFlores

class ManejadorRamos:
    __ListaRamos =  []

    def __init__(self):
        self.__ListaRamos =  []
    
    def AgregarRamoToLista(self,ramo):
        self.__ListaRamos.append(ramo)

    def RegistrarRamo(self,ManejadorFlores):
        print("\n")
        tamanio=-1
        print("Registro de ramos (Creacion) Termina con Cero(0) ")
        print("Tienen que ser ramos de 1 a 4 flores")
        while tamanio != 0:
            tamanio = int(input("Ingrese el tamanio del ramo  : "))
            while tamanio > 4 or tamanio < 0:
                print("OPCION INCORRECTA -> Tienen que ser ramos de 1 a 4 flores")
                tamanio = int(input("Ingrese el tamanio del ramo "))
            if tamanio != 0:
                ramo = ramos(tamanio)
                i=0
                while i<tamanio:
                    print("\n")
                    print("i =",i," , tamanio = ",tamanio)
                    ManejadorFlores.MostrarArreglo()
                    print("\n Elije {} Flor/Flores , por el Numero que llevan :".format(tamanio))
                    num = int(input("Numero elegido :  "))
                    while num < 0 and num >len(ManejadorFlores.RetornaListadeFlores()):
                        print("OPCION INCORRECTA -> Elija entre 1 y {}".format(len(ManejadorFlores.RetornaListadeFlores())))
                        num = int(input("Numero elegido :  "))
                    num = num - 1
                    print("Flor elegida : ",ManejadorFlores.RetornaListadeFlores()[num])
                    ManejadorFlores.RetornaListadeFlores()[num].ContarFlorVendida()
                    # if tamanio == 4 and ManejadorFlores.RetornaListadeFlores()[num].getBoolGrande() != True:
                    #     ManejadorFlores.RetornaListadeFlores()[num].setGrandeTrue()
                    ramo.AgregarFlor(ManejadorFlores.RetornaListadeFlores()[num])
                    i=i+1
                
                self.__ListaRamos.append(ramo)

    def MostrarListaDeRamos(self):
        for i in range (len(self.__ListaRamos)):
            print("Ramo : ",i+1," {} ".format(self.__ListaRamos[i]))

    def MostrarRamos(self):
        print("Longitud : ",len(self.__ListaRamos))
        for i in self.__ListaRamos:
            print(i)

    def MostrarFloresPorTamaño(self,tamaño,ManejadorFlores):
        lista = []
        i=0
        while i<len(ManejadorFlores.RetornaListadeFlores()):
            j=0
            bandera = False
            while j<len(self.__ListaRamos) and bandera == False:
                if self.__ListaRamos[j].getTamaño == tamaño and :
                    pass
                j=j+1
            i=i+1