from PyQt5.QtCore import QVariant
from qgis.core import QgsVectorLayer, QgsFields, QgsField, QgsFeature, QgsGeometry


class RegularGridVectorLayer(QgsVectorLayer):
    def __init__(self, layer_name, layer_crs, data_provider='memory'):
        super().__init__('Point', layer_name, data_provider)
        self.layer_data_provider = self.dataProvider()
        self.layer_fields = QgsFields()
        self.layer_fields.append(QgsField('name', QVariant.String))
        self.layer_fields.append(QgsField('profile', QVariant.Int))
        self.layer_fields.append(QgsField('picket', QVariant.Int))
        self.layer_fields.append(QgsField('order_num', QVariant.Int))
        self.layer_fields.append(QgsField('elevation', QVariant.Double))
        self.layer_data_provider.addAttributes(self.layer_fields)
        self.updateFields()
        self.setCrs(layer_crs)

    def add_feature(self, geometry: QgsGeometry, feat_name, profile_num, picket_num, order_num, elevation=None):
        feature = QgsFeature()
        feature.setFields(self.layer_fields)
        feature.setAttribute('name', feat_name)
        feature.setAttribute('profile', profile_num)
        feature.setAttribute('picket', picket_num)
        feature.setAttribute('order_num', order_num)
        if elevation is not None:
            feature.setAttribute('elevation', elevation)
        feature.setGeometry(geometry)
        self.layer_data_provider.addFeature(feature)
        self.commitChanges()
