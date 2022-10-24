from .regulargrid import RegularGrid
from PyQt5.QtCore import *


def name():
    return "RegularGrid3"


def description():
    return "this plugin builds regular grid of point by select line and exports it in different formats."


def version():
    return "0.3.10.20200601"


def qgisMinimumVersion():
    return "3.0"


def qgisMaximumVersion():
    return "3.26"


def authorName():
    return "Vladimir Morozov"


def icon():
    return "icons/reggrid.png"


def classFactory(iface):
    return RegularGrid(iface)
