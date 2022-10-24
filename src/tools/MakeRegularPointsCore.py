from .SpatialData.RegularGridVectorLayer import RegularGridVectorLayer
from qgis.core import QgsGeometry, QgsPointXY, QgsFeature, QgsProject

class MakeRegularPointsCore:
    def __init__(self, layer_name,
                 first_pk_num, pk_num, pk_shift,
                 first_pr_num, pr_num, pr_shift,
                 rotating_point: QgsPointXY, azimuth,
                 layer_crs):
        self.layer = RegularGridVectorLayer(layer_name, layer_crs)
        # layer_fields = layer.fields()
        self.first_pk_num = first_pk_num
        self.pk_num = pk_num
        self.pk_shift = pk_shift
        self.first_pr_num = first_pr_num
        self.pr_num = pr_num
        self.pr_shift = pr_shift
        self.rotating_point = rotating_point
        self.azimuth = azimuth

    def generate_points(self):
        for pr_n in range(self.pr_num):
            for pk_n in range(self.pk_num):
                x_coord = pr_n * self.pr_shift
                y_coord = pk_n * self.pk_shift
                point_number = ((pr_n * self.pk_num + pk_n) + 1) * ((pr_n + 1) % 2) + \
                               (pr_n % 2) * ((pr_n + 1) * self.pk_num - pk_n)
                geom = QgsGeometry.fromPointXY(QgsPointXY(x_coord + self.rotating_point.x(),
                                                          y_coord + self.rotating_point.y()))
                geom.rotate(self.azimuth, self.rotating_point)
                feat = QgsFeature()
                feat.setGeometry(geom)
                feat.setFields(self.layer.fields())
                feat.setAttribute('name', '{}, {}'.format(pr_n + self.first_pr_num, pk_n + self.first_pk_num))
                feat.setAttribute('profile', pr_n + self.first_pr_num)
                feat.setAttribute('picket', pk_n + self.first_pk_num)
                feat.setAttribute('order_num', point_number)
                feat.setAttribute('elevation', 0)
                self.layer.dataProvider().addFeature(feat)
        self.layer.commitChanges()
        self.layer.updateExtents()

    def add_layer_to_canvas(self):
        QgsProject.instance().addMapLayer(self.layer)
        return self.layer



