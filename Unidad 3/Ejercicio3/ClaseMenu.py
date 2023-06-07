
from ClaseTaller import Taller
from ClasePersona import Persona
from ClaseInscripcion import Inscripcion
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.opcion5
                            }

    def opcion(self,op ,mTaller, mPersona, mInscripcion):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op == '1' or op == '2' or op == '3' or op == '4' or op == '5' or op == '6':
            func(mTaller, mPersona, mInscripcion)
        else:
            func()
    
    def opcion1(self, mTaller, mPersona, mInscripcion):
        unTaller = mTaller.buscarTallerPorId()
        unaPersona = Persona('Pedro Leons', '25550678', 'Alem 300 Sur')
        fecha =('23/05/2023', '%d/%m/%Y')
        pago=(True)
        unaInscripcion = Inscripcion(fecha, pago, unaPersona, unTaller)

        mPersona.agregarPersona(unaPersona)
        mInscripcion.agregarInscrpcion(unaInscripcion)
        
        unTaller.agregarTaller(unaInscripcion)
        unaPersona.agregarInscripcion(unaInscripcion)

    def opcion2(self, mTaller, mPersona, mInscripcion):
        print('Ingrese el DNI')
        dni = int(input('Dni: '))
        unaPersona = mPersona.buscarPersona(dni)
        if unaPersona != None:
            unaPersona.consultarInscripcion()
        else: 
            print('No se encontro')

    def opcion3(self, mTaller, mPersona, mInscripcion):
        unTaller = mTaller.buscarTallerPorId()
        unTaller.consultarInscripcion()
    
    def opcion4(self, mTaller, mPersona, mInscripcion):
        unTaller = mTaller.buscarTallerPorNombre()
        

    def opcion5(self, mTaller, mPersona, mInscripcion):
        mInscripcion.guardarArchivo()

    
