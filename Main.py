
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Gui import Ui_MainWindow
from Contenido.LstInstruccion.ABCInstruccion import ListaInstruccion
from Contenido.Analizadores.Sintactico import analizar_ascendente
from Contenido.LstInstruccion.ABCInstruccion import Ts






def cargar_ventana():

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    return app





#ventana:Ui_MainWindow =cargar_ventana()

def cargar_sin_consola():
    # f = open("C:/Users/norki/Desktop/interprete/entrada.txt", "r")
    f = open("C:/Users/Esnorki/Desktop/interprete/entrada.txt", "r")
    input: str = f.read()
    global Ts
    Ts.guardar_consola(None)
    Ts.nueva_ejecucion()
    raiz_produccion: ListaInstruccion = analizar_ascendente(input)
    Ts.cargar_etiquetas(raiz_produccion)
    Ts.ejecutar_main()
cargar_sin_consola()


#print(raiz_produccion.str_arbol_encabezado())
#raiz_produccion.ejecutar()
# for Prod in raiz_produccion:
#   print(Prod.ejecutar().dar_valor())
#  print(Prod.str_arbol())
