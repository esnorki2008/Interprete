from Contenido.LstInstruccion.Registro.Valor import Valor
import re


def read():
    tipo_resultante = 2
    rst = input()
    x = re.search("^\d+\.\d+$", rst)
    if x is not None:
        tipo_resultante = 1
        rst=float(rst)
    else:
        x = re.search("^\d+$", rst)
        if x is not None:
            tipo_resultante = 0
        rst = int(rst)

    return Valor(rst, tipo_resultante)
