# -*- coding: utf-8 -*-
# Import the PyQt and QGIS libraries

from qgis.core import *

import os.path

from ui_AMEimportDialog import Ui_Dialog

from cadutils import *

class ImportDialogGui(QDialog, QObject, Ui_Dialog):
    def __init__(self, parent, fl):
        QDialog.__init__(self, parent, fl)
        self.setupUi(self)

    def initGui(self, canvas):
        self.textEdit.setText(u'Выберете файлы для импорта')

    @pyqtSignature("on_pushButton_clicked()")
    def on_pushButton_clicked(self):
        fileNames = QFileDialog.getOpenFileNames(caption = u'Выберете выберете файлы координатной привязки для импорта.(Coord, Model)', filter = u'TextFiles (*.txt)')
        coordFilesCounter = 0
        dataFilesCounter = 0

        for fileName in fileNames:
            file = open(fileName, 'r')
            line = file.readline()
            if (line.find('#GEN') != (-1)):
                coordFilesCounter += 1
                self.coordFileName = fileName

            if (line.find('#DATA')) != (-1):
                dataFilesCounter += 1
                self.dataFileName = fileName
            file.close()

        errorFlag = 0
        coordMassage = ''
        dataMassage = ''
        if coordFilesCounter < 1:
            coordMassage = u'Не найдено координатных файлов'
            errorFlag = 1
        if coordFilesCounter > 1:
            coordMassage = u'Координатных файлов более одного'
            errorFlag = 1
        if dataFilesCounter < 1:
            dataMassage = u'Не найдено файлов данных'
            errorFlag = 1
        if dataFilesCounter > 1:
            errorFlag = 1
            dataMassage = u'Файлов данных более одного'

        if errorFlag == 1:
            self.textEdit.setText(coordMassage + '\n' + dataMassage)
        else:
            self.textEdit.setText(os.path.basename(self.coordFileName) + '\n' + os.path.basename(self.dataFileName))


    @pyqtSignature("on_importButton_clicked()")
    def on_importButton_clicked(self):
        layerName = self.lineEdit.text()
        coordFile = open(self.coordFileName, 'r')
        dataFile = open(self.dataFileName, 'r')
        self.genLines = {}
        self.profileBinding = {}

        line = coordFile.readline()
        if (line.find('#GEN') != (-1)):
            line = coordFile.readline()
        else:
            QMessageBox.information(None, "Cancel", u"Ошибка чтения файла, не найдена метка '#GEN'")
            return
        while line.find('#POINT') == (-1):
            genLineCoord = line.split('\t')
            if genLineCoord[0] == 'ID':
                line = coordFile.readline()
            else:
                self.genLines[genLineCoord[0]] = (float(genLineCoord[2]), float(genLineCoord[3]), float(genLineCoord[4]), float(genLineCoord[5]))
                line = coordFile.readline()

        line = dataFile.readline()
        if (line.find('#DATA') != (-1)):
            line = dataFile.readline()
        else:
            QMessageBox.information(None, "Cancel", u"Ошибка чтения файла, не найдена метка '#DATA'")
            return

        while line:
            pointBinding = line.split('\t')
            if pointBinding[0] == 'ID':
                line = dataFile.readline()
            else:
                prnFileName = pointBinding[4].split('_')
                profileNum = int(prnFileName[1])
                self.profileBinding[profileNum] = self.genLines[pointBinding[2]]
                line = dataFile.readline()

        line = coordFile.readline()
        while line:
            pointCoord = line.split('\t')
            if pointCoord[0] == 'PR':
                line = coordFile.readline()
            else:
                p = QgsPointXY()
                p.setX(float(pointCoord[2]))
                p.setY(float(pointCoord[3]))
                gLineTuple = self.profileBinding.get(int(pointCoord[0]), (0,0,0,0))
                addGeometryToCadLayer(QgsGeometry.fromPoint(p), int(pointCoord[0]), int(pointCoord[1]),
                                      float(pointCoord[4]), float(gLineTuple[0]), float(gLineTuple[1]),
                                      float(gLineTuple[2]), float(gLineTuple[3]), layerName)
                line = coordFile.readline()
        QMessageBox.information(None, "Cancel", u"Точки импортированы успешно")
        self.close()







