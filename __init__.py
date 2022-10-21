from .regulargrid import RegularGrid
from PyQt5.QtCore import *


def name():
    return "RegularGrid"


def description():
    return "this plugin builds regular grid of point by select line and exports it in different formats."


def version():
    return "0.3.10.20200601"


def qgisMinimumVersion():
    return "3.0"


def qgisMaximumVersion():
    return "3.10"


def authorName():
    return "Vladimir Morozov"


def icon():
    return "icons/orthopoint.png"


def classFactory(iface):
    return RegularGrid(iface)
