

from tkinter import commondialog


class Menu:
    pass


    def MientrasOP(self):
        print(">>> MENU <<<")
        print("Elija : 1. Ingresar 1 Codigo de Facultad y Mostrar el Nombre de esa Facultad y los Nombres y duracion de cada Carrera de esa Facultad \nElija : 2. Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta. \nElija : 3. >>> Salir del Programa <<<")


    def ChoseOp(self,op,ObjetoManejador):
        if op == 1:
            self.op1(ObjetoManejador)
        if op == 2:
            self.op2(ObjetoManejador)
        if op == 3:
            self.op3()
        
    def op1(self,ObjetoManejador):
        print("\n")
        codigo = int(input("Ingrese el CODIGO de la Facultad (1) o (2)  :  "))
        ObjetoManejador.MostrarFacuEinfo(codigo)
        
    def op2(self,ObjetoManejador):
        print("\n")
        name = str(input("Ingrese un Nombre de Carrera : "))
        # Por si quiere Probar un Nombre Testeado (bien escrito) 
        # ObjetoManejador.MostrarCarreraPorNombreTres("Ingenieria en Alimentos")
        ObjetoManejador.MostrarCarreraPorNombreTres(name)
    def op3(self):
        print(">>> Fin Programa <<<")    