# -*- coding: utf-8 -*-
from .GeneratorLine import *
from PyQt5.QtGui import *

class CoordBind:
    COORD_EPSILON = 0.01
    def __init__(self):
        self.GenLines = []
        self.Pickets = list([])

    def addLine(self, X1, Y1, X2, Y2, I = 0):
        # QMessageBox.information(None, "Cancel", str(len(self.GenLines)))
        if len(self.GenLines) == 0:
            self.GenLines.append(GeneratorLine(1, I, X1, Y1, X2, Y2))
            #QMessageBox.information(None, "Cancel", str(self.GenLines))
            return 1
        else:
            equalCount = 0
            for genLine in self.GenLines:
                # QMessageBox.information(None, "Cancel", u"Отладочный вызов: " +
                #                         '\n(abs(genLine.X1 - X1) < self.COORD_EPSILON): ' + str((abs(genLine.X1 - X1) < self.COORD_EPSILON)) +
                #                         '\n(abs(genLine.Y1 - Y1) < self.COORD_EPSILON): ' + str(abs(genLine.Y1 - Y1) < self.COORD_EPSILON) +
                #                         '\n(abs(genLine.X2 - X2) < self.COORD_EPSILON): ' + str(abs(genLine.X2 - X2) < self.COORD_EPSILON) +
                #                         '\n(abs(genLine.Y2 - Y2) < self.COORD_EPSILON): ' + str(abs(genLine.Y2 - Y2) < self.COORD_EPSILON) +
                #                         '\ngenLine.X1 = ' + str(genLine.X1) + ', X1 = ' + str(X1) +
                #                         '\n(abs(genLine.X1 - X1): ' + str(abs(genLine.X1 - X1)) +
                #                         '\n(abs(genLine.Y1 - Y1): ' + str(abs(genLine.Y1 - Y1)) +
                #                         '\n(abs(genLine.X2 - X2): ' + str(abs(genLine.X2 - X2)) +
                #                         '\n(abs(genLine.Y2 - Y2): ' + str(abs(genLine.Y2 - Y2)))
                if (abs(genLine.X1 - X1) < self.COORD_EPSILON) and (abs(genLine.Y1 - Y1) < self.COORD_EPSILON) and (abs(genLine.X2 - X2) < self.COORD_EPSILON) and (abs(genLine.Y2 - Y2) < self.COORD_EPSILON):
                    genLineN = genLine.ID
                    # QMessageBox.information(None, "Cancel",str(self.GenLines))
                    equalCount += 1
                    break
                # else:
                #     self.GenLines.append(GeneratorLine(len(self.GenLines)+1, I, X1, Y1, X2, Y2))
                #     QMessageBox.information(None, "Cancel", str(self.GenLines))
                #     return len(self.GenLines)
            if equalCount == 0:
                self.GenLines.append(GeneratorLine(len(self.GenLines) + 1, I, X1, Y1, X2, Y2))
                return len(self.GenLines)
            # QMessageBox.information(None, "Cancel", str(self.GenLines))
            return genLineN

    def addPicket(self, pr, pk, x, y, X1, Y1, X2, Y2, elev = 0):
        # QMessageBox.information(None, "Cancel", u"Профиль: " + str(pr) +
        #                         u"\nПикет: " + str(pk) +
        #                         u"\nГенераторная линия: " + str([X1, Y1, X2, Y2])
        #                         )
        genLineN = self.addLine(X1, Y1, X2, Y2)
        # QMessageBox.information(None, "Cancel", u'Линия номер: ' + str(genLineN))
        self.Pickets.append(Picket(genLineN, pr, pk, x, y))
        # QMessageBox.information(None, "Cancel", str(self.Pickets))
