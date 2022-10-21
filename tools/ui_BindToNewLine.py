# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\raulett\Desktop\Work\!Distr\regulargrid\tools\BindToNewLine.ui'
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

class Ui_bindDialog(object):
    def setupUi(self, bindDialog):
        bindDialog.setObjectName(_fromUtf8("bindDialog"))
        bindDialog.resize(350, 186)
        self.buttonBox = QtGui.QDialogButtonBox(bindDialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 150, 81, 21))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.groupBox = QtGui.QGroupBox(bindDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 331, 131))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 70, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 90, 131, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(160, 70, 161, 51))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(20, 40, 131, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.bindButton = QtGui.QPushButton(bindDialog)
        self.bindButton.setGeometry(QtCore.QRect(170, 150, 75, 21))
        self.bindButton.setObjectName(_fromUtf8("bindButton"))

        self.retranslateUi(bindDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), bindDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), bindDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(bindDialog)

    def retranslateUi(self, bindDialog):
        bindDialog.setWindowTitle(_translate("bindDialog", "Bind profiles to new Line", None))
        self.groupBox.setTitle(_translate("bindDialog", "Bind profiles to current line", None))
        self.label.setText(_translate("bindDialog", "Input profiles numbers", None))
        self.label_2.setText(_translate("bindDialog", "<html><head/><body><p>e.g. 1,2,3 or 1-4,</p><p>or leave empty for all profiles</p></body></html>", None))
        self.label_3.setText(_translate("bindDialog", "Input layer name", None))
        self.bindButton.setText(_translate("bindDialog", "Bind", None))

