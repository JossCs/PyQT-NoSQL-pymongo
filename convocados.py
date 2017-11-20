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
        Dialog.resize(638, 496)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.eliminar_button = QtGui.QPushButton(self.tab)
        self.eliminar_button.setGeometry(QtCore.QRect(40, 150, 141, 61))
        self.eliminar_button.setObjectName(_fromUtf8("eliminar_button"))
        self.eliall_button = QtGui.QPushButton(self.tab)
        self.eliall_button.setGeometry(QtCore.QRect(40, 270, 141, 61))
        self.eliall_button.setObjectName(_fromUtf8("eliall_button"))
        self.list_convocados = QtGui.QListWidget(self.tab)
        self.list_convocados.setGeometry(QtCore.QRect(260, 40, 341, 391))
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
        self.label.setGeometry(QtCore.QRect(10, 0, 581, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.agregar_button = QtGui.QPushButton(self.tab_2)
        self.agregar_button.setGeometry(QtCore.QRect(10, 290, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.agregar_button.setFont(font)
        self.agregar_button.setObjectName(_fromUtf8("agregar_button"))
        self.list_equipos = QtGui.QListWidget(self.tab_2)
        self.list_equipos.setGeometry(QtCore.QRect(200, 70, 411, 371))
        self.list_equipos.setObjectName(_fromUtf8("list_equipos"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Equipos", None))

