from ClaseLista import Lista
from ClaseObjectEncoder import ObjectEncoder
from ClaseMenu import Menu
from ClaseUsado import Usado


if __name__ == '__main__':
    menu = Menu()
    jsonF = ObjectEncoder()
    diccionario = jsonF.leerJSONArchivo('Ejercicio6\ autos.json')
    listaAparatos = jsonF.decodificarDiccionario(diccionario)

    print('Seleccione una opcion')
    print('1. Insertar un auto en la colección en una posición determinada.')
    print('2. Agregar un auto a la colección (solicitar el tipo de auto, y luego los datos que correspondan).')
    print('3. Dada una posición de la Lista: Mostrar por pantalla qué tipo de auto se encuentra almacenado en dicha posición.')
    print('4. Mostrar la cantidad de autos.')

    print('5. Mostrar la marca de todos los autos.')
    print('6. Mostrar para todos los autos que la empresa tiene a la venta, marca, modelo e importe de venta.')
    print('7. Almacenar los objetos de la colección Lista en el archivo “autos.json”.')
    opcion = input('\nIngrese una opcion: ')
    while opcion != '8':
        menu.opcion(opcion, listaAparatos)
        opcion = input('\nIngrese una opcion (8 para finalizar): ')
    print('\nSalió del Programa\n')
