
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

from Gui import Ui_MainWindow
from Contenido.LstInstruccion.ABCInstruccion import ListaInstruccion
from Contenido.Analizadores.Sintactico import analizar_ascendente
from Contenido.LstInstruccion.ABCInstruccion import Ts

#sys.setrecursionlimit()

#FALTAN CASTEOS , OPERACIONES CON STRING Y ARREGLOS Y UNSET
def cargar_ventana():

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    return app




def cargar_sin_consola():
    #f = open("C:/Users/norki/Desktop/interprete/entrada.txt", "r")
    f = open("C:/Users/Esnorki/Desktop/interprete/entrada.txt", "r")
    input: str = f.read()
    global Ts
    Ts.guardar_consola(None)
    Ts.nueva_ejecucion()
    raiz_produccion: ListaInstruccion = analizar_ascendente(input)
    if raiz_produccion is not None:
        Ts.cargar_etiquetas(raiz_produccion)
        Ts.ejecutar_main()

    print(Ts.generar_dot())

def graficar_sin_consola():
        #f = open("C:/Users/norki/Desktop/interprete/entrada.txt", "r")
        f = open("C:/Users/Esnorki/Desktop/interprete/entrada.txt", "r")
        input: str = f.read()
        global Ts
        Ts.guardar_consola(None)
        Ts.nueva_ejecucion()
        raiz_produccion: ListaInstruccion = analizar_ascendente(input)
        if raiz_produccion is not None:
            # Ts.cargar_etiquetas(raiz_produccion)
            # Ts.
            # print(raiz_produccion.str_arbol())
            print( raiz_produccion.str_arbol())

#svg_string = graphs[0].create_svg()
#graphs.write_pdf("C:/Users/Norki/Desktop/Interprete/hola.pdf")

#print(dot_string)





#graficar_sin_consola()
#cargar_sin_consola()
#ventana:Ui_MainWindow =cargar_ventana()

#print(raiz_produccion.str_arbol_encabezado())
#raiz_produccion.ejecutar()
# for Prod in raiz_produccion:
#   print(Prod.ejecutar().dar_valor())
#  print(Prod.str_arbol())

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QFont, QColor


class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)


class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('World Country Diagram')
        self.resize(500, 700)

        treeView = QTreeView()
        treeView.setHeaderHidden(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        # America
        america = StandardItem('America', 16, set_bold=True)

        california = StandardItem('California', 14)
        america.appendRow(california)

        oakland = StandardItem('Oakland', 12, color=QColor(155, 0, 0))
        sanfrancisco = StandardItem('San Francisco', 12, color=QColor(155, 0, 0))
        sanjose = StandardItem('San Jose', 12, color=QColor(155, 0, 0))

        california.appendRow(oakland)
        california.appendRow(sanfrancisco)
        california.appendRow(sanjose)

        texas = StandardItem('Texas', 14)
        america.appendRow(texas)

        austin = StandardItem('Austin', 12, color=QColor(155, 0, 0))
        houston = StandardItem('Houston', 12, color=QColor(155, 0, 0))
        dallas = StandardItem('dallas', 12, color=QColor(155, 0, 0))

        texas.appendRow(austin)
        texas.appendRow(houston)
        texas.appendRow(dallas)

        # Canada
        canada = StandardItem('America', 16, set_bold=True)

        alberta = StandardItem('Alberta', 14)
        bc = StandardItem('British Columbia', 14)
        ontario = StandardItem('Ontario', 14)
        canada.appendRows([alberta, bc, ontario])

        rootNode.appendRow(america)
        rootNode.appendRow(canada)

        treeView.setModel(treeModel)
        treeView.expandAll()
        treeView.doubleClicked.connect(self.getValue)

        self.setCentralWidget(treeView)

    def getValue(self, val):
        print(val.data())
        print(val.row())
        print(val.column())


app = QApplication(sys.argv)

demo = AppDemo()
demo.show()

sys.exit(app.exec_())