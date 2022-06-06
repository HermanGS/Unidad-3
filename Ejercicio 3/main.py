from ManejadorEquipos import Manejador_Equipos
from ManejadorJugadores import ManejadorJugadores
from ManejadorContratos import ManejadorContratos
from Contrato import Contrato


if __name__ == '__main__':

    MEquipos = Manejador_Equipos()
    MEquipos.lecturaArchivos()
    MEquipos.MostrarArreglo()
    
    MEquipos.Espacio()
    MEquipos.Espacio()

    MJugadores = ManejadorJugadores()
    MJugadores.IngresoArchivo()
    MJugadores.MostrarListaJugadores()
    
    MContratos = ManejadorContratos()
    

    #Busqueda Equipo y Busqueda Jugador : Funciona Bien
    NombreEquipo = str(input("Ingrese el Nombre del Equipo : "))
    Eq = MEquipos.BuscarEquipo(NombreEquipo)
    print(Eq)
    print("\n")

    NombreJugador = str(input("Ingrese el Nombre del jugador: "))
    Ju = MJugadores.BuscarJugador(NombreJugador)
    print(Ju)
    print("\n")
    


    i=-1
    while i!=0:
        print("Creacion del contrato, ingrese 0 para Dejar de Crear Contratos")
        print("Para Crear el Contrato : ")
        NombreJugador = str(input("Ingrese el Nombre del jugador: "))
        NombreEquipo = str(input("Ingrese el Nombre del Equipo : "))
        fechaInicio = str(input("Ingrese la FECHA de Inicio : "))
        fechaFinal =  str(input("Ingrese la FECHA de FIN  : "))
        PagoMensual = float(input("Ingrese el PAGO MENSUAL : "))
        
        EquipoTemp = MEquipos.BuscarEquipo(NombreEquipo)
        print("Equipo Encontrado : \n",EquipoTemp)
        JugadorTemp = MJugadores.BuscarJugador(NombreJugador)
        print("Jugador Encontrado : \n",JugadorTemp)
        
        if  EquipoTemp != None and JugadorTemp != None:
            Contrat = EquipoTemp.FirmarContrato(JugadorTemp,fechaInicio,fechaFinal,PagoMensual)
            MContratos.AgregarContrato(Contrat)


        
        else:
            print("No se encontró el Jugador o el Equipo \n Vuelva a Ingresar Los Datos : ")
            print("\n")

        i = int(input("\nIngrese 0 (cero) para Dejar de crear Contratos \nIngrese cualquier tecla para Seguir Creando : "))

    Contrat = MEquipos.BuscarEquipo("Boquita").FirmarContrato(MJugadores.BuscarJugador("Slade Koch"),"15/05/2020","16/07/2022",500.0)
    MContratos.AgregarContrato(Contrat)

    Contrat = MEquipos.BuscarEquipo("Boquita").FirmarContrato(MJugadores.BuscarJugador("Xenos Williams"),"15/12/2021","16/06/2023",600.0)
    MContratos.AgregarContrato(Contrat)

    print("\n")
    print("Contratos Ingresados:")
    MContratos.MostrarContratos()
    print("\n")
    print("\n")

    print("Buscar Informacion de un Jugador por DNI , Equipo y Fecha de Vencimiento : ")
    MContratos.BuscarInfoJugadorDNI(3376478)

    IdEquipo = str(input("Ingrese el Nombre del Equipo para Mostrar todos los Jugadores que poseen \n contratos que Vencerán en 6 meses : "))   
    MEquipos.VencimientosEquipo(IdEquipo)
    print("\n")
    print("\n")
    IdEquipo = str(input("Ingrese el Nombre del Equipo para Calcular y Mostrar el Importe del Contrato de todos los jugadores de un Equipo : "))
    MEquipos.Calcular_ImporteTotal(IdEquipo)

    MContratos.Archivo()





