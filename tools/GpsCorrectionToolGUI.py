# -*- coding: utf-8 -*-
# Import the PyQt and QGIS libraries
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *

import gpscorrectiontool

from ui_gpscorrectiontool import Ui_GpsCorrectionDialog

class GPSCorrectionToolGUI(QDialog, QObject, Ui_GpsCorrectionDialog):
    def __init__(self, parent, fl):
        QDialog.__init__(self, parent, fl)
        self.setupUi(self)

    def initGui(self, canvas):
        self.canvas = canvas



    @pyqtSignature("on_pushButton_2_clicked()")
    def on_pushButton_2_clicked(self):
        filenameNew = QFileDialog.getOpenFileName(caption='GPX imported frome device', filter="GPS files (*.gpx)")
        self.lineEdit_2.setText(filenameNew)

    @pyqtSignature("on_pushButton_3_clicked()")
    def on_pushButton_3_clicked(self):
        filenameOld = QFileDialog.getOpenFileName(caption='choose GPX generated before', filter="GPS files (*.gpx)")
        self.lineEdit_3.setText(filenameOld)

    @pyqtSignature("on_pushButton_clicked()")
    def on_pushButton_clicked(self):
        filenameOld = self.lineEdit_3.text()
        filenameNew = self.lineEdit_2.text()
        LayerName = self.lineEdit.text()
        gpscorrectiontool.loadLayer(filenameOld, filenameNew, LayerName)
        self.close()