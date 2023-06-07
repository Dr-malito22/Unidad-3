

class Auto:
    __modelo = None
    def __init__(self, modelo):
        self.__modelo = modelo

    def esAuto(self):
        i = 0
        j = -len(self.__palabra)
        bandera = True
        while i < abs(j) and bandera:
           if self.__modelo[i] != self.__modelo[j]:
               bandera = False
           else:
               i += 1
               j += 1
        return bandera


    def setAuto(self, nuevoAuto):
        self.__modelo = nuevoAuto
