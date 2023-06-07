
from ClaseEmpleado import Empleado

class Contratado(Empleado):
    __fechaInicio = ''
    __fechaFinalizacion = ''    
    __cantidadHoras = 0
    __valorHora = 0.0

    def __init__(self, dni, nombre, direccion, telefono, fechaInicio, fechaFinalizacion, cantidadHoras,valorHora):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fechaInicio = fechaInicio
        self.__fechaFinalizacion = fechaFinalizacion
        self.__cantidadHoras
        self.__valorHora = valorHora

    def calcularSueldo (self):
        return self.__cantidadHoras * self.__valorHora

    def getFechainicio (self):
        return self.__fechaInicio
    def getFechafinalizacion (self):
        return self.__fechaFinalizacion
    def getHoras(self):
        return self.__cantidadHoras
    def getValor (self):
        return self.__valorHora
    def __str__(self):
        cadena = 'DNI: '+ self.getDni() +'\n'
        cadena += 'Nombre: '+ self.getNombre()+', Direccion: '+ self.getDireccion()+', Telefono: '+ self.getTelefono()+', Fecha inicio contrato: '+self.__fechaInicio ++', Fecha finalizacion contrato: '+ self.__fechaFinalizacion +', Cantidad Horas: '+self.__cantidadHoras +', Valor hora: '+self.__valorHora  +'\n'
        return cadena
