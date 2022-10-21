# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *

from .ui_rectangularpoints import Ui_RectangularPoints

class RectangularPointsGui(QDialog, QObject, Ui_RectangularPoints):
    MSG_BOX_TITLE = "Arc Intersection"

    coordSegments = pyqtSignal(float, float, bool, int, int, str)
    closeRectangularPointsGui = pyqtSignal()
    unsetTool = pyqtSignal()
    
    def __init__(self, parent,  fl):
        QDialog.__init__(self, parent,  fl)
        self.setupUi(self)
    
    def initGui(self):
        self.sboxA.setMaximum(10000000)
        self.sboxA.setMinimum(-10000000)
        self.sboxA.setDecimals(4)

        self.sboxO.setMaximum(10000000)
        self.sboxO.setMinimum(-10000000)
        self.sboxO.setDecimals(4)

        self.picNum.setMinimum(1)
        self.proNum.setMinimum(1)

        self.dX.setMaximum(10000000)
        self.dX.setMinimum(-10000000)
        self.dX.setDecimals(4)

        self.dY.setMaximum(10000000)
        self.dY.setMinimum(-10000000)
        self.dY.setDecimals(4)

        self.firstPK.setMaximum(10000000)
        self.firstPK.setMinimum(0)
        self.firstPK.setDecimals(0)

        self.firstPR.setMaximum(10000000)
        self.firstPR.setMinimum(0)
        self.firstPR.setDecimals(0)

        self.btnAdd.clicked.connect(self.on_btnAdd_clicked)
        self.btnCancel.clicked.connect(self.on_btnCancel_clicked)


    def on_btnAdd_clicked(self):
        print('кнопка btnAdd нажата')
        i = 0
        j = 0
        firstPointX = self.sboxA.value()
        firstPointY = self.sboxO.value()
        picketNum = int(self.firstPK.value())
        profileNum = int(self.firstPR.value())
        if self.chckBoxInvert.isChecked():
            sign = 1
            # firstPointY = self.sboxO.value() - (self.proNum.value()-1) * self.dX.value()

        else:
            sign = -1
        LayerName = self.lineEdit.text()
        for i in range(self.proNum.value()):
            for j in range(self.picNum.value()):
                self.coordSegments.emit(firstPointX,  firstPointY,  False, profileNum, picketNum, LayerName)
                firstPointX += self.dX.value()
                picketNum += 1
            picketNum = int(self.firstPK.value())
            firstPointY = firstPointY + sign*self.dY.value()
            firstPointX = self.sboxA.value()
            profileNum += 1
        self.firstPR.setValue(profileNum)

        # QMessageBox.information(None, "Cancel", u'Точки добавлены')
        print('точки добавлены')
        # self.btnAdd.clicked.disconnect(self.on_btnAdd_clicked)
        self.close()
        
    # @pyqtSignature("on_btnCancel_clicked()")
    def on_btnCancel_clicked(self): 
        self.closeRectangularPointsGui.emit()
        self.unsetTool.emit()
        self.close()
