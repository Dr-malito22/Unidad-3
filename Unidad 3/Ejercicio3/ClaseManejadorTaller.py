from re import T
import numpy as np
from ClaseTaller import Taller

class ManejadorTaller:
    __dimension = 0
    __cantidad = 0
    __incremento = 0

    def __init__(self, dimension = 1, incremento = 1):
        self.__arregloTaller = np.empty(dimension, dtype = Taller)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def agregarTaller(self, unTaller):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloTaller.resize(self.__dimension)
        self.__arregloTaller[self.__cantidad]=unTaller
        self.__cantidad += 1

    def leerArchivo(self):
        unTaller = Taller(1, 'Carpinteria',15,1500)
        otroTaller = Taller(2,'Pinura', 9, 1000)
        self.agregarTaller(unTaller)
        self.agregarTaller(otroTaller)

    def buscarTallerPorId(self):
        unTaller = None
        print('Ingrese el identificador')
        for i in range(self.__arregloTaller.size):
            print(f'{i + 1} - {self.__arregloTaller[i]}')
        id = int(input('Id: '))
        unTaller = self.__arregloTaller[id - 1]
        return unTaller

    def buscarTallerPorNombre(self):
        band = False
        i = 0
        unTaller = None
        print('Ingrese el nombre')
        nombre = input('Nombre: ')
        while i < self.__arregloTaller.size and not band:
            if self.__arregloTaller[i].getNombre() == nombre:
                unTaller = self.__arregloTaller[i]
                band = True
        return unTaller

    
