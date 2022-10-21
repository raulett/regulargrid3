class GeneratorLine:
    def __init__(self, id, i, X1, Y1, X2, Y2):
        self.ID = id
        self.I = i
        self.X1 = X1
        self.Y1 = Y1
        self.X2 = X2
        self.Y2 = Y2

class Picket:
    def __init__(self, genLine, pr, pk, x, y, elev = 0):
        self.GenLine = genLine
        self.PR = pr
        self.PK = pk
        self.X = x
        self.Y = y
        self.ELEV = elev
