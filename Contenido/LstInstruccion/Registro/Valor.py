class Valor:
    contenido: object = None
    tipo: int = 0
    tupla = (0, 0)

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

    def guardar_arreglo(self, llaves: [], vaue, nombre, Ts):
        llave_maestra = ""
        cadenita = None
        lla_limit = len(llaves)
        lla_act = 0
        for item in llaves:
            llave_maestra += str(item) + ",";

            if cadenita is not None:
                if cadenita.tipo == 2 and (lla_limit - lla_act == 1):
                    cadenita.guardar_cadena_arreglo([item], nombre, Ts, vaue)
                    return None
                else:
                    Ts.cargar_error(
                        "La variable $" + nombre + " Tiene ocupada la posicion " + llave_maestra, 0,
                        self.tupla)

                    return Valor(0, 0)

            lla_act = lla_act + 1
            cadenita = self.contenido.get(llave_maestra, None)

        self.contenido[llave_maestra] = vaue

    def eliminar_arreglo(self, llaves: [], nombre, Ts):
        llave_maestra = ""
        for item in llaves:
            llave_maestra += str(item) + ",";

        Obtenido = self.contenido.get(llave_maestra, None)
        if Obtenido is None:
            Ts.cargar_error("El Arreglo " + nombre + " En La Posicion " + llave_maestra + " No Se Ha Inicializado", 0,
                            self.tupla)
            return Valor(0, 0)
        else:
            self.contenido.pop(llave_maestra, None)

    def primer_elemento(self):
        vista = self.contenido.values()
        it = iter(vista)
        return next(it)

    def sacar_arreglo(self, llaves: [], Nombre, Ts):
        llave_maestra = ""
        cadenita = None

        for item in llaves:
            llave_maestra += str(item) + ",";

            if cadenita is not None:
                if cadenita.tipo == 2:

                    return cadenita.cadena_arreglo([item], Nombre, Ts)
                else:
                    Ts.cargar_error(
                        "La variable $" + Nombre + " Tiene ocupada la posicion " + llave_maestra, 0,
                        self.tupla)
                    return Valor(0, 0)

            cadenita = self.contenido.get(llave_maestra, None)

        Obtenido = self.contenido.get(llave_maestra, None)
        if Obtenido is None:

            Ts.cargar_error("El Arreglo " + Nombre + " En La Posicion " + llave_maestra + " No Se Ha Inicializado", 0,
                            self.tupla)
            return Valor(0, 0)
        else:
            return Obtenido

    def cadena_arreglo(self, llaves: [], nombre, Ts):
        if len(llaves) != 1:
            Ts.cargar_error("La variable $" + nombre + " al ser una cadena no permite mas de un par de llaves", 0,
                            self.tupla)
            return Valor("", 2)
        else:
            ind = 0
            try:
                ind = int(llaves[0])
            except:
                Ts.cargar_error(
                    "La variable $" + nombre + " al ser una cadena solo permite valores numericos en la llave", 0,
                    self.tupla)
                return Valor("", 2)
            if ind >= len(self.contenido):
                Ts.cargar_error("Fuera De Indice para la cadena $" + nombre + " ", 0, self.tupla)
                return Valor("", 2)
            else:
                return Valor(self.contenido[ind], 2)

        return Valor("", 2)

    def guardar_cadena_arreglo(self, llaves: [], nombre, Ts, vaue):

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

            if vaue.tipo == 2 or vaue.tipo == 0:
                longi = len(self.contenido)
                novo = ""
                tope = longi

                # print(str(tope)+"  "+str(ind))

                if tope <= ind:
                    # if tope == ind :
                    tope = ind + 1
                # else:
                #    tope=ind
                # tope+=1
                # ind=ind-1

                for i in range(0, tope):
                    if ind == (i):
                        novo += str(vaue.contenido)[0]
                    elif i >= longi:
                        novo += " "
                    else:
                        novo += self.contenido[i]
                # print(novo)
                self.contenido = novo
            else:
                Ts.cargar_error("Asignacion a la cadena $" + nombre + " el tipo " + vaue.dar_tipo_str(), 0, self.tupla)

    def dar_valor(self):
        return self.contenido

    def dar_identificador(self):
        return self.contenido
    def dimension(self):
        salida=0
        for item in self.contenido.items():
            comp=str(item[0]).count(",")
            if salida < comp:
                salida = comp

        return str(salida)

    def dar_tipo_str(self):
        if self.tipo == 0:
            return "entero"
        elif self.tipo == 1:
            return "decimal"
        elif self.tipo == 2:
            return "string"
        elif self.tipo == 4:
            return "arreglo"
        elif self.tipo == 5:
            return "referencia"
        else:
            return "indefinido"
