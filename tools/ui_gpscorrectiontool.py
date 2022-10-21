# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\raulett\Desktop\Work\!Distr\regulargrid\tools\gpscorrectiontool.ui'
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

class Ui_GpsCorrectionDialog(object):
    def setupUi(self, GpsCorrectionDialog):
        GpsCorrectionDialog.setObjectName(_fromUtf8("GpsCorrectionDialog"))
        GpsCorrectionDialog.resize(383, 234)
        self.buttonBox = QtGui.QDialogButtonBox(GpsCorrectionDialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 190, 81, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.pushButton = QtGui.QPushButton(GpsCorrectionDialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 200, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox = QtGui.QGroupBox(GpsCorrectionDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 361, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 221, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.groupBox_2 = QtGui.QGroupBox(GpsCorrectionDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 70, 361, 51))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 20, 221, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 20, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.groupBox_3 = QtGui.QGroupBox(GpsCorrectionDialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 130, 361, 51))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 20, 221, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 20, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(GpsCorrectionDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GpsCorrectionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GpsCorrectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GpsCorrectionDialog)

    def retranslateUi(self, GpsCorrectionDialog):
        GpsCorrectionDialog.setWindowTitle(_translate("GpsCorrectionDialog", "Import GPX points", None))
        self.pushButton.setText(_translate("GpsCorrectionDialog", "Import Points", None))
        self.groupBox.setTitle(_translate("GpsCorrectionDialog", "Имя слоя", None))
        self.lineEdit.setText(_translate("GpsCorrectionDialog", "RegularGrid Points", None))
        self.groupBox_2.setTitle(_translate("GpsCorrectionDialog", "Выберете GPX файл с реальными данными с устройства", None))
        self.pushButton_2.setText(_translate("GpsCorrectionDialog", "Выбрать", None))
        self.groupBox_3.setTitle(_translate("GpsCorrectionDialog", "Выберете GPX файл с модельными данными", None))
        self.pushButton_3.setText(_translate("GpsCorrectionDialog", "Выбрать", None))

