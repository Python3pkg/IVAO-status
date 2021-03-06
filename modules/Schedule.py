#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2011 by Antonio (emper0r) Peña Diaz <emperor.cu@gmail.com>
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
#
# Schedule Function

import os
from . import SQL_queries
import configparser
import urllib.request, urllib.error, urllib.parse
import io
import calendar
import datetime
import locale
from PyQt4.Qt import QNetworkProxy
from PyQt4.QtGui import qApp

try:
    # This options to can load LXML module for Linux x86 or x64 arch
    if os.uname()[-1] == 'i686':
        from .x86 import etree
    else:
        from .x64 import etree
except:
    # This options to can load LXML module for Windows 32bits with
    # Python and PyQt devel enviroment
    if os.environ["PROCESSOR_ARCHITECTURE"] == 'x86':
        from .windows import etree
    else:
        print('\nThis software not run here yet.\n')

def Scheduling():
    """This part is a parse HTML from Schedule website from IVAO, because i can't access
       directly to IVAO database to download schedule, so I have to get by other way where users can
       see the schedule for controllers and pilots"""
    config = configparser.RawConfigParser()
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Config.cfg')
    config.read(config_file)
    SQL_queries.sql_query('Clear_Scheduling_tables')
    parser = etree.HTMLParser()
    qApp.processEvents()
    try:
        use_proxy = config.getint('Settings', 'use_proxy')
        auth = config.getint('Settings', 'auth')
        host = config.get('Settings', 'host')
        port = config.get('Settings', 'port')
        user = config.get('Settings', 'user')
        pswd = config.get('Settings', 'pass')
        if use_proxy == 2 and auth == 2:
            passmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
            passmgr.add_password(None, 'http://' + host + ':' + port, user, pswd)
            authinfo = urllib.request.ProxyBasicAuthHandler(passmgr)
            proxy_support = urllib.request.ProxyHandler({"http" : "http://" + host + ':' + port})
            opener = urllib.request.build_opener(proxy_support, authinfo)
            urllib.request.install_opener(opener)
            QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, str(host), int(port), str(user), str(pswd)))
        if use_proxy == 2 and auth == 0:
            proxy_support = urllib.request.ProxyHandler({"http" : "http://" + host + ':' + port})
            opener = urllib.request.build_opener(proxy_support)
            urllib.request.install_opener(opener)
            QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, str(host), int(port)))
        if use_proxy == 0 and auth == 0:
            pass

        """This lines set locales of enviroment at default "English" language to can parse with web"""
        save_locale = locale.getlocale()
        locale.setlocale(locale.LC_ALL, 'C')

        SchedATC_URL = urllib.request.urlopen(config.get('Info', 'scheduling_atc')).read()
        tree = etree.parse(io.StringIO(SchedATC_URL), parser)
        table_atc = tree.xpath("/html/body/div/center/table")[0]
        actual_today = datetime.datetime.today()

        for line_atc_table in table_atc[1:]:
            for day in range(actual_today.day, 31):
                if '%s %s' % (day, calendar.month_name[datetime.datetime.now().month]) in line_atc_table[4][0].text:
                    columns = [td[0].text for td in line_atc_table]
                    SQL_queries.sql_query('Add_Schedule_ATC', columns)
                    qApp.processEvents()

        SchedFlights_URL = urllib.request.urlopen(config.get('Info', 'scheduling_flights')).read()
        tree = etree.parse(io.StringIO(SchedFlights_URL), parser)
        table_flights = tree.xpath("/html/body/div/div/center/table")[0]

        for line_flights_table in table_flights[2:]:
            for day in range(actual_today.day, 31):
                if '%s %s' % (day, calendar.month_name[datetime.datetime.now().month]) in line_flights_table[7][0].text:
                    columns = [td[0].text for td in line_flights_table]
                    SQL_queries.sql_query('Add_Schedule_Flights', columns)
                    qApp.processEvents()

        """Restore locales"""
        locale.setlocale(locale.LC_ALL, save_locale)
        return True
    except IOError:
            return False