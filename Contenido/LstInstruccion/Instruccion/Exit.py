from ..ABCInstruccion import Instruccion

from Contenido.LstInstruccion.ABCInstruccion import Ts

class Exit(Instruccion):

    def __init__(self):
        pass

    def ejecutar(self):
        global Ts
        Ts.exit_exec=0
        return  "exit"

    def str_arbol(self):
        rst = str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "EXIT" + "\"]\n"
        return rst

    def detener_ejecucion(self):
        return 1