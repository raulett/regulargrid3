# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *

def BindElevation(sourceRasterLayer,
                  sourceBandNum,
                  destinationVecLayer,
                  destinationFieldIndex,
                  processOnlyUndef = 0, processOnlySelected = 0):
    # QMessageBox.information(None, "Cancel", u'Вызвана функция BindElevation \n %s \n %s \n %s \n %s' %
    #                         (str(sourceRasterLayer)
    #                         ,str(sourceBandNum)
    #                         ,str(destinationVecLayer)
    #                         ,str(destinationFieldIndex)))
    featIter = destinationVecLayer.getFeatures()
    rasterDataProv = sourceRasterLayer.dataProvider()

    if rasterDataProv.sourceNoDataValue(sourceBandNum):
        noDataValue = rasterDataProv.sourceNoDataValue(sourceBandNum)
    else:
        noDataValue = None
    destinationVecLayer.startEditing()
    for feature in featIter:
        identif = rasterDataProv.identify(feature.geometry().asPoint(), QgsRaster.IdentifyFormatValue)

        val = None
        if identif is not None:
            try:
                val = float(identif.results()[sourceBandNum])
            except TypeError:
                val = None
        if val == noDataValue:
            val = None
        # QMessageBox.information(None, "Cancel", str(val))
        destinationVecLayer.changeAttributeValue(feature.id(), destinationFieldIndex, val)
    destinationVecLayer.commitChanges()



