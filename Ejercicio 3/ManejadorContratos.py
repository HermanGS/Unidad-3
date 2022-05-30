import numpy as np
from Contrato import Contrato 
class ManejadorContratos:
    __arrayContratos = list

    def __init__(self):
        self.__arrayContratos = np.empty(0,dtype=Contrato)

        