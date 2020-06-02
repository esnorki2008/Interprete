from ..ABCInstruccion import Instruccion, ListaInstruccion
from Contenido.LstInstruccion.Registro.Valor import Valor


class If(Instruccion):
    cuerpo: Instruccion = None
    booleano: Instruccion = None

    def __init__(self,booleano:Instruccion,cuerpo:Instruccion):
        self.cuerpo=cuerpo
        self.booleano=booleano

    def ejecutar(self):
        pass

    def str_arbol(self):
        rst = str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "If  )\"]\n"
        rst += self.booleano.str_arbol()
        rst += str(id(self)) + " -> " + str(id(self.booleano)) + "\n"
        rst +=self.cuerpo.str_arbol()
        rst += str(id(self)) + " -> " + str(id(self.cuerpo)) + "\n"
        return rst
