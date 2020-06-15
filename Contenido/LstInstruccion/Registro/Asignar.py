from ..ABCInstruccion import Instruccion, ListaInstruccion, Ts
from Contenido.LstInstruccion.Registro.Valor import Valor
from Contenido.LstInstruccion.ABCInstruccion import Instruccion


class Asignar(Instruccion):
    destino: str = None
    origen: Instruccion = None
    lst: [] = None

    def __init__(self, destino: str, origen: Instruccion):
        self.destino = destino
        self.origen = origen
        self.lst = []

    def buscar_var_referencia(self, nombre):
        if nombre == self.destino:
            return True
        else:
            return None

    def determinar_tipo_funcion(self):
        if self.destino[0] == "v":
            return "v"
        elif self.destino[0] == "a":
            return "a"
        return None

    def ejecutar(self):
        # print(self.origen)

        vaue: Valor = self.origen.ejecutar()
        global Ts
        if len(self.lst) == 0:

            Ts.variable_cambiar_valor(self.destino, vaue)
        else:
            tope = len(self.lst) - 1
            lista_invertida = []
            for index in range(tope, -1, -1):
                lista_invertida.append(self.lst[index].ejecutar().dar_valor())

            Ts.arreglo_cambiar_valor(self.destino, lista_invertida, vaue)

    def indices(self, lst: []):
        self.lst = lst

    def corchetes(self):
        if len(self.lst) == 0:
            return ""
        rst = str(id(self)) + " -> " + str(id(self.lst)) + "\n"
        rst += str(id(self.lst)) + "[shape=rect,sides=4,skew=.4,label=\"" + " INDICES:" + "\"]\n"
        for item in self.lst:
            rst += str(id(self.lst)) + " -> " + str(id(item)) + "\n"
            rst += item.str_arbol()
        return rst

    def str_arbol(self):
        rst = self.origen.str_arbol()
        rst += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + " ASIGNAR: $" + self.destino + "\"]\n"
        rst += str(id(self)) + " -> " + str(id(self.origen)) + "\n"
        rst += self.corchetes()
        return rst
