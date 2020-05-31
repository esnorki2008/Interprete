from ..Valor import Valor


def sumar(param1, param2):
    tipo_resultante = 0
    suma = Valor(param1.dar_valor() + param2.dar_valor(), tipo_resultante)
    return suma
