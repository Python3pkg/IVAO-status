# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUI/Build_UI.ui'
#
# Created: Sat Nov 10 14:19:33 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QBuildDB(object):
    def setupUi(self, QBuildDB):
        QBuildDB.setObjectName(_fromUtf8("QBuildDB"))
        QBuildDB.setWindowModality(QtCore.Qt.ApplicationModal)
        QBuildDB.resize(385, 120)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QBuildDB.sizePolicy().hasHeightForWidth())
        QBuildDB.setSizePolicy(sizePolicy)
        QBuildDB.setMinimumSize(QtCore.QSize(385, 120))
        QBuildDB.setMaximumSize(QtCore.QSize(385, 120))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        QBuildDB.setFont(font)
        QBuildDB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QBuildDB.setFocusPolicy(QtCore.Qt.StrongFocus)
        QBuildDB.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtGui.QWidget(QBuildDB)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Close = QtGui.QPushButton(self.centralwidget)
        self.Close.setEnabled(False)
        self.Close.setGeometry(QtCore.QRect(159, 90, 70, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(8)
        self.Close.setFont(font)
        self.Close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Close.setObjectName(_fromUtf8("Close"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(19, 30, 350, 19))
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.LabelTitle = QtGui.QLabel(self.centralwidget)
        self.LabelTitle.setGeometry(QtCore.QRect(21, 14, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LabelTitle.setFont(font)
        self.LabelTitle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LabelTitle.setObjectName(_fromUtf8("LabelTitle"))
        self.LabelFile = QtGui.QLabel(self.centralwidget)
        self.LabelFile.setGeometry(QtCore.QRect(120, 13, 230, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.LabelFile.setFont(font)
        self.LabelFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LabelFile.setText(_fromUtf8(""))
        self.LabelFile.setObjectName(_fromUtf8("LabelFile"))
        self.progressBarTotal = QtGui.QProgressBar(self.centralwidget)
        self.progressBarTotal.setGeometry(QtCore.QRect(19, 70, 350, 19))
        self.progressBarTotal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.progressBarTotal.setProperty("value", 0)
        self.progressBarTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBarTotal.setObjectName(_fromUtf8("progressBarTotal"))
        self.TotalImported = QtGui.QLabel(self.centralwidget)
        self.TotalImported.setGeometry(QtCore.QRect(21, 54, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TotalImported.setFont(font)
        self.TotalImported.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TotalImported.setObjectName(_fromUtf8("TotalImported"))
        QBuildDB.setCentralWidget(self.centralwidget)

        self.retranslateUi(QBuildDB)
        QtCore.QObject.connect(self.Close, QtCore.SIGNAL(_fromUtf8("clicked()")), QBuildDB.close)
        QtCore.QMetaObject.connectSlotsByName(QBuildDB)

    def retranslateUi(self, QBuildDB):
        QBuildDB.setWindowTitle(QtGui.QApplication.translate("QBuildDB", "Import database from [.dat] files", None, QtGui.QApplication.UnicodeUTF8))
        self.Close.setText(QtGui.QApplication.translate("QBuildDB", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelTitle.setText(QtGui.QApplication.translate("QBuildDB", "Importing File:", None, QtGui.QApplication.UnicodeUTF8))
        self.TotalImported.setText(QtGui.QApplication.translate("QBuildDB", "Total Imports", None, QtGui.QApplication.UnicodeUTF8))

