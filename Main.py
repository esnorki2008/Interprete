
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
    Ts.texto_analisis = input
    raiz_produccion: ListaInstruccion = analizar_ascendente(input)
    if raiz_produccion is not None:
        Ts.cargar_etiquetas(raiz_produccion)
        Ts.ejecutar_main()

    #print(Ts.generar_dot())

def graficar_sin_consola():
        f = open("C:/Users/norki/Desktop/interprete/entrada.txt", "r")
        #f = open("C:/Users/Esnorki/Desktop/interprete/entrada.txt", "r")
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

ventana:Ui_MainWindow =cargar_ventana()
def cargar_proyecto2():
    from AProyecto2.Main import analizar_minor_c_optimizar_3D

    cadenita = '''
    int main(){
        int a[4]={5,508};
    } 

'''
    analizar_minor_c_optimizar_3D(cadenita)

#cargar_proyecto2()