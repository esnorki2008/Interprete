from Contenido.LstInstruccion.Registro.Valor import Valor


def negar(param1 : Valor):
    from Contenido.LstInstruccion.ABCInstruccion import Ts
    global Ts
    tipo_resultante = 0
    rst = 0
    #Solo Se Pueden Valores Numericos
    if(param1.tipo==0):
        tipo_resultante=param1.tipo
        rst=param1.dar_valor()*-1
        

    else:
        Ts.cargar_error("Error En La Negacion Con Tipos: " + param1.dar_tipo_str(), 0,
                        ((0, 0)))
        print("Error En La Negacion Con Tipos: " + param1.dar_tipo_str() )

    return Valor(rst, tipo_resultante)
