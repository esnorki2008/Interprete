class Valor:
    contenido: object = None
    tipo: int = 0

    def __init__(self, contenido: object, tipo: int):
        self.contenido = contenido
        self.tipo = tipo

    def dar_valor(self):
        return self.contenido