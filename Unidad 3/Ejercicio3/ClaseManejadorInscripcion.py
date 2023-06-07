import numpy as np
import csv 
from ClaseInscripcion import Inscripcion


class ManejadorInscripcion:
    __dimension = 0
    __cantidad = 0
    __incremento = 0

    def __init__(self, dimension = 1, incremento = 1):
        self.__arregloInscripcion = np.empty(dimension, dtype = Inscripcion)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def agregarInscripcion(self, unaInscripcion):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloInscripcion.resize(self.__dimension)
        self.__arregloInscripcion[self.__cantidad]=unaInscripcion
        self.__cantidad += 1

    def guardarArchivo(self):      
        myFile = open('Ejercicio3/Talleres.csv', 'w')
        writer = csv.writer(myFile, delimiter=';')
        for i in range(self.__arregloInscripcion.size):
            persona = self.__arregloInscripcion[i].getPersona()
            taller = self.__arregloInscripcion[i].getTaller()
            dni = persona.getDni()
            nombretaller = taller.getNombre()
            fecha = self.__arregloInscripcion[i].getFecha()
            pago = self.__arregloInscripcion[i].getPago()
            writer.writerow([dni, taller, fecha, pago])
        print("Escritura completa")

            

    
