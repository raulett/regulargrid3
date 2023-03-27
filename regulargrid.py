# Import the PyQt and QGIS libraries
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMenu, QMessageBox

from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

from .src.tools.GetLineTool import GetLineTool
from .src.UI.MakeRegularPoints.MakeRegularPointsHandle import MakeRegularPointsHandle
from .src.UI.BindElevation.BindElevationHandle import BindElevationHandle
from .src.UI.MakeFlights.MakeFlightsHandle import MakeFlightsHandle

import os.path
from .resources import *


# Import tools
# from .src.tools.RectangularPointsTool.rectangularpointstool import RectangularPointsTool
# from .src.UI.regulargridabout_handle import CadToolsAboutGui


class RegularGrid:
    debug = 1

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.elevation_dlg = None
        self.grid_azimuth = None
        self.source_point = None
        self.regulargrid_making_window_handler = None
        self.chosen_layer = None
        self.current_tool = None
        self.toolBar = None
        self.plan_flight_dialog = None
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        self.menu = u'&regulargrid3'
        self.actions = []

    def initGui(self):
        # Add toolbar
        self.toolBar = self.iface.addToolBar("regulargrid3")
        self.toolBar.setObjectName("regulargrid3")

        self.menu = QMenu()
        self.menu.setTitle("regulargrid3")

        self.add_action(
            r':/plugins/regulargrid3/icons/select1line_v2.png',
            text=u'Select segment',
            callback=self.do_segment_selection,
            parent=self.iface.mainWindow())
        self.add_action(
            r':/plugins/regulargrid3/icons/reggrid.png',
            text=u'Regular Grid',
            callback=self.make_regulargrid,
            parent=self.iface.mainWindow())
        self.add_action(
            r':/plugins/regulargrid3/icons/elevation_icon.png',
            text=u'Bind elevation',
            callback=self.set_elevation,
            parent=self.iface.mainWindow())
        self.add_action(
            r':/plugins/regulargrid3/icons/DFM.png',
            text=u'Make flight mission',
            callback=self.make_drone_flight_mission,
            parent=self.iface.mainWindow())

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                u'&regulargrid3',
                action)
            self.iface.removeToolBarIcon(action)

    def add_action(
            self,
            icon_path,
            text,
            callback,
            enabled_flag=True,
            add_to_menu=True,
            add_to_toolbar=True,
            status_tip=None,
            whats_this=None,
            parent=None):
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu.title(),
                action)

        self.actions.append(action)

        return action

    # TODO call select segment
    def do_segment_selection(self):
        self.canvas = self.iface.mapCanvas()
        current_layer = self.canvas.currentLayer()

        self.current_tool = GetLineTool(self.canvas, current_layer)
        # connect signals
        self.current_tool.decline_signal.connect(self.unset_map_tool)
        self.current_tool.line_found_signl.connect(self.got_baseline)

        self.canvas.setMapTool(self.current_tool)

    # TODO call generating regulargrid window
    def make_regulargrid(self):
        if self.debug:
            print('regulargrid, call make regulargrid')
        if (self.chosen_layer is None) or (self.source_point is None) or (self.grid_azimuth is None):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('No segment chosen')
            msg.setWindowTitle('No segment chosen')
            msg.exec()
        else:
            if not isinstance(self.regulargrid_making_window_handler, MakeRegularPointsHandle):
                self.unset_map_tool()
                self.regulargrid_making_window_handler = MakeRegularPointsHandle(self.chosen_layer,
                                                                                 self.source_point,
                                                                                 self.grid_azimuth)
                self.current_tool.line_found_signl.connect(self.regulargrid_making_window_handler.got_new_data_slt)
                self.current_tool.decline_signal.connect(self.regulargrid_making_window_handler.showNormal)
                self.regulargrid_making_window_handler.get_map_tool_sgnl.connect(self.set_map_tool)
            else:
                self.regulargrid_making_window_handler.renew_layer_data(self.chosen_layer,
                                                                        self.source_point,
                                                                        self.grid_azimuth)
            self.regulargrid_making_window_handler.show()

    # TODO make set elevation window call
    def set_elevation(self):
        if not isinstance(self.elevation_dlg, BindElevationHandle):
            self.elevation_dlg = BindElevationHandle()
        else:
            self.elevation_dlg.init_gui()
        self.elevation_dlg.show()

    # TODO make drone flight mission window call
    def make_drone_flight_mission(self):
        if not isinstance(self.plan_flight_dialog, MakeFlightsHandle):
            self.plan_flight_dialog = MakeFlightsHandle()
        else:
            self.plan_flight_dialog.init_gui()
        self.plan_flight_dialog.show()

    def unset_map_tool(self):
        self.canvas.unsetMapTool(self.current_tool)

    def set_map_tool(self):
        self.canvas.setMapTool(self.current_tool)

    def got_baseline(self, line_data):
        if self.debug:
            print("Got line data tuple", line_data)
        self.chosen_layer = line_data[0]
        self.source_point = line_data[1]
        self.grid_azimuth = line_data[2]
