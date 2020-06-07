
from ..ABCInstruccion import Instruccion, ListaInstruccion,Ts
from Contenido.LstInstruccion.Registro.Valor import Valor
from Contenido.LstInstruccion.ABCInstruccion import Instruccion


class VariableValor(Instruccion):
    destino: str = None
    lst : [] = None

    def __init__(self, destino: str ):
        self.destino = destino
        self.lst=[]

    def indices(self, lst :[]):
        self.lst = lst

    def ejecutar(self):

        global  Ts

        if len(self.lst)== 0 :
            return Ts.variable_obtener_valor(self.destino)
        else :

            tope = len(self.lst) - 1
            lista_invertida = []
            for index in range(tope, -1, -1):
                lista_invertida.append(self.lst[index].ejecutar().dar_valor())

            return  Ts.arreglo_obtener_valor(self.destino,lista_invertida)

    def corchetes(self):
        if len(self.lst) == 0:
            return ""
        rst = str(id(self)) + " -> " + str(id(self.lst)) + "\n"
        rst += str(id(self.lst)) + "[shape=rect,sides=4,skew=.4,label=\"" + " INDICES:" + "\"]\n"
        for item in self.lst:
            rst += str(id(self.lst)) + " -> " + str(id(item)) + "\n"
            rst +=  item.str_arbol()
        return rst

    def str_arbol(self):
        rst = str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\""+" VALOR VARIABLE: $" + self.destino  + "\"]\n"
        rst +=self.corchetes()
        return rst
