
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
    f = open("C:/Users/norki/Desktop/interprete/entrada.txt", "r")
    #f = open("C:/Users/Esnorki/Desktop/interprete/entrada.txt", "r")
    input: str = f.read()
    global Ts
    Ts.guardar_consola(None)
    Ts.nueva_ejecucion()
    raiz_produccion: ListaInstruccion = analizar_ascendente(input)
    if raiz_produccion is not None:
        Ts.cargar_etiquetas(raiz_produccion)
        Ts.ejecutar_main()
def graficar_sin_consola():
    f = open("C:/Users/norki/Desktop/interprete/entrada.txt", "r")
    #f = open("C:/Users/Esnorki/Desktop/interprete/entrada.txt", "r")
    input: str = f.read()
    global Ts
    Ts.guardar_consola(None)
    Ts.nueva_ejecucion()
    raiz_produccion: ListaInstruccion = analizar_ascendente(input)
    if raiz_produccion is not None:
        #Ts.cargar_etiquetas(raiz_produccion)
        #Ts.
        #print(raiz_produccion.str_arbol())
        return raiz_produccion.str_arbol()


import pydot
dot_string = "graph { "

dot_string += graficar_sin_consola()

dot_string += " } "
graphs = pydot.graph_from_dot_data( dot_string )
#svg_string = graphs[0].create_svg()
#graphs.write_pdf("C:/Users/Norki/Desktop/Interprete/hola.pdf")



from IPython.display import Image, display

class photo(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(photo, self).__init__(parent)
        uic.loadUi('EmployeeUpdate.ui', self)
        self.btn.clicked.connect(self.attachImage)

    def attachImage(self):
        lay = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.imageLabel)
        path = "G:/Data Analytics/Resnsol Face Recognition/a.jpg"
        pixMap = QtGui.QPixmap(path)
        self.imageLabel.setPixmap(pixMap)
        self.imageScrollArea.setWidgetResizable(True)
        self.imageLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


def viewPydot(pdot):

       app = QApplication(sys.argv)
       win = QWidget()
       l1 = QLabel()
       qp = QPixmap()
       qp.loadFromData(pdot[0].create_png())

       l1.setPixmap(qp)

       vbox = QVBoxLayout()
       vbox.addWidget(l1)
       win.setLayout(vbox)
       win.setWindowTitle("QPixmap Demo")
       win.show()
       sys.exit(app.exec_())

viewPydot(graphs)
#cargar_sin_consola()
#ventana:Ui_MainWindow =cargar_ventana()

#print(raiz_produccion.str_arbol_encabezado())
#raiz_produccion.ejecutar()
# for Prod in raiz_produccion:
#   print(Prod.ejecutar().dar_valor())
#  print(Prod.str_arbol())
