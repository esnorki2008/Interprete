class Valor:
    contenido: object = None
    tipo: int = 0

    def __init__(self, contenido: object, tipo: int):
        self.contenido = contenido
        self.tipo = tipo

    '''
        Tipo 0 Entero
        Tipo 1 Decimal
        Tipo 2 Booleano
        Tipo 3 Char
        Tipo 4 String
        Tipo 5 Objeto
    '''

    def guardar_arreglo(self, llaves: [], vaue):
        llave_maestra = ""
        for item in llaves:
            llave_maestra += str(item) + ",";

        self.contenido[llave_maestra] = vaue

    def eliminar_arreglo(self, llaves : [],nombre, Ts):
        llave_maestra = ""
        for item in llaves:
            llave_maestra += str(item) + ",";

        Obtenido = self.contenido.get(llave_maestra, None)
        if Obtenido is None:
            Ts.cargar_error("El Arreglo " + nombre + " En La Posicion " + llave_maestra + " No Se Ha Inicializado", 0)
            return Valor(0, 0)
        else:
            self.contenido.pop(llave_maestra,None)


    def sacar_arreglo(self, llaves: [], Nombre, Ts):
        llave_maestra = ""
        for item in llaves:
            llave_maestra += str(item) + ",";

        Obtenido = self.contenido.get(llave_maestra, None)
        if Obtenido is None:

            Ts.cargar_error("El Arreglo " + Nombre + " En La Posicion " + llave_maestra + " No Se Ha Inicializado", 0)
            return Valor(0, 0)
        else:
            return Obtenido

    def dar_valor(self):
        return self.contenido

    def dar_identificador(self):
        return self.contenido

    def dar_tipo_str(self):
        if self.tipo == 0:
            return "entero"
        elif self.tipo == 1:
            return "decimal"
        elif self.tipo == 2:
            return "string"
        elif self.tipo == 3:
            return "arreglo"
        else:
            return "indefinido"
