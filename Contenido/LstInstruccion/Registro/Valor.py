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
    def dar_valor(self):
        return self.contenido