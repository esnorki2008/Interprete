from Contenido.LstInstruccion.Registro.Valor import Valor


def cast_int(param: Valor):
    tipo_rst = 0
    rst = 0
    if param.tipo == 0:
        rst = param.dar_valor()
    elif param.tipo == 1:
        rst = int(param.dar_valor())
    elif param.tipo == 2:
        rst=0
        if param.dar_valor() != "":
            caracter = param.dar_valor()[0]
            rst = ord(caracter)
    elif param.tipo == 4:
        return cast_int(param.primer_elemento())
    else:
        print(" TIPO NO RECONOCIDO CASTEO")

    return Valor(rst, tipo_rst)
