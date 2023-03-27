from .BindElevation_ui import Ui_bindElevationDialog
from ...tools.ServiceFunctions.LayersHandling import get_layers_list
from ...tools.ServiceFunctions.resolve import resolve
from ...tools.SpatialData.DataFromRasterWorkerObj import DataFromRasterWorkerObj

from qgis.core import QgsProject, QgsRasterLayer, QgsVectorLayer, QgsWkbTypes

from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap


class BindElevationHandle(Ui_bindElevationDialog, QDialog):
    debug = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.cancel_btn)
        self.rasterLayer.currentIndexChanged.connect(self.update_raster_band_combobox)
        self.vectorLayer.currentIndexChanged.connect(self.update_layer_fields_cmbox)
        self.vectorLayer.currentIndexChanged.connect(self.check_layers_crs)
        self.rasterLayer.currentIndexChanged.connect(self.check_layers_crs)
        self.layers_tree = QgsProject.instance().layerTreeRoot()
        self.layers_tree.visibilityChanged.connect(self.init_gui)
        self.layers_tree.addedChildren.connect(self.init_gui)
        self.layers_tree.removedChildren.connect(self.init_gui)
        self.bindElevationButton.clicked.connect(self.bind_elevation_btn)
        self.init_gui()

    def init_gui(self):
        self.rasterLayer.clear()
        self.rasterBand.clear()
        self.vectorLayer.clear()
        self.destinationField.clear()
        points_vector_layers = get_layers_list(QgsVectorLayer,
                                               vector_layer_type=QgsWkbTypes.GeometryType.PointGeometry)
        raster_layers = get_layers_list(QgsRasterLayer)
        for raster_layer in raster_layers:
            self.rasterLayer.addItem(raster_layer.name(), raster_layer)
        for vector_layer in points_vector_layers:
            self.vectorLayer.addItem(vector_layer.name(), vector_layer)

    def bind_elevation_btn(self):
        bind_elevation_worker = DataFromRasterWorkerObj(self.vectorLayer.currentData(),
                                                        self.destinationField.currentText(),
                                                        self.rasterLayer.currentData(),
                                                        self.rasterBand.currentData())
        result_layer = bind_elevation_worker.update_elevation_data()
        self.close()

    def cancel_btn(self):
        self.close()

    def update_raster_band_combobox(self):
        if self.debug:
            print('update band_combobox')
        self.rasterBand.clear()
        if isinstance(self.rasterLayer.currentData(), QgsRasterLayer):
            current_raster_layer = self.rasterLayer.currentData()
            band_count = current_raster_layer.bandCount()
            if self.debug:
                print('update band_combobox, band count', band_count)
            for i in range(band_count):
                self.rasterBand.addItem(str(i+1), i+1)

    def update_layer_fields_cmbox(self):
        if self.debug:
            print('update fields combobox')
        self.destinationField.clear()
        current_vector_layer = self.vectorLayer.currentData()
        if isinstance(current_vector_layer, QgsVectorLayer):
            for name in current_vector_layer.fields().names():
                self.destinationField.addItem(name)
            self.destinationField.setCurrentIndex(self.destinationField.findText('elevation'))


    def check_layers_crs(self):
        vector_layer = QgsProject.instance().mapLayersByName(self.vectorLayer.currentText())
        if self.debug:
            print('check vector layer crs',
                  vector_layer[0].crs().authid() if len(vector_layer) > 0 else 'No layer')
        raster_layer = QgsProject.instance().mapLayersByName(self.rasterLayer.currentText())
        if self.debug:
            print('check raster layer crs',
                  raster_layer[0].crs().authid() if len(raster_layer) > 0 else 'No layer')
        if (vector_layer[0].crs().authid() != raster_layer[0].crs().authid() if len(vector_layer) > 0 and len(
                raster_layer) > 0 else False):
            if self.debug:
                print('pixmap test', resolve('warning.png'))
            self.warning_icon_label.setPixmap(QPixmap(r':/plugins/regulargrid3/icons/warning.png'))
            self.warning_icon_label.setToolTip('Layers crs aren`t the same')
            self.warning_label.setText('{} crs is {}, {} crs is {}'.format(vector_layer[0].name(),
                                                                           vector_layer[0].crs().authid(),
                                                                           raster_layer[0].name(),
                                                                           raster_layer[0].crs().authid()))
        else:
            if self.debug:
                print('crs are the same')
            self.warning_icon_label.setPixmap(QPixmap())
            self.warning_icon_label.setToolTip('')
            self.warning_label.setText('')
