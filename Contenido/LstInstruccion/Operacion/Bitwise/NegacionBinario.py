from Contenido.LstInstruccion.Registro.Valor import Valor


def negar_binario(param1 : Valor):
    tipo_resultante = 0
    rst = 0
    #Solo Se Pueden Valores Numericos
    if(param1.tipo==0):
        tipo_resultante=param1.tipo
        rst = ~param1.dar_valor()
    else:
        print("Error En La NegacionBinaria Con Tipos: " + param1.dar_tipo_str() )

    return Valor(rst, tipo_resultante)
