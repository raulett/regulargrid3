# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\raulett\Desktop\Work\!Distr\ApecMarsCoordExport\tools\AMEexportDialog.ui'
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

class Ui_ExportDialog(object):
    def setupUi(self, ExportDialog):
        ExportDialog.setObjectName(_fromUtf8("ExportDialog"))
        ExportDialog.resize(625, 393)
        ExportDialog.setBaseSize(QtCore.QSize(2, 2))
        ExportDialog.setWindowTitle(_fromUtf8("Picket Export"))
        self.buttonBox = QtGui.QDialogButtonBox(ExportDialog)
        self.buttonBox.setGeometry(QtCore.QRect(520, 350, 81, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.groupBox = QtGui.QGroupBox(ExportDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 441, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(230, 40, 181, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox_2 = QtGui.QGroupBox(ExportDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 601, 201))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.tableWidget = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 581, 161))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.exportButton = QtGui.QPushButton(ExportDialog)
        self.exportButton.setGeometry(QtCore.QRect(440, 350, 75, 31))
        self.exportButton.setObjectName(_fromUtf8("exportButton"))

        self.retranslateUi(ExportDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ExportDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ExportDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExportDialog)

    def retranslateUi(self, ExportDialog):
        self.groupBox.setTitle(_translate("ExportDialog", "Выбор слоя пикетов", None))
        self.label.setText(_translate("ExportDialog", "Выгрузка точек со слоя:", None))
        self.pushButton.setText(_translate("ExportDialog", "Добавить генераторные линии", None))
        self.groupBox_2.setTitle(_translate("ExportDialog", "Параметры генераторных линий", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ExportDialog", "ID", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ExportDialog", "I", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ExportDialog", "X1", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ExportDialog", "Y1", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ExportDialog", "X2", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ExportDialog", "Y2", None))
        self.exportButton.setText(_translate("ExportDialog", "Export", None))

