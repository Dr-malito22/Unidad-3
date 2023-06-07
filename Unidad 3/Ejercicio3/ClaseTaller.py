from ClaseInscripcion import Inscripcion

class Taller:
    __idTaller = 0
    __nombre = ''
    __vacantes=0
    __montoInscripcion = 0
    __listaInscriptos = []

    def __init__(self, idTaller nombre, vacantes, monoInscipcion):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__listaInscriptos = []

    def agregarInscripto(self, inscriptos):
        self.__listaInscriptos.append(inscriptos)

    def consultarInscriptos(self):
        if len(self.__listaInscriptos) >= 1:
            for inscripcion in self.__listaInscriptos:
                print(inscripcion)
        else:
            print('No existen Inscripciones')

    def obtenerTotal(self):
        total = 0
        for inscripcion in self.__listaInscriptos:
            if inscripcion.getPago == True:            
                total += 1
        print(f'total de las inscripciones pagadas {total}')

    def getNombre(self):
        return self.__nombre
        
    def __str__(self):
        return (f'{self.__nombre}')
