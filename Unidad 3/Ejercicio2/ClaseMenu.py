from ClaseHelado import Helado
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            }

    def opcion(self,op, manejadorSabor, manejadorHelados):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op == '1' or op == '2' or op == '3':
            func(manejadorSabor, manejadoHelados)
        else:
            func()
    
    def opcion1(self, manejadorSabor, manejadorHelados):
        print('ingresar grs de helado')
        tamaño = input('Gramos: ')
        unHelado = Helado(gramos)
        print('ingrese nombre de un sabor para agregar o fin para finalizar')
        nombre = input('Nombre: ')
        while nombre != 'fin':
            unSabor = manejadorSabor.buscarSabor(nombre)
            if unSabor != None:
                unHelado.agregarSabor(unSabor)
                print('Sabor agregado con exito')
            else:
                print('Sabor no encontrado. Reintente')
            nombre = input('Nombre: ')
        manejadorHelado.agregarVenta(unSabor)

    def opcion2(self, manejadorSabor, manejadorHelados):
        manejadorHelados.heladosMasVendidos()

    def opcion3(self, manejadorSabor, manejadorHelados):
        tipo = input('Tipo de helado: ')

        manejadorHelados.heladosVendidosTipo(tipo)
