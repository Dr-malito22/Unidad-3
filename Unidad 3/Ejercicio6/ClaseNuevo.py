
from ClaseAuto import Auto

class Nuevo(Auto):
    __version = '' 
    
    def __init__(self, modelo, cantpuertas, color, precioVenta, marca,version):
        super().__init__(modelo, cantpuertas, color, precioVenta, marca)
        self.__version = version
        
    def getImporteVenta(self):
        importe = int(self.getPrecioBase())
        if self.__version == "base":
            importe += importe * 10/100
        if self.__version == "full":
            importe += importe * 10/100 + importe * 2/100        

        return importe

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                modelo = self.getModelo(), 
                cantidadpuertas = self.getCantpuertas(),
                color = self.getColor(),
                precio = self.getImporteVenta(),
                marca = self.getMarca()
                version =self.__version
            )
        )
        return d
