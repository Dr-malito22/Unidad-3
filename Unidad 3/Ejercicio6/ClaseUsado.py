from ClaseAuto import Auto

class Usado(Auto):
    __patente = ''
    __anio = 0
    __kilometraje = 0
    


    def __init__(self, modelo, cantpuertas, color, precioVenta, marca, patente, kilometraje, patente, anio, kilometraje):
        super().__init__(modelo, cantpuertas, color, precioVenta, marca)
        self.__patente = patente
        self.__anio = anio
        self.__kilometraje = kilometraje
        

    def getImporteVenta(self, anioActual):
        importe = int(self.getPrecioBase())
        if self.__kilometraje < 100000:
            importe -= (importe * 1/100 * (anioActual - self.__anio)) - (importe * 2/100)
        else:
            importe -= (importe * 1/100 * (anioActual - self.__anio))
        return importe

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                modelo = self.getModelo(), 
                cantidadpuertas = self.getCantpuertas()
                color = self.getColor(),
                precio = self.getImporteVenta(anioActual),
                marca = self.getMarca(),
                patente = self.__patente,
                anio = self.__anio,
                kilometraje = self.__kilometraje,
            )
        )
        return d
