from ..ABCInstruccion import Instruccion, ListaInstruccion
from Contenido.LstInstruccion.Registro.Valor import Valor
from Contenido.LstInstruccion.ABCInstruccion import Ts
from Contenido.LstInstruccion.Registro import VariableValor


class Referencia(Instruccion):
    ref: Valor = None
    deten: int = 0

    def detener_ejecucion(self):
        return self.deten

    def __init__(self, ref: str, lst: []):
        temp = VariableValor.VariableValor(ref)
        temp.indices(lst)
        self.ref = Valor(temp, 5)

    def ejecutar(self):
        return self.ref

    def str_arbol(self):
        rst = str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "If  )\"]\n"
        rst += self.booleano.str_arbol()
        rst += str(id(self)) + " -> " + str(id(self.booleano)) + "\n"
        rst += self.cuerpo.str_arbol()
        rst += str(id(self)) + " -> " + str(id(self.cuerpo)) + "\n"
        return rst
