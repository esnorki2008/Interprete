from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QSize
from PyQt5.QtGui import QColor, QFont, QColorConstants

from PyQt5.QtWidgets import QPlainTextEdit, QWidget, QFileDialog, QVBoxLayout

from Contenido.LstInstruccion.ABCInstruccion import Ts
from Contenido.LstInstruccion.ABCInstruccion import ListaInstruccion
from Contenido.Analizadores.Sintactico import analizar_ascendente
import re
from PyQt5.Qsci import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Proyecto")
        MainWindow.resize(1074, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_abrir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_abrir.setGeometry(QtCore.QRect(970, 20, 61, 41))
        self.btn_abrir.setObjectName("btn_abrir")
        self.btn_guardar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_guardar.setGeometry(QtCore.QRect(970, 70, 61, 41))
        self.btn_guardar.setObjectName("btn_guardar")
        self.btn_guardar_como = QtWidgets.QPushButton(self.centralwidget)
        self.btn_guardar_como.setGeometry(QtCore.QRect(970, 120, 61, 41))
        self.btn_guardar_como.setObjectName("btn_guardar_como")
        self.btn_ejecutar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ejecutar.setGeometry(QtCore.QRect(960, 220, 81, 41))
        self.btn_ejecutar.setObjectName("btn_ejecutar")
        self.btn_debug = QtWidgets.QPushButton(self.centralwidget)
        self.btn_debug.setGeometry(QtCore.QRect(970, 320, 61, 41))
        self.btn_debug.setObjectName("btn_debug")
        self.btn_siguiente_paso = QtWidgets.QPushButton(self.centralwidget)
        self.btn_siguiente_paso.setGeometry(QtCore.QRect(970, 370, 61, 41))
        self.btn_siguiente_paso.setObjectName("btn_siguiente_paso")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 941, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.txt_consola = QtWidgets.QTextEdit(self.tab)
        self.txt_consola.setGeometry(QtCore.QRect(10, 410, 511, 101))
        self.txt_consola.setObjectName("txt_consola")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_4.setGeometry(QtCore.QRect(0, 0, 531, 391))
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_8)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 521, 361))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.frame_txt_entrada = QtWidgets.QFrame(self.tab_10)
        self.frame_txt_entrada.setGeometry(QtCore.QRect(10, 10, 501, 321))
        self.frame_txt_entrada.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_txt_entrada.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_txt_entrada.setObjectName("frame_txt_entrada")
        self.tabWidget_3.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.frame_txt_entrada_sin_optimizar = QtWidgets.QFrame(self.tab_11)
        self.frame_txt_entrada_sin_optimizar.setGeometry(QtCore.QRect(10, 10, 501, 321))
        self.frame_txt_entrada_sin_optimizar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_txt_entrada_sin_optimizar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_txt_entrada_sin_optimizar.setObjectName("frame_txt_entrada_sin_optimizar")
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tabWidget_4.addTab(self.tab_8, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(540, 20, 391, 491))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.frame_txt_minor_c = QtWidgets.QFrame(self.tab_12)
        self.frame_txt_minor_c.setGeometry(QtCore.QRect(10, 10, 361, 441))
        self.frame_txt_minor_c.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_txt_minor_c.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_txt_minor_c.setObjectName("frame_txt_minor_c")
        self.tabWidget_2.addTab(self.tab_12, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 10, 361, 441))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 518, 422))
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
        self.tab_reporte = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tab_reporte.setGeometry(QtCore.QRect(20, 10, 661, 381))
        self.tab_reporte.setObjectName("tab_reporte")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea_4.setGeometry(QtCore.QRect(0, 10, 641, 341))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 639, 339))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabla_etiqueta = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_4)
        self.tabla_etiqueta.setObjectName("tabla_etiqueta")
        self.tabla_etiqueta.setColumnCount(0)
        self.tabla_etiqueta.setRowCount(0)
        self.verticalLayout.addWidget(self.tabla_etiqueta)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.tab_reporte.addTab(self.tab_4, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.tab_6)
        self.scrollArea_5.setGeometry(QtCore.QRect(0, 10, 641, 341))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 639, 339))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabla_error = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_5)
        self.tabla_error.setObjectName("tabla_error")
        self.tabla_error.setColumnCount(0)
        self.tabla_error.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tabla_error)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.tab_reporte.addTab(self.tab_6, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.textEdit = QtWidgets.QTextEdit(self.tab_9)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 631, 321))
        self.textEdit.setObjectName("textEdit")
        self.tab_reporte.addTab(self.tab_9, "")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.tabWidget.addTab(self.tab_13, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.btn_ejecutar_desc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ejecutar_desc.setGeometry(QtCore.QRect(960, 270, 81, 41))
        self.btn_ejecutar_desc.setObjectName("btn_ejecutar_desc")
        self.btn_ejecutar_minor_c = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ejecutar_minor_c.setGeometry(QtCore.QRect(950, 170, 101, 41))
        self.btn_ejecutar_minor_c.setObjectName("btn_ejecutar_minor_c")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        self.menuAnalisis = QtWidgets.QMenu(self.menubar)
        self.menuAnalisis.setObjectName("menuAnalisis")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_Como = QtWidgets.QAction(MainWindow)
        self.actionGuardar_Como.setObjectName("actionGuardar_Como")
        self.actionGuardar_Como_2 = QtWidgets.QAction(MainWindow)
        self.actionGuardar_Como_2.setObjectName("actionGuardar_Como_2")
        self.actionAscendente = QtWidgets.QAction(MainWindow)
        self.actionAscendente.setObjectName("actionAscendente")
        self.actionDescendente = QtWidgets.QAction(MainWindow)
        self.actionDescendente.setObjectName("actionDescendente")
        self.actionReiniciar_Debug = QtWidgets.QAction(MainWindow)
        self.actionReiniciar_Debug.setObjectName("actionReiniciar_Debug")
        self.actionSiguiente_Paso_Debug = QtWidgets.QAction(MainWindow)
        self.actionSiguiente_Paso_Debug.setObjectName("actionSiguiente_Paso_Debug")
        self.actionCopiar = QtWidgets.QAction(MainWindow)
        self.actionCopiar.setObjectName("actionCopiar")
        self.actionPegar = QtWidgets.QAction(MainWindow)
        self.actionPegar.setObjectName("actionPegar")
        self.actionBuscar = QtWidgets.QAction(MainWindow)
        self.actionBuscar.setObjectName("actionBuscar")
        self.actionReemplazar = QtWidgets.QAction(MainWindow)
        self.actionReemplazar.setObjectName("actionReemplazar")
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_Como)
        self.menuArchivo.addAction(self.actionGuardar_Como_2)
        self.menuEditar.addAction(self.actionCopiar)
        self.menuEditar.addAction(self.actionPegar)
        self.menuEditar.addAction(self.actionBuscar)
        self.menuEditar.addAction(self.actionReemplazar)
        self.menuAnalisis.addAction(self.actionAscendente)
        self.menuAnalisis.addAction(self.actionDescendente)
        self.menuAnalisis.addAction(self.actionReiniciar_Debug)
        self.menuAnalisis.addAction(self.actionSiguiente_Paso_Debug)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuAnalisis.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tab_reporte.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.__myFont = QFont()
        self.__myFont.setPointSize(12)
#=========================================================EDITORES===================================
        self.txt_minor_c = QsciScintilla()
        self.txt_minor_c.setText("")
        self.txt_minor_c.setUtf8(True)
        self.txt_minor_c.setFont(self.__myFont)

        # AJUSTES DE TEXTO
        self.txt_minor_c.setWrapMode(QsciScintilla.WrapWord)
        self.txt_minor_c.setWrapVisualFlags(QsciScintilla.WrapFlagByText)
        self.txt_minor_c.setWrapIndentMode(QsciScintilla.WrapIndentIndented)

        # FIN DE LINEA
        self.txt_minor_c.setEolMode(QsciScintilla.EolWindows)
        self.txt_minor_c.setEolVisibility(False)

        # SANGRIA
        self.txt_minor_c.setIndentationsUseTabs(False)
        self.txt_minor_c.setTabWidth(4)
        self.txt_minor_c.setIndentationGuides(True)
        self.txt_minor_c.setTabIndents(True)
        self.txt_minor_c.setAutoIndent(True)

        self.txt_minor_c.setCaretForegroundColor(QColor("#ff0000ff"))
        self.txt_minor_c.setCaretLineVisible(True)
        self.txt_minor_c.setCaretLineBackgroundColor(QColor("#1f0000ff"))
        self.txt_minor_c.setCaretWidth(2)

        # MARGENES
        self.txt_minor_c.setMarginType(0, QsciScintilla.NumberMargin)
        self.txt_minor_c.setMarginWidth(0, "0000")  # con este se puede quitar la linea
        self.txt_minor_c.setMarginsForegroundColor(QColor("#ff888888"))

        # SE COLOCAN LAS REGLAS DEL EDITOR
        self.__lexer = QsciLexerCPP(self.txt_minor_c)
        self.txt_minor_c.setLexer(self.__lexer)

        self.__lyt = QVBoxLayout()
        self.frame_txt_minor_c.setLayout(self.__lyt)
        self.__lyt.addWidget(self.txt_minor_c)
#====================================ENTRADA===========================
        self.txt_entrada = QsciScintilla()
        self.txt_entrada.setText("")
        self.txt_entrada.setUtf8(True)
        self.txt_entrada.setFont(self.__myFont)

        # AJUSTES DE TEXTO
        self.txt_entrada.setWrapMode(QsciScintilla.WrapWord)
        self.txt_entrada.setWrapVisualFlags(QsciScintilla.WrapFlagByText)
        self.txt_entrada.setWrapIndentMode(QsciScintilla.WrapIndentIndented)

        # FIN DE LINEA
        self.txt_entrada.setEolMode(QsciScintilla.EolWindows)
        self.txt_entrada.setEolVisibility(False)

        # SANGRIA
        self.txt_entrada.setIndentationsUseTabs(False)
        self.txt_entrada.setTabWidth(4)
        self.txt_entrada.setIndentationGuides(True)
        self.txt_entrada.setTabIndents(True)
        self.txt_entrada.setAutoIndent(True)

        self.txt_entrada.setCaretForegroundColor(QColor("#ff0000ff"))
        self.txt_entrada.setCaretLineVisible(True)
        self.txt_entrada.setCaretLineBackgroundColor(QColor("#1f0000ff"))
        self.txt_entrada.setCaretWidth(2)

        # MARGENES
        self.txt_entrada.setMarginType(0, QsciScintilla.NumberMargin)
        self.txt_entrada.setMarginWidth(0, "0000")  # con este se puede quitar la linea
        self.txt_entrada.setMarginsForegroundColor(QColor("#ff888888"))

        # SE COLOCAN LAS REGLAS DEL EDITOR
        self.__lexer = QsciLexerRuby(self.txt_entrada)
        self.txt_entrada.setLexer(self.__lexer)

        self.__lyt = QVBoxLayout()
        self.frame_txt_entrada.setLayout(self.__lyt)
        self.__lyt.addWidget(self.txt_entrada)
#========================Entrada Sin Optimizar======================
        self.txt_entrada_sin_optimizar = QsciScintilla()
        self.txt_entrada_sin_optimizar.setText("")
        self.txt_entrada_sin_optimizar.setUtf8(True)
        self.txt_entrada_sin_optimizar.setFont(self.__myFont)

        # AJUSTES DE TEXTO
        self.txt_entrada_sin_optimizar.setWrapMode(QsciScintilla.WrapWord)
        self.txt_entrada_sin_optimizar.setWrapVisualFlags(QsciScintilla.WrapFlagByText)
        self.txt_entrada_sin_optimizar.setWrapIndentMode(QsciScintilla.WrapIndentIndented)

        # FIN DE LINEA
        self.txt_entrada_sin_optimizar.setEolMode(QsciScintilla.EolWindows)
        self.txt_entrada_sin_optimizar.setEolVisibility(False)

        # SANGRIA
        self.txt_entrada_sin_optimizar.setIndentationsUseTabs(False)
        self.txt_entrada_sin_optimizar.setTabWidth(4)
        self.txt_entrada_sin_optimizar.setIndentationGuides(True)
        self.txt_entrada_sin_optimizar.setTabIndents(True)
        self.txt_entrada_sin_optimizar.setAutoIndent(True)

        self.txt_entrada_sin_optimizar.setCaretForegroundColor(QColor("#ff0000ff"))
        self.txt_entrada_sin_optimizar.setCaretLineVisible(True)
        self.txt_entrada_sin_optimizar.setCaretLineBackgroundColor(QColor("#1f0000ff"))
        self.txt_entrada_sin_optimizar.setCaretWidth(2)

        # MARGENES
        self.txt_entrada_sin_optimizar.setMarginType(0, QsciScintilla.NumberMargin)
        self.txt_entrada_sin_optimizar.setMarginWidth(0, "0000")  # con este se puede quitar la linea
        self.txt_entrada_sin_optimizar.setMarginsForegroundColor(QColor("#ff888888"))

        # SE COLOCAN LAS REGLAS DEL EDITOR
        self.__lexer = QsciLexerRuby(self.txt_entrada_sin_optimizar)
        self.txt_entrada_sin_optimizar.setLexer(self.__lexer)

        self.__lyt = QVBoxLayout()
        self.frame_txt_entrada_sin_optimizar.setLayout(self.__lyt)
        self.__lyt.addWidget(self.txt_entrada_sin_optimizar)

#======================================================================


        #Para Abrir,Guardar,Como
        self.btn_abrir.clicked.connect(self.abrir_archivo)
        self.actionGuardar.triggered.connect(self.abrir_archivo)
        self.btn_guardar_como.clicked.connect(self.guardar_archivo_como)
        self.actionGuardar_Como_2.triggered.connect(self.guardar_archivo_como)
        self.actionGuardar_Como.triggered.connect(self.guardar_archivo)
        self.btn_guardar.clicked.connect(self.guardar_archivo)
        #Ejecucion
        self.btn_ejecutar.clicked.connect(self.parser)
        self.actionAscendente.triggered.connect(self.parser)
        self.btn_ejecutar_desc.clicked.connect(self.parser_descendente)
        self.actionDescendente.triggered.connect(self.parser_descendente)
        self.btn_debug.clicked.connect(self.parser_paso_iniciar)
        self.actionReiniciar_Debug.triggered.connect(self.parser_paso_iniciar)
        self.btn_siguiente_paso.clicked.connect(self.parser_paso_ejecutar)
        self.actionSiguiente_Paso_Debug.triggered.connect(self.parser_paso_ejecutar)

        self.btn_ejecutar_minor_c.clicked.connect(self.ejecutar_main_c)


    def ejecutar_main_c(self):
        from AProyecto2.Main import analizar_minor_c,analizar_minor_c_optimizar_3D
        rst = analizar_minor_c_optimizar_3D(self.txt_minor_c.text())
        self.txt_entrada.setText(rst)

    

    def graficar_arbol(self):
        import pydot
        global Ts
        dot_string = Ts.generar_dot()
        graphs = pydot.graph_from_dot_data(dot_string)

        from PyQt5.QtWidgets import QApplication
        # app = QApplication(sys.argv)
        # win = QWidget()
        # l1 = QLabel()
        from PyQt5.QtGui import QPixmap
        qp = QPixmap()
        qp.loadFromData(graphs[0].create_png())
        self.lbl_graphviz.resize(qp.size())
        # m_imageLabel->resize(m_scaleFactor * m_imageLabel->size());
        self.lbl_graphviz.setPixmap(qp)

        # vbox = QVBoxLayout()
        # vbox.addWidget(l1)
        # win.setLayout(vbox)
        # win.setWindowTitle("QPixmap Demo")
        # win.show()
        # sys.exit(app.exec_())
    archivo_actual=None
    def guardar_archivo(self):
        if self.archivo_actual is None:
            self.guardar_archivo_como()
        else:
            file = open(self.archivo_actual, 'w')
            text = self.txt_entrada.text()
            file.write(text)
            self.color(text)

    def guardar_archivo_como(self):
        try:
            fname = QFileDialog.getSaveFileName()
            file = open(fname[0], 'w')
            text = self.txt_entrada.text()
            file.write(text)
            self.color(text)
        except:
            pass

    def abrir_archivo(self):
        try:
            fname = QFileDialog.getOpenFileName()
            f = open(fname[0], "r")
            input: str = f.read()
            self.color(input)
            self.archivo_actual = fname[0]
            self.txt_minor_c.setText(input)
        except:
            pass




    def color(self,input):
        return
        

    def parser_paso_iniciar(self):
        self.pasex = 1;
        self.ejecutar_main_c()
        try:

            self.txt_consola.clear()
            dim = self.txt_entrada.text()
            input = dim
            global Ts
            Ts.guardar_consola(self.txt_consola)
            Ts.nueva_ejecucion(input)
            raiz_produccion: ListaInstruccion = analizar_ascendente(input)
            self.raiz_global = raiz_produccion
            Ts.guardar_tabla_etiqueta(self.tabla_etiqueta)
            Ts.guardar_tabla_error(self.tabla_error)
            if raiz_produccion is not None:
                Ts.cargar_etiquetas(raiz_produccion)
            else :
                Ts.mensaje_info("Error", "Error En El Codigo")
            #self.color()
            self.graficar_arbol()

            treeView = self.treeView
            treeView.setHeaderHidden(True)
            Ts.guardar_arbol(treeView)
            Ts.actualizar_arbol()


            self.textEdit.clear()
            self.textEdit.append("<div contenteditable>" + Ts.rp_cabecera() + "</div>")
        except:
            import sys
            Ts.mensaje_info("Error", "Error Durante El Analisis")
            print("Oops!", sys.exc_info()[0], "occurred.")
    raiz_global = None
    pasex = 1
    def parser_paso_ejecutar(self):

        try:

            if self.raiz_global is not None:
                #DEFAULT_INDICATOR_ID = 1
                #self.txt_entrada.indicatorDefine(QsciScintilla.FullBoxIndicator, self.pasex)
                #self.txt_entrada.fillIndicatorRange(self.pasex, 0, self.pasex + 1, 0, self.pasex)
                #self.pasex+=1

                #print(self.pasex)
                ex = Ts.paso_a_paso_ejecutar()
                if ex == "exit":
                    Ts.mensaje_info("Informacion", "Ejecucion Paso A Paso Completo")
                    self.raiz_global = None
                treeView = self.treeView
                treeView.setHeaderHidden(True)
                Ts.guardar_arbol(treeView)
                Ts.actualizar_arbol()
            else :
                Ts.mensaje_info("Ejecucion", "No hay nada que ejecutar")


        except:
            import sys
            Ts.mensaje_info("Error", "Error Durante El Analisis")
            print("Oops!", sys.exc_info()[0], "occurred.")

    def parser(self):
        try:
            self.txt_consola.clear()

            global Ts
            Ts.guardar_consola(self.txt_consola)

            dim=self.txt_entrada.text()
            input = dim

            Ts.nueva_ejecucion(input)
            raiz_produccion: ListaInstruccion = analizar_ascendente(input)
            Ts.guardar_tabla_etiqueta(self.tabla_etiqueta)
            Ts.guardar_tabla_error(self.tabla_error)
            if raiz_produccion is not None:
                Ts.cargar_etiquetas(raiz_produccion)
                Ts.ejecutar_main()
            else :
                Ts.mensaje_info("Error", "Error En El Codigo ")

            #self.color()
            self.graficar_arbol()

            treeView = self.treeView
            treeView.setHeaderHidden(True)
            Ts.guardar_arbol(treeView)
            Ts.actualizar_arbol()

            self.textEdit.clear()
            self.textEdit.append("<div contenteditable>"+Ts.rp_cabecera()+"</div>")
        except:
            import sys
            Ts.mensaje_info("Error", "Error Durante El Analisis")
            print("Oops!", sys.exc_info()[0], "occurred.")


    def parser_descendente(self):
        try:
            self.txt_consola.clear()
            global Ts
            Ts.guardar_consola(self.txt_consola)
            dim = self.txt_entrada.text()
            input = dim
            Ts.nueva_ejecucion(input)
            from Contenido.Analizadores.SintacticoDescendente import analizar_descendente
            raiz_produccion: ListaInstruccion = analizar_descendente(input)
            Ts.guardar_tabla_etiqueta(self.tabla_etiqueta)
            Ts.guardar_tabla_error(self.tabla_error)
            if raiz_produccion is not None:
                Ts.cargar_etiquetas(raiz_produccion)
                Ts.ejecutar_main()
            else :
                Ts.mensaje_info("Error", "Error En El Codigo")


            #self.color()
            self.graficar_arbol()

            treeView = self.treeView
            treeView.setHeaderHidden(True)
            Ts.guardar_arbol(treeView)
            Ts.actualizar_arbol()

            self.textEdit.clear()
            self.textEdit.append("<div contenteditable>" + Ts.rp_cabecera() + "</div>")
        except:
            import sys
            Ts.mensaje_info("Error", "Error Durante El Analisis")
            print("Oops!", sys.exc_info()[0], "occurred.")



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_abrir.setText(_translate("MainWindow", "Abrir"))
        self.btn_guardar.setText(_translate("MainWindow", "Guardar"))
        self.btn_guardar_como.setText(_translate("MainWindow", "Guardar\n"
                                                               "Como"))
        self.btn_ejecutar.setText(_translate("MainWindow", "Ejecutar\n"
"Ascendente"))
        self.btn_debug.setText(_translate("MainWindow", "Debug"))
        self.btn_siguiente_paso.setText(_translate("MainWindow", "Siguiente\n"
"Paso"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), _translate("MainWindow", "Optimizada"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("MainWindow", "Sin Optimizar"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_8), _translate("MainWindow", "Salida De MinorC"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), _translate("MainWindow", "Entrada Minor C"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Tabla De Simbolos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Archivo Entrada"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Visualizar"))
        self.tab_reporte.setTabText(self.tab_reporte.indexOf(self.tab_4), _translate("MainWindow", "Etiquetas"))
        self.tab_reporte.setTabText(self.tab_reporte.indexOf(self.tab_6), _translate("MainWindow", "Errores"))
        self.tab_reporte.setTabText(self.tab_reporte.indexOf(self.tab_9), _translate("MainWindow", "Gramatical"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Reporte"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), _translate("MainWindow", "Visualizar Minor C"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Reporte Minor C"))
        self.btn_ejecutar_desc.setText(_translate("MainWindow", "Ejecutar\n"
"Descendente"))
        self.btn_ejecutar_minor_c.setText(_translate("MainWindow", "Ejecutar Minor C"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuEditar.setTitle(_translate("MainWindow", "Editar"))
        self.menuAnalisis.setTitle(_translate("MainWindow", "Analisis"))
        self.actionGuardar.setText(_translate("MainWindow", "Abrir"))
        self.actionGuardar_Como.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar_Como_2.setText(_translate("MainWindow", "Guardar Como"))
        self.actionAscendente.setText(_translate("MainWindow", "Ascendente"))
        self.actionDescendente.setText(_translate("MainWindow", "Descendente"))
        self.actionReiniciar_Debug.setText(_translate("MainWindow", "Reiniciar Debug"))
        self.actionSiguiente_Paso_Debug.setText(_translate("MainWindow", "Siguiente Paso Debug"))
        self.actionCopiar.setText(_translate("MainWindow", "Copiar"))
        self.actionPegar.setText(_translate("MainWindow", "Pegar"))
        self.actionBuscar.setText(_translate("MainWindow", "Buscar"))
        self.actionReemplazar.setText(_translate("MainWindow", "Reemplazar"))

if __name__ == "__main__":
    pass

