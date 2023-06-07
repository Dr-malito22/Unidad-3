import numpy as np
import csv
from ClaseSabor import Sabor

class ManejadorSabor:
    __cantidad = 0
    __dimension = 0
    __incremento = 0

    def __init__(self, dimension = 0, incremento = 1):
        self.__arregloSabor = np.empty(dimension, dtype = Sabor)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def agregarSabor(self, unSabor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloFlores.resize(self.__dimension)
        self.__arregloSabor[self.__cantidad] = unSabor
        self.__cantidad += 1
        
    def leerArchivo(self):
        archivo = open('sabores.csv')
        reader = csv.reader(archivo, delimiter = ';')
        #self.__dimension = len(archivo.readlines())
        for fila in reader:
            idSabor, ingredientes, nombreSabor = fila[0], fila[1], fila[2]
            unSabor = Sabor(idSabor, ingredientes, nombreSabor)
            self.agregarSabor(unSabor)
    
    def buscarSabor(self, nombre):
        unSabor = None
        i = 0
        band = False
        while i < self.__arregloSabor.size and not band:
            if self.__arregloSabor[i].getNombre() == nombre:
                unSabor = self.__arregloSabor[i]
                band = True
            else:
                i += 1
        return unSabor
