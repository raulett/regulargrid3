# -*- coding: utf-8 -*-
from qgis.core import *

# Модуль предоставляет средства для афинного пересчета координат из одной прямоугольной системы координат в другую.
# В данном варианте реализуется только 2 преобразорвания: Перенос и поворот.
# Module provides tools for affine conversion of coordinates from one rectangular coordinate system to another.
# This option is implemented only 2 transformation: translation and rotation.

class AffineTransform:
    # функця преобразует координаты точки sourcePoint из ортонормированной системы координат, заданной осью Х
    # sourceAxisX, в повернутою и сдвинутую относительно нее ортонормированную систему координат,
    # заданную осью Х targetAxisX. Ось задается кортежем из 2х точек, точка задается кортежем из 2х значений double
    # function converts the coordinates of a point 'sourcePoint' of the orthonormal coordinate system defined by the X-axis
    # 'sourceAxisX', rotated and shifted relative to it an orthonormal coordinate system
    # example:  sourceAxisX = ((0,0),(1,0))



    def __init__(self, OYn1, OYn2):
        self.newOYaxis = QgsPointXY()
        self.newOYaxis.setX(OYn2.x()-OYn1.x())
        self.newOYaxis.setY(OYn2.y()-OYn1.y())
        # ShiftVec = QgsPointXY()
        self.ShiftVec = OYn1

        OYnLenght = ((self.newOYaxis.x()**2 + self.newOYaxis.y()**2)**0.5)
        self.SinAngle = self.newOYaxis.x()/OYnLenght
        self.CosAngle = self.newOYaxis.y()/OYnLenght

        self.oldBasis1 = self.transform(QgsPointXY(0,0))
        self.oldBasis2 = self.transform(QgsPointXY(0,1))



    # example:  sourceAxisX = ((0,0),(1,0))
    def shift(self, Point):
        resPoint = QgsPointXY()
        resPoint.setX(Point.x()-self.ShiftVec.x())
        resPoint.setY(Point.y() - self.ShiftVec.y())
        return resPoint

    # Функция пересчитывает координаты точки PointN в новую систему координат. Новая система получается поворотом
    # старой системы координат на угол F, который высчитывается между осью OY(0,1) и осью OYn, заданной точкками (0,0)
    # и точкой OYn. Все точки задаются типом QgsPointXY
    # Функция получает на вход 1 точку на оси OX
    def rotate(self, PointN):
        Xst = PointN.x()*self.CosAngle - PointN.y()*self.SinAngle
        Yst = PointN.x()*self.SinAngle + PointN.y()*self.CosAngle
        PointNew = QgsPointXY()
        PointNew.setX(Xst)
        PointNew.setY(Yst)
        return PointNew

    # Функция последовательно проводит для точки операции сдвига, а затем поворота из старой системы OXY в новую,
    # заданную осью OYn
    def transform(self, sourcePoint):
        return self.rotate(self.shift(sourcePoint))

    def revert(self, pointNew):
        revertTransformation = AffineTransform(self.oldBasis1, self.oldBasis2)
        return revertTransformation.transform(pointNew)


