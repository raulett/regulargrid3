# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.utils import *

from ...utils.rectangularpoint import *
from ..cadutils import *
from ...utils.AffineTransform import *
from .ui_ReggridByPolygon import *
from .reggridByPolygonGui import *







def getPolygons(layer, selectedOnly):
    polygonFeatures = []

    if selectedOnly:
        feats = layer.selectedFeaturesIterator()
    else:
        feats = layer.getFeatures()


    for feat in feats:
        polygonFeatures.append(feat.geometry().asPolygon())

    # QMessageBox.information(None, "Cancel", str(polygonFeatures))
    # polygons = []
    # for featPoly in polygonFeatures:
    #     for polygon in featPoly:
    #         polygons.append(polygon)
    return polygonFeatures



#Функиция получает координаты генераторной линии p1, p2
#Слой, содержащий ограничивающие полигоны
# Флаг, нужно ли учитывать только выделенные полигоны или все полигоны на слое
# Возвращает кортеж из 2 значений. Точка левой нижней границы и точка правой верхней границы, в базисе p1p2.
# горизонтали, протяженность разюиения по вертикали

def getFeaturesLimitsCoord(p1, p2, polygonLayer, selectedFeatures):
    lowest = 9999999999
    high = -9999999999
    leftest = 9999999999
    rightest = -9999999999
    lowLeftPnt = QgsPointXY()
    highRightPnt = QgsPointXY()

    transformToNewBasis = AffineTransform(p1, p2)

    # if selectedFeatures:
    #     feats = polygonLayer.selectedFeaturesIterator()
    # else:
    #     feats = polygonLayer.getFeatures()

    polygons = getPolygons(polygonLayer, selectedFeatures)
    # for feat in feats:
    #     polygons.append(feat.geometry().asPolygon())
    # QMessageBox.information(None, "Cancel", str(polygons))
    points = []
    for featPoly in polygons:
        for polylines in featPoly:
            for point in polylines:
                points.append(point)
                pnt = transformToNewBasis.transform(point)
                if pnt.x() < leftest:
                    leftest =  pnt.x()
                if pnt.x() > rightest:
                    rightest =  pnt.x()
                if pnt.y() > high:
                    high = pnt.y()
                if pnt.y() < lowest:
                    lowest = pnt.y()
                lowLeftPnt.setX(leftest)
                lowLeftPnt.setY(lowest)
                highRightPnt.setX(rightest)
                highRightPnt.setY(high)

    return tuple([lowLeftPnt, highRightPnt])

def addGeometryInPolygon(Dialog, p1, p2, polygonLayer, selectedFeatures, lowLeftPnt, highRightPnt):
    transformToNewBasis = AffineTransform(p1, p2)
    ProfilesDist = Dialog.doubleSpinBox.value()
    PicketDist = Dialog.doubleSpinBox_2.value()
    ProfilesNum = int((highRightPnt.x() - lowLeftPnt.x()) // ProfilesDist)
    PicketNum = int((highRightPnt.y() - lowLeftPnt.y()) // PicketDist)
    IterNumber = ProfilesNum*PicketNum
    currentIteration = 0
    currentProfile = Dialog.spinBox.value()
    currentPicket = Dialog.spinBox_2.value()
    pnt = QgsPointXY()

    polygons = getPolygons(polygonLayer, Dialog.checkBox.isChecked())
    # Dialog.addLogString(u'полигон  ' + str(polygons))

    # #Пробую добавить прогресс бар
    # progressMessageBar = iface.messageBar()
    # progress = QProgressBar()
    # progress.setMaximum(100)
    # progressMessageBar.pushWidget(progress)


    if Dialog.checkBox_3.isChecked():
        layers = QgsProject.instance().mapLayersByName(Dialog.lineEdit.text())
        if len(layers) > 0:
            layer = layers[0]
            # Dialog.addLogString(u"Вход в удалялку, слой " + str(layer) + str(layer.name()))
            layer.startEditing()
            counter = 0
            total = layer.dataProvider().featureCount()
            Dialog.addLogString(u"Удаление точек может занять некоторое время. ")
            for feat in layer.getFeatures():
                counter += 1
                layer.deleteFeature(feat.id())
                a = Dialog.progressBar.value()
                percent = int((counter*100/total))
                # progress.setValue(percent)
                Dialog.progressBar.setValue(percent)
                # Dialog.addLogString(str(percent) + ' ' +  str(total) + ' ' + str(counter))

                # if Dialog.progressBar.value() <> a:
                #     Dialog.progressBar.repaint()
            # Dialog.addLogString(str(counter))
            layer.commitChanges()
            Dialog.addLogString(u"Удаление точек закончено.")

    # Dialog.addLogString(str(polygons))

    minProfile = 99999
    maxProfile = 0
    minPicket = 999999
    maxPicket = 0
    counter = 0

    Dialog.addLogString(u"Начато добавление пикетов.")
    for profile in range(ProfilesNum+2):
        pnt.setX(lowLeftPnt.x() + profile * ProfilesDist)
        for picket in range(PicketNum+2):
            currentIteration += 1
            Dialog.progressBar.setValue(int((currentIteration *100/ IterNumber)))
            QCoreApplication.processEvents()
            pnt.setY(lowLeftPnt.y()+ picket*PicketDist)
            limDistance = Dialog.doubleSpinBox_3.value()
            point = transformToNewBasis.revert(pnt)
            for polygon in polygons:
                gPolygon = QgsGeometry.fromPolygon(polygon)
                check = gPolygon.intersects(QgsGeometry.fromPoint(point)) or \
                        gPolygon.intersects(QgsGeometry.fromPoint(QgsPointXY(point.x()+ limDistance, point.y()))) or \
                        gPolygon.intersects(QgsGeometry.fromPoint(QgsPointXY(point.x()- limDistance, point.y()))) or \
                        gPolygon.intersects(QgsGeometry.fromPoint(QgsPointXY(point.x(), point.y()+ limDistance))) or \
                        gPolygon.intersects(QgsGeometry.fromPoint(QgsPointXY(point.x(), point.y()- limDistance))) or \
                        gPolygon.intersects(QgsGeometry.fromPoint(QgsPointXY(point.x() - limDistance, point.y() - limDistance))) or \
                        gPolygon.intersects(QgsGeometry.fromPoint(QgsPointXY(point.x() - limDistance, point.y() + limDistance))) or \
                        gPolygon.intersects(QgsGeometry.fromPoint(QgsPointXY(point.x() + limDistance, point.y() + limDistance))) or \
                        gPolygon.intersects(QgsGeometry.fromPoint(QgsPointXY(point.x() + limDistance, point.y() - limDistance)))
                if check:
                    addGeometryToCadLayer(QgsGeometry.fromPoint(point), currentProfile, currentPicket, 0,
                                              p1.x(), p1.y(), p2.x(), p2.y(), Dialog.lineEdit.text())
                    counter += 1
            if currentProfile < minProfile:
                minProfile = currentProfile
            if currentProfile > maxProfile:
                maxProfile = currentProfile

            currentPicket += 1
        currentPicket = Dialog.spinBox_2.value()
        # pnt.setY(lowLeftPnt.y())
        currentProfile += 1
    RegGridLayer = getCadLayerByName(Dialog.lineEdit.text())
    RegGridLayer.setCrs(polygonLayer.crs())
    Dialog.addLogString(u"Добавление пикетов окончено.")
    Dialog.addLogString(u"Всего добавлено " + str(counter) + u' пикетов')
    Dialog.addLogString(u"Пикеты добавлены на " + str(maxProfile-minProfile+1) + u' профилей')
    Dialog.addLogString(u"Система координат слоя: " + str(RegGridLayer.crs().description()))
    iface.mapCanvas().refresh()



