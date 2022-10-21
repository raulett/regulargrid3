# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *

from ...utils.LayerSelector import getLayersByType
from ...utils.rectangularpoint import *
from .geometryFunction import *
import webbrowser, os

from .ui_ReggridByPolygon import Ui_reggridByPolygonDialog

class reggridByPolygonGui(QDialog, QObject, Ui_reggridByPolygonDialog):
    def __init__(self, parent, fl):
        QDialog.__init__(self, parent, fl)
        self.setupUi(self)
        self.textEdit.setReadOnly(True)

    def initGui(self, canvas, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.canvas = canvas
        layers = getLayersByType(self.canvas, 2)
        self.progressBar.setUpdatesEnabled(True)
        for layer in layers:
            features = []
            for feat in layer.getFeatures():
                features.append(feat)
            if len(features) > 0:
                self.comboBox.addItem(layer.name())
        self.AddButton.clicked.connect(self.on_AddButton_clicked)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    def addLogString(self, LogString):
        self.textEdit.append(LogString)

    def on_AddButton_clicked(self):
        layers = QgsProject.instance().mapLayersByName(self.comboBox.currentText())
        if len(layers) > 0:
            layer = layers[0]

            limitPoints = getFeaturesLimitsCoord(self.p1, self.p2, layer, self.checkBox.isChecked())

            lowLeftPnt = limitPoints[0]
            highRightPnt = limitPoints[1]
            addGeometryInPolygon(self, self.p1, self.p2, layer,  self.checkBox.isChecked(), lowLeftPnt, highRightPnt)

    def on_pushButton_clicked(self):
        currentPath = os.path.dirname(__file__)
        currentPathToModule = os.path.split(os.path.split(currentPath)[0])[0]
        webbrowser.open(currentPathToModule + "/help/ReggridByPolygon/RegularGridInPolygonHelp.mht")
        # QMessageBox.information(None, "Cancel", str(currentPathToModule))






