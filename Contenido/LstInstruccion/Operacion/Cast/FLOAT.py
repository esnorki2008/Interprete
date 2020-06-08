from Contenido.LstInstruccion.Registro.Valor import Valor


def cast_float(param: Valor):
    tipo_rst = 1
    rst = 0
    if param.tipo == 0:
        rst = float(param.dar_valor())
    elif param.tipo == 1:
        rst = param.dar_valor()
    elif param.tipo == 2:
        rst = 0
        if param.dar_valor() != "":
            caracter = param.dar_valor()[0]
            rst = float(ord(caracter))
    elif param.tipo == 4:
        return cast_float(param.primer_elemento())
    else:
        print(" TIPO NO RECONOCIDO CASTEO")

    return Valor(rst, tipo_rst)
