import os

from .MakeFlights_ui import Ui_makeRegularFlightForm
from PyQt5.QtWidgets import QDialog

from ...tools.ServiceFunctions.LayersHandling import get_layers_list
from ...tools.WAYPOINT_TYPES import WAYPOINT_TYPES

from qgis.core import QgsVectorLayer, QgsWkbTypes, QgsProject, QgsCoordinateReferenceSystem, \
    QgsCoordinateTransform

from PyQt5.QtWidgets import QMessageBox


class MakeFlightsHandle(Ui_makeRegularFlightForm, QDialog):
    debug = 1

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.layers_tree = QgsProject.instance().layerTreeRoot()
        self.layers_tree.visibilityChanged.connect(self.init_gui)
        self.layers_tree.addedChildren.connect(self.init_gui)
        self.layers_tree.removedChildren.connect(self.init_gui)
        self.bindElevationButton.clicked.connect(self.genarate_flight_button_clicked)
        self.cancel_pushButton.clicked.connect(self.cancel_button_handle)
        self.survey_speed_checkBox.stateChanged.connect(self.speed_checkbox_changed)

    def init_gui(self):
        reg_grid_points_layers = get_layers_list(QgsVectorLayer,
                                                 vector_layer_type=QgsWkbTypes.GeometryType.PointGeometry,
                                                 field_names=['order_num', 'elevation'])
        self.regular_points_layer.clear()
        for reggrid_layer in reg_grid_points_layers:
            self.regular_points_layer.addItem(reggrid_layer.name(), reggrid_layer)

    def genarate_flight_button_clicked(self):
        to_alt = self.to_alt_doubleSpinBox.value()
        f_alt = self.f_alt_doubleSpinBox.value()
        f_points = self.generate_flight(to_alt, f_alt)
        generated_str_waypoints = self.generate_waypoint_file(f_points)
        if self.debug:
            print(generated_str_waypoints)
        output_file = self.save_generated_waypoints(generated_str_waypoints, self.regular_points_layer.currentData().name())
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Flight plan created in {output_file}")
        msg.setWindowTitle("Flight plan created")
        msg.exec_()

    def generate_flight(self, to_point_alt, flight_alt):
        reg_points_layer = self.regular_points_layer.currentData()
        if self.debug:
            print(f'current layer type: {type(reg_points_layer)}')
        flight_points = []
        sourceCrs = QgsCoordinateReferenceSystem(reg_points_layer.sourceCrs())
        destCrs = QgsCoordinateReferenceSystem(4326)
        coord_tr = QgsCoordinateTransform(sourceCrs, destCrs, QgsProject.instance())
        for feat in reg_points_layer.getFeatures():
            point = {}
            if self.debug:
                print(f'feature number: {feat.attribute("order_num")}')
            point['order_num'] = feat.attribute("order_num")
            geometry = feat.geometry()
            geometry.transform(coord_tr)
            point['LON'] = geometry.asPoint().x()
            point['LAT'] = geometry.asPoint().y()
            point['ALT'] = feat.attribute("elevation") - to_point_alt + flight_alt
            flight_points.append(point)
        flight_points = sorted(flight_points, key=lambda feature: feature.get('order_num'))
        if self.debug:
            print(f'features list:\n {flight_points}')
        return flight_points

    def generate_waypoint_file(self, flight_points):
        if self.survey_speed_checkBox.isChecked():
            surv_speed = self.survey_speed_doubleSpinBox.value()
            after_surv_speed = self.after_survey_speed_doubleSpinBox.value()
            change_speed_set_flag = 0
        else:
            surv_speed = 0.0
            after_surv_speed = 0.0
            change_speed_set_flag = 2
        flight_waypoints_file = "QGC WPL 110\n"
        point_number = 0
        point_str = f'{point_number}\t1\t3\t{WAYPOINT_TYPES["WAYPOINT"]}\t0.0\t0.0\t0.0\t0.0\t' \
                    f'{flight_points[0].get("LAT")}\t{flight_points[0].get("LON")}\t{flight_points[0].get("ALT")}\t1\n'
        flight_waypoints_file += point_str
        point_number += 1
        for f_point in flight_points:
            point_str = f'{point_number}\t0\t3\t{WAYPOINT_TYPES["WAYPOINT"]}\t0.0\t0.0\t0.0\t0.0\t' \
                        f'{f_point.get("LAT")}\t{f_point.get("LON")}\t{f_point.get("ALT")}\t1\n'
            flight_waypoints_file += point_str
            point_number += 1
            if change_speed_set_flag == 0:
                point_str = f'{point_number}\t0\t3\t{WAYPOINT_TYPES["DO_CHANGE_SPEED"]}\t0.0\t{surv_speed}\t0.0\t0.0\t' \
                            f'{f_point.get("LAT")}\t{f_point.get("LON")}\t{f_point.get("ALT")}\t1\n'
                flight_waypoints_file += point_str
                change_speed_set_flag = 1
                point_number += 1
        if change_speed_set_flag == 1:
            point_str = f'{point_number}\t0\t3\t{WAYPOINT_TYPES["DO_CHANGE_SPEED"]}\t0.0\t{after_surv_speed}\t0.0\t0.0\t' \
                        f'{0.0}\t{0.0}\t{0.0}\t1\n'
            flight_waypoints_file += point_str
            point_number += 1
            change_speed_set_flag = 2
        point_str = f'{point_number}\t0\t3\t{WAYPOINT_TYPES["RETURN_TO_LAUNCH"]}\t0.0\t{0.0}\t0.0\t0.0\t' \
                    f'{0.0}\t{0.0}\t{0.0}\t1\n'
        flight_waypoints_file += point_str
        point_number += 1
        return flight_waypoints_file

    def save_generated_waypoints(self, generated_str_waypoints, name):
        current_poject_path = os.sep.join(QgsProject.instance().homePath().split('/'))
        current_waypoints_path = os.sep.join([current_poject_path, 'flights', 'wp'])
        if not os.path.exists(current_waypoints_path):
            os.makedirs(current_waypoints_path)

        current_file_name = f'{name}.waypoints'
        if self.debug:
            print(f'file: {os.sep.join([current_waypoints_path, current_file_name])} exists: ', os.path.exists(os.sep.join([current_waypoints_path, current_file_name])))
        counter = 0
        while os.path.exists(os.sep.join([current_waypoints_path, current_file_name])):
            counter += 1
            current_file_name = f'{name}_{str(counter)}.waypoints'

        with open(os.sep.join([current_waypoints_path, current_file_name]), 'w') as file:
            file.write(generated_str_waypoints)
        return os.sep.join([current_waypoints_path, current_file_name])


    def cancel_button_handle(self):
        self.close()

    def speed_checkbox_changed(self):
        if self.survey_speed_checkBox.isChecked():
            self.survey_speed_doubleSpinBox.setEnabled(True)
            self.after_survey_speed_doubleSpinBox.setEnabled(True)
        else:
            self.survey_speed_doubleSpinBox.setEnabled(False)
            self.after_survey_speed_doubleSpinBox.setEnabled(False)




