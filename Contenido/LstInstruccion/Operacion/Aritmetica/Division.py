from Contenido.LstInstruccion.Registro.Valor import Valor


def dividir(param1 : Valor, param2 : Valor):
    tipo_resultante = 0
    rst = 0
    from Contenido.LstInstruccion.ABCInstruccion import Ts
    global Ts
    if param2.dar_valor()==0:
        Ts.cargar_error(
            "No se pude dividir entre 0 " , 0,
            ((0, 0)))
        print(" No se puede dividir entre 0")
        return Valor(0, 0)

    #Solo Se Pueden Valores Numericos
    if(param1.tipo==0):
        if param2.tipo==0:
            #Entero
            tipo_resultante=0
            rst=param1.dar_valor() / param2.dar_valor()
        elif param2.tipo==1:
            #Decimal
            tipo_resultante = 1
            rst = param1.dar_valor() / param2.dar_valor()
        else:
            Ts.cargar_error(
                "Error En la division Con Tipos: " + param1.dar_tipo_str() + "," + param2.dar_tipo_str(), 0,
                ((0, 0)))
    elif param1.tipo==1:
        if param2.tipo==0:
            #Decimal
            tipo_resultante=1
            rst=param1.dar_valor() / param2.dar_valor()
        elif param2.tipo==1:
            #Decimal
            tipo_resultante = 1
            rst = param1.dar_valor() / param2.dar_valor()
        else:
            Ts.cargar_error(
                "Error En la division Con Tipos: " + param1.dar_tipo_str() + "," + param2.dar_tipo_str(), 0,
                ((0, 0)))
    else:
        Ts.cargar_error(
            "Error En la division Con Tipos: " + param1.dar_tipo_str() + "," + param2.dar_tipo_str(), 0,
            ((0, 0)))

    return Valor(rst, tipo_resultante)
