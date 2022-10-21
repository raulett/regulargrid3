# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *
from .BindElevation import *

from .ui_BindElevation import Ui_bindElevationDialog

class BindElevationGui(QDialog, QObject, Ui_bindElevationDialog):
    def __init__(self, parent, fl):
        QDialog.__init__(self, parent, fl)
        self.setupUi(self)
        self.label_5.setVisible(False)
        self.additionValue.setVisible(False)
        self.processOnlyNull.setVisible(False)
        self.processOnlySelected.setVisible(False)




    def initGui(self, canvas):
        # QMessageBox.information(None, QCoreApplication.translate("ctools", "Cancel"), u'Начали Инит Гуи')
        self.layers = canvas.layers()
        self.rastLayersList = []
        for layer in self.layers:
            if (type(layer) == QgsRasterLayer):
                self.rastLayersList.append(layer)
                self.rasterLayer.addItem(layer.name())
            if ((type(layer) == QgsVectorLayer) and (layer.geometryType() == 0)):
                self.vectorLayer.addItem(layer.name())
        # slotLambda = lambda: self.findBand(self.rasterLayer.currentText())
        self.rasterLayer.activated.connect(self.findBand)
        self.vectorLayer.activated.connect(self.findField)
        self.bindElevationButton.clicked.connect(self.on_bindElevationButton_clicked)
        self.findBand()
        self.findField()
        # QMessageBox.information(None, QCoreApplication.translate("ctools", "Cancel"), u'закончили Инит Гуи')


    def findBand(self):
        self.rasterBand.clear()
        # QMessageBox.information(None, QCoreApplication.translate("ctools", "Cancel"), u'findBand')
        layers = QgsProject.instance().mapLayersByName(self.rasterLayer.currentText())
        layer = layers[0]
        if layer.isValid():
            for bandNum in range(layer.bandCount()):
                self.rasterBand.addItem(layer.bandName(bandNum))

    def findField(self):
        self.destinationField.clear()
        layers = QgsProject.instance().mapLayersByName(self.vectorLayer.currentText())
        if len(layers) > 0:
            layer = layers[0]
            if layer.isValid():
                for field in layer.dataProvider().fields().toList():
                    self.destinationField.addItem(field.name())

    def on_bindElevationButton_clicked(self):
        # QMessageBox.information(None,"Cancel", u'BindButtonClicked')
        sourceRaster = QgsProject.instance().mapLayersByName(self.rasterLayer.currentText())[0]
        sourceBandIndex = self.rasterBand.currentIndex()+1
        destVectorLayer = QgsProject.instance().mapLayersByName(self.vectorLayer.currentText())[0]
        currentFieldIndex = self.destinationField.currentIndex()
        BindElevation(sourceRaster, sourceBandIndex, destVectorLayer, currentFieldIndex)
        self.close()






