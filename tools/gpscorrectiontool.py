# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis import *
import tools.cadutils

gpsLayerName = "imported GPS Points"
generatedPoints = "Generated Points"

def distCoord(coord1, coord2):
    return (coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2

def loadLayer(generatedGpsFile, inputGpsFile, LayerName):

    layGenerated = core.QgsVectorLayer('%s?type=waypoint' % (generatedGpsFile), generatedPoints, "gpx")
    if not layGenerated.isValid():
        QMessageBox.information(None, QCoreApplication.translate("ctools", "Cancel"),
                                "Generated layer gpx Load incorrect")
    layLoaded = core.QgsVectorLayer('%s?type=waypoint' % (inputGpsFile), gpsLayerName, "gpx")

    if not layLoaded.isValid():
        QMessageBox.information(None, QCoreApplication.translate("ctools", "Cancel"),
                                "Layer gpx Load incorrect")

    crsGK18 = QgsCoordinateReferenceSystem(28418, QgsCoordinateReferenceSystem.EpsgCrsId)
    crsWSG84 = QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId)
    # crsWSG84merc = QgsCoordinateReferenceSystem(3395, QgsCoordinateReferenceSystem.EpsgCrsId)
    xform = QgsCoordinateTransform(crsWSG84, crsGK18, QgsProject.instance())
    #
    # genLProvider = layGenerated.dataProvider()
    # loLProvider = layLoaded.dataProvider()

    loadLFeatures = layLoaded.getFeatures()


    # feat = QgsFeature()
    for lFeat in loadLFeatures:
        minDist = 99999999
        genLFeatures = layGenerated.getFeatures()
        for gFeat in genLFeatures:
            dist = distCoord(gFeat.geometry().asPoint(), lFeat.geometry().asPoint())
            # QMessageBox.information(None, QCoreApplication.translate("ctools", "Cancel"),
            #                          "minDist %s, test" % (str(minDist)))
            if dist<minDist:
                minDist = dist
                # QMessageBox.information(None, QCoreApplication.translate("ctools", "Cancel"),
                #                          "minDist updated %s" % (str(minDist)))
                attrs = gFeat.attributes()
        picketN = int(attrs[0].split(',')[1])
        profileN = int(attrs[0].split(',')[0])
        srcPoint = lFeat.geometry().asPoint()
        # QMessageBox.information(None, QCoreApplication.translate("ctools", "Cancel"), "Source point coord is %s" % (str(srcPoint),))
        destPoint = xform.transform(srcPoint)
        # QMessageBox.information(None, QCoreApplication.translate("ctools", "Cancel"), "dest point is %s" % (str(destPoint)))
        # QMessageBox.information(None, QCoreApplication.translate("ctools", "Cancel"),
        #                         "attributes are %s" % (str(attrs)))
        geometry = QgsGeometry.fromPoint(destPoint)
        cadutils.addGeometryToCadLayer(geometry, profileN, picketN, 0, 0, 0, 0, 0, LayerName)




    else:
        pointsLayer = cadutils.getCadLayerByName(LayerName)

        # core.QgsProject.instance().addMapLayer(layLoaded, True)


