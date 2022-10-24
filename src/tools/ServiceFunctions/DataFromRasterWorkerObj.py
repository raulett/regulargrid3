from PyQt5.QtCore import QObject, pyqtSignal

from qgis.core import QgsFeature, QgsRasterLayer, QgsVectorLayer, QgsRaster


class DataFromRasterWorkerObj(QObject):

    signalStatus = pyqtSignal(str)

    def __init__(self,
                 vector_layer: QgsVectorLayer,
                 field_name: str,
                 raster_layer: QgsRasterLayer,
                 raster_band: int):
        super().__init__()
        self.raster_layer = raster_layer
        self.raster_band = raster_band
        self.vector_layer = vector_layer
        self.field_name = field_name

    def update_elevation_data(self):
        data_provider = self.raster_layer.dataProvider()
        self.vector_layer.startEditing()
        for feature in self.vector_layer.getFeatures():
            identify = data_provider.identify(feature.geometry().asPoint(),
                                              QgsRaster.IdentifyFormat.IdentifyFormatValue)
            value = identify.results()
            raster_value = value[self.raster_band]
            feature.setAttribute(feature.fieldNameIndex(self.field_name), raster_value)
            self.vector_layer.updateFeature(feature)
        self.vector_layer.commitChanges()
        return self.vector_layer

