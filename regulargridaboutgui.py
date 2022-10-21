# -*- coding: latin1 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *
from .ui_regulargridabout import Ui_CadToolsAbout
import webbrowser, os

currentPath = os.path.dirname(__file__)

class CadToolsAboutGui(QDialog, QObject, Ui_CadToolsAbout):
    def __init__(self, iface):
        QDialog.__init__(self, iface)
        self.iface = iface
        self.setupUi(self)
        self.btnWeb.clicked.connect(self.openWeb)
        self.btnHelp.clicked.connect(self.openHelp)
        self.lblVersion.setText("Regular Grid 0.3.10.20200601")
        self.txtAbout.setText(self.getText())    
    
    def openWeb(self):
        webbrowser.open("")


    def openHelp(self):
        webbrowser.open(currentPath + "/help/regulargrid_help.html")
        
    def getText(self):
        return self.tr(""" 
RegularGrid plugin builds regular grid of points by selected segment.

There is some code adopted from CadTools plugin (Stefan ZIegler, edi.gonzales@gmail.com) and the Python console. Thank you!

LICENSING INFORMATION:
RegularGrid is developed by Vladimir Morozov(raulett@gmail.com)

Licensed under the terms of GNU GPL 2
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
""")

