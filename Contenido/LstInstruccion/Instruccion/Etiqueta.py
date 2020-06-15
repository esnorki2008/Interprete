from ..ABCInstruccion import Instruccion, ListaInstruccion


class Etiqueta(Instruccion):
    lst: ListaInstruccion = None
    nombre: str = None
    tengo_retorno = False
    tengo_parametros = False

    def __init__(self, lst: ListaInstruccion, nombre: str):
        self.lst = lst
        self.nombre = nombre
        self.tengo_retorno = False
        self.tengo_parametros = False

    def determinar_tipo_funcion(self, lst: []):
        self.tengo_retorno=self.lst.determinar_tipo_funcion(lst)

    def paso_a_paso_ejecutar(self, ins: int):

        tama = len(self.lst.lst)
        if ins >= tama:
            return None
        else:
            exec = self.lst.lst[ins].ejecutar()
            #print(exec)
            if exec != None:
                return exec

            return 1

    def ejecutar(self):
        exec = self.lst.ejecutar()
        return exec

    def buscar_var_referencia(self,nombre):
        if self.lst.buscar_var_referencia(nombre) is not None:
            return  self.nombre
        else:
            return None

    def str_arbol(self):
        rst = self.lst.str_arbol()
        rst += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + str(self.nombre) + "\"]\n"
        rst += str(id(self)) + " -> " + str(id(self.lst)) + "\n"
        return rst
