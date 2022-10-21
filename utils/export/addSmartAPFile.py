# -*- coding: utf-8 -*-

def addSmartAPFile(file, smartAPmissionArray):
    file = open(file, 'w')
    for waypoint in smartAPmissionArray:
        for el in waypoint:
            file.write(str(el) + '\t')
        file.write('\n')
    file.close()