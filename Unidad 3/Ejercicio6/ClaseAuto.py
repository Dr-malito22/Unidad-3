
class Auto:
    __modelo = ''
    __cantpuertas=0
    __color = ''
    __precioVenta = 0
    __marca = ''
    def __init__(self, modelo, cantpuertas, color, precioVenta, marca):
        self.__modelo = modelo
        self.__cantpuertas = cantpuertas
        self.__color = color
        self.__precioVenta = precioVenta
        self.__marca = marca
    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo
    
    def getColor(self):
        return self.__color
    
    def getCantpuertas(self):
        return self.__cantpuertas

    def getPrecioBase(self):
        return self.__precioVenta



