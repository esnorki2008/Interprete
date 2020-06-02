
from  Contenido.TablaDeSimbolos import  TablaDeSimbolos
from abc import ABC, abstractmethod
from .Operacion.Aritmetica import Division
from .Operacion.Aritmetica import Resta
from .Operacion.Aritmetica import Multiplicacion
from .Operacion.Aritmetica import Suma
from Contenido.LstInstruccion.Registro.Valor import Valor
from Contenido.LstInstruccion.Operacion.Bitwise import AndBinario
from Contenido.LstInstruccion.Operacion.Bitwise import OrBinario
from Contenido.LstInstruccion.Operacion.Bitwise import XorBinario
from Contenido.LstInstruccion.Operacion.Bitwise import ShiftDerecha
from Contenido.LstInstruccion.Operacion.Bitwise import ShiftIzquierda

Ts = TablaDeSimbolos()

class Instruccion(ABC):
    def __init__(self, *args):
        pass

    @abstractmethod
    def str_arbol(self):
        pass

    @abstractmethod
    def ejecutar(self):
        pass


class ListaEtiqueta(Instruccion):
    lst = []

    def __init__(self, lst: []):
        self.lst = lst

    def ejecutar(self):
        for elemento in self.lst:
            elemento.ejecutar()

    def str_arbol_encabezado(self):
        contenido = " digraph G { \n"
        contenido += self.str_arbol()
        contenido += "}"
        return contenido

    def str_arbol(self):
        concatenar = ""
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "LISTA_ETIQUETA" + "\"]\n"
        for elemento in self.lst:
            concatenar += elemento.str_arbol()
            concatenar += str(id(self)) + " -> " + str(id(elemento)) + "\n"
        return concatenar

    def agregar(self, nuevo: Instruccion):
        self.lst.append(nuevo)


class ListaInstruccion(Instruccion):
    lst = []

    def __init__(self, lst: []):
        self.lst = lst

    def ejecutar(self):
        for elemento in self.lst:
            elemento.ejecutar()

    def str_arbol(self):
        concatenar = ""
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "CUERPO" + "\"]\n"
        for elemento in self.lst:
            concatenar += elemento.str_arbol()
            concatenar += str(id(self)) + " -> " + str(id(elemento)) + "\n"
        return concatenar

    def agregar(self, nuevo: Instruccion):
        self.lst.append(nuevo)


class ExpresionDoble(Instruccion):
    hijo_izquierdo: Instruccion = None
    hijo_derecho: Instruccion = None
    tipo_operacion: Instruccion = None

    def __init__(self, hijo_izquierdo: Instruccion, tipo_operacion: Instruccion, hijo_derecho: Instruccion):
        self.hijo_izquierdo = hijo_izquierdo
        self.hijo_derecho = hijo_derecho
        self.tipo_operacion = tipo_operacion

    def str_arbol(self):
        nodo_str = self.hijo_izquierdo.str_arbol() + "\n"
        nodo_str += self.hijo_derecho.str_arbol() + "\n"
        nodo_str += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + str(self.tipo_operacion) + "\"]\n"
        nodo_str += str(id(self)) + " -> " + str(id(self.hijo_izquierdo)) + "\n"
        nodo_str += str(id(self)) + " -> " + str(id(self.hijo_derecho)) + "\n"

        return nodo_str

    def ejecutar(self):
        resultado = None
        val_izq = self.hijo_izquierdo.ejecutar()
        val_der = self.hijo_derecho.ejecutar()
        # Aritmeticos
        if self.tipo_operacion == "+":
            resultado = Suma.sumar(val_izq, val_der)
        elif self.tipo_operacion == "-":
            resultado = Resta.restar(val_izq, val_der)
        elif self.tipo_operacion == "*":
            resultado = Multiplicacion.multiplicar(val_izq, val_der)
        elif self.tipo_operacion == "/":
            resultado = Division.dividir(val_izq, val_der)
        # Bit a bit
        elif self.tipo_operacion == "&":
            resultado = AndBinario.and_binario(val_izq, val_der)
        elif self.tipo_operacion == "|":
            resultado = OrBinario.or_binario(val_izq, val_der)
        elif self.tipo_operacion == "^":
            resultado = XorBinario.xor_binario(val_izq, val_der)
        elif self.tipo_operacion == "<<":
            resultado = ShiftIzquierda.shift_izquierdo(val_izq, val_der)
        elif self.tipo_operacion == ">>":
            resultado = ShiftDerecha.shift_derecho(val_izq, val_der)
        else:
            print("Operacion No Detectada   " + self.tipo_operacion)
        return resultado


class ExpresionSimple(Instruccion):
    contenido: Valor = None
    tipo: int = 0

    def __init__(self, contenido: Valor):
        self.contenido = contenido

    def str_arbol(self):
        nodo_str = str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + str(self.contenido.dar_valor()) + "\"]\n"
        return nodo_str

    def ejecutar(self):
        return self.contenido


class Imprimir(Instruccion):
    contenido: Instruccion = None

    def __init__(self, contenido: Instruccion):
        self.contenido = contenido

    def str_arbol(self):
        nodo_str = str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "Imprimir" + "\"]\n"
        nodo_str += str(id(self)) + " -> " + str(id(self.contenido)) + "\n"
        nodo_str += self.contenido.str_arbol()
        return nodo_str

    def ejecutar(self):
        vaue: Valor = self.contenido.ejecutar()
        print(vaue.dar_valor())
