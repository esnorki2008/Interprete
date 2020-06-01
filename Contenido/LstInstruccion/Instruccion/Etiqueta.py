from ..ABCInstruccion import Instruccion, ListaInstruccion


class Etiqueta(Instruccion):
    lst: ListaInstruccion = None
    nombre: str = None

    def __init__(self, lst: ListaInstruccion, nombre: str):
        self.lst = lst
        self.nombre = nombre

    def ejecutar(self):
        self.lst.ejecutar()



    def str_arbol(self):
        rst = self.lst.str_arbol()
        rst += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" +str(self.nombre) + "\"]\n"
        rst += str(id(self)) + " -> " + str(id(self.lst)) + "\n"
        return rst
