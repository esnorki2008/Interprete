from ..ABCInstruccion import Instruccion, ListaInstruccion
from Contenido.LstInstruccion.Registro.Valor import Valor
from Contenido.LstInstruccion.ABCInstruccion import Instruccion


class Asignar(Instruccion):
    destino: str = None
    origen: Instruccion = None

    def __init__(self, destino: str , origen : Instruccion):
        self.destino = destino
        self.origen = origen

    def ejecutar(self):
        pass

    def str_arbol(self):
        rst = self.origen.str_arbol()
        rst += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\""+" ASIGNAR: $" + self.destino  + "\"]\n"
        rst += str(id(self)) + " -> " + str(id(self.origen)) + "\n"
        return rst
