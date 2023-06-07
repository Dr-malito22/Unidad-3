from ClaseObjectEncoder import ObjectEncoder
from ClaseUsado import Usado
from ClaseNuevo import Nuevo


class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.opcion5,
                            '6':self.opcion6,
                            '7':self.opcion7,
                            }

    def opcion(self,op, listaAutos):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op == '1' or op == '2' or op == '3' or op == '4' or op == '5' or op == '6' or op == '7':
            func(listaAutos)
        else:
            func()
    
    def opcion1(self, listaAutos):
        elemento = Usado('Duna', 4, 'blanco', 199999, 'Fiat', 'ACG109', 1990, 250000)
        element = Nuevo('Palio', 6, 'plata', 500000, 'Fiat','base')
        pos = int(input('Posicion: '))
        try:
            listaAutos.insertarElemento(elemento, pos)
            listaAutos.insertarElemento(element,pos)
        except IndexError:
            print('Error de indice')

    def opcion2(self, listaAparatos):
        elemento1 = Usado('Duna', 4, 'blanco', 199999, 'Fiat', 'ACG109', 1990, 250000)
        elemento2 = Nuevo('Palio', 6, 'plata', 500000, 'Fiat','base')
       
        ''''
        tipo = input('Tipo: ')
        tipo.lower()
        if tipo == 'usado':
            modelo = input('Modelo: ')
            cantidadpuertas = input ('Puertas')            
            color = input('Color: ')
            precio  = input('precio: ')
            marca = input('Marca: ')
            patente = input('patente: ')
            año = input('Año: ')
            kilometraje = input('Kilometraje: ')
            elemento = Usado(modelo, cantpuertas, color, precioVenta, marca, patente, kilometraje, patente, anio, kilometraje)
        elif tipo == 'nuevo':
            modelo = input('Modelo: ')
            cantidadpuertas = input ('Puertas')            
            color = input('Color: ')
            precio  = input('precio: ')
            marca = input('Marca: ')
            version = input('Version: ')
            elemento = Nuevo(modelo, cantpuertas, color, precioVenta, marca, version)
        '''
        listaAutos.agregarElemento(elemento1)
        listaAutos.agregarElemento(elemento2)
       

    
    def opcion3(self, listaAutos):
        print('Ingrese posicion')
        pos = int(input('Posicion'))
        try:
            au = listaAutos.consultarTipoAuto(pos)
        except IndexError:
            print('Posicion no encontrada')

        print(f'El auto en la posicion {pos} es {type(ap).__name__}')


    def opcion4(self, listaAutos):
        print('Ingrese marca')
        marca = input('Marca: ')
        cant = listaAutos.calcularCantidadPorMarca(marca)
        print(f'Cantidad de autos marca {marca} es {cant}')

    def opcion5(self, listaAutos):
        l = listaAutos.obtenerAutos()
        print('Autos:')
        if len(l) > 0:
            for au in l:
                print(f'{au.getMarca()}')

    def opcion6(self, listaAutos):
        listaAutos.mostrarDatos()

    def opcion7(self, listaAutos):
        jsonF = ObjectEncoder()
        d = listaAutos.toJSON()
        jsonF.guardarJSONArchivo(d,'Ejercicio6\ autos.json')
