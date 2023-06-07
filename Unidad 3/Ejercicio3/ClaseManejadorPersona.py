
class ManejadorPersona:
    __listaPersona = []

    def __init__(self):
        self.__listaPersona = []

    def agregarPersona(self, unaPersona):
        self.__listaPersona.append(unaPersona)

    def buscarPersona(self, dni):
        unaPersona = None
        band = False
        i = 0
        while i < len(self.__listaPerosna) and not band:
            if self.__listaPersona[i].getDni() == dni:
                unaPersona = self.__listaPersona[i]
                band = True
        return unaPersona

        
