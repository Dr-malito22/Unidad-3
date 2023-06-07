from Ejercicio3.ClaseMenu import Menu
from ClaseManejadorHelados import ManejadorHelados
from ClaseManejadorSabor import ManejadorSabor


if __name__ == '__main__':
    manejadorSabor = ManejadorSabor()
    manejadorHelados = ManejadorHelados()
    manejadorSabor.leerArchivo()
    menu = Menu()

    print('ingrese una opcion')
    print('1. Registrar un helado vendido')
    print('2. Mostrar el nombre de las 5 sabores  más pedidos en un helado')
    print('3. Ingresar por teclado un tipo de helado y mostrar los sabores vendidos en ese tamaño')
    print('4. Finalizar')
    opcion = input('\nIngrese una opcion: ')
    while opcion != '4':
        menu.opcion(opcion, manejadorSabor, manejadorHelados)
        opcion = input('\nIngrese una opcion (4 para finalizar): ')
    print('\nSalió del Programa\n')
