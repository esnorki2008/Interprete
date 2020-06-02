from Contenido.LstInstruccion.Registro.Valor import Valor


def modular(param1 : Valor, param2 : Valor):
    tipo_resultante = 0
    rst = 0
    #Solo Se Pueden Valores Numericos
    if(param1.tipo==0):
        if param2.tipo==0:
            #Entero
            tipo_resultante=0
            rst=param1.dar_valor() % param2.dar_valor()
        elif param2.tipo==1:
            #Decimal
            tipo_resultante = 1
            rst = param1.dar_valor() % param2.dar_valor()
        else:
            print("Error En La Suma Con Tipos: "+param1.dar_tipo_str()+","+param2.dar_tipo_str())
    elif param1.tipo==1:
        if param2.tipo==0:
            #Decimal
            tipo_resultante=1
            rst=param1.dar_valor() % param2.dar_valor()
        elif param2.tipo==1:
            #Decimal
            tipo_resultante = 1
            rst = param1.dar_valor() % param2.dar_valor()
        else:
            print("Error En El MODULAR Con Tipos: "+param1.dar_tipo_str()+","+param2.dar_tipo_str())
    else:
        print("Error En El MODULAR Con Tipos: " + param1.dar_tipo_str() + "," + param2.dar_tipo_str())

    return Valor(rst, tipo_resultante)
