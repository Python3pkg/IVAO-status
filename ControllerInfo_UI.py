# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUI/ControllerInfo_UI.ui'
#
# Created: Tue Sep 13 15:05:44 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QControllerInfo(object):
    def setupUi(self, QControllerInfo):
        QControllerInfo.setObjectName(_fromUtf8("QControllerInfo"))
        QControllerInfo.setWindowModality(QtCore.Qt.WindowModal)
        QControllerInfo.resize(400, 437)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QControllerInfo.sizePolicy().hasHeightForWidth())
        QControllerInfo.setSizePolicy(sizePolicy)
        QControllerInfo.setMinimumSize(QtCore.QSize(400, 437))
        QControllerInfo.setMaximumSize(QtCore.QSize(400, 437))
        QControllerInfo.setCursor(QtCore.Qt.PointingHandCursor)
        QControllerInfo.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget = QtGui.QWidget(QControllerInfo)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ControllerLabel = QtGui.QLabel(self.centralwidget)
        self.ControllerLabel.setGeometry(QtCore.QRect(9, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.ControllerLabel.setFont(font)
        self.ControllerLabel.setCursor(QtCore.Qt.PointingHandCursor)
        self.ControllerLabel.setObjectName(_fromUtf8("ControllerLabel"))
        self.ControllerText = QtGui.QLabel(self.centralwidget)
        self.ControllerText.setGeometry(QtCore.QRect(78, 10, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.ControllerText.setFont(font)
        self.ControllerText.setCursor(QtCore.Qt.PointingHandCursor)
        self.ControllerText.setText(_fromUtf8(""))
        self.ControllerText.setObjectName(_fromUtf8("ControllerText"))
        self.VidLabel = QtGui.QLabel(self.centralwidget)
        self.VidLabel.setGeometry(QtCore.QRect(10, 45, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.VidLabel.setFont(font)
        self.VidLabel.setCursor(QtCore.Qt.PointingHandCursor)
        self.VidLabel.setObjectName(_fromUtf8("VidLabel"))
        self.VidText = QtGui.QLabel(self.centralwidget)
        self.VidText.setGeometry(QtCore.QRect(40, 45, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.VidText.setFont(font)
        self.VidText.setCursor(QtCore.Qt.PointingHandCursor)
        self.VidText.setText(_fromUtf8(""))
        self.VidText.setObjectName(_fromUtf8("VidText"))
        self.ControllingLabel = QtGui.QLabel(self.centralwidget)
        self.ControllingLabel.setGeometry(QtCore.QRect(140, 45, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.ControllingLabel.setFont(font)
        self.ControllingLabel.setCursor(QtCore.Qt.PointingHandCursor)
        self.ControllingLabel.setObjectName(_fromUtf8("ControllingLabel"))
        self.ControllingText = QtGui.QLabel(self.centralwidget)
        self.ControllingText.setGeometry(QtCore.QRect(140, 60, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.ControllingText.setFont(font)
        self.ControllingText.setCursor(QtCore.Qt.PointingHandCursor)
        self.ControllingText.setText(_fromUtf8(""))
        self.ControllingText.setObjectName(_fromUtf8("ControllingText"))
        self.Flag = QtGui.QLabel(self.centralwidget)
        self.Flag.setGeometry(QtCore.QRect(234, 40, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.Flag.setFont(font)
        self.Flag.setCursor(QtCore.Qt.PointingHandCursor)
        self.Flag.setText(_fromUtf8(""))
        self.Flag.setObjectName(_fromUtf8("Flag"))
        self.FacilityLabel = QtGui.QLabel(self.centralwidget)
        self.FacilityLabel.setGeometry(QtCore.QRect(11, 110, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.FacilityLabel.setFont(font)
        self.FacilityLabel.setCursor(QtCore.Qt.PointingHandCursor)
        self.FacilityLabel.setObjectName(_fromUtf8("FacilityLabel"))
        self.facility_freq_Text = QtGui.QLabel(self.centralwidget)
        self.facility_freq_Text.setGeometry(QtCore.QRect(115, 108, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.facility_freq_Text.setFont(font)
        self.facility_freq_Text.setCursor(QtCore.Qt.PointingHandCursor)
        self.facility_freq_Text.setText(_fromUtf8(""))
        self.facility_freq_Text.setObjectName(_fromUtf8("facility_freq_Text"))
        self.ATISInfo = QtGui.QTextEdit(self.centralwidget)
        self.ATISInfo.setGeometry(QtCore.QRect(8, 130, 381, 141))
        self.ATISInfo.setProperty(_fromUtf8("cursor"), QtCore.Qt.PointingHandCursor)
        self.ATISInfo.setAutoFormatting(QtGui.QTextEdit.AutoAll)
        self.ATISInfo.setReadOnly(True)
        self.ATISInfo.setAcceptRichText(False)
        self.ATISInfo.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.ATISInfo.setObjectName(_fromUtf8("ATISInfo"))
        self.separator = QtGui.QFrame(self.centralwidget)
        self.separator.setGeometry(QtCore.QRect(10, 80, 381, 16))
        self.separator.setCursor(QtCore.Qt.PointingHandCursor)
        self.separator.setFrameShape(QtGui.QFrame.HLine)
        self.separator.setFrameShadow(QtGui.QFrame.Sunken)
        self.separator.setObjectName(_fromUtf8("separator"))
        self.ConnectionLabel = QtGui.QLabel(self.centralwidget)
        self.ConnectionLabel.setGeometry(QtCore.QRect(10, 300, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.ConnectionLabel.setFont(font)
        self.ConnectionLabel.setCursor(QtCore.Qt.PointingHandCursor)
        self.ConnectionLabel.setObjectName(_fromUtf8("ConnectionLabel"))
        self.separator_2 = QtGui.QFrame(self.centralwidget)
        self.separator_2.setGeometry(QtCore.QRect(10, 280, 381, 16))
        self.separator_2.setCursor(QtCore.Qt.PointingHandCursor)
        self.separator_2.setFrameShape(QtGui.QFrame.HLine)
        self.separator_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.separator_2.setObjectName(_fromUtf8("separator_2"))
        self.TimeOnLineText = QtGui.QLabel(self.centralwidget)
        self.TimeOnLineText.setGeometry(QtCore.QRect(10, 320, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.TimeOnLineText.setFont(font)
        self.TimeOnLineText.setCursor(QtCore.Qt.PointingHandCursor)
        self.TimeOnLineText.setText(_fromUtf8(""))
        self.TimeOnLineText.setObjectName(_fromUtf8("TimeOnLineText"))
        self.SoftwareText = QtGui.QLabel(self.centralwidget)
        self.SoftwareText.setGeometry(QtCore.QRect(74, 350, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.SoftwareText.setFont(font)
        self.SoftwareText.setCursor(QtCore.Qt.PointingHandCursor)
        self.SoftwareText.setText(_fromUtf8(""))
        self.SoftwareText.setObjectName(_fromUtf8("SoftwareText"))
        self.ConnectedText = QtGui.QLabel(self.centralwidget)
        self.ConnectedText.setGeometry(QtCore.QRect(341, 351, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.ConnectedText.setFont(font)
        self.ConnectedText.setCursor(QtCore.Qt.PointingHandCursor)
        self.ConnectedText.setText(_fromUtf8(""))
        self.ConnectedText.setObjectName(_fromUtf8("ConnectedText"))
        self.Close = QtGui.QPushButton(self.centralwidget)
        self.Close.setGeometry(QtCore.QRect(200, 400, 99, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Close.setFont(font)
        self.Close.setCursor(QtCore.Qt.PointingHandCursor)
        self.Close.setObjectName(_fromUtf8("Close"))
        self.AddFriend = QtGui.QPushButton(self.centralwidget)
        self.AddFriend.setGeometry(QtCore.QRect(95, 400, 99, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AddFriend.setFont(font)
        self.AddFriend.setCursor(QtCore.Qt.PointingHandCursor)
        self.AddFriend.setObjectName(_fromUtf8("AddFriend"))
        self.separator_3 = QtGui.QFrame(self.centralwidget)
        self.separator_3.setGeometry(QtCore.QRect(10, 370, 381, 16))
        self.separator_3.setCursor(QtCore.Qt.PointingHandCursor)
        self.separator_3.setFrameShape(QtGui.QFrame.HLine)
        self.separator_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.separator_3.setObjectName(_fromUtf8("separator_3"))
        self.SoftwareLabel = QtGui.QLabel(self.centralwidget)
        self.SoftwareLabel.setGeometry(QtCore.QRect(10, 353, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.SoftwareLabel.setFont(font)
        self.SoftwareLabel.setCursor(QtCore.Qt.PointingHandCursor)
        self.SoftwareLabel.setObjectName(_fromUtf8("SoftwareLabel"))
        self.ConnectedLabel = QtGui.QLabel(self.centralwidget)
        self.ConnectedLabel.setGeometry(QtCore.QRect(250, 351, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.ConnectedLabel.setFont(font)
        self.ConnectedLabel.setCursor(QtCore.Qt.PointingHandCursor)
        self.ConnectedLabel.setObjectName(_fromUtf8("ConnectedLabel"))
        self.rating_img = QtGui.QLabel(self.centralwidget)
        self.rating_img.setGeometry(QtCore.QRect(290, 8, 105, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.rating_img.setFont(font)
        self.rating_img.setCursor(QtCore.Qt.PointingHandCursor)
        self.rating_img.setText(_fromUtf8(""))
        self.rating_img.setObjectName(_fromUtf8("rating_img"))
        QControllerInfo.setCentralWidget(self.centralwidget)

        self.retranslateUi(QControllerInfo)
        QtCore.QObject.connect(self.Close, QtCore.SIGNAL(_fromUtf8("clicked()")), QControllerInfo.close)
        QtCore.QMetaObject.connectSlotsByName(QControllerInfo)

    def retranslateUi(self, QControllerInfo):
        QControllerInfo.setWindowTitle(QtGui.QApplication.translate("QControllerInfo", "Controller Info", None, QtGui.QApplication.UnicodeUTF8))
        self.ControllerLabel.setText(QtGui.QApplication.translate("QControllerInfo", "Controller", None, QtGui.QApplication.UnicodeUTF8))
        self.VidLabel.setText(QtGui.QApplication.translate("QControllerInfo", "VID", None, QtGui.QApplication.UnicodeUTF8))
        self.ControllingLabel.setText(QtGui.QApplication.translate("QControllerInfo", "Controlling in ", None, QtGui.QApplication.UnicodeUTF8))
        self.FacilityLabel.setText(QtGui.QApplication.translate("QControllerInfo", "Facility Details", None, QtGui.QApplication.UnicodeUTF8))
        self.ConnectionLabel.setText(QtGui.QApplication.translate("QControllerInfo", "Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.Close.setText(QtGui.QApplication.translate("QControllerInfo", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.AddFriend.setText(QtGui.QApplication.translate("QControllerInfo", "Add Friend", None, QtGui.QApplication.UnicodeUTF8))
        self.SoftwareLabel.setText(QtGui.QApplication.translate("QControllerInfo", "Software", None, QtGui.QApplication.UnicodeUTF8))
        self.ConnectedLabel.setText(QtGui.QApplication.translate("QControllerInfo", "Connected to", None, QtGui.QApplication.UnicodeUTF8))

