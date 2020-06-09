from ..ABCInstruccion import Instruccion, ListaInstruccion
from Contenido.LstInstruccion.Registro.Valor import Valor
from Contenido.LstInstruccion.ABCInstruccion import Ts

class Goto(Instruccion):
    etique: str = None

    def __init__(self, etique: str):
        self.etique = etique

    def determinar_tipo_funcion(self):
        return self.etique

    def ejecutar(self):
        #Ts.ejecutar_etiqueta(self.etique)
        return  self.etique

    def str_arbol(self):
        rst = str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "Goto ( " + self.etique + " )\"]\n"
        return rst

    def detener_ejecucion(self):
        return 1