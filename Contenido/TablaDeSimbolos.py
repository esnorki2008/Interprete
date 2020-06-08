from PyQt5.QtGui import QStandardItem, QFont, QColor, QStandardItemModel

from Contenido.LstInstruccion.Registro.Valor import Valor

import copy


class ArbolItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)


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
    texto_analisis = ""
    lista_variables = None
    lista_etiquetas = None
    lista_errores = None
    salida_consola = None
    etiqueta_actual = None
    lista_instrucciones = None
    recuperacion_etiquetas = None
    salida_arbol = None
    def nueva_ejecucion(self):
        self.texto_analisis=""
        #print("Limpieza Tabla")
        self.exit_exec = 1
        self.lista_etiquetas = {}
        self.lista_variables = {}
        self.lista_errores = []
        self.etiqueta_actual = ""
        self.lista_instrucciones = []
        self.recuperacion_etiquetas = []

    def nueva_etiqueta(self, nombre):
        self.lista_instrucciones = []
        self.etiqueta_actual = nombre

    def nueva_instruaccion(self, instr):
        self.lista_instrucciones.append(instr)

    def consolidar_etiqueta(self):
        from Contenido.LstInstruccion.Instruccion import Etiqueta
        from Contenido.LstInstruccion.ABCInstruccion import ListaEtiqueta
        if self.etiqueta_actual is not None:
            if len(self.lista_instrucciones) > 1:
                eti = self.etiqueta_actual
                self.recuperacion_etiquetas.append(Etiqueta.Etiqueta(ListaEtiqueta(self.lista_instrucciones), eti))
        self.lista_instrucciones = []

    def generar_dot(self):
        from Contenido.LstInstruccion.ABCInstruccion import ListaEtiqueta
        from Contenido.LstInstruccion.Instruccion import Etiqueta
        l_temp = []
        if len(self.lista_etiquetas) != 0:
            for item in self.lista_etiquetas.items():
                l_temp.append(item[1])
        else:
            l_temp = self.recuperacion_etiquetas

        if len(self.lista_instrucciones) != 0:
            temp_eti = Etiqueta.Etiqueta(ListaEtiqueta(self.lista_instrucciones), "RECUPERADO ERROR")
            l_temp.append(temp_eti)
        l_eti = ListaEtiqueta(l_temp)
        return l_eti.str_arbol_encabezado()

    def __init__(self):
        self.exit_exec = 0
        self.lista_etiquetas = {}
        self.lista_variables = {}
        self.lista_errores = []
        self.etiqueta_actual = ""
        self.lista_instrucciones = []
        self.recuperacion_etiquetas = []

    def guardar_consola(self, consola):
        self.salida_consola = consola

    def guardar_arbol(self, arbol):
        self.salida_arbol = arbol

    def actualizar_arbol(self):


        if self.salida_arbol is None :
            print("No Se Cargo El ARBOL DE SALIDA")
        else :

            var_raiz = ArbolItem("Variables",12,set_bold=True, color=QColor(0,0,0))

            var_int = ArbolItem("int", 12, set_bold=True, color=QColor(0, 0, 0))
            var_float = ArbolItem("float", 12, set_bold=True, color=QColor(0, 0, 0))
            var_string = ArbolItem("string", 12, set_bold=True, color=QColor(0, 0, 0))
            var_array = ArbolItem("array", 12, set_bold=True, color=QColor(0, 0, 0))
            var_ref = ArbolItem("puntero", 12, set_bold=True, color=QColor(0, 0, 0))

            var_raiz.appendRow(var_int)
            var_raiz.appendRow(var_float)
            var_raiz.appendRow(var_string)
            var_raiz.appendRow(var_array)
            var_raiz.appendRow(var_ref)


            for vari in self.lista_variables.items() :
                texto_nodo= "Id : $"+str(vari[0])

                if vari[1].tipo != 4 :
                    if vari[1].tipo == 5:
                        texto_nodo += " Referencia : $" + str(vari[1].contenido.destino)
                        texto_nodo +="";
                    else:
                        texto_nodo += " Valor : " + str(vari[1].dar_valor())
                nuevo_nodo=ArbolItem(texto_nodo,8, color=QColor(7,26,142))

                if vari[1].tipo == 0 :
                    var_int.appendRow(nuevo_nodo)
                elif vari[1].tipo == 1 :
                    var_float.appendRow(nuevo_nodo)
                elif vari[1].tipo == 2:
                    var_string.appendRow(nuevo_nodo)
                elif vari[1].tipo == 5:
                    var_ref.appendRow(nuevo_nodo)
                else:
                    var_array.appendRow(nuevo_nodo)


            treeModel = QStandardItemModel()
            rootNode = treeModel.invisibleRootItem()
            rootNode.appendRow(var_raiz)

            self.salida_arbol.setModel(treeModel)
            self.salida_arbol.expandAll()
            self.salida_arbol.doubleClicked.connect(self.getValue)



    def getValue(self, val):
        print(val.data())
        print(val.row())
        print(val.column())

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
        else:
            if (retorno.tipo == 4):
                return copy.deepcopy(retorno)
            if (retorno.tipo == 5):

                return retorno.contenido.ejecutar()
            else:
                return retorno

    def cargar_error(self, descripcion: str, tipado: int):
        self.lista_errores.append(Errores(descripcion, tipado))

    def variable_cambiar_valor(self, nombre: str, conte: Valor):
        if conte.tipo == 5 :
            self.lista_variables[nombre] = conte
            nombre = conte.contenido.destino
            conte = conte.contenido.ejecutar()

        retorno = self.lista_variables.get(nombre, None)
        if retorno is not None:
            if retorno.tipo == 5 :
                refe = retorno.contenido.destino
                self.lista_variables[refe] = conte
            else:
                self.lista_variables[nombre] = conte
        else :
            self.lista_variables[nombre] = conte

    def arreglo_cambiar_valor(self, nombre: str, llaves: [], vaue: Valor):
        #Si El Valor Es Una Referencio
        if vaue.tipo == 5 :
            nombre = vaue.contenido.destino
            llaves = vaue.contenido.lst

        retorno = self.lista_variables.get(nombre, None)
        if retorno is None:
            self.lista_variables[nombre] = Valor({}, 4)
            retorno = self.lista_variables.get(nombre, None)
            retorno.guardar_arreglo(llaves, vaue)
        else:

            if retorno.tipo == 4:
                retorno.guardar_arreglo(llaves, vaue)
            if retorno.tipo == 5:
                self.arreglo_cambiar_valor(retorno.contenido.destino,llaves,vaue)

            else:
                self.lista_errores.append(Errores("El Registro " + nombre + " No Se Ha Inicializado", 0))


    def eliminar_variable(self,nombre : str ,llaves : []):
        retorno = self.lista_variables.get(nombre, None)
        if retorno is None:
            self.lista_errores.append(Errores("El Registro " + nombre + " No Se Ha Inicializado", 0))
        else:
            if retorno.tipo == 4:
                vaue : Valor = retorno
                vaue.eliminar_arreglo(llaves,nombre,self)
            else:
                self.lista_variables.pop(nombre, None)


    def arreglo_obtener_valor(self, nombre: str, llaves: []):
        retorno = self.lista_variables.get(nombre, None)
        if retorno is None:
            return Valor(0, 0)
        else:
            if retorno.tipo == 4:
                return retorno.sacar_arreglo(llaves, nombre, self)
            if retorno.tipo == 5:
                return self.arreglo_obtener_valor(retorno.contenido.destino,llaves)
            else:
                self.lista_errores.append(Errores("El Registro " + nombre + " No Se Ha Inicializado", 0))

    def cargar_etiquetas(self, raiz):
        if self.exit_exec == 0:
            return

        for elemento in raiz.lst:
            self.lista_etiquetas[elemento.nombre] = elemento

    def ejecutar_main(self):
        if self.exit_exec == 0:
            print("No Se Puede Ejecutar Si Hay Error Sintactico")
            return
        maincito = self.lista_etiquetas.get("main", None)
        if maincito is None:
            print("No Se Puede Ejecutar Si No Hay Main")
            self.lista_errores.append(Errores("No Se Puede Ejecutar Si No Hay Main", 0))
        else:
            #exec = maincito.ejecutar()
            exec = "main"
            temp = "main"
            while exec is not None:
                if exec != "exit":


                    temp = exec
                    exec = self.lista_etiquetas.get(exec, None)
                    if exec is None:
                        print("No Se Puede Ejecutar La Etiqueta " + str(temp))
                        self.lista_errores.append(Errores("No Se Puede Ejecutar La Etiqueta " + temp, 0))
                    else:
                        exec = exec.ejecutar()
                        #BORRAR SI DA ERROR
                        if exec is None :

                            aceptar = False
                            for llave in self.lista_etiquetas.keys():
                                if aceptar:
                                    maincito = self.lista_etiquetas.get(llave, None)
                                    exec = maincito.ejecutar()
                                    if exec is not None:
                                        break

                                if llave == temp:
                                    aceptar = True

                        #TERMINAR BORRADO
                else:
                    break





    def ejecutar_etiqueta(self, nombre: str):
        if self.exit_exec == 0:
            return
        maincito = self.lista_etiquetas.get(nombre, None)
        if maincito is None:
            print("No Se Puede Ejecutar, No Existe La Etiqueta :" + nombre)
            self.lista_errores.append(Errores("No Se Puede Ejecutar, No Existe La Etiqueta :" + nombre, 2))
        else:
            maincito.ejecutar()
            # retu = maincito.ejecutar()
            return 1
            print("DETENER")

            if retu == 1:
                return 1
            # print(nombre)
            aceptar = False
            for llave in self.lista_etiquetas.keys():

                if aceptar:
                    # print(llave + "____" + nombre + "_____" + str(aceptar))
                    self.ejecutar_etiqueta(llave)

                if llave == nombre:
                    aceptar = True
