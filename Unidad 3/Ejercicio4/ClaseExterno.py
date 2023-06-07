from ClaseEmpleado import Empleado

class Externo(Empleado):
    __tarea = ''
    __fechaInicio = ''
    __fechaFinalizacion = ''
    __viatico = 0.0
    __costoObra = 0.0
    __seguro = 0.0


    def __init__(self, dni, nombre, direccion, telefono, tarea, fechaInicio, fechaFinalizacion, viatico, costoObra, seguro):
        super().__init__(dni, nombre, direccion, telefono)
        self.__tarea = tarea
        self.__fechaInicio = fechaInicio
        self.__fechaFinalizacion = fechaFinalizacion
        self.__viatico = viatico
        self.__costoObra = costoObra
        self.__seguro = seguro

    def calcularSueldo(self):
        return self.__costoObra - self.__viatico - self.__seguro 

    def getTarea (self):
        return self.__tarea    
    def getFechainicio (self):
        return self.__fechaInicio
    def getFechafinalizacion (self):
        return self.__fechaFinalizacion
    def getViatico(self):
        return self.__viatico
    def getCostoobra (self):
        return self.__costoObra
    def getSeguro (self):
        return self.__seguro
    def __str__(self):
        cadena = 'DNI: '+ self.getDni() +'\n'
        cadena += 'Nombre: '+ self.getNombre()+', Direccion: '+ self.getDireccion()+', Telefono: '+ self.getTelefono()+', Fecha inicio contrato: '+self.__fechaInicio ++', Fecha finalizacion contrato: '+ self.__fechaFinalizacion +', Costo de obra: '+self.__costoObra +', Viatico: '+self.__viatico  +', Seguro: '+self.__seguro +'\n'
        return cadena
