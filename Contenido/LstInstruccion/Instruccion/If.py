from ..ABCInstruccion import Instruccion, ListaInstruccion
from Contenido.LstInstruccion.Registro.Valor import Valor
from Contenido.LstInstruccion.ABCInstruccion import Ts


class If(Instruccion):
    cuerpo: Instruccion = None
    booleano: Instruccion = None
    deten: int = 0

    def detener_ejecucion(self):
        return self.deten

    def __init__(self, booleano: Instruccion, cuerpo: Instruccion):
        self.cuerpo = cuerpo
        self.booleano = booleano

    def ejecutar(self):
        condicion: Valor = self.booleano.ejecutar()
        if condicion.tipo == 0:
            if condicion.dar_valor() >= 1:
                return self.cuerpo.ejecutar()
        else:
            global Ts
            Ts.cargar_error("En La Condicional Del IF Se Necesita El Tipo ENTERO ", 0,self.tupla)

    def str_arbol(self):
        rst = str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "If  )\"]\n"
        rst += self.booleano.str_arbol()
        rst += str(id(self)) + " -> " + str(id(self.booleano)) + "\n"
        rst += self.cuerpo.str_arbol()
        rst += str(id(self)) + " -> " + str(id(self.cuerpo)) + "\n"
        return rst
