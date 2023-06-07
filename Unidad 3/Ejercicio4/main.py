from ClaseManejadorEmpleados import ManejadorEmpleados
from ClaseMenu import Menu
from ClaseEmpleado import Empleado


if __name__ == '__main__':
    
    print('Ingrese cantidad de empleados')
    dimension = int(input('Cantidad'))
    manejadorEmpleados = ManejadorEmpleados(dimension)
    manejadorEmpleados.leerArchivo()
    menu = Menu()

    print('ingrese una opcion')
    print('1. Mostrar sueldos minimos de empleados de planta')
    print('2. Mostrar  sueldos minimos de empleados contratados')
    print('3. Mostrar sueldos minimos de empleados externos.')
    print('4. Mostrar sueldos minimos de empleados')
    print('5. Finalizar')
    opcion = input('\nIngrese una opcion: ')
    while opcion != '5':
        menu.opcion(opcion, manejadorEmpleados)
        opcion = input('\nIngrese una opcion (5 para finalizar): ')
    print('\nSalió del Programa\n')
