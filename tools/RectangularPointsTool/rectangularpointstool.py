# -*- coding: utf-8 -*-
# Import the PyQt and QGIS libraries
from ..RectangularPointsTool.cadutils import *
# from .BindToNewLineGui import BindToNewLine
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ..ReggridByPolygon.reggridByPolygonGui import reggridByPolygonGui
from qgis.core import *
from .rectangularpointsgui import RectangularPointsGui
from ..singlesegmentfindertool import SingleSegmentFinderTool

from .rectangularpoint import RectangularPoint
from ..BindElevationGui import BindElevationGui
# from .GpsCorrectionToolGUI import GPSCorrectionToolGUI
from ..DroneFlightMission.DroneFlightMissionGUI import DroneFlightMissionGUI
from regulargrid.utils.rectangularpoint import RectangularPoint
# from ..tools.FlightPointTool.FlightPoint import FlightPoint



class RectangularPointsTool():
    
        def __init__(self, iface,  toolBar):
            # Save reference to the QGIS interface
            self.iface = iface
            self.canvas = self.iface.mapCanvas()
            
            # the 2 points of the segment
            # p1 is always the left point
            self.p1 = None
            self.p2 = None
                
            # Create actions 
            self.act_rectpoints = QAction(QIcon(":/plugins/regulargrid/icons/orthopoint.png"),
                                          QCoreApplication.translate("ctools", "Regular Grid"),
                                          self.iface.mainWindow())
            self.act_selectlinesegment= QAction(QIcon(":/plugins/regulargrid/icons/select1line_v2.png"),
                                                QCoreApplication.translate("ctools", "Select Line Segments"),
                                                self.iface.mainWindow())
            # self.act_bindtonewline = QAction(QIcon(":/plugins/regulargrid/icons/bindToNewLine.png"),
            #                                     "Bind Profiles to new Line",
            #                                     self.iface.mainWindow())
            # Add new feature icon. VMorozov
            # self.act_importgpx = QAction(QIcon(":/plugins/regulargrid/icons/importGPX.png"),
            #                                      QCoreApplication.translate("ctools", "Import GPX"),
            #                                      self.iface.mainWindow())

            #Add reggrid by polygon feature icon. VMorozov.
            self.act_reggridInPolygon = QAction(QIcon(":/plugins/regulargrid/icons/reggridPolygon.png"),
                                         "add regular grid in poligon",
                                         self.iface.mainWindow())

            self.act_selectlinesegment.setCheckable(True)

            # Add Elevation tool
            self.act_elevation = QAction(QIcon(":/plugins/regulargrid/icons/elevation_icon.png"),
                                                "Bind Elevation",
                                                 self.iface.mainWindow())

            #Add Flight Mission tool
            self.act_DFMtool = QAction(QIcon(":/plugins/regulargrid/icons/DFM.png"),
                                                "Create Flight Mission",
                                                 self.iface.mainWindow())

            #Add FlightPointTool tool
            self.act_FlightPoint = QAction(QIcon(":/plugins/regulargrid/icons/fPoint.png"),
                                           "Model Of Flight Mission",
                                           self.iface.mainWindow())

            # Connect to signals for button behaviour
            self.act_rectpoints.triggered.connect(self.showDialog)
            # self.act_selectlinesegment.triggered.connect(self.selectlinesegment)
            # self.act_bindtonewline.triggered.connect(self.bindToNewLineDialog)
            self.act_elevation.triggered.connect(self.bindElevation)
            self.act_DFMtool.triggered.connect(self.CreateDroneFlightMission)
            self.act_FlightPoint.triggered.connect(self.showFlightPointGUI)

            self.act_reggridInPolygon.triggered.connect(self.reggridByPolygonDialog)

            # Add new feature icon. VMorozov
            # self.act_importgpx.triggered.connect(self.importGPX)
            self.canvas.mapToolSet.connect(self.deactivate)

            # Add actions to the toolbar
            toolBar.addSeparator()
            toolBar.addAction(self.act_selectlinesegment)
            toolBar.addAction(self.act_rectpoints)
            # Add reggrid by polygon feature icon to th toolbar. VMorozov.
            toolBar.addAction(self.act_reggridInPolygon)

            # toolBar.addAction(self.act_bindtonewline)

            # Add Elevation tool icon

            toolBar.addAction(self.act_elevation)
            toolBar.addSeparator()

            # Add Flight Mission tool icon
            toolBar.addAction(self.act_DFMtool)
            # toolBar.addAction(self.act_FlightPoint)
            toolBar.addSeparator()

            # Add new feature icon. VMorozov
            # toolBar.addAction(self.act_importgpx)

            # Get the tool
            self.tool = SingleSegmentFinderTool(self.canvas)

        #add showFlightPoint feature
        def showFlightPointGUI(self):
            # QMessageBox.information(None, "Cancel", "No segment selected.")
            self.ctrl = FlightPoint(self.iface)
            self.ctrl.initGui()



        #Add Drone Flight Mission feat
        def CreateDroneFlightMission(self):
            flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint
            self.ctrl = DroneFlightMissionGUI(self.iface.mainWindow(), flags)
            self.ctrl.initGui(self.canvas)
            self.ctrl.show()

        # Add new feature icon. VMorozov
        # def importGPX(self):
        #     flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint
        #     self.ctrl = GPSCorrectionToolGUI(self.iface.mainWindow(), flags)
        #     self.ctrl.initGui(self.canvas)
        #     self.ctrl.show()

        #Add binding profiles to new line feature
        # def bindToNewLineDialog(self):
        #     if self.p1 == None or self.p2 == None:
        #         QMessageBox.information(None, QCoreApplication.translate("ctools", "Cancel"), "No segment selected.")
        #     else:
        #         flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint
        #         self.ctrl = BindToNewLine(self.iface.mainWindow(), flags)
        #         self.ctrl.initGui(self.canvas, self.p1, self.p2)
        #         self.ctrl.show()

        # Add binding profiles to new line feature
        def reggridByPolygonDialog(self):
            if self.p1 == None or self.p2 == None:
                QMessageBox.information(None, "Cancel", "No segment selected.")
            else:
                flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint
                self.ctrl = reggridByPolygonGui(self.iface.mainWindow(), flags)
                self.ctrl.initGui(self.canvas, self.p1, self.p2)
                self.ctrl.show()

        #Add bindinf elevation feature
        def bindElevation(self):
            flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint
            self.ctrl = BindElevationGui(self.iface.mainWindow(), flags)
            self.ctrl.initGui(self.canvas)
            self.ctrl.show()



        def showDialog(self):
            currLayer = self.canvas.currentLayer()
            selectedFeat = currLayer.selectedFeatures()
            points = selectedFeat[0].geometry().asPolyline()

            self.p1 = points[0]
            self.p2 = points[1]
            # #     QMessageBox.information(None, QCoreApplication.translate("ctools", "Cancel"), QCoreApplication.translate("ctools", "No segment selected."))
            # else:
            flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint
            self.ctrl = RectangularPointsGui(self.iface.mainWindow(),  flags)
            self.ctrl.initGui()
            self.ctrl.show()
            # connect the signals
            self.ctrl.coordSegments.connect(self.calculateRectangularPoint)
            # self.ctrl.closeRectangularPointsGui.connect(self.deactivate)
            # self.ctrl.unsetTool.connect(self.unsetTool)
                         
        def calculateRectangularPoint(self, dX, dY,  inverse, profileNum, picketNum, layerName):
            # I still don't get it.....
            pt1 = QgsPointXY()
            pt1.setX(self.p1.x())
            pt1.setY(self.p1.y())
            pt2 = QgsPointXY()
            pt2.setX(self.p2.x())
            pt2.setY(self.p2.y())

            GenLineFirstPointXcoord = self.p1.x()
            GenLineFirstPointYcoord = self.p1.y()
            GenLineSecPointXcoord = self.p2.x()
            GenLineSecPointYcoord = self.p2.y()
            
            # Calculate the new (rectangular) Point
            result = RectangularPoint.point(pt1, pt2, dX, dY, inverse)
            elevation = 0
            
            if result == 0:
                mc = self.canvas
                mc.unsetMapTool(self.tool)             
                return
            else:
                print(result)
                addGeometryToCadLayer(QgsGeometry.fromPointXY(result), profileNum, picketNum, elevation,
                                               GenLineFirstPointXcoord, GenLineFirstPointYcoord, GenLineSecPointXcoord,
                                               GenLineSecPointYcoord, layerName)
                self.canvas.refresh()
                
            self.p1 = pt1
            self.p2 = pt2
            
        # Select  Line Segment
        def selectlinesegment(self):
            pass
            mc = self.canvas
            layer = mc.currentLayer()

            # Set SegmentFinderTool as current tool
            mc.setMapTool(self.tool)
            self.act_selectlinesegment.setChecked(True)        
                    
            #Connect to the SegmentFinderTool
            self.tool.segmentFound.connect(self.storeSegmentPoints)



        def storeSegmentPoints(self,  result):

            if result[0].x() < result[1].x():
                self.p1 = result[0]
                self.p2 = result[1]
            elif result[0].x() == result[1].x():
                self.p1 = result[0]
                self.p2 = result[1]
            else:
                self.p1 = result[0]
                self.p2 = result[1]


            layerCrs = self.canvas.currentLayer().crs()
            projectCrs = self.canvas.mapRenderer().destinationCrs()
            coordTransform = QgsCoordinateTransform(projectCrs, layerCrs, QgsProject.instance())
            self.p1 = coordTransform.transform(self.p1)
            self.p2 = coordTransform.transform(self.p2)
        
        def unsetTool(self):
            mc = self.canvas
            mc.unsetMapTool(self.tool)             
                
        def deactivate(self):
            #QMessageBox.information(None,  "Cancel",  str(self.ctrl))
            self.p1 = None
            self.p2 = None
                    
            #uncheck the button/menu and get rid off the SSFtool signal
            self.act_selectlinesegment.setChecked(False)
            try:
                self.tool.segmentFound.disconnect(self.storeSegmentPoints)
            except TypeError:
                pass
