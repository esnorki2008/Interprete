from ..ABCInstruccion import Instruccion, ListaInstruccion
from Contenido.LstInstruccion.Registro.Valor import Valor


class Unset(Instruccion):
    vaue: Valor = None

    def __init__(self, vaue: Valor):
        self.vaue = vaue

    def ejecutar(self):
        pass

    def str_arbol(self):
        rst = self.lst.str_arbol()
        rst += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "Unset" + "\"]\n"
        rst += str(id(self)) + " -> " + str(id(self.lst)) + "\n"
        return rst
