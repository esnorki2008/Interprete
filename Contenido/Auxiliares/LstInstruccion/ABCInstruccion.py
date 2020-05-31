from abc import ABC, abstractmethod
from .Operacion import Suma
from .Valor import  Valor
class Instruccion(ABC):
    def __init__(self, *args):
        pass

    @abstractmethod
    def str_arbol(self):
        pass

    @abstractmethod
    def ejecutar(self):
        pass


class ListaInstruccion(Instruccion):
    lst = []

    def __init__(self, lst: []):
        self.lst = lst

    def ejecutar(self):
        for elemento in self.lst:
            elemento.ejecutar()

    def str_arbol(self):
        concatenar = ""
        for elemento in self.lst:
            concatenar = + elemento.str_arbol()
        return concatenar

    def agregar(self, nuevo: Instruccion):
        self.lstappend(nuevo)


class ExpresionDoble(Instruccion):
    hijo_izquierdo: Instruccion = None
    hijo_derecho: Instruccion = None
    tipo_operacion: Instruccion = None

    def __init__(self, hijo_izquierdo: Instruccion, tipo_operacion: Instruccion, hijo_derecho: Instruccion):
        self.hijo_izquierdo = hijo_izquierdo
        self.hijo_derecho = hijo_derecho
        self.tipo_operacion = tipo_operacion

    def str_arbol(self):
        pass

    def ejecutar(self):
        resultado=None
        val_izq = self.hijo_izquierdo.ejecutar()
        val_der = self.hijo_derecho.ejecutar()

        if self.tipo_operacion == "+":
           resultado=Suma.sumar(val_izq,val_der)
        return resultado






class ExpresionSimple(Instruccion):
    contenido: Valor = None
    tipo: int = 0

    def __init__(self, contenido: Valor):
        self.contenido = contenido

    def str_arbol(self):
        pass

    def ejecutar(self):
        return self.contenido


class Imprimir(Instruccion):
    contenido: Instruccion = None

    def __init__(self, contenido: Instruccion):
        self.contenido = contenido

    def str_arbol(self):
        pass

    def ejecutar(self):
        print(self.contenido.ejecutar())
