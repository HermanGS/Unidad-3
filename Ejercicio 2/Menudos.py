class Menudos:
    pass

    def __init__(self):
        pass

    def MientrasOP(self):
        print("Ingrese la opcion que quiera elegir : ")
        print("Elija : 1  para <<<  Registrar un ramo vendido (instancia de la clase ramo), solicitando las flores que lo que se pondrán en el ramo. \n Elija : 2 para <<< Mostrar el nombre de las 5 flores  más pedidas en un ramo, considerando todos los ramos vendidos. \n Elija : 3 para <<< Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos. ")    
    
    def ChoseOP(self,op,MF,MR):
        if op==1:
            self.op1(MF,MR)
        if op==2:
            self.op2(MF,MR)
        if op==3:
            self.op3(MF,MR)
        if op==4:
            self.op4()

    def op1(self,MF,MR):
        print("Registrar Un Ramo Vendido :")
        
        
        pass
    def op2(self,MF,MR):
        pass
    def op3(self,MF,MR):
        pass
    def op4(self):
        print(">>> Fin Programa <<<")