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
        self.link.setText(
            "https://platinum.upchiapas.edu.mx/alumnos/calificaciones/historial")
        self.matricula.setText("193262")
        self.password.setText("SqeadsltV=(h+c)*a_up19")

    def iniciar(self):
        datos, status, cal = main(self.link.text(), self.matricula.text(),
                             self.password.text())
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_datos()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

        header_view = self.ui.table.horizontalHeader()
        idx = header_view.count() - 2
        header_view.setSectionResizeMode(
            idx, QtWidgets.QHeaderView.ResizeToContents)
        fila = 0
        for x in reversed(range(len(datos))):
            columna = 0
            self.ui.table.insertRow(fila)
            celda = QTableWidgetItem(datos[x])
            self.ui.table.setItem(fila, columna, celda)
            columna = 1
            celda = QTableWidgetItem(status[x])
            self.ui.table.setItem(fila, columna, celda)
            for i in cal[x]:
                columna += 1
                celda = QTableWidgetItem(i)
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

    def buscar_trasicion(self, estado, dato):
        for i in self.funcion_transicion:
            status = [self.estados[estado], dato] == i[0:2]
            if status == True:
                return status, i
        return status, i

    def validar_dato(self, dato):
        self.alfabeto_abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                                    'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Á', 'É', 'Í', 'Ó', 'Ú']
        self.alfabeto_espacio = [' ', '.']
        self.alfabeto_numeros = ['0', '1', '2',
                                 '3', '4', '5', '6', '7', '8', '9']
        self.abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                           'l', 'm', 'n',  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                           'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú']
        self.estados = ['A', 'B', 'C', 'D', 'E', 'F',
                        'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        self.estados_finales = ['B', 'C', 'D',
                                'E', 'G', 'H', 'K', 'L', 'N']

        self.funcion_transicion = [
            [self.estados[0], self.alfabeto_abecedario[0], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[1], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[2], self.estados[1]], 
            [self.estados[0], self.alfabeto_abecedario[3], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[4], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[5], self.estados[1]], 
            [self.estados[0], self.alfabeto_abecedario[6], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[7], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[8], self.estados[1]], 
            [self.estados[0], self.alfabeto_abecedario[9], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[10], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[11], self.estados[1]], 
            [self.estados[0], self.alfabeto_abecedario[12], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[13], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[14], self.estados[1]], 
            [self.estados[0], self.alfabeto_abecedario[15], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[16], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[17], self.estados[1]], 
            [self.estados[0], self.alfabeto_abecedario[18], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[19], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[20], self.estados[1]], 
            [self.estados[0], self.alfabeto_abecedario[21], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[22], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[23], self.estados[1]], 
            [self.estados[0], self.alfabeto_abecedario[24], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[25], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[26], self.estados[1]], 
            [self.estados[0], self.alfabeto_abecedario[27], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[28], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[29], self.estados[1]], 
            [self.estados[0], self.alfabeto_abecedario[30], self.estados[1]], [self.estados[0], self.alfabeto_abecedario[31], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[0], self.estados[1]], 
            [self.estados[1], self.alfabeto_abecedario[1], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[2], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[3], self.estados[1]], 
            [self.estados[1], self.alfabeto_abecedario[4], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[5], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[6], self.estados[1]], 
            [self.estados[1], self.alfabeto_abecedario[7], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[8], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[9], self.estados[1]], 
            [self.estados[1], self.alfabeto_abecedario[10], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[11], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[12], self.estados[1]], 
            [self.estados[1], self.alfabeto_abecedario[13], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[14], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[15], self.estados[1]], 
            [self.estados[1], self.alfabeto_abecedario[16], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[17], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[18], self.estados[1]], 
            [self.estados[1], self.alfabeto_abecedario[19], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[20], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[21], self.estados[1]], 
            [self.estados[1], self.alfabeto_abecedario[22], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[23], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[24], self.estados[1]], 
            [self.estados[1], self.alfabeto_abecedario[25], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[26], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[27], self.estados[1]], 
            [self.estados[1], self.alfabeto_abecedario[28], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[29], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[30], self.estados[1]], 
            [self.estados[1], self.alfabeto_abecedario[31], self.estados[1]], [self.estados[1], self.alfabeto_espacio[0], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[0], self.estados[2]], 
            [self.estados[2], self.alfabeto_abecedario[1], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[2], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[3], self.estados[2]], 
            [self.estados[2], self.alfabeto_abecedario[4], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[5], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[6], self.estados[2]], 
            [self.estados[2], self.alfabeto_abecedario[7], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[8], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[9], self.estados[2]], 
            [self.estados[2], self.alfabeto_abecedario[10], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[11], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[12], self.estados[2]],
            [self.estados[2], self.alfabeto_abecedario[13], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[14], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[15], self.estados[2]], 
            [self.estados[2], self.alfabeto_abecedario[16], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[17], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[18], self.estados[2]], 
            [self.estados[2], self.alfabeto_abecedario[19], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[20], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[21], self.estados[2]], 
            [self.estados[2], self.alfabeto_abecedario[22], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[23], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[24], self.estados[2]], 
            [self.estados[2], self.alfabeto_abecedario[25], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[26], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[27], self.estados[2]], 
            [self.estados[2], self.alfabeto_abecedario[28], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[29], self.estados[2]], [self.estados[2], self.alfabeto_abecedario[30], self.estados[2]], 
            [self.estados[2], self.alfabeto_abecedario[31], self.estados[2]], [self.estados[2], self.alfabeto_espacio[0], self.estados[1]], [self.estados[0], self.alfabeto_numeros[1], self.estados[5]], 
            [self.estados[5], self.alfabeto_numeros[0], self.estados[6]], [self.estados[6], self.alfabeto_numeros[0], self.estados[7]], [self.estados[5], self.alfabeto_numeros[1], self.estados[8]], 
            [self.estados[5], self.alfabeto_numeros[2], self.estados[8]], [self.estados[5], self.alfabeto_numeros[3], self.estados[8]], [self.estados[5], self.alfabeto_numeros[4], self.estados[8]], 
            [self.estados[5], self.alfabeto_numeros[5], self.estados[8]], [self.estados[5], self.alfabeto_numeros[6], self.estados[8]], [self.estados[5], self.alfabeto_numeros[7], self.estados[8]], 
            [self.estados[5], self.alfabeto_numeros[8], self.estados[8]], [self.estados[5], self.alfabeto_numeros[9], self.estados[8]], [self.estados[8], self.alfabeto_espacio[1], self.estados[9]], 
            [self.estados[9], self.alfabeto_numeros[1], self.estados[10]], [self.estados[9], self.alfabeto_numeros[2], self.estados[10]], [self.estados[9], self.alfabeto_numeros[3], self.estados[10]], 
            [self.estados[9], self.alfabeto_numeros[4], self.estados[10]], [self.estados[9], self.alfabeto_numeros[5], self.estados[10]], [self.estados[9], self.alfabeto_numeros[6], self.estados[10]], 
            [self.estados[9], self.alfabeto_numeros[7], self.estados[10]], [self.estados[9], self.alfabeto_numeros[8], self.estados[10]], [self.estados[9], self.alfabeto_numeros[9], self.estados[10]], 
            [self.estados[10], self.alfabeto_numeros[1], self.estados[11]], [self.estados[10], self.alfabeto_numeros[2], self.estados[11]], [self.estados[10], self.alfabeto_numeros[3], self.estados[11]], 
            [self.estados[10], self.alfabeto_numeros[4], self.estados[11]], [self.estados[10], self.alfabeto_numeros[5], self.estados[11]], [self.estados[10], self.alfabeto_numeros[6], self.estados[11]], 
            [self.estados[10], self.alfabeto_numeros[7], self.estados[11]], [self.estados[10], self.alfabeto_numeros[8], self.estados[11]], [self.estados[10], self.alfabeto_numeros[9], self.estados[11]], 
            [self.estados[9], self.alfabeto_numeros[0], self.estados[12]], [self.estados[12], self.alfabeto_numeros[1], self.estados[13]], [self.estados[12], self.alfabeto_numeros[2], self.estados[13]], 
            [self.estados[12], self.alfabeto_numeros[3], self.estados[13]], [self.estados[12], self.alfabeto_numeros[4], self.estados[13]], [self.estados[12], self.alfabeto_numeros[5], self.estados[13]], 
            [self.estados[12], self.alfabeto_numeros[6], self.estados[13]], [self.estados[12], self.alfabeto_numeros[7], self.estados[13]], [self.estados[12], self.alfabeto_numeros[8], self.estados[13]], 
            [self.estados[12], self.alfabeto_numeros[9], self.estados[13]], [self.estados[0], self.alfabeto_numeros[2], self.estados[3]], [self.estados[0], self.alfabeto_numeros[3], self.estados[3]], 
            [self.estados[0], self.alfabeto_numeros[4], self.estados[3]], [self.estados[0], self.alfabeto_numeros[5], self.estados[3]], [self.estados[0], self.alfabeto_numeros[6], self.estados[3]],
            [self.estados[0], self.alfabeto_numeros[7], self.estados[3]], [self.estados[0], self.alfabeto_numeros[8], self.estados[3]], [self.estados[0], self.alfabeto_numeros[9], self.estados[3]],
            [self.estados[3], self.alfabeto_numeros[0], self.estados[4]], [self.estados[3], self.alfabeto_numeros[1], self.estados[4]], [self.estados[3], self.alfabeto_numeros[2], self.estados[4]],
            [self.estados[3], self.alfabeto_numeros[3], self.estados[4]], [self.estados[3], self.alfabeto_numeros[4], self.estados[4]], [self.estados[3], self.alfabeto_numeros[5], self.estados[4]],
            [self.estados[3], self.alfabeto_numeros[6], self.estados[4]], [self.estados[3], self.alfabeto_numeros[7], self.estados[4]], [self.estados[3], self.alfabeto_numeros[8], self.estados[4]],
            [self.estados[3], self.alfabeto_numeros[9], self.estados[4]], [self.estados[4], self.alfabeto_espacio[1], self.estados[9]]
        ]
        
        self.estado_siguiente = 0
        self.estado_final = 'A'
        self.estatus = False
        for x in range(len(dato)):
            simbolo_actual = dato[x]
            self.estatus, transicion = self.buscar_trasicion(self.estado_siguiente, simbolo_actual)
            self.estado_siguiente = self.estados.index(transicion[2])
            self.estado_final = self.estados[self.estado_siguiente]   
            if (self.estatus == False):
                return False
            # estatus = [self.estados[self.estado_inicial], simbolo_actual] == self.funcion_transicion[0][0:2]
            print(self.funcion_transicion[0][0:2])
            print("simbolo ", simbolo_actual, "con estatus: " , self.estatus)
        if self.estado_final in self.estados_finales:
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
    materias, cal = programa.obtener_datos(link, matricula, password)
    materias.append("MATEMATICAS 2")
    cal.append(["10.0", "101", "0", "20..0"])
    materias_validas = []
    status = []
    cal_validas = []
    for x in cal:
        aux = []
        for y in x:
            res = programa.validar_dato(y)
            if (res):
                aux.append(y)
                print(y, "es", "calificación válida")
            else:
                aux.append(y)
                print(y, "es", "calificación invalida")
        cal_validas.append(aux)
    for i in materias:
        res = programa.validar_dato(i.upper())
        if (res):
            materias_validas.append(i.upper())
            status.append("válido")
            print(i.upper(), "es", "materia válida")
        else:
            materias_validas.append(i.upper())
            status.append("Inválido")
            print(i.upper(), "es", "materia invalida")
    return materias_validas, status, cal_validas


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
