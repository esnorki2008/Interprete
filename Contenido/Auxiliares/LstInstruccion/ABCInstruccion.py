from abc import ABC, abstractmethod


class Instruccion(ABC):
    def __Init__(self, *args):
        pass

    @abstractmethod
    def str_arbol(self):
        pass

    @abstractmethod
    def ejecutar(self):
        pass


class ListaInstruccion(Instruccion):
    lst = []

    def __Init__(self, lst: []):
        self.lst=lst

    def ejecutar(self):
        for elemento in self.lst:
            elemento.ejecutar()

    def str_arbol(self):
        pass


class ExpresionDoble(Instruccion):
    hijo_izquierdo: Instruccion = None
    hijo_derecho: Instruccion = None
    tipo_operacion: Instruccion = None

    def __Init__(self, hijo_izquierdo: Instruccion, tipo_operacion: Instruccion, hijo_derecho: Instruccion):
        self.hijo_derecho = hijo_izquierdo
        self.hijo_derecho = hijo_derecho
        self.tipo_operacion = tipo_operacion

    def str_arbol(self):
        pass

    def ejecutar(self):
        print("No Implementado")


class Valor:
    contenido: object = None
    tipo: int = 0

    def __Init__(self, contenido: object, tipo: int):
        self.contenido = contenido
        self.tipo = tipo

    def evaluar(self):
        return self.contenido


class ExpresionSimple(Instruccion):
    contenido: Valor = None
    tipo: int = 0

    def __Init__(self, contenido: Valor):
        self.contenido = contenido

    def str_arbol(self):
        pass

    def ejecutar(self):
        return self.contenido


class Print(Instruccion):
    contenido: Instruccion = None

    def __Init__(self, contenido: Instruccion):
        self.contenido = contenido

    def str_arbol(self):
        pass

    def ejecutar(self):
        print(self.contenido.ejecutar())
