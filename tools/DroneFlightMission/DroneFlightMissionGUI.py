# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *
import re
from .ui_DroneFlightMission import Ui_FlightMissionDialog
from .FlightMission import *
from ...utils.export.addTopXgunFile import addTopXgunFile
from ...utils.export.addSmartAPFile import addSmartAPFile
from ...utils.export.addMissionPlannerFile import addMissionPlannerFile



class DroneFlightMissionGUI(QDialog, QObject, Ui_FlightMissionDialog):
    def __init__(self, parent, fl):
        QDialog.__init__(self, parent, fl)
        self.setupUi(self)

    def initGui(self, canvas):

        self.tableWidget.horizontalHeader().resizeSection(0, 30)
        self.tableWidget.horizontalHeader().resizeSection(1, 45)
        self.tableWidget.horizontalHeader().resizeSection(2, 40)
        self.tableWidget.horizontalHeader().resizeSection(3, 60)
        self.tableWidget.horizontalHeader().resizeSection(6, 50)
        self.tableWidget.horizontalHeader().resizeSection(7, 50)
        self.tableWidget.horizontalHeader().resizeSection(8, 50)
        self.tableWidget.horizontalHeader().resizeSection(9, 50)
        self.tableWidget.horizontalHeader().resizeSection(10, 50)
        self.tableWidget.horizontalHeader().resizeSection(11, 50)
        self.tableWidget.horizontalHeader().resizeSection(12, 50)
        self.FlightMission = FlightMission()
        self.refreshMissionPropsGUI()
        self.refreshLayersComboboxGUI()
        self.lineEdit.isReadOnly()
        self.lineEdit_2.isReadOnly()
        self.layers = canvas.layers()
        self.check = self.checkBox.isChecked()


        self.IsPatrolComboBox.currentIndexChanged.connect(self.updateMissionProps)
        self.StartWayPointIndexComboBox.currentIndexChanged.connect(self.updateMissionProps)
        self.MissionTimeLimitSpinBox.valueChanged.connect(self.updateMissionProps)
        self.spinBox.valueChanged.connect(self.updateMissionProps)
        self.pushButton.pressed.connect(self.updateAllWPprops)
        # self.doubleSpinBox.valueChanged.connect(self.updateAllWPprops)
        # self.doubleSpinBox_2.valueChanged.connect(self.updateAllWPprops)
        # self.doubleSpinBox_3.valueChanged.connect(self.updateAllWPprops)
        # self.comboBox_3.currentIndexChanged.connect(self.updateAllWPprops)
        self.loadFromLayerButton.pressed.connect(self.loadFromReggridLayer)
        self.loadFromLayerButton_2.pressed.connect(self.loadFromMissionLayer)
        self.pushButton_4.pressed.connect(self.serializeXML)
        self.pushButton_5.pressed.connect(self.serializeFMLayer)
        self.comboBox.currentIndexChanged.connect(self.refreshWPsPropsGUI)
        self.doubleSpinBox_5.valueChanged.connect(self.updateWPprops)
        self.doubleSpinBox_4.valueChanged.connect(self.updateWPprops)
        self.spinBox_2.valueChanged.connect(self.updateWPprops)
        self.spinBox_3.valueChanged.connect(self.updateWPprops)
        self.spinBox_4.valueChanged.connect(self.updateWPprops)
        self.spinBox_5.valueChanged.connect(self.updateWPprops)
        self.spinBox_6.valueChanged.connect(self.updateWPprops)
        self.spinBox_7.valueChanged.connect(self.updateWPprops)
        self.comboBox_2.currentIndexChanged.connect(self.updateWPprops)
        self.pushButton_3.pressed.connect(self.loadFromXml)
        self.pushButton_6.pressed.connect(self.saveAsTopXgun)
        self.pushButton_7.pressed.connect(self.saveAsSmartAP)
        self.pushButton_8.pressed.connect(self.saveAsMissionPlanner)

    def refreshLayersComboboxGUI(self):
        self.PointLayerComboBox.clear()
        self.PointLayerComboBox_2.clear()
        layers = QgsProject.instance().mapLayers()
        # self.layersList = []
        for layerName in layers.keys():
            # check vector layer
            layer = layers[layerName]
            if (type(layer) == QgsVectorLayer):
                # Check geometry type on the layer
                if (layer.geometryType() == 0):
                    counter = 0
                    for field in layer.dataProvider().fields().toList():
                        if re.search('Name|ProfileNum|PicketNum|Elevation|GLineX1|GLineY1|GLineX2|GLineY2'
                                , field.name()) != None:
                            counter += 1
                        if counter == 8:
                            # Add this layer into combobox
                            # self.layersList.append(layer)
                            self.PointLayerComboBox.addItem(layer.name())
                            # QMessageBox.information(None, "Cancel", str(layer.name()))
                    for field in layer.dataProvider().fields().toList():
                        if re.search('ID|Latitude|Longitude|Altitude|Elevation'
                                , field.name()) != None:
                            counter += 1
                        if counter == 5:
                            # Add this layer into combobox
                            self.PointLayerComboBox_2.addItem(layer.name())
                            # QMessageBox.information(None, "Cancel", str(layer.name()))


    #Берет данные из объекта и выводит их на форму в группу свойств задания
    def refreshMissionPropsGUI(self):
        self.MissionTimeLimitSpinBox.setValue(self.FlightMission.MissionTimeLmt)

        if self.FlightMission.IsPatrol == 'Start_To_End':
            self.IsPatrolComboBox.setCurrentIndex(0)
        else:
            self.IsPatrolComboBox.setCurrentIndex(1)

        self.StartWayPointIndexComboBox.clear()
        pointsNum = self.FlightMission.WayPoints.keys()
        for pointNum in pointsNum:
            self.StartWayPointIndexComboBox.addItem(str(pointNum))
        self.spinBox.setValue(self.FlightMission.VerticalSpeedLimit)




    def refreshWPsPropsGUI(self):
        if self.comboBox.currentIndex() >= 0:
            wp = self.FlightMission.WayPoints[self.comboBox.currentIndex()]
            self.lineEdit.setText(str(wp.Latitude))
            self.lineEdit_2.setText(str(wp.Longitude))
            self.doubleSpinBox_5.setValue(wp.Altitude)
            self.doubleSpinBox_4.setValue(wp.Speed)
            self.spinBox_2.setValue(wp.YawDegree)
            self.spinBox_3.setValue(wp.HoldTime)
            self.spinBox_4.setValue(wp.StartDelay)
            self.spinBox_5.setValue(wp.Period)
            self.spinBox_6.setValue(wp.RepeatTime)
            self.spinBox_7.setValue(wp.RepeatDistance)
            if wp.TurnMode == 'Adaptive_Bank_Turn':
                i = 0
            elif wp.TurnMode == 'Bank_turn':
                i = 1
            else:
                i = 2
            self.comboBox_2.setCurrentIndex(i)

    def refreshWPsTableGUI(self):
        keys = self.FlightMission.WayPoints.keys()
        self.tableWidget.setRowCount(len(keys))
        i = 0
        for key in keys:
            wp = self.FlightMission.WayPoints[key]
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(key)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(wp.Altitude)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(wp.Speed)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(wp.TurnMode)))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(wp.Latitude)))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(wp.Longitude)))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(str(wp.TimeLimit)))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(str(wp.HoldTime)))
            self.tableWidget.setItem(i, 8, QTableWidgetItem(str(wp.StartDelay)))
            self.tableWidget.setItem(i, 9, QTableWidgetItem(str(wp.Period)))
            self.tableWidget.setItem(i, 10, QTableWidgetItem(str(wp.RepeatTime)))
            self.tableWidget.setItem(i, 11, QTableWidgetItem(str(wp.RepeatDistance)))
            self.tableWidget.setItem(i, 12, QTableWidgetItem(str(wp.YawDegree)))
            i = i + 1


    # Берет данные о высоте стартовой точки и обновляет для всех точек атрибут возвышения
    def updateAllWPprops(self):
        # QMessageBox.information(None, "Cancel", u'Событие обработки альтитьюда')
        for key in self.FlightMission.WayPoints.keys():
            wayPoint = self.FlightMission.WayPoints[key]
            wayPoint.Altitude = wayPoint.Elevation - self.doubleSpinBox.value() + self.doubleSpinBox_2.value()
            wayPoint.Speed = self.doubleSpinBox_3.value()
            wayPoint.TurnMode = self.comboBox_3.currentText()
        self.refreshWPsTableGUI()
        self.refreshWPsPropsGUI()

    def updateWPprops(self):
        wp = self.FlightMission.WayPoints[self.comboBox.currentIndex()]
        wp.Altitude = self.doubleSpinBox_5.value()
        wp.Speed = self.doubleSpinBox_4.value()
        wp.TurnMode = self.comboBox_2.currentText()
        wp.YawDegree = self.spinBox_2.value()
        wp.HoldTime = self.spinBox_3.value()
        wp.StartDelay = self.spinBox_4.value()
        wp.Period = self.spinBox_5.value()
        wp.RepeatTime = self.spinBox_6.value()
        wp.RepeatDistance = self.spinBox_7.value()
        self.refreshWPsTableGUI()


    # Берет данные по свойствам задания и пихает их в объект
    def updateMissionProps(self):
        self.FlightMission.MissionTimeLmt = self.MissionTimeLimitSpinBox.value()
        self.FlightMission.IsPatrol =  self.IsPatrolComboBox.currentText()
        if self.StartWayPointIndexComboBox.count() == 0:
            self.FlightMission.StartWayPointIndex = 0
        else:
            self.FlightMission.StartWayPointIndex = int(self.StartWayPointIndexComboBox.currentText())
        self.FlightMission.VerticalSpeedLimit = self.spinBox.value()

    def loadFromReggridLayer(self):
        layer = QgsProject.instance().mapLayersByName(self.PointLayerComboBox.currentText())[0]
        features = layer.getFeatures()
        currentCrs = layer.crs()
        targetCrs = QgsCoordinateReferenceSystem(4326)
        xform = QgsCoordinateTransform(currentCrs, targetCrs, QgsProject.instance())

        profiles = {}
        for feat in features:
            if profiles.get(feat['ProfileNum']) == None:
                profiles[feat['ProfileNum']] = {}
                profiles[feat['ProfileNum']][feat['PicketNum']] = feat
            else:
                profiles[feat['ProfileNum']][feat['PicketNum']] = feat
        # QMessageBox.information(None, "Cancel", str(profiles))
        ID = 0
        even = 1
        for key in profiles.keys():

            maxPickNum = max(profiles[key].keys())
            minPickNum = min(profiles[key].keys())

            if even == 1:
                a = minPickNum
                b = maxPickNum
            elif even == -1:
                b = minPickNum
                a = maxPickNum
            # QMessageBox.information(None, "Cancel", str(range(a, b + even, even)))
            for j in range(a, b + even, even):

                feature = profiles[key][j]
                point = xform.transform(feature.geometry().asPoint())
                altitude = feature['Elevation'] - self.doubleSpinBox.value()
                elev = feature['Elevation']
                self.FlightMission.addWaypoint(ID, point[1], point[0], altitude, elev)
                # QMessageBox.information(None, "Cancel", str(self.FlightMission.WayPoints))
                ID += 1
            even *= -1
        # QMessageBox.information(None, "Cancel", str(self.FlightMission.WayPoints))
        # for point in self.FlightMission.WayPoints.keys():
        #     # QMessageBox.information(None, "Cancel", str(self.FlightMission.WayPoints[point].Elevation))
        self.refrashIdComboBoxGUI()
        self.refreshWPsTableGUI()

    def loadFromMissionLayer(self):
        layer = QgsProject.instance().mapLayersByName(self.PointLayerComboBox_2.currentText())[0]
        features = layer.getFeatures()
        self.FlightMission = FlightMission.FlightMission()

        for feat in features:
            self.FlightMission.addWaypoint(feat['ID'], feat['Latitude'], feat['Longitude'],
                                           feat['Altitude'], feat['Elevation'], feat['Speed'],
                                           feat['TurnMode'],
                                           feat['YawDegree'], feat['HoldTime'], feat['StartDelay'],
                                           feat['Period'], feat['RepeatTime'], feat['RepeatDist'])
        self.refrashIdComboBoxGUI()
        self.refrashIdComboBoxGUI()
        self.refreshWPsTableGUI()

    def loadFromXml(self):
        loadFile = QFileDialog.getOpenFileName(caption = u'Выберете файл для импорта', filter = u'AWM files (*.awm)')
        self.FlightMission = self.FlightMission.loadFromAWM(loadFile)
        self.refreshWPsTableGUI()
        self.refreshMissionPropsGUI()
        self.refrashIdComboBoxGUI()

    def serializeXML(self):
        saveFile = QFileDialog.getSaveFileName(self, u'Введите имя файла для выгрузки', 'FlightMission', '*.awm')
        self.FlightMission.check = self.checkBox.isChecked()
        self.FlightMission.serializeAWM(saveFile)

    def saveAsTopXgun(self):
        # QMessageBox.information(None, "Cancel", "Save Top X Gun")
        saveFile =  QFileDialog.getSaveFileName(self, u'Введите имя файла для выгрузки', 'FlightMission', '*.export')
        missionArray = self.FlightMission.createTopXGunArray()
        addTopXgunFile(saveFile, missionArray)

    def saveAsMissionPlanner(self):
        # QMessageBox.information(None, "Cancel", "Save Miss planner")
        saveFile = QFileDialog.getSaveFileName(self, u'Введите имя файла для выгрузки', '*.waypoints', '*.waypoints')
        missionArray = self.FlightMission.createMissionPlanner()
        addMissionPlannerFile(saveFile, missionArray)

    def saveAsSmartAP(self):
        saveFile = QFileDialog.getSaveFileName(self, u'Введите имя файла для выгрузки', 'FlightMission', '*.msn')
        missionArray = self.FlightMission.createSmartAPArray()
        addSmartAPFile(saveFile, missionArray)


    def serializeFMLayer(self):
        layersByName = QgsProject.instance().mapLayersByName(self.lineEdit_7.displayText())
        # QMessageBox.information(None, "Cancel", str(layersByName))
        if len(layersByName) > 0:
            layer = layersByName[0]
            layer.startEditing()
            for feat in layer.getFeatures():
                layer.deleteFeature(feat.id())
            layer.commitChanges()

        for pointKey in self.FlightMission.WayPoints.keys():
            point = self.FlightMission.WayPoints[pointKey]
            geom = QgsGeometry.fromPoint(QgsPointXY(point.Longitude, point.Latitude))

            self.addGeometryToFMLayer(geom, pointKey, point.Latitude, point.Longitude,
                                      point.Altitude, point.Elevation, point.Speed,
                                      point.TurnMode, point.YawDegree, point.HoldTime, point.StartDelay,
                                      point.Period, point.RepeatTime,
                                      point.RepeatDistance, point.TimeLimit, self.lineEdit_7.displayText())
        layer = QgsProject.instance().mapLayersByName(self.lineEdit_7.displayText())[0]
        layer.setCustomProperty('MissionTimeLmt', self.MissionTimeLimitSpinBox.value())
        layer.setCustomProperty('IsPatrol', self.IsPatrolComboBox.currentText())
        layer.setCustomProperty('StartWayPointIndex', self.StartWayPointIndexComboBox.currentText())
        layer.setCustomProperty('VerticalSpeedLimit', self.spinBox.value())
        self.refreshLayersComboboxGUI()

    def addGeometryToFMLayer(self, geometry, ID, Latitude, Longitude, Altitude, Elevation, Speed,
                             TurnMode, YawDegree, HoldTime, StartDelay, Period, RepeatTime,
                             RepeatDistance, TimeLimit, layerName="NewFlightMissionLayer"):
        def getLayerByName(lName):
            layermap = QgsProject.instance().mapLayers()
            for name, layer in layermap.iteritems():
                if layer.name() == lName:
                    if layer.isValid():
                        return layer
                    else:
                        return None

        type = geometry.type()
        if type == 0:
            theName = layerName
            theType = "Point"

        if getLayerByName(theName) == None:
            vl = QgsVectorLayer(theType, theName, "memory")
            # savingfile = QFileDialog.getSaveFileName(caption='Save File', filter="Shape file (*.shp)")
            # QgsVectorFileWriter.writeAsVectorFormat(vl, savingfile, "utf-8", None, "ESRI Shapefile")
            # ??????? ???? ? ??????? ?????? ? ???????
            # Add fields with Name and Profile Picket Numbers VMorozov
            vl.dataProvider().addAttributes([QgsField('ID', QVariant.Int),
                                             QgsField('Latitude', QVariant.Double),
                                             QgsField('Longitude', QVariant.Double),
                                             QgsField('Altitude', QVariant.Double),
                                             QgsField('Elevation', QVariant.Double),
                                             QgsField('Speed', QVariant.Double),
                                             QgsField('TurnMode', QVariant.String),
                                             QgsField('YawDegree', QVariant.Int),
                                             QgsField('HoldTime', QVariant.Int),
                                             QgsField('StartDelay', QVariant.Int),
                                             QgsField('Period', QVariant.Int),
                                             QgsField('RepeatTime', QVariant.Int),
                                             QgsField('RepeatDist', QVariant.Int),
                                             QgsField('TimeLimit', QVariant.Int),])
            vl.updateFields()
            pr = vl.dataProvider()
            # ??????? ????????? ??? ????? ?????
            # Add attributes for new point
            # QMessageBox.information(None, "Cancel", self.lineEdit_7.displayText())
            layerCrs = vl.crs()
            geomCRS = QgsCoordinateReferenceSystem(4326)
            xform = QgsCoordinateTransform(geomCRS, layerCrs, QgsProject.instance())
            feat = QgsFeature(vl.fields())
            feat.setAttributes([ID, Latitude, Longitude, Altitude, Elevation, Speed,
                             TurnMode, YawDegree, HoldTime, StartDelay, Period, RepeatTime,
                             RepeatDistance, TimeLimit])
            feat.setGeometry(QgsGeometry.fromPoint(xform.transform(geometry.asPoint())))
            pr.addFeatures([feat])
            vl.updateExtents()
            QgsProject.instance().addMapLayer(vl, True)
        else:
            layer = getLayerByName(theName)
            layerCrs = layer.crs()
            geomCRS = QgsCoordinateReferenceSystem(4326)
            xform = QgsCoordinateTransform(geomCRS, layerCrs, QgsProject.instance())
            pr = layer.dataProvider()
            # ??????? ????????? ??? ????? ?????
            # Add attributes for new point
            feat = QgsFeature(layer.fields())
            feat.setAttributes([ID, Latitude, Longitude, Altitude, Elevation, Speed,
                             TurnMode, YawDegree, HoldTime, StartDelay, Period, RepeatTime,
                             RepeatDistance, TimeLimit])
            # feat = QgsFeature()
            feat.setGeometry(QgsGeometry.fromPoint(xform.transform(geometry.asPoint())))
            pr.addFeatures([feat])
            layer.updateExtents()


    def refrashIdComboBoxGUI(self):
        self.comboBox.clear()
        for id in self.FlightMission.WayPoints.keys():
            self.comboBox.addItem(str(id))










