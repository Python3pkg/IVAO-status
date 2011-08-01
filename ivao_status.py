#!/bin/python -W
# Copyright (c) 2011 by Antonio (emper0r) P. Diaz <emperor.cu@gmail.com>
#
# GNU General Public Licence (GPL)
# 
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA  02111-1307  USA
#
# IVAO-status :: License GPLv3+
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
import MainWindow_UI
import urllib2
import sqlite3
import threading

IVAO_STATUS = 'whazzup.txt'

class Main(QtGui.QMainWindow):
    def __init__(self,):
        QtGui.QMainWindow.__init__(self)
        self.ui = MainWindow_UI.Ui_MainWindow()
        self.ui.setupUi(self)

        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move ((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        self.setWindowIcon(QtGui.QIcon('./airlines/ivao.jpg'))
        self.connect(self.ui.ExitBtn, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT("quit()"))
        self.connect(self.ui.UpdateBtn, QtCore.SIGNAL('clicked()'), self.UpdateDB)
        self.connect(self.ui.country_list, QtCore.SIGNAL('activated(QString)'), self.country_view)

        connection = sqlite3.connect('database/ivao.db')
        cursor = connection.cursor()
        countries = cursor.execute("SELECT DISTINCT(Country) FROM iata_icao_codes desc;")
        connection.commit()

        for line in countries:
            country = "%s" % line
            self.ui.country_list.addItem(country)

        connection.close()

    def UpdateDB(self):

        action_update = threading.local()
        action_update = self.ui.action_update.setText("Downloading from IVAO status update...")
        thread = threading.Thread(action_update)
        thread.start()
        thread.join()

        pilot_list = []
        atc_list = []

        StatusURL = urllib2.urlopen('http://de3.www.ivao.aero/' + IVAO_STATUS)

        self.ui.action_update.setText("Ready... Counting players...")

        for logged_users in StatusURL.readlines():
            if "PILOT" in logged_users:
                pilot_list.append(logged_users)
            if "ATC" in logged_users:
                atc_list.append(logged_users)

        self.ui.TotalPilots.setText(str(len(pilot_list)))
        self.ui.TotalATC.setText(str(len(atc_list)))
        self.ui.TotalPlayers.setText(str(len(atc_list) + len(pilot_list)))

        self.ui.action_update.setText("Inserting into DB...")

        connection = sqlite3.connect('database/ivao.db')
        cursor = connection.cursor()

        cursor.execute("BEGIN TRANSACTION;")
        cursor.execute("DELETE FROM status_ivao;")

        for rows in pilot_list:
            fields = rows.split(":")
            callsign = fields[0]
            vid = fields[1]
            realname = rows.rsplit(":")[2].decode('latin-1')
            clienttype = fields[3]
            latitude = fields[5]
            longitude = fields[6]
            altitude = fields[7]
            groundspeed = fields[8]
            planned_aircraft = fields[9]
            planned_tascruise = fields[10]
            planned_depairport = fields[11]
            planned_altitude = fields[12]
            planned_destairport = fields[13]
            server = fields[14]
            protrevision = fields[15]
            rating = fields[16]
            transponder = fields[17]
            visualrange = fields[19]
            planned_revision = fields[20]
            planned_flighttype = fields[21]
            planned_deptime = fields[22]
            planned_actdeptime = fields[23]
            planned_hrsenroute = fields[24]
            planned_minenroute = fields[25]
            planned_hrsfuel = fields[26]
            planned_minfuel = fields[27]
            planned_altairport = fields[28]
            planned_remarks = fields[29]
            planned_route = fields[30]
            planned_depairport_lat = fields[31]
            planned_depairport_lon = fields[32]
            planned_destairport_lat = fields[33]
            planned_destairport_lon = fields[34]
            time_last_atis_received = fields[36]
            time_connected = fields[37]
            client_software_name = fields[38]
            client_software_version = fields[39]
            adminrating = fields[40]
            atc_or_pilotrating = fields[41]
            planned_altairport2 = fields[42]
            planned_typeofflight = fields[43]
            planned_pob = fields[44]
            true_heading = fields[45]
            onground = fields[46]

            cursor.execute("INSERT INTO status_ivao (callsign, vid, realname, server, clienttype \
            , latitude, longitude, altitude, groundspeed, planned_aircraft, planned_tascruise \
            , planned_depairport, planned_altitude, planned_destairport, server, protrevision \
            , rating, transponder, visualrange, planned_revision, planned_flighttype \
            , planned_deptime, planned_actdeptime, planned_hrsenroute, planned_minenroute, planned_hrsfuel \
            , planned_minfuel, planned_altairport, planned_remarks, planned_route, planned_depairport_lat \
            , planned_depairport_lon, planned_destairport_lat, planned_destairport_lon \
            , time_last_atis_received, time_connected, client_software_name, client_software_version \
            , adminrating, atc_or_pilotrating, planned_altairport2, planned_typeofflight, planned_pob, true_heading \
            , onground) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
            (callsign, vid, realname, server, clienttype, latitude, longitude, altitude, groundspeed, planned_aircraft \
             , planned_tascruise, planned_depairport, planned_altitude, planned_destairport, server, protrevision \
             , rating, transponder, visualrange, planned_revision, planned_flighttype \
             , planned_deptime, planned_actdeptime, planned_hrsenroute, planned_minenroute, planned_hrsfuel \
             , planned_minfuel, planned_altairport, planned_remarks, planned_route, planned_depairport_lat \
             , planned_depairport_lon, planned_destairport_lat, planned_destairport_lon \
             , time_last_atis_received, time_connected, client_software_name, client_software_version \
             , adminrating, atc_or_pilotrating, planned_altairport2, planned_typeofflight, planned_pob, true_heading \
             , onground))

        connection.commit()

        for rows in atc_list:
            fields = rows.split(":")
            callsign = fields[0]
            vid = fields[1]
            realname = rows.rsplit(":")[2].decode('latin-1')
            clienttype = fields[3]
            frequency = fields[4]
            latitude = fields[5]
            longitude = fields[6]
            altitude = fields[7]
            server = fields[14]
            protrevision = fields[15]
            rating = fields[16]
            facilitytype = fields[18]
            visualrange = fields[19]
            atis_message = fields[35]
            time_last_atis_received = fields[36]
            time_connected = fields[37]
            client_software_name = fields[38]
            client_software_version = fields[39]
            adminrating = fields[40]
            atc_or_atcrating = fields[41]

            cursor.execute("INSERT INTO status_ivao (callsign, vid, realname, server, clienttype, frequency \
            , latitude, longitude, altitude, server, protrevision \
            , rating, facilitytype, visualrange \
            , time_last_atis_received, time_connected, client_software_name, client_software_version \
            , adminrating, atc_or_pilotrating) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
            (callsign, vid, realname, server, clienttype, frequency, latitude, longitude, altitude, server \
             , protrevision, rating, facilitytype, visualrange, time_last_atis_received, time_connected \
             , client_software_name, client_software_version, adminrating, atc_or_pilotrating))

        connection.commit()
        connection.close()

        self.ui.action_update.setText("Ready")

    def  country_view(self):

        country_selected = self.ui.country_list.currentText()
        connection = sqlite3.connect('database/ivao.db')
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT(flagCode) FROM iata_icao_codes WHERE Country=?", (str(country_selected),))
        flagCode = cursor.fetchone()
        connection.commit()

        flagCodePath = ('./flags/%s.gif') % flagCode
        Pixmap = QtGui.QPixmap(flagCodePath)
        self.ui.flagIcon.fileName = flagCodePath
        self.ui.flagIcon.setPixmap(Pixmap)

        cursor.execute("SELECT vid, facilitytype, frequency, rating, realname FROM status_ivao where clienttype='ATC' order by vid desc;")
        rows = cursor.fetchall()

        self.ui.ATCtableWidget.clearContents()
        self.ui.ATCtableWidget.insertRow(self.ui.ATCtableWidget.rowCount())
        self.ui.ATCtableWidget.setCurrentCell(0, 0)
                    
        for row in rows:
            col_vid = QtGui.QTableWidgetItem(str(row[0]), 0)
            self.ui.ATCtableWidget.setItem(self.ui.ATCtableWidget.rowCount()-1, 0, col_vid)
#           col_country = QtGui.QTableWidgetItem(str(row[1]), 0)
#           self.ui.ATCtableWidget.setItem(self.ui.ATCtableWidget.rowCount()-1, 1, "col_country")
            col_facility = QtGui.QTableWidgetItem(str(row[1]), 0)
            self.ui.ATCtableWidget.setItem(self.ui.ATCtableWidget.rowCount()-1, 2, col_facility)
            col_frequency = QtGui.QTableWidgetItem(str(row[2]), 0)
            self.ui.ATCtableWidget.setItem(self.ui.ATCtableWidget.rowCount()-1, 3, col_frequency)
            col_rating = QtGui.QTableWidgetItem(str(row[3]), 0)
            self.ui.ATCtableWidget.setItem(self.ui.ATCtableWidget.rowCount()-1, 4, col_rating)
            col_realname = QtGui.QTableWidgetItem(str(row[4].encode('latin-1')), 0)
            self.ui.ATCtableWidget.setItem(self.ui.ATCtableWidget.rowCount()-1, 5, col_realname)
            self.ui.ATCtableWidget.update()

        connection.close()

def main():
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()