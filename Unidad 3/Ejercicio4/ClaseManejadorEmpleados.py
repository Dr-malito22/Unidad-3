
import numpy as np
import csv
from ClaseEmpleado import Empleado
from ClasePlanta import Planta
from ClaseContratado import Contratado
from ClaseExterno import Externo
class ManejadorEmpleado:
    __dimension = 0
    __cantidad = 0
    __incremento = 0

    def __init__(self, dimension):
        self.__arregloEmpleado = np.empty(dimension, dtype = Empleado)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = 1

    def agregarEmpleado(self, unEmpleado):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloEmpleado.resize(self.__dimension)
        self.__arregloEmpleado[self.__cantidad] = unEmpleado
        self.__cantidad += 1

    def leerArchivo(self):
        archivo = open('planta.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            dni, nombre, direccion, telefono, sueldobasico, antiguedad = fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]
            unEmpleado = Planta(dni, nombre, direccion, telefono, sueldobasico, antiguedad)
            self.agregarEmpleado(unEmpleado)
        archivo.close()

        archivo = open('contratados.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            dni, nombre, direccion, telefono, fechaInicio, fechaFinalizacion, cantidadHoras,valorHora= fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7]
            unEmpleado = Contratado(dni, nombre, direccion, telefono, fechaInicio, fechaFinalizacion, cantidadHoras,valorHora)
            self.agregarEmpleado(unEmpleado)
        archivo.close()
        
        archivo = open('externos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            dni, nombre, direccion, telefono, tarea, fechaInicio, fechaFinalizacion, viatico, costoObra, seguro = fila[0], fila[1], fila[2], fila[3],fila[4], fila[5], fila[6],fila[7], fila[8], fila[9]
            unEmpleado = Externos(dni, nombre, direccion, telefono, tarea, fechaInicio, fechaFinalizacion, viatico, costoObra, seguro)
            self.agregarEmpleado(unEmpleado)
        archivo.close()
    
    def buscarMenorSueldoplanta(self):
        min = 9999999
        aux = None
        for i in range(self.__arregloEmpleados.size):
            if isinstance(self.__arregloEmpleados[i], Planta):
                x = self.__arregloEmpleados[i].calcularSueldo()
                if x < min:
                    min = x
                    aux = self.__arregloEmpleados[i]
        return aux 
            

    def buscarMenorSueldocontratado(self):
        min = 9999999
        aux = None
        for i in range(self.__arregloEmpleados.size):
            if isinstance(self.__arregloEmpleados[i], Contratado):
                x = self.__arregloEmpleados[i].calcularSueldo()
                if x < min:
                    min = x
                    aux = self.__arregloEmpleados[i]
        return aux 
    def buscarMenorSueldoexterno(self):
        min = 9999999
        aux = None
        for i in range(self.__arregloEmpleados.size):
            if isinstance(self.__arregloEmpleados[i], Externo):
                x = self.__arregloEmpleados[i].calcularSueldo()
                if x < min:
                    min = x
                    aux = self.__arregloEmpleados[i]
        return aux 

            
    def buscarSueldo(self):
        min = None
        aux = None
        for i in range(self.__arregloEmpleados.size):
            min = self.__arregloEmpleados[0].calcularSueldo()
            aux = self.__arregloEmpleados[i]

        
