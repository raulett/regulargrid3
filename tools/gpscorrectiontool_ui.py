# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\YandexDisk\Work\ProjectsRepositories\20221021_regulargrid\regulargrid3\tools\gpscorrectiontool.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GpsCorrectionDialog(object):
    def setupUi(self, GpsCorrectionDialog):
        GpsCorrectionDialog.setObjectName("GpsCorrectionDialog")
        GpsCorrectionDialog.setEnabled(True)
        GpsCorrectionDialog.resize(383, 234)
        self.buttonBox = QtWidgets.QDialogButtonBox(GpsCorrectionDialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 190, 81, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(GpsCorrectionDialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(GpsCorrectionDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 361, 51))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(GpsCorrectionDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 70, 361, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 20, 221, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_3 = QtWidgets.QGroupBox(GpsCorrectionDialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 130, 361, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 20, 221, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 20, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(GpsCorrectionDialog)
        self.buttonBox.accepted.connect(GpsCorrectionDialog.accept)
        self.buttonBox.rejected.connect(GpsCorrectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GpsCorrectionDialog)

    def retranslateUi(self, GpsCorrectionDialog):
        _translate = QtCore.QCoreApplication.translate
        GpsCorrectionDialog.setWindowTitle(_translate("GpsCorrectionDialog", "Import GPX points"))
        self.pushButton.setText(_translate("GpsCorrectionDialog", "Import Points"))
        self.groupBox.setTitle(_translate("GpsCorrectionDialog", "Имя слоя"))
        self.lineEdit.setText(_translate("GpsCorrectionDialog", "RegularGrid Points"))
        self.groupBox_2.setTitle(_translate("GpsCorrectionDialog", "Выберете GPX файл с реальными данными с устройства"))
        self.pushButton_2.setText(_translate("GpsCorrectionDialog", "Выбрать"))
        self.groupBox_3.setTitle(_translate("GpsCorrectionDialog", "Выберете GPX файл с модельными данными"))
        self.pushButton_3.setText(_translate("GpsCorrectionDialog", "Выбрать"))