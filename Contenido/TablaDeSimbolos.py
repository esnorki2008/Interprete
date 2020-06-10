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
    tupla :()
    exit_exec: int = 0

    def __init__(self, descripcion, tipo,tupla):
        self.descripcion = descripcion
        self.tipo = tipo
        self.tupla=tupla
        # self.pos_x=pos_x
        # self.pos_y=pos_y



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

    paso_lista_etiquetas = []
    paso_etiqueta_actual = 0;
    paso_instruccion_actual = 0;

    def nueva_ejecucion(self, texto):
        self.texto_analisis = texto
        # print("Limpieza Tabla")
        self.exit_exec = 1
        self.lista_etiquetas = {}
        self.lista_variables = {}
        self.lista_errores = []
        self.etiqueta_actual = ""
        self.lista_instrucciones = []
        self.recuperacion_etiquetas = []

        self.paso_lista_etiquetas = None
        self.paso_etiqueta_actual = "main";
        self.paso_instruccion_actual = 0;

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

        self.paso_lista_etiquetas = None
        self.paso_etiqueta_actual = "main";
        self.paso_instruccion_actual = 0;

    def guardar_consola(self, consola):
        self.salida_consola = consola

    def guardar_arbol(self, arbol):
        self.salida_arbol = arbol

    def actualizar_arbol(self):

        if self.salida_arbol is None:
            print("No Se Cargo El ARBOL DE SALIDA")
        else:

            var_raiz = ArbolItem("Variables", 12, set_bold=True, color=QColor(0, 0, 0))

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

            for vari in self.lista_variables.items():
                texto_nodo = "Id : $" + str(vari[0])

                if vari[1].tipo != 4:
                    if vari[1].tipo == 5:
                        texto_nodo += " Referencia : $" + str(vari[1].contenido.destino)
                        texto_nodo += "";
                    else:
                        texto_nodo += " Valor : " + str(vari[1].dar_valor())
                nuevo_nodo = ArbolItem(texto_nodo, 8, color=QColor(7, 26, 142))

                if vari[1].tipo == 0:
                    var_int.appendRow(nuevo_nodo)
                elif vari[1].tipo == 1:
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
            self.cargar_error("El Registro " + nombre + " No Se Ha Inicializado", 0,(0,0))
            return retorno
        else:
            if (retorno.tipo == 4):
                return copy.deepcopy(retorno)
            if (retorno.tipo == 5):

                return retorno.contenido.ejecutar()
            else:
                return retorno

    def cargar_error(self, descripcion: str, tipado: int, tupla):
        self.lista_errores.append(Errores(descripcion, tipado,tupla))

    def variable_cambiar_valor(self, nombre: str, conte: Valor):
        if conte.tipo == 5:
            self.lista_variables[nombre] = conte
            nombre = conte.contenido.destino
            conte = conte.contenido.ejecutar()

        retorno = self.lista_variables.get(nombre, None)
        if retorno is not None:
            if retorno.tipo == 5:
                refe = retorno.contenido.destino
                self.lista_variables[refe] = conte
            else:
                self.lista_variables[nombre] = conte
        else:
            self.lista_variables[nombre] = conte

    def arreglo_cambiar_valor(self, nombre: str, llaves: [], vaue: Valor):
        # Si El Valor Es Una Referencio
        if vaue.tipo == 5:
            nombre = vaue.contenido.destino
            llaves = vaue.contenido.lst

        retorno = self.lista_variables.get(nombre, None)
        if retorno is None:
            self.lista_variables[nombre] = Valor({}, 4)
            retorno = self.lista_variables.get(nombre, None)
            retorno.guardar_arreglo(llaves, vaue)
        else:
            if retorno.tipo ==2 :
                retorno.guardar_cadena_arreglo(llaves,nombre,self,vaue)
            elif retorno.tipo == 4:
                retorno.guardar_arreglo(llaves, vaue)
            elif retorno.tipo == 5:
                self.arreglo_cambiar_valor(retorno.contenido.destino, llaves, vaue)
            else:
                self.cargar_error("El Registro 11" + nombre +str(llaves) +" No Se Ha Inicializado", 0,(0,0))

    def eliminar_variable(self, nombre: str, llaves: []):
        retorno = self.lista_variables.get(nombre, None)
        if retorno is None:
            self.cargar_error("El Registro " + nombre +str(llaves) + " No Se Ha Inicializado", 0,(0,0))
        else:
            if retorno.tipo == 4:
                vaue: Valor = retorno
                vaue.eliminar_arreglo(llaves, nombre, self)
            else:
                self.lista_variables.pop(nombre, None)



    def arreglo_obtener_valor(self, nombre: str, llaves: []):
        retorno = self.lista_variables.get(nombre, None)
        if retorno is None:
            return Valor(0, 0)
        else:
            if retorno.tipo ==2 :
                return retorno.cadena_arreglo(llaves,nombre,self)
            elif retorno.tipo == 4:
                return retorno.sacar_arreglo(llaves, nombre, self)
            elif retorno.tipo == 5:
                return self.arreglo_obtener_valor(retorno.contenido.destino, llaves)
            else:
                self.cargar_error("El Registro " + nombre + " No Se Ha Inicializado", 0,(0,0))

    def cargar_etiquetas(self, raiz):
        if self.exit_exec == 0:
            return

        self.paso_etiqueta_actual = "main";
        self.paso_instruccion_actual = 0;
        self.paso_lista_etiquetas = raiz

        raiz.determinar_tipo_funcion()
        self.cargar_tabla_etiqueta(raiz.lst)
        for elemento in raiz.lst:
            #print(str(elemento.tengo_retorno)+str(elemento.tengo_parametros))
            self.lista_etiquetas[elemento.nombre] = elemento

    tabla_etiqueta = None

    def guardar_tabla_etiqueta(self, tabla):
        tabla.clear()
        self.tabla_etiqueta = tabla

    def cargar_tabla_etiqueta(self, lst: []):
        self.tabla_etiqueta.setRowCount(len(lst)+1)
        self.tabla_etiqueta.setColumnCount(4)
        from PyQt5.QtWidgets import QTableWidgetItem
        self.tabla_etiqueta.setItem(0, 0, QTableWidgetItem("Nombre"))
        self.tabla_etiqueta.setItem(0, 1, QTableWidgetItem("Tipo"))
        self.tabla_etiqueta.setItem(0, 2, QTableWidgetItem("columna"))
        self.tabla_etiqueta.setItem(0, 3, QTableWidgetItem("fila"))
        conta=1
        for elemento in lst:
            #print(elemento.tupla)
            #print(str(elemento.tengo_retorno) + str(elemento.tengo_parametros))
            f_tipo="Estructura De Control"
            if elemento.tengo_retorno == True:
                f_tipo="Función"
            else:
                if elemento.tengo_parametros == True:
                    f_tipo="Procedimiento"

            self.tabla_etiqueta.setItem(conta, 0, QTableWidgetItem(elemento.nombre))
            self.tabla_etiqueta.setItem(conta, 1, QTableWidgetItem(f_tipo))
            self.tabla_etiqueta.setItem(conta, 2, QTableWidgetItem(str(elemento.tupla[0])))
            self.tabla_etiqueta.setItem(conta, 3, QTableWidgetItem(str(elemento.tupla[1])))

            conta += 1

    tabla_error = None

    def guardar_tabla_error(self, tabla):
        self.tabla_error = tabla
        self.cargar_errores()

    def cargar_errores(self):
        self.tabla_error.setRowCount(len(self.lista_errores) + 1)
        self.tabla_error.setColumnCount(4)
        from PyQt5.QtWidgets import QTableWidgetItem
        self.tabla_error.setItem(0, 0, QTableWidgetItem("Tipo"))
        self.tabla_error.setItem(0, 1, QTableWidgetItem("Descripcion"))
        self.tabla_error.setItem(0, 2, QTableWidgetItem("columna"))
        self.tabla_error.setItem(0, 3, QTableWidgetItem("fila"))
        conta = 1
        for elemento in self.lista_errores:
            # print(elemento.tupla)
            # print(str(elemento.tengo_retorno) + str(elemento.tengo_parametros))
            f_tipo = "Error Semantico"
            if elemento.tipo == 20:
                f_tipo = "Error Sintactico"
            elif elemento.tipo == 30:
                f_tipo = "Error Lexico"

            self.tabla_error.setItem(conta, 0, QTableWidgetItem(f_tipo))
            self.tabla_error.setItem(conta, 1, QTableWidgetItem(str(elemento.descripcion)))
            self.tabla_error.setItem(conta, 2, QTableWidgetItem(str(elemento.tupla[0])))
            self.tabla_error.setItem(conta, 3, QTableWidgetItem(str(elemento.tupla[1])))

            conta += 1

    def ejecutar_main(self):
        if self.exit_exec == 0:
            self.mensaje_info("Erro","No Se Puede Ejecutar Si Hay Error Sintactico")
            return
        maincito = self.lista_etiquetas.get("main", None)
        if maincito is None:
            self.mensaje_info("Erro","No Se Puede Ejecutar Si No Se Define MAIN")
            self.cargar_error("No Se Puede Ejecutar Si No Hay Main", 0,(0,0))
        else:
            # exec = maincito.ejecutar()
            exec = "main"
            temp = "main"
            while exec is not None:
                if exec != "exit":

                    temp = exec
                    exec = self.lista_etiquetas.get(exec, None)
                    if exec is None:
                        print("No Se Puede Ejecutar La Etiqueta " + str(temp))
                        self.cargar_error("No Se Puede Ejecutar La Etiqueta " + temp, 0,(0,0))
                    else:
                        exec = exec.ejecutar()
                        # BORRAR SI DA ERROR
                        if exec is None:

                            aceptar = False
                            for llave in self.lista_etiquetas.keys():
                                if aceptar:
                                    maincito = self.lista_etiquetas.get(llave, None)
                                    exec = maincito.ejecutar()
                                    if exec is not None:
                                        break

                                if llave == temp:
                                    aceptar = True

                        # TERMINAR BORRADO
                else:
                    break
        self.cargar_errores()
        self.mensaje_info("Informacion", "Ejecucion Completada")

    def mensaje_info(self,Titulo,Texto):
        #return
        from PyQt5.QtWidgets import QMessageBox
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(Titulo)
        msg.setText(Texto)
        msg.exec_()


    def paso_a_paso_ejecutar(self):
        if self.exit_exec == 0:
            self.cargar_errores()
            self.mensaje_info("Erro","No Se Puede Ejecutar Si Hay Error Sintactico")
            return None

        maincito = self.lista_etiquetas.get("main", None)
        if maincito is None:
            print("No Se Puede Ejecutar Si No Hay Main")
            self.cargar_error("No Se Puede Ejecutar Si No Hay Main", 0,(0,0))
        else:
            # exec = maincito.ejecutar()

            exec = self.paso_etiqueta_actual
            temp = exec
            if exec != "exit":

                temp = self.paso_etiqueta_actual
                exec = self.lista_etiquetas.get(exec, None)

                if exec is None:
                    print("No Se Puede Ejecutar La Etiqueta " + str(temp))
                    self.cargar_error("No Se Puede Ejecutar La Etiqueta " + temp, 0,(0,0))
                else:
                    # print(exec)
                    exec = exec.paso_a_paso_ejecutar(self.paso_instruccion_actual)
                    # print(self.paso_etiqueta_actual)
                    # BORRAR SI DA ERROR
                    if exec is None:
                        self.paso_instruccion_actual = 0

                        aceptar = False
                        for llave in self.lista_etiquetas.keys():
                            if aceptar:
                                self.paso_etiqueta_actual = llave
                                return None  # Terminar Paso

                            if llave == temp:
                                aceptar = True

                        self.paso_etiqueta_actual = "exit"
                        return "exit"
                    else:
                        if exec == self.paso_etiqueta_actual:
                            self.paso_instruccion_actual = 0
                        elif exec == 1:
                            self.paso_instruccion_actual += 1
                        else:
                            self.paso_instruccion_actual = 0
                            self.paso_etiqueta_actual = exec
                            if exec == "exit":
                                return "exit"
        self.cargar_errores()
        return None
        # TERMINAR BORRADO

