from Contenido.LstInstruccion.Registro.Valor import Valor


def not_num(param1 : Valor):
    tipo_resultante = 0
    rst = 0
    from Contenido.LstInstruccion.ABCInstruccion import Ts
    global Ts
    #Solo Se Pueden Valores Numericos
    if(param1.tipo==0):
        tipo_resultante=param1.tipo
        if param1.dar_valor()>0:
            rst=0
        else:
            rst=1
    else:

        Ts.cargar_error("Error En La Resta Unaria Con Tipos: " + param1.dar_tipo_str(), 0,
                        ((0, 0)))

        print("Error En La Resta Unaria Con Tipos: " + param1.dar_tipo_str() )

    return Valor(rst, tipo_resultante)
