from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog

from .MakeRegularPoints_ui import Ui_RegularPointsDialog
from ...tools.MakeRegularPointsCore import MakeRegularPointsCore

from qgis.core import QgsMapLayer, QgsVectorLayer


class MakeRegularPointsHandle(Ui_RegularPointsDialog, QDialog):
    debug = 0
    get_map_tool_sgnl = pyqtSignal()

    def __init__(self, line_layer: QgsMapLayer, source_point, azimuth):
        super().__init__()
        self.reggrid_azimuth = azimuth
        self.source_point = source_point
        self.got_layer = line_layer
        self.current_layer_crs = None
        self.setupUi(self)

        self.btnCancel.clicked.connect(self.hide)
        self.pushButton.clicked.connect(self.get_new_sourseline_btn)
        self.btnAdd.clicked.connect(self.add_layer_btn)
        self.init_gui()

    def init_gui(self):
        if isinstance(self.got_layer, QgsMapLayer):
            self.current_layer_crs = self.got_layer.crs()
            self.layer_name_label.setText('{} ({})'.format(self.got_layer.name(),
                                                           self.current_layer_crs.authid()))
            if self.debug:
                print('chosen baseline layer crs:', self.current_layer_crs.authid())
                print('current layer:', self.got_layer, type(self.got_layer), isinstance(self.got_layer, QgsMapLayer))

    def got_new_data_slt(self, line_data):
        if isinstance(line_data[0], QgsMapLayer):
            self.got_layer = line_data[0]
            self.source_point = line_data[1]
            self.reggrid_azimuth = line_data[2]

    def renew_layer_data(self, line_layer: QgsMapLayer, source_point, azimuth):
        self.got_layer = line_layer
        self.source_point = source_point
        self.reggrid_azimuth = azimuth
        self.init_gui()

    def init_warning_icon(self):
        if not ((r'units=m' in self.current_layer_crs.toProj()) |
                self.got_layer.type() != 0 |
                self.got_layer.geometryType() >= 1):
            self.warning_icon_label.setPixmap(QPixmap(r":/plugins/regulargrid3/icons/warning.png"))
            self.warning_icon_label.setToolTip('Incorrect line layer type or CRS')
        else:
            self.warning_icon_label.setPixmap(QPixmap())
            self.warning_icon_label.setToolTip('')

    def get_new_sourseline_btn(self):
        self.showMinimized()
        self.get_map_tool_sgnl.emit()

    def add_layer_btn(self):
        make_regular_points = MakeRegularPointsCore(self.lineEdit.text(),
                                                    int(self.firstPK.value()),
                                                    self.pkNum.value(),
                                                    self.dX.value(),
                                                    int(self.firstPR.value()),
                                                    self.proNum.value(),
                                                    self.dY.value(),
                                                    self.source_point,
                                                    self.reggrid_azimuth,
                                                    self.got_layer.crs())
        make_regular_points.generate_points()
        make_regular_points.add_layer_to_canvas()
        self.hide()


