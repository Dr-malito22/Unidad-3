import abc
from abc import ABC

class Empleado(ABC):
    __dni = ''
    __nombre = ''
    __direccion = ''
    __telefono = ''
 
    def __init__(self, dni, nombre, direccion, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono   
    @abc.abstractmethod 
    def calcularSueldo(self, nombre, telefono):
        pass

    def getdni(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre
    
    def getDireccion (self):
        return self.__direccion

    def getTelefono (self):
        return self.__telefono
