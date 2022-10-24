from qgis.core import QgsProject


current_layer = iface.mapCanvas().currentLayer()
print(current_layer)
print(current_layer.height())
print('rasterUnitsPerPixelX: ', current_layer.rasterUnitsPerPixelX())
print('rasterUnitsPerPixelY: ', current_layer.rasterUnitsPerPixelY())