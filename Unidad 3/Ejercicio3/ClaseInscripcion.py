

class Inscripcion:
    __fechaInscripcion = None
    __pago = bool
    
    def __init__(self, fechaInscripcion, pago):
        self.__fechaInscripcion = fechaInscripcion
        self.__pago = pago
        
    def __str__(self) -> str:
        cadena = 'Fecha de inscripcion:'+ str(self.__fechaInscripcion)+'\n' 
        cadena += 'Pago : '+ str(self.__pago)+'\n'
        return cadena

    def getFechaInscripcion(self):
        return self.__fechaInscrpcion

    def getPago(self):
        return self.__pago
