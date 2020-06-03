import ply.lex as lex
import ply.yacc as yacc
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Gui import Ui_MainWindow
from Contenido.LstInstruccion.ABCInstruccion import Ts
from Contenido.Analizadores.Lexico import *
from Contenido.Analizadores.Sintactico import *

def cargar_ventana():

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    return app



# Construyendo el analizador léxico
lexer = lex.lex()
parser = yacc.yacc()

#f = open("C:/Users/norki/Desktop/interprete/entrada.txt", "r")
f = open("C:/Users/Esnorki/Desktop/interprete/entrada.txt", "r")
input: str = f.read()
# print(input)
global Ts
raiz_produccion: ABCInstruccion.ListaInstruccion = parser.parse(input)
ventana:Ui_MainWindow =cargar_ventana()

Ts.cargar_etiquetas(raiz_produccion)
Ts.ejecutar_main()

#

#print(raiz_produccion.str_arbol_encabezado())
#raiz_produccion.ejecutar()
# for Prod in raiz_produccion:
#   print(Prod.ejecutar().dar_valor())
#  print(Prod.str_arbol())
