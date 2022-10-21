# -*- coding: utf-8 -*-

def addMissionPlannerFile(file,MissionPlannerArray):

    file = open(file[0], 'w')
    file.write("QGC WPL 110\n")
    for waypoint in MissionPlannerArray:
        for el in waypoint:
            file.write(str(el) + '\t')
        file.write('\n')
    file.close()