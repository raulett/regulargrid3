# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *

from .ui_BindToNewLine import Ui_bindDialog
import re

class BindToNewLine(QDialog, QObject, Ui_bindDialog):
    def __init__(self, parent, fl):
        QDialog.__init__(self, parent, fl)
        self.setupUi(self)

    def initGui(self, canvas, p1, p2):
        self.p1 = p1
        self.p2 = p2
        layers = canvas.layers()
        self.layersList = []
        for layer in layers:
            if ((type(layer) == QgsVectorLayer) and (layer.geometryType() == 0)):
                counter = 0
                for field in layer.dataProvider().fields().toList():
                    if re.search('Name|ProfileNum|PicketNum|Elevation|GLineX1|GLineY1|GLineX2|GLineY2'
                            , field.name()) != None:
                        counter += 1
                if counter == 8:
                    self.layersList.append(layer)
                    self.comboBox.addItem(layer.name())

    @pyqtSignature("on_bindButton_clicked()")
    def on_bindButton_clicked(self):
        valList = self.lineEdit.text().split(',')
        # QMessageBox.information(None, "Cancel", str(valList))
        profiles = []
        layers = QgsProject.instance().mapLayersByName(self.comboBox.currentText())
        layer = layers[0]
        # QMessageBox.information(None, "Cancel", str(len(valList)))
        # QMessageBox.information(None, "Cancel", str(valList))
        # QMessageBox.information(None, "Cancel", str(len(self.lineEdit.text().strip())))
        if len(self.lineEdit.text().strip()) > 0:
            # QMessageBox.information(None, "Cancel", u"Че за нахуй")
            # QMessageBox.information(None, "Cancel", str(len(self.lineEdit.text().strip()) == 0))
            for el in valList:
                if (el.isdigit):
                    if (el.find('-') == -1):
                        profiles.append(int(float(el)))
                    else:
                        a = el.split('-')
                        if int(float(a[0]))<int(float(a[1])):
                            for i in range(int(float(a[0])), int(float(a[1]))+1):
                                profiles.append(i)
                        else:
                            QMessageBox.information(None, "Cancel", u'Некорректно задан диапазон значений')
                else:
                    QMessageBox.information(None, "Cancel", u'Некорректно задано значение '
                                            + el + u'.\n Элемент не является числом')
                    break
            # QMessageBox.information(None, "Cancel", str(profiles))
            profiles = list(set(profiles))
            profiles = dict(zip(profiles, profiles)).values()
            # QMessageBox.information(None, "Cancel", str(profiles))
            layer.startEditing()
            for profile in profiles:
                expr = QgsExpression("\"ProfileNum\" LIKE " + str(profile))
                features = layer.getFeatures(QgsFeatureRequest(expr))
                for feature in features:
                    layer.changeAttributeValue(feature.id(), 4, self.p1.x())
                    layer.changeAttributeValue(feature.id(), 5, self.p1.y())
                    layer.changeAttributeValue(feature.id(), 6, self.p2.x())
                    layer.changeAttributeValue(feature.id(), 7, self.p2.y())
            layer.commitChanges()
        else:
            layer.startEditing()
            features = layer.getFeatures()
            for feature in features:
                layer.changeAttributeValue(feature.id(), 4, self.p1.x())
                layer.changeAttributeValue(feature.id(), 5, self.p1.y())
                layer.changeAttributeValue(feature.id(), 6, self.p2.x())
                layer.changeAttributeValue(feature.id(), 7, self.p2.y())
            layer.commitChanges()
        QMessageBox.information(None, "Cancel", u'Привязка профилей к новой генераторной линии осуществлена успешно')
        self.close()




