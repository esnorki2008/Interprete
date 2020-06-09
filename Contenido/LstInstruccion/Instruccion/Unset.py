from ..ABCInstruccion import Instruccion, ListaInstruccion
from Contenido.LstInstruccion.Registro.Valor import Valor


class Unset(Instruccion):
    vaue: str = None
    lst : [] = None

    def __init__(self, vaue: str):
        self.vaue = vaue
        self.lst = []

    def indices(self, lst: []):
        self.lst = lst

    def ejecutar(self):
        from Contenido.LstInstruccion.ABCInstruccion import  Ts
        global  Ts

        tope = len(self.lst) - 1
        lista_invertida = []
        for index in range(tope, -1, -1):
            lista_invertida.append(self.lst[index].ejecutar().dar_valor())

        Ts.eliminar_variable(self.vaue,lista_invertida)

    def str_arbol(self):
        rst = str(
            id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "Unse( " + self.vaue+ " )\"]\n"

        return rst
