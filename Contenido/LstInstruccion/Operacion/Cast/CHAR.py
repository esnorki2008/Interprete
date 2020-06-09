from Contenido.LstInstruccion.Registro.Valor import Valor


def cast_char(param: Valor):
    tipo_rst = 2
    rst = 0
    if param.tipo == 0:
        val_ascii=param.dar_valor()
        if param.dar_valor() > 255:
            val_ascii= param.dar_valor() % 256
        rst = chr(val_ascii)
    elif param.tipo == 1:
        val_ascii = int(param.dar_valor())
        if param.dar_valor() > 255:
            val_ascii = param.dar_valor() % 256
        rst = chr(val_ascii)
    elif param.tipo == 2:
        rst = ""
        if param.dar_valor() != "":
            caracter = param.dar_valor()[0]
            rst = caracter
    elif param.tipo == 4:
        return cast_char(param.primer_elemento())
    else:
        print(" TIPO NO RECONOCIDO CASTEO")

    return Valor(rst, tipo_rst)
