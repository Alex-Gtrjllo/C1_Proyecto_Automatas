# from obtenerCalificaciones import *
import obtenerCalificaciones
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import sys
from Vista.ui_datos import Ui_datos
qtCreatorFile = "Vista/main.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class CustomTableWidgetItem(QtWidgets.QTableWidgetItem):
    def __init__ (self, value):
        super(CustomTableWidgetItem, self).__init__(str(value))

    def __lt__ (self, other):
        if (isinstance(other, CustomTableWidgetItem)):
            try:
                value  = float(self.data(QtCore.Qt.EditRole))
                other_value = float(other.data(QtCore.Qt.EditRole))
                return value < other_value
            except ValueError:
                pass
        return super().__lt__(other)


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
        datos_columnas, filas = main(self.link.text(), self.matricula.text(),
                          self.password.text())
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_datos()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        columnas = []
        for i in datos_columnas:
            columnas.append(i.upper())

        self.ui.table.setRowCount(len(filas))
        self.ui.table.setColumnCount(len(columnas))
        
        self.ui.table.setHorizontalHeaderLabels(columnas)
        # header_view = self.ui.table.horizontalHeader()
        # idx = header_view.count() - 1
        # header_view.setSectionResizeMode(
        #     idx, QtWidgets.QHeaderView.ResizeToContents)

        for fila, lista in enumerate(filas):
            for columna, elemento in enumerate(lista):
                if type(elemento)==str:
                    dato_fila = elemento.upper()
                    self.ui.table.setItem(fila, columna,
                                         CustomTableWidgetItem(dato_fila)
                                         )
                else:
                    self.ui.table.setItem(fila, columna,
                                            CustomTableWidgetItem(elemento)
                                            )
        header_view = self.ui.table.verticalHeader()
        # idx = header_view.count() - 1
        header_view.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # self.ui.table.setSortingEnabled(True)


class automata:

    def obtener_datos(self, link, matricula, password):
        webscrapping = obtenerCalificaciones.calificaciones(
            link, matricula, password)
        datos = webscrapping.obtener_datos()
        return datos

    def buscar_trasicion(self, estado, dato):
        for i in self.funcion_transicion:
            status = [self.estados[estado], dato] == i[0:2]
            if status == True:
                return status, i
        return status, i

    def validar_datos(self, datos):
        self.alfabeto_abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                                    'l', 'm', 'n',  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'á', 'é', 'í', 'ó', 'ú', 'ñ', ' ', '"', '<', '>', '/', '=', '-', '.', '\n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.estados = ['Q0', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19',
                        'Q20', 'Q21', 'Q22', 'Q23', 'Q24', 'Q25', 'Q26', 'Q27', 'Q28', 'Q29', 'Q30', 'Q31', 'Q32', 'Q33', 'Q34', 'Q35', 'Q36', 'Q37', 'Q38',
                        'Q39', 'Q40', 'Q41', 'Q42', 'Q43', 'Q44', 'Q45', 'Q46', 'Q47', 'Q48', 'Q49', 'Q50', 'Q51', 'Q52', 'Q53', 'Q54', 'Q55', 'Q56', 'Q57',
                        'Q58', 'Q59', 'Q60', 'Q61', 'Q62', 'Q63', 'Q64', 'Q65', 'Q66', 'Q67', 'Q68', 'Q69', 'Q70', 'Q71', 'Q72', 'Q73', 'Q74', 'Q75', 'Q76',
                        'Q77', 'Q78', 'Q79', 'Q80', 'Q81', 'Q82', 'Q83', 'Q84', 'Q85', 'Q86', 'Q87', 'Q88', 'Q89', 'Q90', 'Q91', 'Q92', 'Q93', 'Q94', 'Q95',
                        'Q96', 'Q97', 'Q98', 'Q99', 'Q100', 'Q101', 'Q102', 'Q103', 'Q104', 'Q105', 'Q106', 'Q107', 'Q108', 'Q109', 'Q110', 'Q111', 'Q112',
                        'Q113', 'Q114', 'Q115', 'Q116', 'Q117', 'Q118', 'Q119', 'Q120', 'Q121', 'Q122', 'Q123', 'Q124', 'Q125', 'Q126', 'Q127', 'Q128', 'Q129',
                        'Q130', 'Q131', 'Q132', 'Q133', 'Q134', 'Q135', 'Q136', 'Q137', 'Q138', 'Q139', 'Q140', 'Q141', 'Q142', 'Q143', 'Q144', 'Q145', 'Q146',
                        'Q147', 'Q148', 'Q149', 'Q150', 'Q151', 'Q152', 'Q153', 'Q154', 'Q155', 'Q156', 'Q157', 'Q158', 'Q159', 'Q160', 'Q161', 'Q162', 'Q163',
                        'Q164', 'Q165', 'Q166', 'Q167', 'Q168', 'Q169', 'Q170', 'Q171', 'Q172', 'Q173', 'Q174', 'Q175', 'Q176', 'Q177', 'Q178', 'Q179', 'Q180',
                        'Q181', 'Q182', 'Q183', 'Q184', 'Q185', 'Q186', 'Q187', 'Q188', 'Q189', 'Q190', 'Q191', 'Q192', 'Q193', 'Q194', 'Q195', 'Q196', 'Q197',
                        'Q198', 'Q199', 'Q200', 'Q201', 'Q202', 'Q203', 'Q204', 'Q205', 'Q206', 'Q207', 'Q208', 'Q209', 'Q210', 'Q211', 'Q212', 'Q213', 'Q214',
                        'Q215', 'Q216', 'Q217', 'Q218', 'Q219', 'Q220', 'Q221', 'Q222', 'Q223', 'Q224', 'Q225', 'Q226', 'Q227', 'Q228', 'Q229', 'Q230', 'Q231',
                        'Q232', 'Q233', 'Q234', 'Q235', 'Q236', 'Q237', 'Q238', 'Q239', 'Q240', 'Q241', 'Q242', 'Q243', 'Q244', 'Q245', 'Q246', 'Q247', 'Q248',
                        'Q249', 'Q250', 'Q251', 'Q252', 'Q253', 'Q254', 'Q255', 'Q256', 'Q257', 'Q258', 'Q259', 'Q260', 'Q261', 'Q262', 'Q263', 'Q264', 'Q265',
                        'Q266', 'Q267', 'Q268', 'Q269', 'Q270', 'Q271', 'Q272', 'Q273', 'Q274', 'Q275', 'Q276', 'Q277', 'Q278', 'Q279', 'Q280', 'Q281', 'Q282',
                        'Q283', 'Q284', 'Q285', 'Q286', 'Q287', 'Q288', 'Q289', 'Q290', 'Q291', 'Q292', 'Q293', 'Q294', 'Q295', 'Q296', 'Q297', 'Q298', 'Q299', 
                        'Q300', 'Q301', 'Q302', 'Q303', 'Q304', 'Q305', 'Q306', 'Q307', 'Q308', 'Q309', 'Q310', 'Q311', 'Q312', 'Q313', 'Q314', 'Q315', 'Q316',
                        'Q317', 'Q318', 'Q319', 'Q320', 'Q321', 'Q322', 'Q323', 'Q324', 'Q325', 'Q326', 'Q327', 'Q328', 'Q329', 'Q330', 'Q331', 'Q332', 'Q333',
                        'Q334', 'Q335', 'Q336', 'Q337', 'Q338', 'Q339', 'Q340', 'Q341', 'Q342', 'Q343', 'Q344', 'Q345', 'Q346', 'Q347', 'Q348', 'Q349', 'Q350',
                        'Q351', 'Q352', 'Q353', 'Q354', 'Q355', 'Q356', 'Q357', 'Q358', 'Q359', 'Q360', 'Q361', 'Q362', 'Q363', 'Q364', 'Q365', 'Q366', 'Q367',
                        'Q368', 'Q369', 'Q370', 'Q371', 'Q372', 'Q373', 'Q374', 'Q375', 'Q376', 'Q377', 'Q378', 'Q379', 'Q380', 'Q381', 'Q382', 'Q383', 'Q384',
                        'Q385', 'Q386', 'Q387', 'Q388', 'Q389', 'Q390', 'Q391', 'Q392', 'Q393', 'Q394', 'Q395', 'Q396', 'Q397', 'Q398', 'Q399', 'Q400', 'Q401',
                        'Q402', 'Q403', 'Q404', 'Q405', 'Q406', 'Q407', 'Q408', 'Q409', 'Q410', 'Q411', 'Q412', 'Q413', 'Q414', 'Q415', 'Q416', 'Q417', 'Q418',
                        'Q419', 'Q420', 'Q421', 'Q422', 'Q423', 'Q424', 'Q425', 'Q426', 'Q427', 'Q428', 'Q429', 'Q430', 'Q431', 'Q432', 'Q433', 'Q434', 'Q435',
                        'Q436', 'Q437', 'Q438', 'Q439', 'Q440', 'Q441', 'Q442', 'Q443', 'Q444', 'Q445', 'Q446', 'Q447', 'Q448', 'Q449', 'Q450', 'Q451', 'Q452',
                        'Q453', 'Q454', 'Q455', 'Q456', 'Q457', 'Q458', 'Q459', 'Q460', 'Q461', 'Q462', 'Q463', 'Q464', 'Q465', 'Q466', 'Q467', 'Q468', 'Q469',
                        'Q470', 'Q471', 'Q472', 'Q473', 'Q474', 'Q475', 'Q476', 'Q477', 'Q478', 'Q479', 'Q480', 'Q481', 'Q482', 'Q483', 'Q484', 'Q485', 'Q486',
                        'Q487', 'Q488', 'Q489', 'Q490']

        self.funcion_transicion = [
            [self.estados[0], self.alfabeto_abecedario[34], self.estados[1]], [self.estados[1], self.alfabeto_abecedario[19], self.estados[2]], 
            [self.estados[2], self.alfabeto_abecedario[0], self.estados[3]], [self.estados[3], self.alfabeto_abecedario[1], self.estados[4]], 
            [self.estados[4], self.alfabeto_abecedario[11], self.estados[5]], [self.estados[5], self.alfabeto_abecedario[4], self.estados[6]], 
            [self.estados[6], self.alfabeto_abecedario[32], self.estados[7]], [self.estados[7], self.alfabeto_abecedario[1], self.estados[8]], 
            [self.estados[8], self.alfabeto_abecedario[14], self.estados[9]], [self.estados[9], self.alfabeto_abecedario[17], self.estados[10]], 
            [self.estados[10], self.alfabeto_abecedario[3], self.estados[11]], [self.estados[11], self.alfabeto_abecedario[4], self.estados[12]], 
            [self.estados[12], self.alfabeto_abecedario[17], self.estados[13]], [self.estados[13], self.alfabeto_abecedario[37], self.estados[14]], 
            [self.estados[14], self.alfabeto_abecedario[33], self.estados[15]], [self.estados[15], self.alfabeto_abecedario[41], self.estados[16]], 
            [self.estados[16], self.alfabeto_abecedario[33], self.estados[17]], [self.estados[17], self.alfabeto_abecedario[32], self.estados[18]], 
            [self.estados[18], self.alfabeto_abecedario[2], self.estados[19]], [self.estados[19], self.alfabeto_abecedario[4], self.estados[20]], 
            [self.estados[20], self.alfabeto_abecedario[11], self.estados[21]], [self.estados[21], self.alfabeto_abecedario[11], self.estados[22]], 
            [self.estados[22], self.alfabeto_abecedario[15], self.estados[23]], [self.estados[23], self.alfabeto_abecedario[0], self.estados[24]],
            [self.estados[24], self.alfabeto_abecedario[3], self.estados[25]], [self.estados[25], self.alfabeto_abecedario[3], self.estados[26]],
            [self.estados[26], self.alfabeto_abecedario[8], self.estados[27]], [self.estados[27], self.alfabeto_abecedario[13], self.estados[28]],
            [self.estados[28], self.alfabeto_abecedario[6], self.estados[29]], [self.estados[29], self.alfabeto_abecedario[37], self.estados[30]],
            [self.estados[30], self.alfabeto_abecedario[33], self.estados[31]], [self.estados[31], self.alfabeto_abecedario[41], self.estados[32]],
            [self.estados[32], self.alfabeto_abecedario[33], self.estados[33]], [self.estados[33], self.alfabeto_abecedario[32], self.estados[34]],
            [self.estados[34], self.alfabeto_abecedario[2], self.estados[35]], [self.estados[35], self.alfabeto_abecedario[4], self.estados[36]],
            [self.estados[36], self.alfabeto_abecedario[11], self.estados[37]], [self.estados[37], self.alfabeto_abecedario[11], self.estados[38]],
            [self.estados[38], self.alfabeto_abecedario[18], self.estados[39]], [self.estados[39], self.alfabeto_abecedario[15], self.estados[40]],
            [self.estados[40], self.alfabeto_abecedario[0], self.estados[41]], [self.estados[41], self.alfabeto_abecedario[2], self.estados[42]],
            [self.estados[42], self.alfabeto_abecedario[8], self.estados[43]], [self.estados[43], self.alfabeto_abecedario[13], self.estados[44]],
            [self.estados[44], self.alfabeto_abecedario[6], self.estados[45]], [self.estados[45], self.alfabeto_abecedario[37], self.estados[46]],
            [self.estados[46], self.alfabeto_abecedario[33], self.estados[47]], [self.estados[47], self.alfabeto_abecedario[41], self.estados[48]],
            [self.estados[48], self.alfabeto_abecedario[33], self.estados[49]], [self.estados[49], self.alfabeto_abecedario[32], self.estados[50]],
            [self.estados[50], self.alfabeto_abecedario[2], self.estados[51]], [self.estados[51], self.alfabeto_abecedario[11], self.estados[52]],
            [self.estados[52], self.alfabeto_abecedario[0], self.estados[53]], [self.estados[53], self.alfabeto_abecedario[18], self.estados[54]],
            [self.estados[54], self.alfabeto_abecedario[18], self.estados[55]], [self.estados[55], self.alfabeto_abecedario[37], self.estados[56]],
            [self.estados[56], self.alfabeto_abecedario[33], self.estados[57]], [self.estados[57], self.alfabeto_abecedario[2], self.estados[58]],
            [self.estados[58], self.alfabeto_abecedario[0], self.estados[59]], [self.estados[59], self.alfabeto_abecedario[11], self.estados[60]],
            [self.estados[60], self.alfabeto_abecedario[8], self.estados[61]], [self.estados[61], self.alfabeto_abecedario[5], self.estados[62]],
            [self.estados[62], self.alfabeto_abecedario[19], self.estados[63]], [self.estados[63], self.alfabeto_abecedario[0], self.estados[64]],
            [self.estados[64], self.alfabeto_abecedario[1], self.estados[65]], [self.estados[65], self.alfabeto_abecedario[11], self.estados[66]],
            [self.estados[66], self.alfabeto_abecedario[4], self.estados[67]], [self.estados[67], self.alfabeto_abecedario[33], self.estados[68]],
            [self.estados[68], self.alfabeto_abecedario[35], self.estados[69]], [self.estados[69], self.alfabeto_abecedario[40], self.estados[70]],
            [self.estados[70], self.alfabeto_abecedario[32], self.estados[71]], [self.estados[71], self.alfabeto_abecedario[32], self.estados[72]],
            [self.estados[72], self.alfabeto_abecedario[32], self.estados[73]], [self.estados[73], self.alfabeto_abecedario[32], self.estados[74]],
            [self.estados[74], self.alfabeto_abecedario[32], self.estados[75]], [self.estados[75], self.alfabeto_abecedario[34], self.estados[76]],
            [self.estados[76], self.alfabeto_abecedario[19], self.estados[77]], [self.estados[77], self.alfabeto_abecedario[17], self.estados[78]],
            [self.estados[78], self.alfabeto_abecedario[35], self.estados[79]], [self.estados[79], self.alfabeto_abecedario[40], self.estados[80]],
            [self.estados[80], self.alfabeto_abecedario[32], self.estados[81]], [self.estados[81], self.alfabeto_abecedario[32], self.estados[82]],
            [self.estados[82], self.alfabeto_abecedario[32], self.estados[83]], [self.estados[83], self.alfabeto_abecedario[32], self.estados[84]],
            [self.estados[84], self.alfabeto_abecedario[32], self.estados[85]], [self.estados[85], self.alfabeto_abecedario[32], self.estados[86]],
            [self.estados[86], self.alfabeto_abecedario[34], self.estados[87]], [self.estados[87], self.alfabeto_abecedario[19], self.estados[88]],
            [self.estados[88], self.alfabeto_abecedario[7], self.estados[89]], [self.estados[89], self.alfabeto_abecedario[32], self.estados[90]],
            [self.estados[90], self.alfabeto_abecedario[2], self.estados[91]], [self.estados[91], self.alfabeto_abecedario[14], self.estados[92]],
            [self.estados[92], self.alfabeto_abecedario[11], self.estados[93]], [self.estados[93], self.alfabeto_abecedario[18], self.estados[94]],
            [self.estados[94], self.alfabeto_abecedario[15], self.estados[95]], [self.estados[95], self.alfabeto_abecedario[0], self.estados[96]],
            [self.estados[96], self.alfabeto_abecedario[13], self.estados[97]], [self.estados[97], self.alfabeto_abecedario[37], self.estados[98]],
            [self.estados[98], self.alfabeto_abecedario[33], self.estados[99]], [self.estados[99], self.alfabeto_abecedario[42], self.estados[100]],
            [self.estados[100], self.alfabeto_abecedario[42], self.estados[101]], [self.estados[101], self.alfabeto_abecedario[33], self.estados[102]],
            [self.estados[102], self.alfabeto_abecedario[35], self.estados[103]], [self.estados[103], self.alfabeto_abecedario[40], self.estados[104]],
            [self.estados[104], self.alfabeto_abecedario[32], self.estados[105]], [self.estados[105], self.alfabeto_abecedario[32], self.estados[106]],
            [self.estados[106], self.alfabeto_abecedario[32], self.estados[107]], [self.estados[107], self.alfabeto_abecedario[32], self.estados[108]],
            [self.estados[108], self.alfabeto_abecedario[32], self.estados[109]], [self.estados[109], self.alfabeto_abecedario[32], self.estados[110]],
            [self.estados[110], self.alfabeto_abecedario[32], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[38], self.estados[112]],
            [self.estados[112], self.alfabeto_abecedario[32], self.estados[113]], [self.estados[113], self.alfabeto_abecedario[40], self.estados[114]],
            [self.estados[114], self.alfabeto_abecedario[32], self.estados[115]], [self.estados[115], self.alfabeto_abecedario[32], self.estados[116]],
            [self.estados[116], self.alfabeto_abecedario[32], self.estados[117]], [self.estados[117], self.alfabeto_abecedario[32], self.estados[118]],
            [self.estados[118], self.alfabeto_abecedario[32], self.estados[119]], [self.estados[119], self.alfabeto_abecedario[32], self.estados[120]],
            [self.estados[120], self.alfabeto_abecedario[34], self.estados[121]], [self.estados[121], self.alfabeto_abecedario[36], self.estados[122]],
            [self.estados[122], self.alfabeto_abecedario[19], self.estados[123]], [self.estados[123], self.alfabeto_abecedario[7], self.estados[124]],
            [self.estados[124], self.alfabeto_abecedario[35], self.estados[125]], [self.estados[125], self.alfabeto_abecedario[40], self.estados[126]],
            [self.estados[126], self.alfabeto_abecedario[32], self.estados[127]], [self.estados[127], self.alfabeto_abecedario[32], self.estados[128]],
            [self.estados[128], self.alfabeto_abecedario[32], self.estados[129]], [self.estados[129], self.alfabeto_abecedario[32], self.estados[130]],
            [self.estados[130], self.alfabeto_abecedario[32], self.estados[131]], [self.estados[131], self.alfabeto_abecedario[34], self.estados[132]],
            [self.estados[132], self.alfabeto_abecedario[36], self.estados[133]], [self.estados[133], self.alfabeto_abecedario[19], self.estados[134]],
            [self.estados[134], self.alfabeto_abecedario[17], self.estados[135]], [self.estados[135], self.alfabeto_abecedario[35], self.estados[136]],
            [self.estados[136], self.alfabeto_abecedario[40], self.estados[137]], [self.estados[137], self.alfabeto_abecedario[32], self.estados[138]],
            [self.estados[138], self.alfabeto_abecedario[32], self.estados[139]], [self.estados[139], self.alfabeto_abecedario[32], self.estados[140]],
            [self.estados[140], self.alfabeto_abecedario[32], self.estados[141]], [self.estados[141], self.alfabeto_abecedario[32], self.estados[142]],
            [self.estados[142], self.alfabeto_abecedario[34], self.estados[143]], [self.estados[143], self.alfabeto_abecedario[19], self.estados[144]],
            [self.estados[144], self.alfabeto_abecedario[17], self.estados[145]], [self.estados[145], self.alfabeto_abecedario[35], self.estados[146]],
            [self.estados[146], self.alfabeto_abecedario[40], self.estados[147]], [self.estados[147], self.alfabeto_abecedario[32], self.estados[148]],
            [self.estados[148], self.alfabeto_abecedario[32], self.estados[149]], [self.estados[149], self.alfabeto_abecedario[32], self.estados[150]],
            [self.estados[150], self.alfabeto_abecedario[32], self.estados[151]], [self.estados[151], self.alfabeto_abecedario[32], self.estados[152]],
            [self.estados[152], self.alfabeto_abecedario[32], self.estados[153]], [self.estados[153], self.alfabeto_abecedario[34], self.estados[154]],
            [self.estados[154], self.alfabeto_abecedario[19], self.estados[155]], [self.estados[155], self.alfabeto_abecedario[7], self.estados[156]],
            [self.estados[156], self.alfabeto_abecedario[35], self.estados[157]], [self.estados[157], self.alfabeto_abecedario[40], self.estados[158]],
            [self.estados[158], self.alfabeto_abecedario[32], self.estados[159]], [self.estados[159], self.alfabeto_abecedario[32], self.estados[160]],
            [self.estados[160], self.alfabeto_abecedario[32], self.estados[161]], [self.estados[161], self.alfabeto_abecedario[32], self.estados[162]],
            [self.estados[162], self.alfabeto_abecedario[32], self.estados[163]], [self.estados[163], self.alfabeto_abecedario[32], self.estados[164]],
            [self.estados[164], self.alfabeto_abecedario[34], self.estados[165]], [self.estados[165], self.alfabeto_abecedario[36], self.estados[166]],
            [self.estados[166], self.alfabeto_abecedario[19], self.estados[167]], [self.estados[167], self.alfabeto_abecedario[7], self.estados[168]],
            [self.estados[168], self.alfabeto_abecedario[35], self.estados[169]], [self.estados[169], self.alfabeto_abecedario[40], self.estados[170]],
            [self.estados[170], self.alfabeto_abecedario[32], self.estados[171]], [self.estados[171], self.alfabeto_abecedario[32], self.estados[172]],
            [self.estados[172], self.alfabeto_abecedario[32], self.estados[173]], [self.estados[173], self.alfabeto_abecedario[32], self.estados[174]],
            [self.estados[174], self.alfabeto_abecedario[32], self.estados[175]], [self.estados[175], self.alfabeto_abecedario[32], self.estados[176]],
            [self.estados[176], self.alfabeto_abecedario[34], self.estados[177]], [self.estados[177], self.alfabeto_abecedario[19], self.estados[178]],
            [self.estados[178], self.alfabeto_abecedario[7], self.estados[179]], [self.estados[179], self.alfabeto_abecedario[35], self.estados[180]],
            [self.estados[180], self.alfabeto_abecedario[40], self.estados[181]], [self.estados[181], self.alfabeto_abecedario[32], self.estados[182]],
            [self.estados[182], self.alfabeto_abecedario[32], self.estados[183]], [self.estados[183], self.alfabeto_abecedario[32], self.estados[184]],
            [self.estados[184], self.alfabeto_abecedario[32], self.estados[185]], [self.estados[185], self.alfabeto_abecedario[32], self.estados[186]],
            [self.estados[186], self.alfabeto_abecedario[32], self.estados[187]], [self.estados[187], self.alfabeto_abecedario[32], self.estados[188]],
            [self.estados[188], self.alfabeto_abecedario[32], self.estados[189]], [self.estados[189], self.alfabeto_abecedario[42], self.estados[190]],
            [self.estados[190], self.alfabeto_abecedario[40], self.estados[191]], [self.estados[188], self.alfabeto_abecedario[40], self.estados[191]],
            [self.estados[191], self.alfabeto_abecedario[32], self.estados[192]], [self.estados[192], self.alfabeto_abecedario[32], self.estados[193]],
            [self.estados[193], self.alfabeto_abecedario[32], self.estados[194]], [self.estados[194], self.alfabeto_abecedario[32], self.estados[195]],
            [self.estados[195], self.alfabeto_abecedario[32], self.estados[196]], [self.estados[196], self.alfabeto_abecedario[32], self.estados[197]],
            [self.estados[197], self.alfabeto_abecedario[34], self.estados[198]], [self.estados[198], self.alfabeto_abecedario[36], self.estados[199]],
            [self.estados[199], self.alfabeto_abecedario[19], self.estados[200]], [self.estados[200], self.alfabeto_abecedario[7], self.estados[201]],
            [self.estados[201], self.alfabeto_abecedario[35], self.estados[202]], [self.estados[202], self.alfabeto_abecedario[40], self.estados[170]],
            [self.estados[175], self.alfabeto_abecedario[34], self.estados[203]], [self.estados[203], self.alfabeto_abecedario[36], self.estados[204]],
            [self.estados[204], self.alfabeto_abecedario[19], self.estados[205]], [self.estados[205], self.alfabeto_abecedario[17], self.estados[206]],
            [self.estados[206], self.alfabeto_abecedario[35], self.estados[69]], [self.estados[207], self.alfabeto_abecedario[32], self.estados[208]],
            [self.estados[88], self.alfabeto_abecedario[3], self.estados[235]], [self.estados[207], self.alfabeto_abecedario[32], self.estados[28]],
            [self.estados[208], self.alfabeto_abecedario[2], self.estados[209]], [self.estados[209], self.alfabeto_abecedario[11], self.estados[210]],
            [self.estados[210], self.alfabeto_abecedario[0], self.estados[211]], [self.estados[211], self.alfabeto_abecedario[18], self.estados[212]],
            [self.estados[212], self.alfabeto_abecedario[18], self.estados[213]], [self.estados[213], self.alfabeto_abecedario[37], self.estados[214]],
            [self.estados[214], self.alfabeto_abecedario[33], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[33], self.estados[224]],
            [self.estados[224], self.alfabeto_abecedario[35], self.estados[225]], [self.estados[225], self.alfabeto_abecedario[40], self.estados[226]],
            [self.estados[226], self.alfabeto_abecedario[32], self.estados[227]], [self.estados[227], self.alfabeto_abecedario[32], self.estados[228]],
            [self.estados[228], self.alfabeto_abecedario[32], self.estados[229]], [self.estados[229], self.alfabeto_abecedario[32], self.estados[230]],
            [self.estados[230], self.alfabeto_abecedario[32], self.estados[231]], [self.estados[231], self.alfabeto_abecedario[32], self.estados[232]],
            [self.estados[232], self.alfabeto_abecedario[34], self.estados[233]], [self.estados[233], self.alfabeto_abecedario[19], self.estados[234]],
            [self.estados[234], self.alfabeto_abecedario[3], self.estados[235]], [self.estados[235], self.alfabeto_abecedario[32], self.estados[236]],
            [self.estados[236], self.alfabeto_abecedario[22], self.estados[237]], [self.estados[237], self.alfabeto_abecedario[8], self.estados[238]],
            [self.estados[238], self.alfabeto_abecedario[3], self.estados[239]], [self.estados[239], self.alfabeto_abecedario[19], self.estados[240]],
            [self.estados[240], self.alfabeto_abecedario[7], self.estados[241]], [self.estados[241], self.alfabeto_abecedario[37], self.estados[242]],
            [self.estados[242], self.alfabeto_abecedario[33], self.estados[243]], [self.estados[243], self.alfabeto_abecedario[42], self.estados[244]],
            [self.estados[244], self.alfabeto_abecedario[33], self.estados[245]], [self.estados[245], self.alfabeto_abecedario[35], self.estados[246]],
            [self.estados[246], self.alfabeto_abecedario[40], self.estados[247]], [self.estados[247], self.alfabeto_abecedario[32], self.estados[248]],
            [self.estados[248], self.alfabeto_abecedario[32], self.estados[249]], [self.estados[249], self.alfabeto_abecedario[32], self.estados[250]],
            [self.estados[250], self.alfabeto_abecedario[32], self.estados[251]], [self.estados[251], self.alfabeto_abecedario[32], self.estados[252]],
            [self.estados[252], self.alfabeto_abecedario[32], self.estados[253]], [self.estados[253], self.alfabeto_abecedario[32], self.estados[254]],
            [self.estados[254], self.alfabeto_abecedario[34], self.estados[255]], [self.estados[255], self.alfabeto_abecedario[18], self.estados[256]],
            [self.estados[256], self.alfabeto_abecedario[15], self.estados[257]], [self.estados[257], self.alfabeto_abecedario[0], self.estados[258]],
            [self.estados[258], self.alfabeto_abecedario[13], self.estados[259]], [self.estados[259], self.alfabeto_abecedario[32], self.estados[260]],
            [self.estados[260], self.alfabeto_abecedario[2], self.estados[261]], [self.estados[261], self.alfabeto_abecedario[11], self.estados[262]],
            [self.estados[262], self.alfabeto_abecedario[0], self.estados[263]], [self.estados[263], self.alfabeto_abecedario[18], self.estados[264]],
            [self.estados[264], self.alfabeto_abecedario[18], self.estados[265]], [self.estados[265], self.alfabeto_abecedario[37], self.estados[266]],
            [self.estados[266], self.alfabeto_abecedario[33], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[32], self.estados[268]],
            [self.estados[268], self.alfabeto_abecedario[38], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[33], self.estados[270]],
            [self.estados[270], self.alfabeto_abecedario[35], self.estados[271]], [self.estados[271], self.alfabeto_abecedario[40], self.estados[272]],
            [self.estados[272], self.alfabeto_abecedario[32], self.estados[273]], [self.estados[273], self.alfabeto_abecedario[32], self.estados[274]],
            [self.estados[274], self.alfabeto_abecedario[32], self.estados[275]], [self.estados[275], self.alfabeto_abecedario[32], self.estados[276]],
            [self.estados[276], self.alfabeto_abecedario[32], self.estados[277]], [self.estados[277], self.alfabeto_abecedario[32], self.estados[278]],
            [self.estados[278], self.alfabeto_abecedario[32], self.estados[279]], [self.estados[279], self.alfabeto_abecedario[34], self.estados[280]],
            [self.estados[280], self.alfabeto_abecedario[36], self.estados[281]], [self.estados[281], self.alfabeto_abecedario[18], self.estados[282]],
            [self.estados[282], self.alfabeto_abecedario[15], self.estados[283]], [self.estados[283], self.alfabeto_abecedario[0], self.estados[284]],
            [self.estados[284], self.alfabeto_abecedario[13], self.estados[285]], [self.estados[285], self.alfabeto_abecedario[35], self.estados[286]],
            [self.estados[286], self.alfabeto_abecedario[40], self.estados[287]], [self.estados[287], self.alfabeto_abecedario[32], self.estados[288]],
            [self.estados[288], self.alfabeto_abecedario[32], self.estados[289]], [self.estados[289], self.alfabeto_abecedario[32], self.estados[290]],
            [self.estados[290], self.alfabeto_abecedario[32], self.estados[291]], [self.estados[291], self.alfabeto_abecedario[32], self.estados[292]],
            [self.estados[292], self.alfabeto_abecedario[32], self.estados[293]], [self.estados[293], self.alfabeto_abecedario[34], self.estados[294]],
            [self.estados[294], self.alfabeto_abecedario[36], self.estados[295]], [self.estados[295], self.alfabeto_abecedario[19], self.estados[296]],
            [self.estados[296], self.alfabeto_abecedario[3], self.estados[297]], [self.estados[297], self.alfabeto_abecedario[35], self.estados[298]], [self.estados[298], self.alfabeto_abecedario[40], self.estados[490]],
            [self.estados[490], self.alfabeto_abecedario[32], self.estados[299]], [self.estados[299], self.alfabeto_abecedario[32], self.estados[300]],
            [self.estados[300], self.alfabeto_abecedario[32], self.estados[301]], [self.estados[301], self.alfabeto_abecedario[32], self.estados[302]],
            [self.estados[302], self.alfabeto_abecedario[32], self.estados[303]], [self.estados[303], self.alfabeto_abecedario[32], self.estados[304]],
            [self.estados[304], self.alfabeto_abecedario[34], self.estados[305]], [self.estados[305], self.alfabeto_abecedario[19], self.estados[306]],
            [self.estados[306], self.alfabeto_abecedario[3], self.estados[307]], [self.estados[307], self.alfabeto_abecedario[32], self.estados[308]],
            [self.estados[308], self.alfabeto_abecedario[13], self.estados[309]], [self.estados[309], self.alfabeto_abecedario[14], self.estados[310]],
            [self.estados[310], self.alfabeto_abecedario[22], self.estados[311]], [self.estados[311], self.alfabeto_abecedario[17], self.estados[312]],
            [self.estados[312], self.alfabeto_abecedario[0], self.estados[313]], [self.estados[313], self.alfabeto_abecedario[15], self.estados[314]],
            [self.estados[314], self.alfabeto_abecedario[37], self.estados[315]], [self.estados[315], self.alfabeto_abecedario[33], self.estados[316]],
            [self.estados[316], self.alfabeto_abecedario[13], self.estados[317]], [self.estados[317], self.alfabeto_abecedario[14], self.estados[318]],
            [self.estados[318], self.alfabeto_abecedario[22], self.estados[319]], [self.estados[319], self.alfabeto_abecedario[17], self.estados[320]],
            [self.estados[320], self.alfabeto_abecedario[0], self.estados[321]], [self.estados[321], self.alfabeto_abecedario[15], self.estados[322]],
            [self.estados[322], self.alfabeto_abecedario[33], self.estados[323]], [self.estados[323], self.alfabeto_abecedario[32], self.estados[324]],
            [self.estados[324], self.alfabeto_abecedario[22], self.estados[325]], [self.estados[325], self.alfabeto_abecedario[8], self.estados[326]],
            [self.estados[326], self.alfabeto_abecedario[3], self.estados[327]], [self.estados[327], self.alfabeto_abecedario[19], self.estados[328]],
            [self.estados[328], self.alfabeto_abecedario[7], self.estados[329]], [self.estados[329], self.alfabeto_abecedario[37], self.estados[330]],
            [self.estados[330], self.alfabeto_abecedario[33], self.estados[331]], [self.estados[331], self.alfabeto_abecedario[42], self.estados[332]],
            [self.estados[332], self.alfabeto_abecedario[33], self.estados[333]], [self.estados[333], self.alfabeto_abecedario[35], self.estados[334]],
            [self.estados[334], self.alfabeto_abecedario[40], self.estados[335]], [self.estados[335], self.alfabeto_abecedario[32], self.estados[336]],
            [self.estados[336], self.alfabeto_abecedario[32], self.estados[337]], [self.estados[337], self.alfabeto_abecedario[32], self.estados[338]],
            [self.estados[338], self.alfabeto_abecedario[32], self.estados[339]], [self.estados[339], self.alfabeto_abecedario[32], self.estados[340]],
            [self.estados[340], self.alfabeto_abecedario[32], self.estados[341]], [self.estados[341], self.alfabeto_abecedario[32], self.estados[342]],
            [self.estados[342], self.alfabeto_abecedario[40], self.estados[344]], [self.estados[344], self.alfabeto_abecedario[32], self.estados[345]],
            [self.estados[345], self.alfabeto_abecedario[32], self.estados[346]], [self.estados[346], self.alfabeto_abecedario[32], self.estados[347]],
            [self.estados[347], self.alfabeto_abecedario[32], self.estados[348]], [self.estados[348], self.alfabeto_abecedario[32], self.estados[349]],
            [self.estados[349], self.alfabeto_abecedario[32], self.estados[350]], [self.estados[350], self.alfabeto_abecedario[34], self.estados[351]],
            [self.estados[351], self.alfabeto_abecedario[36], self.estados[352]], [self.estados[352], self.alfabeto_abecedario[19], self.estados[353]],
            [self.estados[353], self.alfabeto_abecedario[3], self.estados[354]], [self.estados[354], self.alfabeto_abecedario[35], self.estados[355]],
            [self.estados[355], self.alfabeto_abecedario[40], self.estados[356]], [self.estados[356], self.alfabeto_abecedario[32], self.estados[357]],
            [self.estados[357], self.alfabeto_abecedario[32], self.estados[358]], [self.estados[358], self.alfabeto_abecedario[32], self.estados[359]],
            [self.estados[359], self.alfabeto_abecedario[32], self.estados[360]], [self.estados[360], self.alfabeto_abecedario[32], self.estados[361]],
            [self.estados[406], self.alfabeto_abecedario[34], self.estados[362]], [self.estados[362], self.alfabeto_abecedario[36], self.estados[363]],
            [self.estados[363], self.alfabeto_abecedario[19], self.estados[364]], [self.estados[364], self.alfabeto_abecedario[17], self.estados[365]],
            [self.estados[365], self.alfabeto_abecedario[35], self.estados[69]], [self.estados[361], self.alfabeto_abecedario[32], self.estados[366]],
            [self.estados[366], self.alfabeto_abecedario[34], self.estados[367]], [self.estados[367], self.alfabeto_abecedario[19], self.estados[368]],
            [self.estados[368], self.alfabeto_abecedario[3], self.estados[369]], [self.estados[369], self.alfabeto_abecedario[32], self.estados[370]],
            [self.estados[370], self.alfabeto_abecedario[22], self.estados[371]], [self.estados[371], self.alfabeto_abecedario[8], self.estados[372]],
            [self.estados[372], self.alfabeto_abecedario[3], self.estados[373]], [self.estados[373], self.alfabeto_abecedario[19], self.estados[374]],
            [self.estados[374], self.alfabeto_abecedario[7], self.estados[375]], [self.estados[375], self.alfabeto_abecedario[37], self.estados[376]],
            [self.estados[376], self.alfabeto_abecedario[33], self.estados[377]], [self.estados[377], self.alfabeto_abecedario[42], self.estados[378]],
            [self.estados[378], self.alfabeto_abecedario[33], self.estados[379]], [self.estados[379], self.alfabeto_abecedario[35], self.estados[380]],
            [self.estados[380], self.alfabeto_abecedario[40], self.estados[381]], [self.estados[381], self.alfabeto_abecedario[32], self.estados[382]],
            [self.estados[382], self.alfabeto_abecedario[32], self.estados[383]], [self.estados[383], self.alfabeto_abecedario[32], self.estados[384]],
            [self.estados[384], self.alfabeto_abecedario[32], self.estados[385]], [self.estados[385], self.alfabeto_abecedario[32], self.estados[386]],
            [self.estados[386], self.alfabeto_abecedario[32], self.estados[387]], [self.estados[387], self.alfabeto_abecedario[32], self.estados[388]],
            [self.estados[388], self.alfabeto_abecedario[40], self.estados[389]], [self.estados[389], self.alfabeto_abecedario[32], self.estados[390]],
            [self.estados[390], self.alfabeto_abecedario[32], self.estados[391]], [self.estados[391], self.alfabeto_abecedario[32], self.estados[392]],
            [self.estados[392], self.alfabeto_abecedario[32], self.estados[393]], [self.estados[393], self.alfabeto_abecedario[32], self.estados[394]],
            [self.estados[394], self.alfabeto_abecedario[32], self.estados[395]], [self.estados[395], self.alfabeto_abecedario[34], self.estados[396]],
            [self.estados[396], self.alfabeto_abecedario[36], self.estados[397]], [self.estados[397], self.alfabeto_abecedario[19], self.estados[398]],
            [self.estados[398], self.alfabeto_abecedario[3], self.estados[399]], [self.estados[399], self.alfabeto_abecedario[35], self.estados[400]],
            [self.estados[400], self.alfabeto_abecedario[40], self.estados[401]], [self.estados[401], self.alfabeto_abecedario[32], self.estados[402]],
            [self.estados[402], self.alfabeto_abecedario[32], self.estados[403]], [self.estados[403], self.alfabeto_abecedario[32], self.estados[404]],
            [self.estados[404], self.alfabeto_abecedario[32], self.estados[405]], [self.estados[405], self.alfabeto_abecedario[32], self.estados[406]],
            [self.estados[406], self.alfabeto_abecedario[32], self.estados[407]], [self.estados[407], self.alfabeto_abecedario[34], self.estados[408]],
            [self.estados[408], self.alfabeto_abecedario[19], self.estados[409]], [self.estados[409], self.alfabeto_abecedario[3], self.estados[410]],
            [self.estados[410], self.alfabeto_abecedario[32], self.estados[411]], [self.estados[411], self.alfabeto_abecedario[22], self.estados[412]],
            [self.estados[412], self.alfabeto_abecedario[8], self.estados[413]], [self.estados[413], self.alfabeto_abecedario[3], self.estados[414]],
            [self.estados[414], self.alfabeto_abecedario[19], self.estados[415]], [self.estados[415], self.alfabeto_abecedario[7], self.estados[416]],
            [self.estados[416], self.alfabeto_abecedario[37], self.estados[417]], [self.estados[417], self.alfabeto_abecedario[33], self.estados[418]],
            [self.estados[418], self.alfabeto_abecedario[42], self.estados[419]], [self.estados[419], self.alfabeto_abecedario[33], self.estados[420]],
            [self.estados[420], self.alfabeto_abecedario[35], self.estados[421]], [self.estados[421], self.alfabeto_abecedario[40], self.estados[422]],
            [self.estados[422], self.alfabeto_abecedario[32], self.estados[423]], [self.estados[423], self.alfabeto_abecedario[32], self.estados[424]],
            [self.estados[424], self.alfabeto_abecedario[32], self.estados[425]], [self.estados[425], self.alfabeto_abecedario[32], self.estados[426]],
            [self.estados[426], self.alfabeto_abecedario[32], self.estados[427]], [self.estados[427], self.alfabeto_abecedario[32], self.estados[428]],
            [self.estados[428], self.alfabeto_abecedario[32], self.estados[429]], [self.estados[429], self.alfabeto_abecedario[34], self.estados[430]],
            [self.estados[430], self.alfabeto_abecedario[18], self.estados[431]], [self.estados[431], self.alfabeto_abecedario[15], self.estados[432]],
            [self.estados[432], self.alfabeto_abecedario[0], self.estados[433]], [self.estados[433], self.alfabeto_abecedario[13], self.estados[434]],
            [self.estados[434], self.alfabeto_abecedario[32], self.estados[435]], [self.estados[435], self.alfabeto_abecedario[2], self.estados[436]],
            [self.estados[436], self.alfabeto_abecedario[11], self.estados[437]], [self.estados[437], self.alfabeto_abecedario[0], self.estados[438]],
            [self.estados[438], self.alfabeto_abecedario[18], self.estados[439]], [self.estados[439], self.alfabeto_abecedario[18], self.estados[440]],
            [self.estados[440], self.alfabeto_abecedario[37], self.estados[441]], [self.estados[441], self.alfabeto_abecedario[33], self.estados[442]],
            [self.estados[442], self.alfabeto_abecedario[33], self.estados[443]], [self.estados[443], self.alfabeto_abecedario[35], self.estados[444]],
            [self.estados[444], self.alfabeto_abecedario[40], self.estados[445]], [self.estados[445], self.alfabeto_abecedario[32], self.estados[446]],
            [self.estados[446], self.alfabeto_abecedario[32], self.estados[447]], [self.estados[447], self.alfabeto_abecedario[32], self.estados[448]],
            [self.estados[448], self.alfabeto_abecedario[32], self.estados[449]], [self.estados[449], self.alfabeto_abecedario[32], self.estados[450]],
            [self.estados[450], self.alfabeto_abecedario[32], self.estados[451]], [self.estados[451], self.alfabeto_abecedario[32], self.estados[452]],
            [self.estados[452], self.alfabeto_abecedario[32], self.estados[453]], [self.estados[453], self.alfabeto_abecedario[39], self.estados[454]],
            [self.estados[454], self.alfabeto_abecedario[40], self.estados[455]], [self.estados[453], self.alfabeto_abecedario[40], self.estados[455]],
            [self.estados[455], self.alfabeto_abecedario[32], self.estados[456]], [self.estados[456], self.alfabeto_abecedario[32], self.estados[457]],
            [self.estados[457], self.alfabeto_abecedario[32], self.estados[458]], [self.estados[458], self.alfabeto_abecedario[32], self.estados[459]],
            [self.estados[459], self.alfabeto_abecedario[32], self.estados[460]], [self.estados[460], self.alfabeto_abecedario[32], self.estados[461]],
            [self.estados[461], self.alfabeto_abecedario[32], self.estados[462]], [self.estados[462], self.alfabeto_abecedario[34], self.estados[463]],
            [self.estados[463], self.alfabeto_abecedario[36], self.estados[464]], [self.estados[464], self.alfabeto_abecedario[18], self.estados[465]],
            [self.estados[465], self.alfabeto_abecedario[15], self.estados[466]], [self.estados[466], self.alfabeto_abecedario[0], self.estados[467]],
            [self.estados[467], self.alfabeto_abecedario[13], self.estados[468]], [self.estados[468], self.alfabeto_abecedario[35], self.estados[469]],
            [self.estados[469], self.alfabeto_abecedario[40], self.estados[470]], [self.estados[470], self.alfabeto_abecedario[32], self.estados[471]],
            [self.estados[471], self.alfabeto_abecedario[32], self.estados[472]], [self.estados[472], self.alfabeto_abecedario[32], self.estados[473]],
            [self.estados[473], self.alfabeto_abecedario[32], self.estados[474]], [self.estados[474], self.alfabeto_abecedario[32], self.estados[475]],
            [self.estados[475], self.alfabeto_abecedario[32], self.estados[476]], [self.estados[476], self.alfabeto_abecedario[34], self.estados[477]],
            [self.estados[477], self.alfabeto_abecedario[36], self.estados[478]], [self.estados[478], self.alfabeto_abecedario[19], self.estados[479]],
            [self.estados[479], self.alfabeto_abecedario[3], self.estados[480]], [self.estados[480], self.alfabeto_abecedario[35], self.estados[481]],
            [self.estados[481], self.alfabeto_abecedario[40], self.estados[401]], [self.estados[74], self.alfabeto_abecedario[34], self.estados[482]],
            [self.estados[482], self.alfabeto_abecedario[36], self.estados[483]], [self.estados[483], self.alfabeto_abecedario[19], self.estados[484]],
            [self.estados[484], self.alfabeto_abecedario[0], self.estados[485]], [self.estados[485], self.alfabeto_abecedario[1], self.estados[486]],
            [self.estados[486], self.alfabeto_abecedario[11], self.estados[487]], [self.estados[487], self.alfabeto_abecedario[4], self.estados[488]],
            [self.estados[488], self.alfabeto_abecedario[35], self.estados[489]], [self.estados[342], self.alfabeto_abecedario[32], self.estados[343]],
            [self.estados[343], self.alfabeto_abecedario[32], self.estados[342]], [self.estados[189], self.alfabeto_abecedario[43], self.estados[190]],
            [self.estados[189], self.alfabeto_abecedario[44], self.estados[190]], [self.estados[78], self.alfabeto_abecedario[32], self.estados[208]],
            [self.estados[343], self.alfabeto_abecedario[40], self.estados[344]],

            [self.estados[111], self.alfabeto_abecedario[0], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[1], self.estados[111]],
            [self.estados[111], self.alfabeto_abecedario[2], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[3], self.estados[111]],
            [self.estados[111], self.alfabeto_abecedario[4], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[5], self.estados[111]],
            [self.estados[111], self.alfabeto_abecedario[6], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[7], self.estados[111]],
            [self.estados[111], self.alfabeto_abecedario[8], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[9], self.estados[111]],
            [self.estados[111], self.alfabeto_abecedario[10], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[11], self.estados[111]],
            [self.estados[111], self.alfabeto_abecedario[12], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[13], self.estados[111]],
            [self.estados[111], self.alfabeto_abecedario[14], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[15], self.estados[111]],
            [self.estados[111], self.alfabeto_abecedario[16], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[17], self.estados[111]],
            [self.estados[111], self.alfabeto_abecedario[18], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[19], self.estados[111]],
            [self.estados[111], self.alfabeto_abecedario[20], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[21], self.estados[111]],
            [self.estados[111], self.alfabeto_abecedario[22], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[23], self.estados[111]],
            [self.estados[111], self.alfabeto_abecedario[24], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[25], self.estados[111]],
            [self.estados[111], self.alfabeto_abecedario[26], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[27], self.estados[111]],
            [self.estados[111], self.alfabeto_abecedario[28], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[29], self.estados[111]],
            [self.estados[111], self.alfabeto_abecedario[30], self.estados[111]], [self.estados[111], self.alfabeto_abecedario[31], self.estados[111]],

            [self.estados[112], self.alfabeto_abecedario[0], self.estados[112]], [self.estados[112], self.alfabeto_abecedario[1], self.estados[112]],
            [self.estados[112], self.alfabeto_abecedario[2], self.estados[112]], [self.estados[112], self.alfabeto_abecedario[3], self.estados[112]],
            [self.estados[112], self.alfabeto_abecedario[4], self.estados[112]], [self.estados[112], self.alfabeto_abecedario[5], self.estados[112]],
            [self.estados[112], self.alfabeto_abecedario[6], self.estados[112]], [self.estados[112], self.alfabeto_abecedario[7], self.estados[112]],
            [self.estados[112], self.alfabeto_abecedario[8], self.estados[112]], [self.estados[112], self.alfabeto_abecedario[9], self.estados[112]],
            [self.estados[112], self.alfabeto_abecedario[10], self.estados[112]], [self.estados[112], self.alfabeto_abecedario[11], self.estados[112]],
            [self.estados[112], self.alfabeto_abecedario[12], self.estados[112]], [self.estados[112], self.alfabeto_abecedario[13], self.estados[112]],
            [self.estados[112], self.alfabeto_abecedario[14], self.estados[112]], [self.estados[112], self.alfabeto_abecedario[15], self.estados[112]],
            [self.estados[112], self.alfabeto_abecedario[16], self.estados[112]], [self.estados[112], self.alfabeto_abecedario[17], self.estados[112]],
            [self.estados[112], self.alfabeto_abecedario[18], self.estados[112]], [self.estados[112], self.alfabeto_abecedario[19], self.estados[112]],
            [self.estados[112], self.alfabeto_abecedario[20], self.estados[112]], [self.estados[112], self.alfabeto_abecedario[21], self.estados[112]],
            [self.estados[112], self.alfabeto_abecedario[22], self.estados[112]], [self.estados[112], self.alfabeto_abecedario[23], self.estados[112]],
            [self.estados[112], self.alfabeto_abecedario[24], self.estados[112]], [self.estados[112], self.alfabeto_abecedario[25], self.estados[112]],
            [self.estados[112], self.alfabeto_abecedario[26], self.estados[112]], [self.estados[112], self.alfabeto_abecedario[27], self.estados[112]],
            [self.estados[112], self.alfabeto_abecedario[28], self.estados[112]], [self.estados[112], self.alfabeto_abecedario[29], self.estados[112]],
            [self.estados[112], self.alfabeto_abecedario[30], self.estados[112]], [self.estados[112], self.alfabeto_abecedario[31], self.estados[112]],

            [self.estados[188], self.alfabeto_abecedario[0], self.estados[188]], [self.estados[188], self.alfabeto_abecedario[1], self.estados[188]],
            [self.estados[188], self.alfabeto_abecedario[2], self.estados[188]], [self.estados[188], self.alfabeto_abecedario[3], self.estados[188]],
            [self.estados[188], self.alfabeto_abecedario[4], self.estados[188]], [self.estados[188], self.alfabeto_abecedario[5], self.estados[188]],
            [self.estados[188], self.alfabeto_abecedario[6], self.estados[188]], [self.estados[188], self.alfabeto_abecedario[7], self.estados[188]],
            [self.estados[188], self.alfabeto_abecedario[8], self.estados[188]], [self.estados[188], self.alfabeto_abecedario[9], self.estados[188]],
            [self.estados[188], self.alfabeto_abecedario[10], self.estados[188]], [self.estados[188], self.alfabeto_abecedario[11], self.estados[188]],
            [self.estados[188], self.alfabeto_abecedario[12], self.estados[188]], [self.estados[188], self.alfabeto_abecedario[13], self.estados[188]],
            [self.estados[188], self.alfabeto_abecedario[14], self.estados[188]], [self.estados[188], self.alfabeto_abecedario[15], self.estados[188]],
            [self.estados[188], self.alfabeto_abecedario[16], self.estados[188]], [self.estados[188], self.alfabeto_abecedario[17], self.estados[188]],
            [self.estados[188], self.alfabeto_abecedario[18], self.estados[188]], [self.estados[188], self.alfabeto_abecedario[19], self.estados[188]],
            [self.estados[188], self.alfabeto_abecedario[20], self.estados[188]], [self.estados[188], self.alfabeto_abecedario[21], self.estados[188]],
            [self.estados[188], self.alfabeto_abecedario[22], self.estados[188]], [self.estados[188], self.alfabeto_abecedario[23], self.estados[188]],
            [self.estados[188], self.alfabeto_abecedario[24], self.estados[188]], [self.estados[188], self.alfabeto_abecedario[25], self.estados[188]],
            [self.estados[188], self.alfabeto_abecedario[26], self.estados[188]], [self.estados[188], self.alfabeto_abecedario[27], self.estados[188]],
            [self.estados[188], self.alfabeto_abecedario[28], self.estados[188]], [self.estados[188], self.alfabeto_abecedario[29], self.estados[188]],
            [self.estados[188], self.alfabeto_abecedario[30], self.estados[188]], [self.estados[188], self.alfabeto_abecedario[31], self.estados[188]],

            [self.estados[267], self.alfabeto_abecedario[0], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[1], self.estados[267]],
            [self.estados[267], self.alfabeto_abecedario[2], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[3], self.estados[267]],
            [self.estados[267], self.alfabeto_abecedario[4], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[5], self.estados[267]],
            [self.estados[267], self.alfabeto_abecedario[6], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[7], self.estados[267]],
            [self.estados[267], self.alfabeto_abecedario[8], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[9], self.estados[267]],
            [self.estados[267], self.alfabeto_abecedario[10], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[11], self.estados[267]],
            [self.estados[267], self.alfabeto_abecedario[12], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[13], self.estados[267]],
            [self.estados[267], self.alfabeto_abecedario[14], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[15], self.estados[267]],
            [self.estados[267], self.alfabeto_abecedario[16], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[17], self.estados[267]],
            [self.estados[267], self.alfabeto_abecedario[18], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[19], self.estados[267]],
            [self.estados[267], self.alfabeto_abecedario[20], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[21], self.estados[267]],
            [self.estados[267], self.alfabeto_abecedario[22], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[23], self.estados[267]],
            [self.estados[267], self.alfabeto_abecedario[24], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[25], self.estados[267]],
            [self.estados[267], self.alfabeto_abecedario[26], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[27], self.estados[267]],
            [self.estados[267], self.alfabeto_abecedario[28], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[29], self.estados[267]],
            [self.estados[267], self.alfabeto_abecedario[30], self.estados[267]], [self.estados[267], self.alfabeto_abecedario[31], self.estados[267]],

            [self.estados[268], self.alfabeto_abecedario[0], self.estados[268]], [self.estados[268], self.alfabeto_abecedario[1], self.estados[268]],
            [self.estados[268], self.alfabeto_abecedario[2], self.estados[268]], [self.estados[268], self.alfabeto_abecedario[3], self.estados[268]],
            [self.estados[268], self.alfabeto_abecedario[4], self.estados[268]], [self.estados[268], self.alfabeto_abecedario[5], self.estados[268]],
            [self.estados[268], self.alfabeto_abecedario[6], self.estados[268]], [self.estados[268], self.alfabeto_abecedario[7], self.estados[268]],
            [self.estados[268], self.alfabeto_abecedario[8], self.estados[268]], [self.estados[268], self.alfabeto_abecedario[9], self.estados[268]],
            [self.estados[268], self.alfabeto_abecedario[10], self.estados[268]], [self.estados[268], self.alfabeto_abecedario[11], self.estados[268]],
            [self.estados[268], self.alfabeto_abecedario[12], self.estados[268]], [self.estados[268], self.alfabeto_abecedario[13], self.estados[268]],
            [self.estados[268], self.alfabeto_abecedario[14], self.estados[268]], [self.estados[268], self.alfabeto_abecedario[15], self.estados[268]],
            [self.estados[268], self.alfabeto_abecedario[16], self.estados[268]], [self.estados[268], self.alfabeto_abecedario[17], self.estados[268]],
            [self.estados[268], self.alfabeto_abecedario[18], self.estados[268]], [self.estados[268], self.alfabeto_abecedario[19], self.estados[268]],
            [self.estados[268], self.alfabeto_abecedario[20], self.estados[268]], [self.estados[268], self.alfabeto_abecedario[21], self.estados[268]],
            [self.estados[268], self.alfabeto_abecedario[22], self.estados[268]], [self.estados[268], self.alfabeto_abecedario[23], self.estados[268]],
            [self.estados[268], self.alfabeto_abecedario[24], self.estados[268]], [self.estados[268], self.alfabeto_abecedario[25], self.estados[268]],
            [self.estados[268], self.alfabeto_abecedario[26], self.estados[268]], [self.estados[268], self.alfabeto_abecedario[27], self.estados[268]],
            [self.estados[268], self.alfabeto_abecedario[28], self.estados[268]], [self.estados[268], self.alfabeto_abecedario[29], self.estados[268]],
            [self.estados[268], self.alfabeto_abecedario[30], self.estados[268]], [self.estados[268], self.alfabeto_abecedario[31], self.estados[268]],

            [self.estados[269], self.alfabeto_abecedario[0], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[1], self.estados[269]],
            [self.estados[269], self.alfabeto_abecedario[2], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[3], self.estados[269]],
            [self.estados[269], self.alfabeto_abecedario[4], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[5], self.estados[269]],
            [self.estados[269], self.alfabeto_abecedario[6], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[7], self.estados[269]],
            [self.estados[269], self.alfabeto_abecedario[8], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[9], self.estados[269]],
            [self.estados[269], self.alfabeto_abecedario[10], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[11], self.estados[269]],
            [self.estados[269], self.alfabeto_abecedario[12], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[13], self.estados[269]],
            [self.estados[269], self.alfabeto_abecedario[14], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[15], self.estados[269]],
            [self.estados[269], self.alfabeto_abecedario[16], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[17], self.estados[269]],
            [self.estados[269], self.alfabeto_abecedario[18], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[19], self.estados[269]],
            [self.estados[269], self.alfabeto_abecedario[20], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[21], self.estados[269]],
            [self.estados[269], self.alfabeto_abecedario[22], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[23], self.estados[269]],
            [self.estados[269], self.alfabeto_abecedario[24], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[25], self.estados[269]],
            [self.estados[269], self.alfabeto_abecedario[26], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[27], self.estados[269]],
            [self.estados[269], self.alfabeto_abecedario[28], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[29], self.estados[269]],
            [self.estados[269], self.alfabeto_abecedario[30], self.estados[269]], [self.estados[269], self.alfabeto_abecedario[31], self.estados[269]],

            [self.estados[342], self.alfabeto_abecedario[0], self.estados[342]], [self.estados[342], self.alfabeto_abecedario[1], self.estados[342]],
            [self.estados[342], self.alfabeto_abecedario[2], self.estados[342]], [self.estados[342], self.alfabeto_abecedario[3], self.estados[342]],
            [self.estados[342], self.alfabeto_abecedario[4], self.estados[342]], [self.estados[342], self.alfabeto_abecedario[5], self.estados[342]],
            [self.estados[342], self.alfabeto_abecedario[6], self.estados[342]], [self.estados[342], self.alfabeto_abecedario[7], self.estados[342]],
            [self.estados[342], self.alfabeto_abecedario[8], self.estados[342]], [self.estados[342], self.alfabeto_abecedario[9], self.estados[342]],
            [self.estados[342], self.alfabeto_abecedario[10], self.estados[342]], [self.estados[342], self.alfabeto_abecedario[11], self.estados[342]],
            [self.estados[342], self.alfabeto_abecedario[12], self.estados[342]], [self.estados[342], self.alfabeto_abecedario[13], self.estados[342]],
            [self.estados[342], self.alfabeto_abecedario[14], self.estados[342]], [self.estados[342], self.alfabeto_abecedario[15], self.estados[342]],
            [self.estados[342], self.alfabeto_abecedario[16], self.estados[342]], [self.estados[342], self.alfabeto_abecedario[17], self.estados[342]],
            [self.estados[342], self.alfabeto_abecedario[18], self.estados[342]], [self.estados[342], self.alfabeto_abecedario[19], self.estados[342]],
            [self.estados[342], self.alfabeto_abecedario[20], self.estados[342]], [self.estados[342], self.alfabeto_abecedario[21], self.estados[342]],
            [self.estados[342], self.alfabeto_abecedario[22], self.estados[342]], [self.estados[342], self.alfabeto_abecedario[23], self.estados[342]],
            [self.estados[342], self.alfabeto_abecedario[24], self.estados[342]], [self.estados[342], self.alfabeto_abecedario[25], self.estados[342]],
            [self.estados[342], self.alfabeto_abecedario[26], self.estados[342]], [self.estados[342], self.alfabeto_abecedario[27], self.estados[342]],
            [self.estados[342], self.alfabeto_abecedario[28], self.estados[342]], [self.estados[342], self.alfabeto_abecedario[29], self.estados[342]],
            [self.estados[342], self.alfabeto_abecedario[30], self.estados[342]], [self.estados[342], self.alfabeto_abecedario[31], self.estados[342]],

            [self.estados[343], self.alfabeto_abecedario[0], self.estados[343]], [self.estados[343], self.alfabeto_abecedario[1], self.estados[343]],
            [self.estados[343], self.alfabeto_abecedario[2], self.estados[343]], [self.estados[343], self.alfabeto_abecedario[3], self.estados[343]],
            [self.estados[343], self.alfabeto_abecedario[4], self.estados[343]], [self.estados[343], self.alfabeto_abecedario[5], self.estados[343]],
            [self.estados[343], self.alfabeto_abecedario[6], self.estados[343]], [self.estados[343], self.alfabeto_abecedario[7], self.estados[343]],
            [self.estados[343], self.alfabeto_abecedario[8], self.estados[343]], [self.estados[343], self.alfabeto_abecedario[9], self.estados[343]],
            [self.estados[343], self.alfabeto_abecedario[10], self.estados[343]], [self.estados[343], self.alfabeto_abecedario[11], self.estados[343]],
            [self.estados[343], self.alfabeto_abecedario[12], self.estados[343]], [self.estados[343], self.alfabeto_abecedario[13], self.estados[343]],
            [self.estados[343], self.alfabeto_abecedario[14], self.estados[343]], [self.estados[343], self.alfabeto_abecedario[15], self.estados[343]],
            [self.estados[343], self.alfabeto_abecedario[16], self.estados[343]], [self.estados[343], self.alfabeto_abecedario[17], self.estados[343]],
            [self.estados[343], self.alfabeto_abecedario[18], self.estados[343]], [self.estados[343], self.alfabeto_abecedario[19], self.estados[343]],
            [self.estados[343], self.alfabeto_abecedario[20], self.estados[343]], [self.estados[343], self.alfabeto_abecedario[21], self.estados[343]],
            [self.estados[343], self.alfabeto_abecedario[22], self.estados[343]], [self.estados[343], self.alfabeto_abecedario[23], self.estados[343]],
            [self.estados[343], self.alfabeto_abecedario[24], self.estados[343]], [self.estados[343], self.alfabeto_abecedario[25], self.estados[343]],
            [self.estados[343], self.alfabeto_abecedario[26], self.estados[343]], [self.estados[343], self.alfabeto_abecedario[27], self.estados[343]],
            [self.estados[343], self.alfabeto_abecedario[28], self.estados[343]], [self.estados[343], self.alfabeto_abecedario[29], self.estados[343]],
            [self.estados[343], self.alfabeto_abecedario[30], self.estados[343]], [self.estados[343], self.alfabeto_abecedario[31], self.estados[343]],

            [self.estados[388], self.alfabeto_abecedario[0], self.estados[388]], [self.estados[388], self.alfabeto_abecedario[1], self.estados[388]],
            [self.estados[388], self.alfabeto_abecedario[2], self.estados[388]], [self.estados[388], self.alfabeto_abecedario[3], self.estados[388]],
            [self.estados[388], self.alfabeto_abecedario[4], self.estados[388]], [self.estados[388], self.alfabeto_abecedario[5], self.estados[388]],
            [self.estados[388], self.alfabeto_abecedario[6], self.estados[388]], [self.estados[388], self.alfabeto_abecedario[7], self.estados[388]],
            [self.estados[388], self.alfabeto_abecedario[8], self.estados[388]], [self.estados[388], self.alfabeto_abecedario[9], self.estados[388]],
            [self.estados[388], self.alfabeto_abecedario[10], self.estados[388]], [self.estados[388], self.alfabeto_abecedario[11], self.estados[388]],
            [self.estados[388], self.alfabeto_abecedario[12], self.estados[388]], [self.estados[388], self.alfabeto_abecedario[13], self.estados[388]],
            [self.estados[388], self.alfabeto_abecedario[14], self.estados[388]], [self.estados[388], self.alfabeto_abecedario[15], self.estados[388]],
            [self.estados[388], self.alfabeto_abecedario[16], self.estados[388]], [self.estados[388], self.alfabeto_abecedario[17], self.estados[388]],
            [self.estados[388], self.alfabeto_abecedario[18], self.estados[388]], [self.estados[388], self.alfabeto_abecedario[19], self.estados[388]],
            [self.estados[388], self.alfabeto_abecedario[20], self.estados[388]], [self.estados[388], self.alfabeto_abecedario[21], self.estados[388]],
            [self.estados[388], self.alfabeto_abecedario[22], self.estados[388]], [self.estados[388], self.alfabeto_abecedario[23], self.estados[388]],
            [self.estados[388], self.alfabeto_abecedario[24], self.estados[388]], [self.estados[388], self.alfabeto_abecedario[25], self.estados[388]],
            [self.estados[388], self.alfabeto_abecedario[26], self.estados[388]], [self.estados[388], self.alfabeto_abecedario[27], self.estados[388]],
            [self.estados[388], self.alfabeto_abecedario[28], self.estados[388]], [self.estados[388], self.alfabeto_abecedario[29], self.estados[388]],
            [self.estados[388], self.alfabeto_abecedario[30], self.estados[388]], [self.estados[388], self.alfabeto_abecedario[31], self.estados[388]],

            [self.estados[442], self.alfabeto_abecedario[0], self.estados[442]], [self.estados[442], self.alfabeto_abecedario[1], self.estados[442]],
            [self.estados[442], self.alfabeto_abecedario[2], self.estados[442]], [self.estados[442], self.alfabeto_abecedario[3], self.estados[442]],
            [self.estados[442], self.alfabeto_abecedario[4], self.estados[442]], [self.estados[442], self.alfabeto_abecedario[5], self.estados[442]],
            [self.estados[442], self.alfabeto_abecedario[6], self.estados[442]], [self.estados[442], self.alfabeto_abecedario[7], self.estados[442]],
            [self.estados[442], self.alfabeto_abecedario[8], self.estados[442]], [self.estados[442], self.alfabeto_abecedario[9], self.estados[442]],
            [self.estados[442], self.alfabeto_abecedario[10], self.estados[442]], [self.estados[442], self.alfabeto_abecedario[11], self.estados[442]],
            [self.estados[442], self.alfabeto_abecedario[12], self.estados[442]], [self.estados[442], self.alfabeto_abecedario[13], self.estados[442]],
            [self.estados[442], self.alfabeto_abecedario[14], self.estados[442]], [self.estados[442], self.alfabeto_abecedario[15], self.estados[442]],
            [self.estados[442], self.alfabeto_abecedario[16], self.estados[442]], [self.estados[442], self.alfabeto_abecedario[17], self.estados[442]],
            [self.estados[442], self.alfabeto_abecedario[18], self.estados[442]], [self.estados[442], self.alfabeto_abecedario[19], self.estados[442]],
            [self.estados[442], self.alfabeto_abecedario[20], self.estados[442]], [self.estados[442], self.alfabeto_abecedario[21], self.estados[442]],
            [self.estados[442], self.alfabeto_abecedario[22], self.estados[442]], [self.estados[442], self.alfabeto_abecedario[23], self.estados[442]],
            [self.estados[442], self.alfabeto_abecedario[24], self.estados[442]], [self.estados[442], self.alfabeto_abecedario[25], self.estados[442]],
            [self.estados[442], self.alfabeto_abecedario[26], self.estados[442]], [self.estados[442], self.alfabeto_abecedario[27], self.estados[442]],
            [self.estados[442], self.alfabeto_abecedario[28], self.estados[442]], [self.estados[442], self.alfabeto_abecedario[29], self.estados[442]],
            [self.estados[442], self.alfabeto_abecedario[30], self.estados[442]], [self.estados[442], self.alfabeto_abecedario[31], self.estados[442]],

            [self.estados[215], self.alfabeto_abecedario[0], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[1], self.estados[215]],
            [self.estados[215], self.alfabeto_abecedario[2], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[3], self.estados[215]],
            [self.estados[215], self.alfabeto_abecedario[4], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[5], self.estados[215]],
            [self.estados[215], self.alfabeto_abecedario[6], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[7], self.estados[215]],
            [self.estados[215], self.alfabeto_abecedario[8], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[9], self.estados[215]],
            [self.estados[215], self.alfabeto_abecedario[10], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[11], self.estados[215]],
            [self.estados[215], self.alfabeto_abecedario[12], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[13], self.estados[215]],
            [self.estados[215], self.alfabeto_abecedario[14], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[15], self.estados[215]],
            [self.estados[215], self.alfabeto_abecedario[16], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[17], self.estados[215]],
            [self.estados[215], self.alfabeto_abecedario[18], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[19], self.estados[215]],
            [self.estados[215], self.alfabeto_abecedario[20], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[21], self.estados[215]],
            [self.estados[215], self.alfabeto_abecedario[22], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[23], self.estados[215]],
            [self.estados[215], self.alfabeto_abecedario[24], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[25], self.estados[215]],
            [self.estados[215], self.alfabeto_abecedario[26], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[27], self.estados[215]],
            [self.estados[215], self.alfabeto_abecedario[28], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[29], self.estados[215]],
            [self.estados[215], self.alfabeto_abecedario[30], self.estados[215]], [self.estados[215], self.alfabeto_abecedario[31], self.estados[215]],

            [self.estados[113], self.alfabeto_abecedario[41], self.estados[113]], [self.estados[113], self.alfabeto_abecedario[42], self.estados[113]],
            [self.estados[113], self.alfabeto_abecedario[43], self.estados[113]], [self.estados[113], self.alfabeto_abecedario[44], self.estados[113]],
            [self.estados[113], self.alfabeto_abecedario[45], self.estados[113]], [self.estados[113], self.alfabeto_abecedario[46], self.estados[113]],
            [self.estados[113], self.alfabeto_abecedario[47], self.estados[113]], [self.estados[113], self.alfabeto_abecedario[48], self.estados[113]],
            [self.estados[113], self.alfabeto_abecedario[49], self.estados[113]], [self.estados[113], self.alfabeto_abecedario[50], self.estados[113]], 

            [self.estados[453], self.alfabeto_abecedario[41], self.estados[453]], [self.estados[453], self.alfabeto_abecedario[42], self.estados[453]],
            [self.estados[453], self.alfabeto_abecedario[43], self.estados[453]], [self.estados[453], self.alfabeto_abecedario[44], self.estados[453]],
            [self.estados[453], self.alfabeto_abecedario[45], self.estados[453]], [self.estados[453], self.alfabeto_abecedario[46], self.estados[453]],
            [self.estados[453], self.alfabeto_abecedario[47], self.estados[453]], [self.estados[453], self.alfabeto_abecedario[48], self.estados[453]],
            [self.estados[453], self.alfabeto_abecedario[49], self.estados[453]], [self.estados[453], self.alfabeto_abecedario[50], self.estados[453]], 

            [self.estados[454], self.alfabeto_abecedario[41], self.estados[454]], [self.estados[454], self.alfabeto_abecedario[42], self.estados[454]],
            [self.estados[454], self.alfabeto_abecedario[43], self.estados[454]], [self.estados[454], self.alfabeto_abecedario[44], self.estados[454]],
            [self.estados[454], self.alfabeto_abecedario[45], self.estados[454]], [self.estados[454], self.alfabeto_abecedario[46], self.estados[454]],
            [self.estados[454], self.alfabeto_abecedario[47], self.estados[454]], [self.estados[454], self.alfabeto_abecedario[48], self.estados[454]],
            [self.estados[454], self.alfabeto_abecedario[49], self.estados[454]], [self.estados[454], self.alfabeto_abecedario[50], self.estados[454]], 
        ]

        self.estado_final = ['Q489']

        self.filas = []
        self.columnas = []
        self.estado_siguiente = 0
        self.estatus = False
        datos_minus = datos.lower()
        periodo = ''
        encabezado = ''
        contador = 0
        materia = ''
        examen = ''
        calificacion = ''
        datos_tabla = []
        contador_encabezados = 0
        for x in range(len(datos_minus)):
            simbolo_actual = datos_minus[x]
            self.estatus, transicion = self.buscar_trasicion(self.estado_siguiente, simbolo_actual)
            if self.estatus == True:
                print(datos_minus[x], x)
                self.estado_siguiente = self.estados.index(transicion[2])
                self.final = self.estados[self.estado_siguiente]
                # ----------------------bloque de codigo para el periodo----------------------
                # if (self.estado_siguiente == 111 and simbolo_actual in self.alfabeto_abecedario[0:32]):
                #     periodo = periodo + simbolo_actual
                # if (self.estado_siguiente == 112 and simbolo_actual == self.alfabeto_abecedario[38]):
                #     periodo = periodo + simbolo_actual
                # if (self.estado_siguiente == 112 and simbolo_actual in self.alfabeto_abecedario[0:32]):
                #     periodo = periodo + simbolo_actual
                # if (self.estado_siguiente == 113 and simbolo_actual in self.alfabeto_abecedario[32]):
                #     periodo = periodo + simbolo_actual
                # if (self.estado_siguiente == 113 and simbolo_actual in self.alfabeto_abecedario[41:51]):
                #     periodo = periodo + simbolo_actual
                # if (self.estado_siguiente == 114):
                #     self.columnas.append(periodo)
                #     periodo = ''
                # ----------------------bloque de codigo para el periodo----------------------
                # ----------------------bloque de codigo para los encabezados----------------------
                if (contador_encabezados == 0):
                    if (self.estado_siguiente == 188 and simbolo_actual in self.alfabeto_abecedario[0:32]):
                        encabezado = encabezado + simbolo_actual
                    if (self.estado_siguiente == 189 and simbolo_actual in self.alfabeto_abecedario[32]):
                        encabezado = encabezado + simbolo_actual
                    if (self.estado_siguiente == 190 and simbolo_actual in self.alfabeto_abecedario[42:45]):
                        encabezado = encabezado + simbolo_actual
                    if (self.estado_siguiente == 191):
                        self.columnas.append(encabezado)
                        encabezado = ''
                        contador = contador + 1
                    if contador == 10:
                        contador_encabezados = 1
                # ----------------------bloque de codigo para los encabezados----------------------
                # ----------------------bloque de codigo para los datos de la tabla----------------------
                if (self.estado_siguiente == 342 and simbolo_actual in self.alfabeto_abecedario[0:31]):
                    materia = materia + simbolo_actual
                if (self.estado_siguiente == 343 and simbolo_actual in self.alfabeto_abecedario[32]):
                    materia = materia + simbolo_actual
                if (self.estado_siguiente == 343 and simbolo_actual in self.alfabeto_abecedario[0:31]):
                    materia = materia + simbolo_actual
                if (self.estado_siguiente == 342 and simbolo_actual in self.alfabeto_abecedario[32]):
                    materia = materia + simbolo_actual
                if (self.estado_siguiente == 345):
                    datos_tabla.append(materia)
                    materia = ''

                if (self.estado_siguiente == 388 and simbolo_actual in self.alfabeto_abecedario[0:31]):
                    examen = examen + simbolo_actual
                if (self.estado_siguiente == 389):
                    datos_tabla.append(examen)
                    examen = ''
                
                if (self.estado_siguiente == 453 and simbolo_actual in self.alfabeto_abecedario[41:51]):
                    calificacion = calificacion + simbolo_actual
                if (self.estado_siguiente == 454 and simbolo_actual in self.alfabeto_abecedario[39]):
                    calificacion = calificacion + simbolo_actual
                if (self.estado_siguiente == 454 and simbolo_actual in self.alfabeto_abecedario[41:51]):
                    calificacion = calificacion + simbolo_actual
                if (self.estado_siguiente == 455):
                    datos_tabla.append(calificacion)
                    calificacion = ''

                if (self.estado_siguiente == 365):
                    self.filas.append(datos_tabla)
                    datos_tabla = []
                # ----------------------bloque de codigo para los datos de la tabla----------------------
                if self.final in self.estado_final:
                    print("Aceptado")
                    break
        
            else:
                self.estado_siguiente = 0
        if not self.final in self.estado_final:
            print("Código no válido")
        
        return self.columnas, self.filas


def main(link, matricula, password):
    programa = automata()
    datos = programa.obtener_datos(link, matricula, password)
    columnas, filas = programa.validar_datos(datos)
    # datos_validos = []
    # status = []
    # # for i in datos:
    # #     res = programa.validar_dato(i.upper())
    # #     if (res):
    # #         datos_validos.append(i.upper())
    # #         status.append("válido")
    # #         print(i.upper(), "es", "materia válida")
    # #     else:
    # #         datos_validos.append(i.upper())
    # #         status.append("Inválido")
    # #         print(i.upper(), "es", "materia invalida")
    # # return datos_validos, status
    return columnas, filas


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
