# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\Work\Programming\!Distr\regulargrid\tools\BindElevation.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bindElevationDialog(object):
    def setupUi(self, bindElevationDialog):
        bindElevationDialog.setObjectName("bindElevationDialog")
        bindElevationDialog.resize(400, 247)
        self.buttonBox = QtWidgets.QDialogButtonBox(bindElevationDialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 210, 341, 21))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.rasterLayer = QtWidgets.QComboBox(bindElevationDialog)
        self.rasterLayer.setGeometry(QtCore.QRect(210, 20, 171, 22))
        self.rasterLayer.setObjectName("rasterLayer")
        self.label_4 = QtWidgets.QLabel(bindElevationDialog)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 204, 20))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(bindElevationDialog)
        self.label_6.setGeometry(QtCore.QRect(20, 50, 31, 20))
        self.label_6.setObjectName("label_6")
        self.rasterBand = QtWidgets.QComboBox(bindElevationDialog)
        self.rasterBand.setGeometry(QtCore.QRect(260, 50, 120, 20))
        self.rasterBand.setMinimumSize(QtCore.QSize(120, 0))
        self.rasterBand.setObjectName("rasterBand")
        self.vectorLayer = QtWidgets.QComboBox(bindElevationDialog)
        self.vectorLayer.setGeometry(QtCore.QRect(180, 80, 201, 20))
        self.vectorLayer.setObjectName("vectorLayer")
        self.label = QtWidgets.QLabel(bindElevationDialog)
        self.label.setGeometry(QtCore.QRect(20, 80, 101, 20))
        self.label.setObjectName("label")
        self.destinationField = QtWidgets.QComboBox(bindElevationDialog)
        self.destinationField.setGeometry(QtCore.QRect(180, 110, 201, 20))
        self.destinationField.setObjectName("destinationField")
        self.label_2 = QtWidgets.QLabel(bindElevationDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 204, 20))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(bindElevationDialog)
        self.label_5.setGeometry(QtCore.QRect(23, 140, 131, 20))
        self.label_5.setObjectName("label_5")
        self.additionValue = QtWidgets.QDoubleSpinBox(bindElevationDialog)
        self.additionValue.setGeometry(QtCore.QRect(160, 140, 59, 20))
        self.additionValue.setMinimum(-999.99)
        self.additionValue.setMaximum(999.99)
        self.additionValue.setObjectName("additionValue")
        self.processOnlySelected = QtWidgets.QCheckBox(bindElevationDialog)
        self.processOnlySelected.setGeometry(QtCore.QRect(20, 193, 414, 17))
        self.processOnlySelected.setObjectName("processOnlySelected")
        self.processOnlyNull = QtWidgets.QCheckBox(bindElevationDialog)
        self.processOnlyNull.setGeometry(QtCore.QRect(20, 170, 414, 17))
        self.processOnlyNull.setObjectName("processOnlyNull")
        self.bindElevationButton = QtWidgets.QPushButton(bindElevationDialog)
        self.bindElevationButton.setGeometry(QtCore.QRect(220, 210, 75, 21))
        self.bindElevationButton.setObjectName("bindElevationButton")

        self.retranslateUi(bindElevationDialog)
        self.buttonBox.accepted.connect(bindElevationDialog.accept)
        self.buttonBox.rejected.connect(bindElevationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(bindElevationDialog)

    def retranslateUi(self, bindElevationDialog):
        _translate = QtCore.QCoreApplication.translate
        bindElevationDialog.setWindowTitle(_translate("bindElevationDialog", "Bind Elevation"))
        self.label_4.setText(_translate("bindElevationDialog", "Слой - источник данных"))
        self.label_6.setText(_translate("bindElevationDialog", "Канал"))
        self.label.setText(_translate("bindElevationDialog", "Слой назначения"))
        self.label_2.setText(_translate("bindElevationDialog", "Поле назначения"))
        self.label_5.setText(_translate("bindElevationDialog", "Прибавить к значению"))
        self.processOnlySelected.setText(_translate("bindElevationDialog", "Обрабатывать только выделенные объекты"))
        self.processOnlyNull.setText(_translate("bindElevationDialog", "Обрабатывать только объекты, где поле назначения не определено"))
        self.bindElevationButton.setText(_translate("bindElevationDialog", "Bind"))
