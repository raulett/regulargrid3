# Import the PyQt and QGIS libraries
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *

import webbrowser, os
import os.path, sys

# Set up current path.
currentPath = os.path.dirname( __file__ )

#Import tools
from .tools.rectangularpointstool import RectangularPointsTool
from .regulargridaboutgui import CadToolsAboutGui
# from .tools.AMcoordExportTool import ApecMarsCoordExport

from .resources import *

class RegularGrid:

    def __init__(self, iface):
    # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = self.iface.mapCanvas()

        # # Initialise the translation environment.
        userPluginPath = QFileInfo(QgsApplication.qgisUserDatabaseFilePath()).path()+"/python/plugins/regulargrid"
        systemPluginPath = QgsApplication.prefixPath()+"/share/qgis/python/plugins/regulargrid"


    def initGui(self):
        # Add toolbar
        self.toolBar = self.iface.addToolBar("RegularGrid")
        self.toolBar.setObjectName("RegularGrid")

        self.menu = QMenu()
        self.menu.setTitle( QCoreApplication.translate( "RegulrGrid","RegulrGrid" ) )
        self.cadtools_help = QAction( QCoreApplication.translate("RegulrGrid", "Help" ), self.iface.mainWindow() )
        self.cadtools_about = QAction( QCoreApplication.translate("RegulrGrid", "About" ), self.iface.mainWindow() )


        self.menu.addActions([self.cadtools_help, self.cadtools_about])

        menu_bar = self.iface.mainWindow().menuBar()
        actions = menu_bar.actions()
        lastAction = actions[ len( actions ) - 1 ]
        menu_bar.insertMenu( lastAction, self.menu )

        self.cadtools_about.triggered.connect(self.doAbout)
        self.cadtools_help.triggered.connect(self.doHelp)
        # self.cadtools_settings.triggered.connect(self.doSettings)

        # Get the tools
        self.rectangularpoints = RectangularPointsTool(self.iface, self.toolBar)
        # self.AMEexportTool = ApecMarsCoordExport(self.iface, self.toolBar)


    def doAbout(self):
        d = CadToolsAboutGui(self.iface.mainWindow())
        d.show()

    def doHelp(self):
        webbrowser.open(currentPath + "/help/regulargrid_help.html")

    # def doSettings(self):
    #     settings = RegularGridAboutGui(self.iface.mainWindow())
    #     settings.show()

    def unload(self):
        # remove toolbar and menubar
        del self.toolBar
        del self.menu
