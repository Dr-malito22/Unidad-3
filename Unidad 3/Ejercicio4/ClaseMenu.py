
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            }

    def opcion(self,op, manejadorEmpleados):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op == '1' or op == '2' or op == '3':
            func(manejadorCalefactor)
        else:
            func()
    
    def opcion1(self, manejadorEmpleados):
        c = manejadorEmpleados.buscarMenorSueldoplanta()
        print (c)

    def opcion2(self, manejadorEmpleados):
        c = manejadorEmpleados.buscarMenorSueldocontratado()
        print(c)
    
    def opcion2(self, manejadorEmpleados):
        c = manejadorCalefactor.buscarMenorSueldoexterno()
        print(c)
        
    def opcion3(self, manejadorEmpleado):
        manejadorEmpleados.buscarSueldo()
