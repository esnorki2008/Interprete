from Contenido.LstInstruccion.Registro.Valor import Valor


def and_binario(param1 : Valor, param2 : Valor):
    tipo_resultante = 0
    rst = 0
    from Contenido.LstInstruccion.ABCInstruccion import Ts
    global Ts
    #Solo Se Pueden Valores Numericos
    if(param1.tipo==0):
        if param2.tipo==0:
            #Entero
            tipo_resultante=0
            rst=param1.dar_valor() & param2.dar_valor()

        else:
            Ts.cargar_error(
                "Error En And Binario Con Tipos: " + param1.dar_tipo_str() + "," + param2.dar_tipo_str(), 0,
                ((0, 0)))
            print("Error En And Binario Con Tipos: "+param1.dar_tipo_str()+","+param2.dar_tipo_str())

    else:
        Ts.cargar_error(
            "Error En & Con Tipos: " + param1.dar_tipo_str() + "," + param2.dar_tipo_str(), 0,
            ((0, 0)))
        print("Error En & Con Tipos: " + param1.dar_tipo_str() + "," + param2.dar_tipo_str())

    return Valor(rst, tipo_resultante)
