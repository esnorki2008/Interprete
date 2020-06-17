from Contenido.TablaDeSimbolos import TablaDeSimbolos
from abc import ABC, abstractmethod
from .Operacion.Aritmetica import Division
from .Operacion.Aritmetica import Resta
from .Operacion.Aritmetica import Multiplicacion
from .Operacion.Aritmetica import Suma
from .Operacion.Aritmetica import Mod
from .Operacion.Aritmetica import Negacion
from .Operacion.Aritmetica import Not
from Contenido.LstInstruccion.Registro.Valor import Valor
from Contenido.LstInstruccion.Operacion.Bitwise import AndBinario
from Contenido.LstInstruccion.Operacion.Bitwise import OrBinario
from Contenido.LstInstruccion.Operacion.Bitwise import XorBinario
from Contenido.LstInstruccion.Operacion.Bitwise import ShiftDerecha
from Contenido.LstInstruccion.Operacion.Bitwise import ShiftIzquierda
from Contenido.LstInstruccion.Operacion.Bitwise import NegacionBinario
from Contenido.LstInstruccion.Operacion.Logica import And
from Contenido.LstInstruccion.Operacion.Logica import Or
from Contenido.LstInstruccion.Operacion.Logica import Xor
from Contenido.LstInstruccion.Operacion.Comparacion import Diferente
from Contenido.LstInstruccion.Operacion.Comparacion import Igual
from Contenido.LstInstruccion.Operacion.Comparacion import Mayor
from Contenido.LstInstruccion.Operacion.Comparacion import MayorIgual
from Contenido.LstInstruccion.Operacion.Comparacion import Menor
from Contenido.LstInstruccion.Operacion.Comparacion import MenorIgual
from Contenido.LstInstruccion.Operacion.ValorOperacion import Abs
from Contenido.LstInstruccion.Operacion.ValorOperacion import Read
from Contenido.LstInstruccion.Operacion.ValorOperacion import Array
from Contenido.LstInstruccion.Operacion.Cast import INT
from Contenido.LstInstruccion.Operacion.Cast import FLOAT
from Contenido.LstInstruccion.Operacion.Cast import CHAR

Ts = TablaDeSimbolos()
print("Nueva Tabla")


class Instruccion(ABC):
    tupla: () = (0, 0)

    def n_t(self, tupla: ()):
        self.tupla = tupla

    def determinar_tipo_funcion(self):
        return None

    def __init__(self, *args):
        pass

    @abstractmethod
    def str_arbol(self):
        pass

    @abstractmethod
    def ejecutar(self):
        pass

    def detener_ejecucion(self):
        return 0

    def buscar_var_referencia(self,nombre):
        return  None

class ListaEtiqueta(Instruccion):
    lst = []

    def __init__(self, lst: []):
        self.lst = lst

    def determinar_tipo_funcion(self):
        for item in self.lst:
            item.determinar_tipo_funcion(self.lst)
        return None

    def ejecutar_a_paso(self):
        pass

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

    def determinar_tipo_funcion(self, lst: []):
        var_a = False
        var_v = False
        for item in self.lst:
            ret = item.determinar_tipo_funcion()
            if ret == "a":
                var_a = True
            elif ret == "v":
                var_v = True
            elif ret is not None:
                for aux in lst:
                    if aux.nombre == ret:
                        if aux.tengo_parametros :
                            var_a=True
                        aux.tengo_parametros = var_a
                        var_a = False
                        break;
        return var_v

    def ejecutar(self):
        for elemento in self.lst:
            exec = elemento.ejecutar()
            if exec != None:
                return exec
            # print(elemento.ejecutar())
            # if elemento.detener_ejecucion() == 1:
            # return 1

        return None

    def str_arbol(self):
        concatenar = ""
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "CUERPO" + "\"]\n"
        for elemento in self.lst:
            concatenar += elemento.str_arbol()
            concatenar += str(id(self)) + " -> " + str(id(elemento)) + "\n"
        return concatenar

    def agregar(self, nuevo: Instruccion):
        self.lst.append(nuevo)

    def buscar_var_referencia(self,nombre):
        for elemento in self.lst:
            exec = elemento.buscar_var_referencia(nombre)
            if exec != None:
                return exec
        return None

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
        elif self.tipo_operacion == "%":
            resultado = Mod.modular(val_izq, val_der)
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
        # Logica
        elif self.tipo_operacion == "&&":
            resultado = And.and_entero(val_izq, val_der)
        elif self.tipo_operacion == "||":
            resultado = Or.or_entero(val_izq, val_der)
        elif self.tipo_operacion == "xor":
            resultado = Xor.xor_entero(val_izq, val_der)
        # Comparacion
        elif self.tipo_operacion == "!=":
            resultado = Diferente.diferente(val_izq, val_der)
        elif self.tipo_operacion == "==":
            resultado = Igual.igual(val_izq, val_der)
        elif self.tipo_operacion == ">":
            resultado = Mayor.mayor(val_izq, val_der)
        elif self.tipo_operacion == ">=":
            resultado = MayorIgual.mayor_igual(val_izq, val_der)
        elif self.tipo_operacion == "<":
            resultado = Menor.menor(val_izq, val_der)
        elif self.tipo_operacion == "<=":
            resultado = MenorIgual.menor_igual(val_izq, val_der)
        else:
            print("Operacion DOBLE No Detectada   " + self.tipo_operacion)
        return resultado


class ExpresionSimpleOperacion(Instruccion):
    hijo: Instruccion = None
    tipo_operacion: str = None

    def __init__(self, hijo, tipo_operacion: str):
        self.hijo = hijo
        self.tipo_operacion = tipo_operacion

    def str_arbol(self):
        nodo_str = ""
        if type(self.hijo) != str:
            nodo_str += self.hijo.str_arbol() + "\n"
            nodo_str += str(id(self)) + " -> " + str(id(self.hijo)) + "\n"
        nodo_str += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + str(self.tipo_operacion) + "\"]\n"

        return nodo_str

    def ejecutar(self):
        resultado = None
        vaue: Valor = None

        if self.tipo_operacion != "read" and self.tipo_operacion != "array":
            vaue = self.hijo.ejecutar()

        if self.tipo_operacion == "+":
            resultado = vaue
        elif self.tipo_operacion == "-":
            resultado = Negacion.negar(vaue)
        elif self.tipo_operacion == "!":
            resultado = Not.not_num(vaue)
        elif self.tipo_operacion == "abs":
            resultado = Abs.absoluto(vaue)
        elif self.tipo_operacion == "read":
            resultado = Read.read()
        elif self.tipo_operacion == "array":
            resultado = Array.array()
        elif self.tipo_operacion == "~":
            resultado = NegacionBinario.negar_binario(vaue)
        elif self.tipo_operacion == "int":
            resultado = INT.cast_int(vaue)
        elif self.tipo_operacion == "float":
            resultado = FLOAT.cast_float(vaue)
        elif self.tipo_operacion == "char":
            resultado = CHAR.cast_char(vaue)


        else:
            print("Operacion SIMPLE No Detectada   " + self.tipo_operacion)
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
        if vaue.dar_valor()!="\\n":
            print(vaue.dar_valor())

            global Ts

            if(vaue.tipo==4) :
                Ts.cargar_error("No Se Puede Imprimir Arreglos",0,(0,0))
                return
            Ts.print(vaue.dar_valor())


