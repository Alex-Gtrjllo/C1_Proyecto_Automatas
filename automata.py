# from obtenerCalificaciones import *
import obtenerCalificaciones
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import sys
from Vista.ui_datos import Ui_datos
qtCreatorFile = "Vista/main.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_iniciar.clicked.connect(self.iniciar)

    def iniciar(self):
        datos, status = main(self.link.text(), self.matricula.text(),
                     self.password.text())
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_datos()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

        header_view = self.ui.table.horizontalHeader()
        idx = header_view.count() - 2
        header_view.setSectionResizeMode(idx, QtWidgets.QHeaderView.ResizeToContents)
        fila = 0
        for x in reversed(range(len(datos))):
            columna = 0
            self.ui.table.insertRow(fila)
            celda = QTableWidgetItem(datos[x])
            self.ui.table.setItem(fila, columna, celda)
            columna+=1
            celda = QTableWidgetItem(status[x])
            self.ui.table.setItem(fila, columna, celda)
        self.ui.table.setSortingEnabled(True) 


class automata:

    def obtener_datos(self, link, matricula, password):
        webscrapping = obtenerCalificaciones.calificaciones(
            link, matricula, password)
        calificaciones = webscrapping.obtener_materias()
        return calificaciones

    def imprimir(self):
        datos = automata.obtener_datos(self)
        for i in datos:
            print(i)
        print(self.cadena)

    def validar_dato(self, dato):
        self.abecedario = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                           'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                           'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú'}
        self.estado = 1
        for x in range(len(dato)):
            if (self.estado == 1):
                if (dato[x] in self.abecedario):
                    self.estado = 2
                else:
                    return False
            elif (self.estado == 2):
                if (dato[x] in self.abecedario):
                    self.estado = 2
                elif(dato[x] == " "):
                    self.estado = 3
                else:
                    return False
            elif (self.estado == 3):
                if (dato[x] in self.abecedario):
                    self.estado = 3
                elif(dato[x] == " "):
                    self.estado = 2
                else:
                    return False
        if (self.estado == 2 or self.estado == 3):
            return True

    def validar_datos(self):
        self.abecedario_simple = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
        self.abecedario = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú'}

        self.datos = automata.obtener_datos(self)
        self.estado = 1
        for i in self.datos:
            for x in range(len(i)):
                if (self.estado == 1):
                    if (i[x] in self.abecedario):
                        self.estado = 2
                    else:
                        return False
                elif (self.estado == 2):
                    if (i[x] in self.abecedario):
                        self.estado = 2
                    else:
                        return False
            if (self.estado == 2):
                return True


def main(link, matricula, password):
    programa = automata()
    # programa.imprimir()
    # res = programa.validar_datos()
    datos = programa.obtener_datos(link, matricula, password)
    validos = []
    status = []
    for i in datos:
        res = programa.validar_dato(i)
        if (res):
            validos.append(i)
            status.append("válido")
            print(i, "es", "materia válida")
        else:
            validos.append(i)
            status.append("Inválido")
            print(i, "es", "materia invalida")
    return validos, status


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
