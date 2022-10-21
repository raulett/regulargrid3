# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *

import re

#Функция отбирающая слои на карте, соответствующие определенным признакам (тип слоя, и перечень полей)
#На вход функции подается canvas,
# тип геометрии, с которыми отбираются слои (geometryType) 0 - точки, 1 - линии, 2 - полигоны:
# fieldsString Строка вида "Имя поля|Имя поля2|Имя поля3|итд..."
# fieldsNumber число имен полей, которые должны совпадать со строкой fieldsString
def getLayersByType(canvas, geometryType):
    layers = canvas.layers()
    layersList = []

    for layer in layers:
        if ((type(layer) == QgsVectorLayer) and (layer.geometryType() == geometryType)) :
            layersList.append(layer)
    # QMessageBox.information(None, "Cancel", str(layersList))
    return layersList