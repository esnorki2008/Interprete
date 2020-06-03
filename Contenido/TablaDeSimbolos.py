from Contenido.LstInstruccion.Registro.Valor import Valor


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


# Tipo De Error Maximo 3
class TablaDeSimbolos:
    lista_variables = None
    lista_etiquetas = None
    lista_errores = None
    salida_consola = None

    def __init__(self):
        self.lista_etiquetas = {}
        self.lista_variables = {}
        self.lista_errores = []

    def guardar_consola(self, consola):
        self.salida_consola = consola

    def print(self, vaue):
        if (self.salida_consola is None):
            print("ERROR NO SE GUARDO LA CONSOLA")
        else:
            self.salida_consola.append(str(vaue))

    def variable_obtener_valor(self, nombre: str):
        retorno = self.lista_variables.get(nombre, None)
        if retorno is None:
            retorno = Valor(0, 0)
            print("El Registro " + nombre + " No Se Ha Inicializado")
            self.lista_errores.append(Errores("El Registro " + nombre + " No Se Ha Inicializado", 0))
        return retorno

    def nueva_ejecucion(self):
        self.lista_etiquetas = {}
        self.lista_variables = {}
        self.lista_errores = []

    def cargar_error(self, descripcion: str, tipado: int):
        self.lista_errores.append(Errores(descripcion, tipado))

    def variable_cambiar_valor(self, nombre: str, conte: Valor):
        self.lista_variables[nombre] = conte

    def cargar_etiquetas(self, raiz):
        self.lista_etiquetas = {}
        for elemento in raiz.lst:
            self.lista_etiquetas[elemento.nombre] = elemento

    def ejecutar_main(self):
        maincito = self.lista_etiquetas.get("main", None)
        if maincito is None:
            print("No Se Puede Ejecutar Si No Hay Main")
            self.lista_errores.append(Errores("No Se Puede Ejecutar Si No Hay Main", 1))
        else:
            if maincito.ejecutar() == 1:
                return
            for llave in self.lista_etiquetas.keys():
                if llave != "main":
                    self.ejecutar_etiqueta(llave)


    def ejecutar_etiqueta(self, nombre: str):
        maincito = self.lista_etiquetas.get(nombre, None)
        if maincito is None:
            print("No Se Puede Ejecutar, No Existe La Etiqueta :" + nombre)
            self.lista_errores.append(Errores("No Se Puede Ejecutar, No Existe La Etiqueta :" + nombre, 2))
        else:
            maincito.ejecutar()
            #aceptar=False
           # if maincito.ejecutar() == 1:
            #    return
           # for llave in self.lista_etiquetas.keys():
           #     if aceptar:
            #        self.ejecutar_etiqueta(llave)
             #   if llave == nombre:
              #      aceptar=True


