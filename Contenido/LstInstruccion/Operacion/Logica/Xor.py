from Contenido.LstInstruccion.Registro.Valor import Valor


def xor_entero(param1: Valor, param2: Valor):
    from Contenido.LstInstruccion.ABCInstruccion import Ts
    global Ts
    tipo_resultante = 0
    rst = 0
    # Solo Se Pueden Valores Numericos
    if param1.tipo == 0:
        if param2.tipo == 0:
            # Entero
            tipo_resultante = 0
            if param1.dar_valor() != param2.dar_valor():
                rst = 1
            else:
                rst = 0

        else:
            Ts.cargar_error(
                "Error En XOR Con Tipos: " + param1.dar_tipo_str() + "," + param2.dar_tipo_str(), 0,
                ((0, 0)))
            print("Error En La Operacion XOR Con Tipos: " + param1.dar_tipo_str() + "," + param2.dar_tipo_str())

    else:
        Ts.cargar_error(
            "Error En XOR Con Tipos: " + param1.dar_tipo_str() + "," + param2.dar_tipo_str(), 0,
            ((0, 0)))
        print("Error En La Operacion XOR Con Tipos: " + param1.dar_tipo_str() + "," + param2.dar_tipo_str())

    return Valor(rst, tipo_resultante)
