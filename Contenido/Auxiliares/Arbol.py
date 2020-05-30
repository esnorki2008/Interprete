from .LstInstruccion import ABCInstruccion


class Arbol:
    raiz: ABCInstruccion.Instruccion() = None

    def __init__(self):
        self.raiz = ABCInstruccion.Instruccion()
        super().__init__()

    def recorrer_grafica(self) -> str:
        return self.raiz.str_arbol();
