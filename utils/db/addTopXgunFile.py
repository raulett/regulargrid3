# -*- coding: utf-8 -*-
import sqlite3


# Create array of tuples (int Number, int Attribute, double Lon, double Lat, double Alt, int Head, double Velocity,
# int Delay, bool WPTask) to add to SQLite DB
def addTopXgunFile(file, topXgunArray):
    connection = sqlite3.connect(file)
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS waypoint")
    cursor.execute('''CREATE TABLE waypoint (`Number`	INT, `Attribute`	INT,
                            `Lon`	DOUBLE(10,7), `Lat`	DOUBLE(9,7), `Alt`	DOUBLE(4,1), `Head`	INT,
	                        `Velocity`	DOUBLE(3,1), `Delay`	INT, `WPTask`	bool)''')
    cursor.executemany("INSERT INTO waypoint VALUES (?,?,?,?,?,?,?,?,?);", topXgunArray)
    connection.commit()
    connection.close()
