from Contenido.LstInstruccion.Registro.Valor import Valor
import  copy

class Errores:
    descripcion: str = None
    tipo: int = 110
    pos_x: int = 0
    pos_y: int = 0
    exit_exec: int = 0

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
        self.exit_exec = 0
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
        else :
            if (retorno.tipo == 4):
                return copy.deepcopy(retorno)
            else :
                return  retorno

    def nueva_ejecucion(self):
        print("Limpieza Tabla")
        self.exit_exec = 1
        self.lista_etiquetas = {}
        self.lista_variables = {}
        self.lista_errores = []

    def cargar_error(self, descripcion: str, tipado: int):
        self.lista_errores.append(Errores(descripcion, tipado))

    def variable_cambiar_valor(self, nombre: str, conte: Valor):
        self.lista_variables[nombre] = conte

    def arreglo_cambiar_valor(self, nombre: str, llaves: [], vaue : Valor):
        retorno = self.lista_variables.get(nombre, None)
        if retorno is None:
            self.lista_variables[nombre] = Valor({},4)
            retorno = self.lista_variables.get(nombre, None)
            retorno.guardar_arreglo(llaves, vaue)
        else:
            if retorno.tipo == 4:
                retorno.guardar_arreglo(llaves,vaue)
            else:
                self.lista_errores.append(Errores("El Registro " + nombre + " No Se Ha Inicializado", 0))

    def arreglo_obtener_valor(self, nombre: str, llaves: []):
        retorno = self.lista_variables.get(nombre, None)
        if retorno is None:
            return  Valor(0,0)
        else:
            if retorno.tipo == 4:
                return retorno.sacar_arreglo(llaves, nombre,self)
            else:
                self.lista_errores.append(Errores("El Registro " + nombre + " No Se Ha Inicializado", 0))

    def cargar_etiquetas(self, raiz):
        self.lista_etiquetas = {}
        for elemento in raiz.lst:
            self.lista_etiquetas[elemento.nombre] = elemento

    def ejecutar_main(self):
        if self.exit_exec == 0:
            return
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
        if self.exit_exec == 0:
            return
        maincito = self.lista_etiquetas.get(nombre, None)
        if maincito is None:
            print("No Se Puede Ejecutar, No Existe La Etiqueta :" + nombre)
            self.lista_errores.append(Errores("No Se Puede Ejecutar, No Existe La Etiqueta :" + nombre, 2))
        else:
            retu = maincito.ejecutar()
            aceptar = False
            if retu == 1:
                return 1
            # print(nombre)
            for llave in self.lista_etiquetas.keys():

                if aceptar:
                    # print(llave + "____" + nombre + "_____" + str(aceptar))
                    self.ejecutar_etiqueta(llave)

                if llave == nombre:
                    aceptar = True
