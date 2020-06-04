from Contenido.LstInstruccion.Registro.Valor import Valor


def absoluto(param1 : Valor):
    tipo_resultante = 0
    rst = 0
    #Solo Se Pueden Valores Numericos
    if(param1.tipo==0):
        rst = abs(param1.dar_valor())
        tipo_resultante=0
    elif param1.tipo==1:
        tipo_resultante = 1
        rst=abs(param1.dar_valor())
    else:
        print("Error En La ABS Con Tipos: " + param1.dar_tipo_str() )

    return Valor(rst, tipo_resultante)
