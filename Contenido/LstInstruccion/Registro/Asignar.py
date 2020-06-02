
from ..ABCInstruccion import Instruccion, ListaInstruccion,Ts
from Contenido.LstInstruccion.Registro.Valor import Valor
from Contenido.LstInstruccion.ABCInstruccion import Instruccion


class Asignar(Instruccion):
    destino: str = None
    origen: Instruccion = None

    def __init__(self, destino: str , origen : Instruccion):
        self.destino = destino
        self.origen = origen

    def ejecutar(self):
        global  Ts
        vaue :Valor=self.origen.ejecutar()
        Ts.variable_cambiar_valor(self.destino,vaue)


    def str_arbol(self):
        rst = self.origen.str_arbol()
        rst += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\""+" ASIGNAR: $" + self.destino  + "\"]\n"
        rst += str(id(self)) + " -> " + str(id(self.origen)) + "\n"
        return rst
