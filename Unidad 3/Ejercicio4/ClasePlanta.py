
from ClaseEmpleado import Empleado

class Planta(Empleado):
    __sueldobasico = 0
    __antiguedad = 0

    def __init__(self, dni, nombre, direccion, telefono, sueldobasico, antiguedad):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldobasico = sueldobasico
        self.__antiguedad = antiguedad

    def calcularSueldo(self):
        return self.__sueldobasico + (self.__sueldobasico* 0.01)* self.__antiguedad

    def getSueldobasico(self):
        return self.__sueldobasico

    def getAntiguedad(self):
        return self.__antiguedad
    
    def __str__(self) -> str:
        cadena = 'Dni: '+ self.getDni() +'\n'
        cadena += 'Nombre: '+ self.getNombre()+',Direccion:'+self.getDireccion() +',Telefono:'+self.getTelefono() + ', Sueldo Basico:'+ self.__sueldobasico  +', Antiguedad: '+self.__antiguedad +'\n'
        cadena += 'Sueldo: ' + self.calcularSueldo()
        return cadena
