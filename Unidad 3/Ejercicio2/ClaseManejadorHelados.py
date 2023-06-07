
class ManejadorHelados:
    __ventasHelados = []

    def __init__(self):
        self.__ventasHelados = []

    def agregarVenta(self, unHelado):
        self.__ventasHelados.append(unHelado)
            
    def HeladosMasVendidos(self):
        diccionario = {}

        for helados in self.__ventasHelados:
            for sabor in helados.getHelados():
                if not sabor.getNombre() in diccionario.keys():
                    diccionario.setdefault(sabor.getNombre(), 1)
                else: 
                    diccionario[sabor.getNombre()] += 1
        
        l = list(diccionario.values())
        l.sort(reverse=True)
        top5 = l[0 : 5]

        for clave, valor in diccionario.items(): 
            if valor in top5:
                print(f'{clave} : {valor}')

    def heladosVendidosTipo(self, tipo):
        heladosVendidos = []
        for helado in self.__ventasHelados:
            if helado.getGramos() == tipo:
                for sabor in helado.getSabor():
                    if not sabor.getNombre() in heladosVendidos:
                        heladoVendidos.append(sabor)
        
        for sabor in heladosVendidos:
            print(sabor.getNombre())
