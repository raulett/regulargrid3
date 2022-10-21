# Import the PyQt and QGIS libraries
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *

import webbrowser, os
import os.path, sys

# Set up current path.
currentPath = os.path.dirname( __file__ )

# Initialize Qt resources from file resources.py
from regulargrid import resources


#Import tools
from .AMEexportDialogGui import ExportDialogGui
from .AMEimportDialogGui import ImportDialogGui

class ApecMarsCoordExport:

    def __init__(self, iface, toolBar):
    # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = self.iface.mapCanvas()


        # Add actions
        self.act_export = QAction(QIcon(":/plugins/regulargrid/icons/exportpoints.png"),
                                  "Export Points from Layer to Apec Mars format",
                                  self.iface.mainWindow())
        self.act_import = QAction(QIcon(":/plugins/regulargrid/icons/importpoints.png"),
                                  "Import Points from Apec Mars format",
                                  self.iface.mainWindow())

        # Add Actions to the toolbar
        toolBar.addSeparator()
        toolBar.addAction(self.act_export)
        toolBar.addAction(self.act_import)

        self.act_export.triggered.connect(self.ShowMarsExportDialog)
        self.act_import.triggered.connect(self.ShowMarsImportDialog)

    def ShowMarsExportDialog(self):
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint
        self.ctrl = ExportDialogGui(self.iface.mainWindow(), flags)
        self.ctrl.initGui(self.canvas)
        self.ctrl.show()

    def ShowMarsImportDialog(self):
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint
        self.ctrl = ImportDialogGui(self.iface.mainWindow(), flags)
        self.ctrl.initGui(self.canvas)
        self.ctrl.show()


    def unload(self):
        # remove toolbar and menubar
        del self.toolBar
        del self.menu
