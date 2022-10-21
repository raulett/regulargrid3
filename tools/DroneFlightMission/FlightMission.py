# from xml.etree import ElementTree as etree
from lxml import etree
from lxml import objectify

from PyQt5.QtGui import *
import os

# PROCESSOR_ARCHITECTURE = os.environ.get('PROCESSOR_ARCHITECTURE')
# if PROCESSOR_ARCHITECTURE == 'AMD64':
#     from lib.lxml.lxml64.lxml import etree
#     from lib.lxml.lxml64.lxml import objectify
# else:
#     from lib.lxml.lxml32.lxml import etree
#     from lib.lxml.lxml32.lxml import objectify

class FlightMission:
    def __init__(self, MissionTimeLmt = 65535,
                 IsPatrol = 'Start_To_End',
                 StartWayPointIndex = 0,
                 VerticalSpeedLimit = 2):

        self.MissionTimeLmt = MissionTimeLmt
        self.IsPatrol = IsPatrol
        self.StartWayPointIndex = StartWayPointIndex
        self.VerticalSpeedLimit = VerticalSpeedLimit
        self.WayPoints = {}
        self.check = False


    def addWaypoint(self, ID, Lat, Lon, Alt, elev, spd = 5, TM  = 'Adaptive_Bank_Turn', YawDegree = 360, HoldTime = 0,
                 StartDelay = 0, Period = 0, RepeatTime = 0, RepeatDistance = 0, TimeLimit = 65535):
        self.WayPoints[ID] = WayPoint(Lat, Lon, Alt, elev, spd, TM, YawDegree, HoldTime,
                 StartDelay, Period, RepeatTime, RepeatDistance, TimeLimit)

    def serializeAWM(self, fileName):

        if self.check:
            delimiter = ','
        else:
            delimiter = '.'
        root = etree.Element('Mission', MissionTimeLmt = str(self.MissionTimeLmt),
                                         IsPatrol = str(self.IsPatrol),
                                         StartWayPointIndex = str(self.StartWayPointIndex),
                                         VerticalSpeedLimit = str(self.VerticalSpeedLimit).replace('.', delimiter))
        for key in self.WayPoints.keys():

            wp = etree.SubElement(root, 'WayPoint', {'id': str(key)})
            etree.SubElement(wp, 'Latitude').text = str(self.WayPoints[key].Latitude).replace('.', delimiter)
            etree.SubElement(wp, 'Longitude').text = str(self.WayPoints[key].Longitude).replace('.', delimiter)
            etree.SubElement(wp, 'Altitude').text = str(self.WayPoints[key].Altitude).replace('.', delimiter)
            etree.SubElement(wp, 'Speed').text = str(self.WayPoints[key].Speed).replace('.', delimiter)
            etree.SubElement(wp, 'TimeLimit').text = str(self.WayPoints[key].TimeLimit)
            etree.SubElement(wp, 'YawDegree').text = str(self.WayPoints[key].YawDegree)
            etree.SubElement(wp, 'HoldTime').text = str(self.WayPoints[key].HoldTime)
            etree.SubElement(wp, 'StartDelay').text = str(self.WayPoints[key].StartDelay)
            etree.SubElement(wp, 'Period').text = str(self.WayPoints[key].Period)
            etree.SubElement(wp, 'RepeatTime').text = str(self.WayPoints[key].RepeatTime)
            etree.SubElement(wp, 'RepeatDistance').text = str(self.WayPoints[key].RepeatDistance)
            etree.SubElement(wp, 'TurnMode').text = str(self.WayPoints[key].TurnMode)


        tree = etree.tounicode(root, pretty_print=True)
        file = open(fileName, 'w')
        file.writelines(tree)
        file.close()

    # Create array of tuples (int Number, int Attribute, double Lon, double Lat, double Alt, int Head, double Velocity,
    # int Delay, bool WPTask) to add to SQLite DB
    # i dont know what mean some fields (Attribute, Head, WPTask) and leave valuye by default.
    def createTopXGunArray(self):
        missionArray = []
        for key in self.WayPoints.keys():
            wayPoint = (int(key), 16, self.WayPoints[key].Longitude, self.WayPoints[key].Latitude,
                             self.WayPoints[key].Altitude, 0, self.WayPoints[key].Speed, self.WayPoints[key].HoldTime,0)
            missionArray.append(wayPoint)
        return missionArray

    def createSmartAPArray(self):
        missionArray = []
        for key in self.WayPoints.keys():
            wayPoint = (int(key), 0, 0, 1, self.WayPoints[key].HoldTime, 1, self.WayPoints[key].Speed,
                        self.WayPoints[key].YawDegree, self.WayPoints[key].Latitude, self.WayPoints[key].Longitude,
                        self.WayPoints[key].Altitude, 1)
            missionArray.append(wayPoint)
        return missionArray

    def createMissionPlanner(self):
        missionArray = []
        wp = 16
        returnToLand = 20
        key = 0
        wayPoint = (0, 1, 0, wp, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1)
        missionArray.append(wayPoint)
        for key in self.WayPoints.keys():
            wayPoint = (int(key), 0, 3, wp, 0.0, 0.0, 0.0, 0.0, self.WayPoints[key].Latitude, self.WayPoints[key].Longitude,
                        self.WayPoints[key].Altitude, 1)
            missionArray.append(wayPoint)
        wayPoint = (len(self.WayPoints.keys()), 0, 3, returnToLand, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1)
        missionArray.append(wayPoint)
        return missionArray


    def loadFromAWM(self, fileName):
        file = open(fileName, 'r')
        xml = file.read()
        Mission = objectify.fromstring(xml)
        self.IsPatrol = Mission.get('IsPatrol')
        self.MissionTimeLmt = int(Mission.get('MissionTimeLmt'))
        self.StartWayPointIndex = int(Mission.get('StartWayPointIndex'))
        self.VerticalSpeedLimit = float((str(Mission.get('VerticalSpeedLimit'))).replace(',', '.'))
        for id in range(len(Mission.WayPoint)):
            wp = Mission.WayPoint[id]
            ID = int(wp.get('id'))
            Latitude = float(str(wp.Latitude).replace(',' , '.'))
            Longitude = float(str(wp.Longitude).replace(',' , '.'))
            Altitude = float((str(wp.Altitude)).replace(',' , '.'))
            Speed = float((str(wp.Speed)).replace(',' , '.'))
            TurnMode = wp.TurnMode
            YawDegree = int(wp.YawDegree)
            HoldTime = int(wp.HoldTime)
            StartDelay = int(wp.StartDelay)
            Period = int(wp.Period)
            RepeatTime = int(wp.RepeatTime)
            RepeatDistance = int(wp.RepeatDistance)
            TimeLimit = int(wp.TimeLimit)
            Elevation = 0
            self.addWaypoint(ID, Latitude, Longitude, Altitude, Elevation, Speed, TurnMode, YawDegree, HoldTime,
                 StartDelay, Period, RepeatTime, RepeatDistance, TimeLimit)
        return self




class WayPoint:
    def __init__(self, Latitude, Longitude, Altitude, Elevation, Speed, TurnMode = 'Adaptive_Bank_Turn',
                 YawDegree = 360, HoldTime = 0,
                 StartDelay = 0, Period = 0, RepeatTime = 0, RepeatDistance = 0, TimeLimit = 65535):
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.Altitude = Altitude
        self.Speed = Speed
        self.TurnMode = TurnMode
        self.YawDegree = YawDegree
        self.HoldTime = HoldTime
        self.StartDelay = StartDelay
        self.Period = Period
        self.RepeatTime = RepeatTime
        self.RepeatDistance = RepeatDistance
        self.TimeLimit = TimeLimit
        self.Elevation = Elevation
