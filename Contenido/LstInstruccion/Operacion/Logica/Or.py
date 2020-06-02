from Contenido.LstInstruccion.Registro.Valor import Valor


def or_entero(param1: Valor, param2: Valor):
    tipo_resultante = 0
    rst = 0
    # Solo Se Pueden Valores Numericos
    if (param1.tipo == 0):
        if param2.tipo == 0:
            # Entero
            tipo_resultante = 0
            if (param1.dar_valor() == 1) or (param2.dar_valor() == 1):
                rst = 1
            else:
                rst = 0

        else:
            print("Error En La Operacion || Con Tipos: " + param1.dar_tipo_str() + "," + param2.dar_tipo_str())

    else:
        print("Error En La Operacion || Con Tipos: " + param1.dar_tipo_str() + "," + param2.dar_tipo_str())

    return Valor(rst, tipo_resultante)
