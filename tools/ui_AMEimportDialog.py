# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\raulett\Desktop\Work\!Distr\regulargrid\tools\AMEimportDialog.ui'
#
# Created by: PyQt5 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

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
        Dialog.resize(387, 270)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(270, 220, 81, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 80, 341, 131))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(250, 40, 75, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(20, 30, 221, 61))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.importButton = QtGui.QPushButton(Dialog)
        self.importButton.setGeometry(QtCore.QRect(190, 220, 75, 31))
        self.importButton.setObjectName(_fromUtf8("importButton"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 341, 51))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 221, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Импорт файлов координатной привязки", None))
        self.groupBox.setTitle(_translate("Dialog", "Файлы для импорта", None))
        self.pushButton.setText(_translate("Dialog", "Обзор", None))
        self.importButton.setText(_translate("Dialog", "Импорт", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Имя слоя для добавления", None))
        self.lineEdit.setText(_translate("Dialog", "RegularGrid Points", None))

