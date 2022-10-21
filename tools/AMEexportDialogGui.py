# -*- coding: utf-8 -*-
# Import the PyQt and QGIS libraries
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *

import os.path
import re

from .ui_AMEexportDialog import Ui_ExportDialog
from .CoordBind import *

class ExportDialogGui(QDialog, QObject, Ui_ExportDialog):
    def __init__(self, parent, fl):
        QDialog.__init__(self, parent, fl)
        self.setupUi(self)
        self.coordBind = NULL


    def initGui(self, canvas):
        layers = canvas.layers()
        self.layersList = []
        for layer in layers:
            # check vector layer
            if (type(layer) == QgsVectorLayer):
                # Check geometry type on the layer
                if (layer.geometryType() == 0):
                    # Add this layer into combobox
                    self.layersList.append(layer)
                    self.comboBox.addItem(layer.name())
        self.tableWidget.horizontalHeader().resizeSection(0, 30)
        self.tableWidget.horizontalHeader().resizeSection(1, 30)

    @pyqtSignature("on_pushButton_clicked()")
    def on_pushButton_clicked(self):
        # QMessageBox.information(None, "Cancel", "Combo box num %d"%self.comboBox.currentIndex())
        layer = self.layersList[self.comboBox.currentIndex()]
        i = 0
        j=0
        attributesNum = []

        for fieldNum in layer.dataProvider().fields().allAttributesList():
            if re.search('ProfileNum|PicketNum', layer.dataProvider().fields().field(fieldNum).name()) != None:
                j += 1
                attributesNum.append(fieldNum)
            if re.search('X1|Y1|X2|Y2', layer.dataProvider().fields().field(fieldNum).name()) != None:
                i += 1
                attributesNum.append(fieldNum)

        if i != 4:
            QMessageBox.information(None, "Cancel", u"Данный слой не содержит информации о генераторной линии.")
        elif j != 2:
            QMessageBox.information(None, "Cancel", u"Данный слой содержит некорректную информацию об имени профиля или пикета")
        else:
            features = layer.getFeatures()
            self.coordBind = CoordBind()
            for feature in features:
                point = feature.geometry().asPoint()
                attrs = feature.attributes()
                # QMessageBox.information(None, "Cancel", u"Добавляем пикет: профиль:%d, пикет %d, x=%d, y=%d, X1=%d, Y1=%d, X2=%d, Y2=%d" % (attrs[1], attrs[2], point.x(), point.y(), attrs[4], attrs[5], attrs[6], attrs[7]) )
                self.coordBind.addPicket(attrs[attributesNum[0]], attrs[attributesNum[1]], point.x(), point.y(),
                                         attrs[attributesNum[2]], attrs[attributesNum[3]],
                                         attrs[attributesNum[4]], attrs[attributesNum[5]])
            self.tableWidget.setRowCount(len(self.coordBind.GenLines))
            i = 0
            for GenLine in self.coordBind.GenLines:
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(GenLine.ID)))
                self.tableWidget.item(i, 0).setFlags(Qt.ItemIsEditable)
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(GenLine.I)))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(GenLine.X1)))
                self.tableWidget.item(i,2).setFlags(Qt.ItemIsEditable)
                self.tableWidget.setItem(i, 3, QTableWidgetItem(str(GenLine.Y1)))
                self.tableWidget.item(i, 3).setFlags(Qt.ItemIsEditable)
                self.tableWidget.setItem(i, 4, QTableWidgetItem(str(GenLine.X2)))
                self.tableWidget.item(i, 4).setFlags(Qt.ItemIsEditable)
                self.tableWidget.setItem(i, 5, QTableWidgetItem(str(GenLine.Y2)))
                self.tableWidget.item(i,5).setFlags(Qt.ItemIsEditable)
                i+=1
            # for GLines in self.coordBind.GenLines:

    @pyqtSignature("on_exportButton_clicked()")
    def on_exportButton_clicked(self):
        if self.coordBind == NULL:
            QMessageBox.information(None, "Cancel", u"Выберете слой с пикетами и добавьте генераторные линии")
        else:
            fileName = QFileDialog.getSaveFileName(self, u'Введите имя координатного файла. Файл данных будет сохранен в ту же папку с именем Data.txt', 'Coord_Model', '*.txt' )
            # QMessageBox.information(None, "Cancel", str(directory))
            file = open(fileName, 'w')
            file.write('#GEN\n' + 'ID\tI\tX1\tY1\tX2\tY2\n')
            for i in range(self.tableWidget.rowCount()):
                for j in range(self.tableWidget.columnCount()):
                    file.write(self.tableWidget.item(i,j).text() + '\t')
                file.write('\n')
            file.write('#POINT\n' + 'PR\tPK\tX\tY\tELEV\n')
            for picket in self.coordBind.Pickets:
                file.write(str(picket.PR) + '\t' +
                           str(picket.PK) + '\t' +
                           str(picket.X) + '\t' +
                           str(picket.Y) + '\t' +
                           str(picket.ELEV) + '\n')
            file.close()

            prevFileName = os.path.basename(fileName)
            fileName = os.path.dirname(fileName) + '\Data.txt'
            file = open(fileName, 'w')
            file.write('#DATA\t' + prevFileName + '\n')
            file.write('ID\tfrm\tGEN\tRec\tFileName\n')
            for i in range(len(self.coordBind.Pickets)-1):
                if (self.coordBind.Pickets[i].PR == self.coordBind.Pickets[i+1].PR):
                    file.write(str(i+1) + '\t' +
                               'mrs' + '\t' +
                               str(self.coordBind.Pickets[i].GenLine) + '\t' +
                               str(i+1) + '\t' +
                               'Profile_%d_Picket_%d_%d.prn' % (self.coordBind.Pickets[i].PR,
                                                                self.coordBind.Pickets[i].PK,
                                                                self.coordBind.Pickets[i+1].PK) + '\n')
            file.close()
        QMessageBox.information(None, "Cancel", u'Данные слоя экспортированы успешно')
        self.close()



