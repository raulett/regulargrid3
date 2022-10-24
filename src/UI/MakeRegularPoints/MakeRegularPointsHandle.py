from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QDialog

from .MakeRegularPoints_ui import Ui_RegularPointsDialog

from qgis.core import QgsMapLayer, QgsVectorLayer


class MakeRegularPointsHandle(Ui_RegularPointsDialog, QDialog):
    debug = 0
    get_map_tool_sgnl = pyqtSignal()

    def __init__(self, line_layer: QgsMapLayer, source_point, azimuth):
        super().__init__()
        self.current_layer_crs = None
        self.setupUi(self)
        self.got_layer = line_layer
        self.source_point = source_point
        self.reggrid_azimuth = azimuth

        self.btnCancel.clicked.connect(self.hide)
        self.init_gui()

    def init_gui(self):
        self.current_layer_crs = self.got_layer.crs()
        self.layer_name_label.setText('{} ({})'.format(self.got_layer.name(),
                                                             self.current_layer_crs.authid()))
        if self.debug:
            print('chosen baseline layer crs:', self.current_layer_crs.authid())

    def got_new_data_slt(self):
        pass
