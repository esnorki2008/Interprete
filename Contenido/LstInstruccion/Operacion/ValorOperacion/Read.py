from Contenido.LstInstruccion.Registro.Valor import Valor
import re

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel)
import sys


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Entrada De La Consola'
        self.left = 10
        self.top = 10
        self.width = 20
        self.height = 20
        self.initUI()
        self.leido=""

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Entrada", "Ingrese La Entrada:", QLineEdit.Normal, "")
        self.leido=text


def read():
    tipo_resultante = 2
    S = App()
    (S.getText())
    rst = S.leido#input("")
    # rst = input()
    x = re.search("^\d+\.\d+$", rst)
    if x is not None:
        tipo_resultante = 1
        rst = float(rst)
    else:
        x = re.search("^\d+$", rst)
        if x is not None:
            tipo_resultante = 0
            rst = int(rst)
    print(tipo_resultante)
    return Valor(rst, tipo_resultante)
