from ..ABCInstruccion import Instruccion, ListaInstruccion
from Contenido.LstInstruccion.Registro.Valor import Valor


class Unset(Instruccion):
    vaue: Valor = None

    def __init__(self, vaue: Valor):
        self.vaue = vaue

    def ejecutar(self):
        pass

    def str_arbol(self):
        rst = str(
            id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "Unse( " + self.vaue.dar_identificador() + " )\"]\n"

        return rst
