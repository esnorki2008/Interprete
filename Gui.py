from PyQt5 import QtCore, QtGui, QtWidgets
from Contenido.LstInstruccion.ABCInstruccion import Ts
from Contenido.LstInstruccion.ABCInstruccion import ListaInstruccion
from Contenido.Analizadores.Sintactico import analizar_ascendente
import re


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(724, 559)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_abrir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_abrir.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.btn_abrir.setObjectName("btn_abrir")
        self.btn_guardar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_guardar.setGeometry(QtCore.QRect(80, 10, 61, 41))
        self.btn_guardar.setObjectName("btn_guardar")
        self.btn_guardar_como = QtWidgets.QPushButton(self.centralwidget)
        self.btn_guardar_como.setGeometry(QtCore.QRect(150, 10, 61, 41))
        self.btn_guardar_como.setObjectName("btn_guardar_como")
        self.btn_ejecutar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ejecutar.setGeometry(QtCore.QRect(220, 10, 61, 41))
        self.btn_ejecutar.setObjectName("btn_ejecutar")
        self.btn_debug = QtWidgets.QPushButton(self.centralwidget)
        self.btn_debug.setGeometry(QtCore.QRect(290, 10, 61, 41))
        self.btn_debug.setObjectName("btn_debug")
        self.btn_siguiente_paso = QtWidgets.QPushButton(self.centralwidget)
        self.btn_siguiente_paso.setGeometry(QtCore.QRect(360, 10, 61, 41))
        self.btn_siguiente_paso.setObjectName("btn_siguiente_paso")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 70, 711, 451))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.txt_consola = QtWidgets.QTextEdit(self.tab)
        self.txt_consola.setGeometry(QtCore.QRect(10, 340, 391, 71))
        self.txt_consola.setObjectName("txt_consola")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_4.setGeometry(QtCore.QRect(0, 0, 411, 331))
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.txt_entrada = QtWidgets.QTextEdit(self.tab_7)
        self.txt_entrada.setGeometry(QtCore.QRect(10, 20, 391, 281))
        self.txt_entrada.setObjectName("txt_entrada")
        self.tabWidget_4.addTab(self.tab_7, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(410, 20, 291, 391))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 10, 276, 351))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 518, 332))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeView = QtWidgets.QTreeView(self.scrollAreaWidgetContents_2)        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QtCore.QSize(500, 0))
        self.treeView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.treeView.setAnimated(True)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout.addWidget(self.treeView)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_3.setGeometry(QtCore.QRect(10, 10, 681, 411))
        self.scrollArea_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 679, 409))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_graphviz = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.lbl_graphviz.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_graphviz.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_graphviz.setText("")
        self.lbl_graphviz.setScaledContents(False)
        self.lbl_graphviz.setObjectName("lbl_graphviz")
        self.verticalLayout_2.addWidget(self.lbl_graphviz)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 681, 411))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 679, 409))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 661, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 724, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.btn_abrir.clicked.connect(self.color)
        self.btn_ejecutar.clicked.connect(self.parser)



    def graficar_arbol(self):

        import pydot
        global  Ts
        dot_string = Ts.generar_dot()
        graphs = pydot.graph_from_dot_data(dot_string)

        from PyQt5.QtWidgets import QApplication
        #app = QApplication(sys.argv)
        #win = QWidget()
        #l1 = QLabel()
        from PyQt5.QtGui import QPixmap
        qp = QPixmap()
        qp.loadFromData(graphs[0].create_png())
        self.lbl_graphviz.resize(qp.size())
        #m_imageLabel->resize(m_scaleFactor * m_imageLabel->size());
        self.lbl_graphviz.setPixmap(qp)

        #vbox = QVBoxLayout()
        #vbox.addWidget(l1)
        #win.setLayout(vbox)
        #win.setWindowTitle("QPixmap Demo")
        #win.show()
        #sys.exit(app.exec_())

    def hola(self):
        print(self.txt_entrada.toPlainText())

    def pintar_comentarios(self,entrada):
        ini_span = "<span style=" + chr(34) + "color: #015002" + chr(34) + ">"
        return re.sub(r'(#(.*)(\n)?)', ini_span + (r"\1") + "</span>", entrada)

    def pintar_valores(self,entrada):
        ini_span = "<span style=" + chr(34) + "color: #011E94 " + chr(34) + ">"
        return re.sub(r'(("([^"]*)")|( [0-9]+ )|([0-9]\.[0-9]+))', ini_span + (r"\1") + "</span>", entrada)

    def pintar_simbolos(self,entrada):
        ini_span = "<span style=" + chr(34) + "color: #738786 " + chr(34) + ">"
        return re.sub(r'((\+)|(-)|( / )|(\*)|( > )|( < )|( = )|(%)|(!=)|(==)|(\()|(\)))', ini_span + (r"\1") + "</span>", entrada)

    def pintar_variables(self,entrada):
        ini_span = "<span style=" + chr(34) + "color: #058695" + chr(34) + ">"
        return re.sub(r"(\$[a-z]([a-z]|[0-9])*)", ini_span + (r"\1") + "</span>", entrada)

    def pintar_reservadas_grises(self,entrada):
        ini_span = "<span style=" + chr(34) + "color: #738786" + chr(34) + ">"
        return re.sub(r"((main)|(print)|(exit))", ini_span + (r"\1") + "</span>", entrada)

    def pintar_reservadas_moradas(self,entrada):
        ini_span = "<span style=" + chr(34) + "color: #830495  " + chr(34) + ">"
        return re.sub(r"((if)|(goto)|(array))", ini_span + (r"\1") + "</span>", entrada)

    def color(self):

        self.txt_entrada.clear()
        f = open("C:/Users/norki/Desktop/interprete/entrada.txt", "r")
        #f = open("C:/Users/Esnorki/Desktop/interprete/entrada.txt", "r")
        input: str = f.read()

        input = self.pintar_comentarios(input)

        #input = self.pintar_valores(input)

        input = self.pintar_reservadas_grises(input)
        input = self.pintar_reservadas_moradas(input)
        input = self.pintar_variables(input)

        input = self.pintar_simbolos(input)
        input = re.sub(r"(;)", (r"\1") , input)
        input = re.sub(r"(\n)","<br>", input)
        #
        #
        input= "<div contenteditable>\n"+ input

        input +="\n</div>"

        #print(input)
        self.txt_entrada.append(input)

        #print(self.txt_entrada.toPlainText())

    def parser(self):
        try:
            self.txt_consola.clear()
            self.txt_entrada.clear()
            f = open("C:/Users/norki/Desktop/interprete/entrada.txt", "r")
            #f = open("C:/Users/Esnorki/Desktop/interprete/entrada.txt", "r")
            input: str = f.read()
            self.txt_entrada.append(input)
            global Ts
            Ts.guardar_consola(self.txt_consola)




            Ts.nueva_ejecucion()
            raiz_produccion: ListaInstruccion = analizar_ascendente(input)
            if raiz_produccion is not None:
                Ts.cargar_etiquetas(raiz_produccion)
                Ts.ejecutar_main()
            self.color()
            self.graficar_arbol()

            treeView = self.treeView
            treeView.setHeaderHidden(True)
            Ts.guardar_arbol(treeView)
            Ts.actualizar_arbol()

            from PyQt5.QtWidgets import QHeaderView

        except:
            import sys
            print("Oops!", sys.exc_info()[0], "occurred.")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_abrir.setText(_translate("MainWindow", "Abrir"))
        self.btn_guardar.setText(_translate("MainWindow", "Guardar"))
        self.btn_guardar_como.setText(_translate("MainWindow", "Guardar\n"
"Como"))
        self.btn_ejecutar.setText(_translate("MainWindow", "Ejecutar"))
        self.btn_debug.setText(_translate("MainWindow", "Debug"))
        self.btn_siguiente_paso.setText(_translate("MainWindow", "Siguiente\n"
"Paso"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_7), _translate("MainWindow", "Archivo"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Tabla De Simbolos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Archivo Entrada"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Visualizar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Reporte"))
