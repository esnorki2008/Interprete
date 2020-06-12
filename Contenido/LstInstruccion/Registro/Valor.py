class Valor:
    contenido: object = None
    tipo: int = 0
    tupla= (0,0)

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
            Ts.cargar_error("El Arreglo " + nombre + " En La Posicion " + llave_maestra + " No Se Ha Inicializado", 0,self.tupla)
            return Valor(0, 0)
        else:
            self.contenido.pop(llave_maestra,None)

    def primer_elemento(self):
        vista=self.contenido.values()
        it=iter(vista)
        return next(it)

    def sacar_arreglo(self, llaves: [], Nombre, Ts):
        llave_maestra = ""
        for item in llaves:
            llave_maestra += str(item) + ",";

        Obtenido = self.contenido.get(llave_maestra, None)
        if Obtenido is None:

            Ts.cargar_error("El Arreglo " + Nombre + " En La Posicion " + llave_maestra + " No Se Ha Inicializado", 0,self.tupla)
            return Valor(0, 0)
        else:
            return Obtenido

    def cadena_arreglo(self, llaves: [],nombre, Ts):
        if len(llaves) != 1 :
            Ts.cargar_error("La variable $" + nombre + " al ser una cadena no permite mas de un par de llaves", 0,self.tupla)
            return Valor("", 2)
        else :
            ind=0
            try :
                ind=int(llaves[0])
            except :
                Ts.cargar_error("La variable $" + nombre + " al ser una cadena solo permite valores numericos en la llave", 0, self.tupla)
                return Valor("", 2)
            if ind >= len(self.contenido):
                Ts.cargar_error("Fuera De Indice para la cadena $" + nombre + " ", 0,self.tupla)
                return Valor("", 2)
            else :
                return Valor(self.contenido[ind],2)

        return Valor("", 2)

    def guardar_cadena_arreglo(self, llaves: [],nombre, Ts, vaue):

        if len(llaves) != 1:
            Ts.cargar_error("La variable $" + nombre + " al ser una cadena no permite mas de un par de llaves", 0,
                            self.tupla)
        else:
            ind = 0
            try:
                ind = int(llaves[0])
            except:
                Ts.cargar_error(
                    "La variable $" + nombre + " al ser una cadena solo permite valores numericos en la llave", 0,
                    self.tupla)
            if ind >= len(self.contenido):
                Ts.cargar_error("Fuera De Indice para la cadena $" + nombre + " ", 0, self.tupla)
            else:
                if vaue.tipo==2 or vaue.tipo==0 :
                    longi=len(self.contenido)
                    novo=""
                    for i in range (0,longi):
                        if ind == i :
                            novo+=str(vaue.contenido)[0]
                        else:
                            novo+=self.contenido[i]

                    self.contenido=novo
                else:
                    Ts.cargar_error("Asignacion a la cadena $" + nombre + " el tipo "+vaue.dar_tipo_str(), 0, self.tupla)


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
        elif self.tipo == 4:
            return "arreglo"
        else:
            return "indefinido"
