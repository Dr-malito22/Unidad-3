class Sabor:
    __idsabor = 0
    __ingredientes = ''
    __nombreSabor = ''
    
    def __init__(self, idSabor, ingredientes, nombreSabor):
        self.__idSabor = idSabor
        self.__ingredientes = ingredientes
        self.__nombreSabor = nombreSabor
        
    def getNombre(self):
        return self.__nombreSabor
