# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convocados.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(647, 494)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.eliminar_button = QtGui.QPushButton(self.tab)
        self.eliminar_button.setGeometry(QtCore.QRect(40, 150, 141, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(17)
        self.eliminar_button.setFont(font)
        self.eliminar_button.setObjectName(_fromUtf8("eliminar_button"))
        self.eliall_button = QtGui.QPushButton(self.tab)
        self.eliall_button.setGeometry(QtCore.QRect(40, 270, 141, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.eliall_button.setFont(font)
        self.eliall_button.setObjectName(_fromUtf8("eliall_button"))
        self.list_convocados = QtGui.QListWidget(self.tab)
        self.list_convocados.setGeometry(QtCore.QRect(260, 40, 341, 401))
        self.list_convocados.setObjectName(_fromUtf8("list_convocados"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.Equipos_Cbox = QtGui.QComboBox(self.tab_2)
        self.Equipos_Cbox.setGeometry(QtCore.QRect(20, 130, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Equipos_Cbox.setFont(font)
        self.Equipos_Cbox.setObjectName(_fromUtf8("Equipos_Cbox"))
        self.Equipos_Cbox.addItem(_fromUtf8(""))
        self.Equipos_Cbox.addItem(_fromUtf8(""))
        self.Equipos_Cbox.addItem(_fromUtf8(""))
        self.Equipos_Cbox.addItem(_fromUtf8(""))
        self.Equipos_Cbox.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 0, 581, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.agregar_button = QtGui.QPushButton(self.tab_2)
        self.agregar_button.setGeometry(QtCore.QRect(30, 320, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.agregar_button.setFont(font)
        self.agregar_button.setObjectName(_fromUtf8("agregar_button"))
        self.list_equipos = QtGui.QListWidget(self.tab_2)
        self.list_equipos.setGeometry(QtCore.QRect(200, 70, 411, 371))
        self.list_equipos.setObjectName(_fromUtf8("list_equipos"))
        self.mostrar_button = QtGui.QPushButton(self.tab_2)
        self.mostrar_button.setGeometry(QtCore.QRect(30, 220, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.mostrar_button.setFont(font)
        self.mostrar_button.setObjectName(_fromUtf8("mostrar_button"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.nombre_text = QtGui.QLineEdit(self.tab_3)
        self.nombre_text.setGeometry(QtCore.QRect(270, 40, 113, 20))
        self.nombre_text.setObjectName(_fromUtf8("nombre_text"))
        self.apellido_text = QtGui.QLineEdit(self.tab_3)
        self.apellido_text.setGeometry(QtCore.QRect(270, 110, 113, 20))
        self.apellido_text.setObjectName(_fromUtf8("apellido_text"))
        self.label_6 = QtGui.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(110, 250, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.edad_SB = QtGui.QSpinBox(self.tab_3)
        self.edad_SB.setGeometry(QtCore.QRect(320, 160, 42, 22))
        self.edad_SB.setMinimum(20)
        self.edad_SB.setMaximum(35)
        self.edad_SB.setObjectName(_fromUtf8("edad_SB"))
        self.Equipos_CB = QtGui.QComboBox(self.tab_3)
        self.Equipos_CB.setGeometry(QtCore.QRect(270, 250, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Equipos_CB.setFont(font)
        self.Equipos_CB.setObjectName(_fromUtf8("Equipos_CB"))
        self.Equipos_CB.addItem(_fromUtf8(""))
        self.Equipos_CB.addItem(_fromUtf8(""))
        self.Equipos_CB.addItem(_fromUtf8(""))
        self.Equipos_CB.addItem(_fromUtf8(""))
        self.Equipos_CB.addItem(_fromUtf8(""))
        self.label_7 = QtGui.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(110, 200, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(110, 160, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(110, 110, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(110, 40, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.Tipo_CB = QtGui.QComboBox(self.tab_3)
        self.Tipo_CB.setGeometry(QtCore.QRect(270, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Tipo_CB.setFont(font)
        self.Tipo_CB.setObjectName(_fromUtf8("Tipo_CB"))
        self.Tipo_CB.addItem(_fromUtf8(""))
        self.Tipo_CB.addItem(_fromUtf8(""))
        self.Tipo_CB.addItem(_fromUtf8(""))
        self.Tipo_CB.addItem(_fromUtf8(""))
        self.Tipo_CB.addItem(_fromUtf8(""))
        self.ingresar_button = QtGui.QPushButton(self.tab_3)
        self.ingresar_button.setGeometry(QtCore.QRect(180, 320, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.ingresar_button.setFont(font)
        self.ingresar_button.setObjectName(_fromUtf8("ingresar_button"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "NoSQL", None))
        self.eliminar_button.setText(_translate("Dialog", "Eliminar", None))
        self.eliall_button.setText(_translate("Dialog", "Eliminar todos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Convocados", None))
        self.Equipos_Cbox.setItemText(0, _translate("Dialog", "Flamengo", None))
        self.Equipos_Cbox.setItemText(1, _translate("Dialog", "Barcelona", None))
        self.Equipos_Cbox.setItemText(2, _translate("Dialog", "River", None))
        self.Equipos_Cbox.setItemText(3, _translate("Dialog", "Alianza Lima", None))
        self.Equipos_Cbox.setItemText(4, _translate("Dialog", "Universitario", None))
        self.label.setText(_translate("Dialog", "Al seleccionar el equipo,te saldra la lista de jugadores disponibles para convocar", None))
        self.agregar_button.setText(_translate("Dialog", "Agregar", None))
        self.mostrar_button.setText(_translate("Dialog", "Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Equipos", None))
        self.label_6.setText(_translate("Dialog", "Equipo", None))
        self.Equipos_CB.setItemText(0, _translate("Dialog", "Flamengo", None))
        self.Equipos_CB.setItemText(1, _translate("Dialog", "Barcelona", None))
        self.Equipos_CB.setItemText(2, _translate("Dialog", "River", None))
        self.Equipos_CB.setItemText(3, _translate("Dialog", "Alianza Lima", None))
        self.Equipos_CB.setItemText(4, _translate("Dialog", "Universitario", None))
        self.label_7.setText(_translate("Dialog", "Tipo", None))
        self.label_8.setText(_translate("Dialog", "Edad", None))
        self.label_9.setText(_translate("Dialog", "Apellido", None))
        self.label_10.setText(_translate("Dialog", "Nombre", None))
        self.Tipo_CB.setItemText(0, _translate("Dialog", "Portero", None))
        self.Tipo_CB.setItemText(1, _translate("Dialog", "Delantero", None))
        self.Tipo_CB.setItemText(2, _translate("Dialog", "Central", None))
        self.Tipo_CB.setItemText(3, _translate("Dialog", "Lateral", None))
        self.Tipo_CB.setItemText(4, _translate("Dialog", "Defensa", None))
        self.ingresar_button.setText(_translate("Dialog", "Ingresar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Ingresar Jugador", None))

