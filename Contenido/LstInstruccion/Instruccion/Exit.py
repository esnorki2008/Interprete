from ..ABCInstruccion import Instruccion


class Exit(Instruccion):

    def __init__(self):
        pass

    def ejecutar(self):
        pass

    def str_arbol(self):
        rst = str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "EXIT" + "\"]\n"
        return rst
