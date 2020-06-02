from ..ABCInstruccion import Instruccion, ListaInstruccion
from Contenido.LstInstruccion.Registro.Valor import Valor


class Goto(Instruccion):
    etique: str = None

    def __init__(self, etique: str):
        self.etique = etique

    def ejecutar(self):
        pass

    def str_arbol(self):
        rst = str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "Goto ( " + self.etique + " )\"]\n"
        return rst
