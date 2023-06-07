
class Persona:
    __nombre = ''
    __dni = ''
    __direccion = ''
    __listaInscripcion = []

    def __init__(self, nombre, direccion, dni):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni
        self.__listaInscripcion = []

    def __str__(self):
        return (f'{self.__nombre}')
    
    def getDni(self):
        return self.__dni

    def agregarInscripcion(self, inscripcion):
        self.__listaInscripcion.append(inscripcion)
    
    def consultarContratos(self):
        if len(self.__listaInscripcion) >= 1:
            for contrato in self.__listaInscripcion:
                print (str(inscripcion.getTaller()))
                print(str(inscripcion.getNombre()))
        else: 
            print('No tiene contratos')
