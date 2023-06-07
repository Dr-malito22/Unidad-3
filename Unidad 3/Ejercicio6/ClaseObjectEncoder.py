from ClaseLista import Lista
import json
from pathlib import Path
from ClaseUsado import Usado
from ClaseNuevo import Nuevo



class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'Lista':
                autos = d['autos']
                dAuto = autos[0]
                lista = class_()
                for i in range(len(autos)):
                    dAuto = autos[i]
                    class_name = dAuto.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dAuto['__atributos__']
                    unAuto = class_(**atributos)
                    lista.agregarElemento(unAuto)
            return lista

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario
       
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close() 
