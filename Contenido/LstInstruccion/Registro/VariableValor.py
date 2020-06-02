
from ..ABCInstruccion import Instruccion, ListaInstruccion,Ts
from Contenido.LstInstruccion.Registro.Valor import Valor
from Contenido.LstInstruccion.ABCInstruccion import Instruccion


class VariableValor(Instruccion):
    destino: str = None


    def __init__(self, destino: str ):
        self.destino = destino


    def ejecutar(self):
        global  Ts
        return Ts.variable_obtener_valor(self.destino)


    def str_arbol(self):
        rst = str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\""+" VALOR VARIABLE: $" + self.destino  + "\"]\n"
        return rst
