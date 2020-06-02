from Contenido.LstInstruccion.Registro.Valor import Valor


def igual(param1: Valor, param2: Valor):
    tipo_resultante = 0
    rst = 0
    # Solo Se Pueden Valores Numericos

    if param1.dar_valor() == param2.dar_valor():
        rst = 1
    else:
        rst = 0

    return Valor(rst, tipo_resultante)
