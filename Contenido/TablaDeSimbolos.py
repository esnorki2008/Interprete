from Contenido.LstInstruccion.Registro.Valor import Valor


class TablaDeSimbolos:
    lista_variables = None
    lista_etiquetas = None
    lista_errores = None

    def __init__(self):
        self.lista_etiquetas = {}
        self.lista_variables = {}
        self.lista_errores = []

    def variable_obtener_valor(self, nombre: str):
        retorno = self.lista_variables.get(nombre, None)
        if retorno is None:
            retorno = Valor(0, 0)
            self.lista_errores.append(Errores("El Registro " + nombre + " No Se Ha Inicializado"), 0)
        return retorno

    def variable_cambiar_valor(self, nombre: str, conte: Valor):
        self.lista_variables[nombre] = conte


class Errores:
    descripcion: str = None
    tipo: int = 110
    pos_x: int = 0
    pos_y: int = 0

    def __init__(self, descripcion, tipo):
        self.descripcion = descripcion
        self.tipo = tipo
        # self.pos_x=pos_x
        # self.pos_y=pos_y


class ValorTabla:
    def __init__(self):
        pass

    def valor_obtener(self):
        pass

    def valor_cambiar(self):
        pass
