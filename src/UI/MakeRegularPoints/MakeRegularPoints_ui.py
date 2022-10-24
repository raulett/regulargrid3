# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\YandexDisk\Work\ProjectsRepositories\20221021_regulargrid\regulargrid3\src\UI\MakeRegularPoints\MakeRegularPoints.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegularPointsDialog(object):
    def setupUi(self, RegularPointsDialog):
        RegularPointsDialog.setObjectName("RegularPointsDialog")
        RegularPointsDialog.resize(444, 337)
        self.verticalLayout = QtWidgets.QVBoxLayout(RegularPointsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(RegularPointsDialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_9.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(RegularPointsDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.warning_icon_label = QtWidgets.QLabel(self.groupBox_2)
        self.warning_icon_label.setMinimumSize(QtCore.QSize(32, 32))
        self.warning_icon_label.setMaximumSize(QtCore.QSize(32, 32))
        self.warning_icon_label.setText("")
        self.warning_icon_label.setObjectName("warning_icon_label")
        self.horizontalLayout_7.addWidget(self.warning_icon_label)
        self.layer_name_label = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layer_name_label.sizePolicy().hasHeightForWidth())
        self.layer_name_label.setSizePolicy(sizePolicy)
        self.layer_name_label.setMinimumSize(QtCore.QSize(100, 32))
        self.layer_name_label.setObjectName("layer_name_label")
        self.horizontalLayout_7.addWidget(self.layer_name_label)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(RegularPointsDialog)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.firstPK = QtWidgets.QDoubleSpinBox(RegularPointsDialog)
        self.firstPK.setDecimals(0)
        self.firstPK.setMaximum(1000.0)
        self.firstPK.setProperty("value", 1.0)
        self.firstPK.setObjectName("firstPK")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstPK)
        self.label = QtWidgets.QLabel(RegularPointsDialog)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.pkNum = QtWidgets.QSpinBox(RegularPointsDialog)
        self.pkNum.setMaximum(1000)
        self.pkNum.setProperty("value", 50)
        self.pkNum.setObjectName("pkNum")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pkNum)
        self.label_4 = QtWidgets.QLabel(RegularPointsDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.dX = QtWidgets.QDoubleSpinBox(RegularPointsDialog)
        self.dX.setProperty("value", 40.0)
        self.dX.setObjectName("dX")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dX)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(RegularPointsDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.firstPR = QtWidgets.QDoubleSpinBox(RegularPointsDialog)
        self.firstPR.setDecimals(0)
        self.firstPR.setMaximum(1000.0)
        self.firstPR.setProperty("value", 1.0)
        self.firstPR.setObjectName("firstPR")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstPR)
        self.label_3 = QtWidgets.QLabel(RegularPointsDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.proNum = QtWidgets.QSpinBox(RegularPointsDialog)
        self.proNum.setMaximum(1000)
        self.proNum.setProperty("value", 2)
        self.proNum.setObjectName("proNum")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.proNum)
        self.label_2 = QtWidgets.QLabel(RegularPointsDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.dY = QtWidgets.QDoubleSpinBox(RegularPointsDialog)
        self.dY.setProperty("value", 50.0)
        self.dY.setObjectName("dY")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dY)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 112, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton = QtWidgets.QPushButton(RegularPointsDialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_12.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btnAdd = QtWidgets.QPushButton(RegularPointsDialog)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout_10.addWidget(self.btnAdd)
        self.btnAddElev = QtWidgets.QPushButton(RegularPointsDialog)
        self.btnAddElev.setObjectName("btnAddElev")
        self.horizontalLayout_10.addWidget(self.btnAddElev)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.btnCancel = QtWidgets.QPushButton(RegularPointsDialog)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_11.addWidget(self.btnCancel)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.retranslateUi(RegularPointsDialog)
        QtCore.QMetaObject.connectSlotsByName(RegularPointsDialog)
        RegularPointsDialog.setTabOrder(self.lineEdit, self.firstPR)
        RegularPointsDialog.setTabOrder(self.firstPR, self.firstPK)
        RegularPointsDialog.setTabOrder(self.firstPK, self.pkNum)
        RegularPointsDialog.setTabOrder(self.pkNum, self.proNum)
        RegularPointsDialog.setTabOrder(self.proNum, self.dX)
        RegularPointsDialog.setTabOrder(self.dX, self.dY)
        RegularPointsDialog.setTabOrder(self.dY, self.btnAdd)
        RegularPointsDialog.setTabOrder(self.btnAdd, self.btnCancel)

    def retranslateUi(self, RegularPointsDialog):
        _translate = QtCore.QCoreApplication.translate
        RegularPointsDialog.setWindowTitle(_translate("RegularPointsDialog", "Generate regular points"))
        self.groupBox.setTitle(_translate("RegularPointsDialog", "Имя слоя для добавления точек"))
        self.lineEdit.setText(_translate("RegularPointsDialog", "RegularGrid Points"))
        self.groupBox_2.setTitle(_translate("RegularPointsDialog", "Source line layer"))
        self.layer_name_label.setText(_translate("RegularPointsDialog", "Layer Name (EPSG:)"))
        self.label_6.setText(_translate("RegularPointsDialog", "FirstPK"))
        self.label.setText(_translate("RegularPointsDialog", "PicketNumber(X)"))
        self.label_4.setText(_translate("RegularPointsDialog", "PicketShift(dX)"))
        self.label_5.setText(_translate("RegularPointsDialog", "FirstPR"))
        self.label_3.setText(_translate("RegularPointsDialog", "ProfilesNum(Y)"))
        self.label_2.setText(_translate("RegularPointsDialog", "ProfilesShift(dY)"))
        self.pushButton.setText(_translate("RegularPointsDialog", "Set new baseline"))
        self.btnAdd.setText(_translate("RegularPointsDialog", "Add points"))
        self.btnAddElev.setText(_translate("RegularPointsDialog", "Add and elevation"))
        self.btnCancel.setText(_translate("RegularPointsDialog", "Cancel"))
