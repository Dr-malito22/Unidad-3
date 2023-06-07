class Helado:
    __gramos = 0.0
    __precio = 0.0
    __venta=[]
    def __init__(self, gramos,precio):
        self.__gramos = gramos
        self.__precio = precio        
        self.__venta = []

    def agregarventa(self, unHelado):
        self.__helados.append(unHelado)

    def getHelados(self):
        return self.__helados

    def getGramos(self):
        return self.__gramos
    def getPrecio(self):
        return self.__precio
