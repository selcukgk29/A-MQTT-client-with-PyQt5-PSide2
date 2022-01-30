# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardBYaDoF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1805, 869)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 1801, 871))
        self.frame.setStyleSheet(u"background-color: rgb(222, 223, 220);\n"
"border-top-right-radius:60;\n"
"border-top-left-radius:60;")
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(10)
        self.frame.setMidLineWidth(5)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 1801, 80))
        self.frame_2.setStyleSheet(u"background-color: rgb(41, 42, 55);\n"
"border-top-right-radius:60;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(80, 10, 61, 61))
        self.frame_11.setStyleSheet(u"background-image: url(:/newPrefix/icon/icons8-smart-home-64.png);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 20, 211, 41))
        font = QFont()
        font.setFamily(u"Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:#FFF;\n"
"")
        self.frame_14 = QFrame(self.frame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(910, 140, 120, 80))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(90, 130, 300, 300))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"background-color: rgb(41, 42, 55);\n"
"border-style: outset;\n"
"border-color:#FFF;\n"
"border-width:2px;\n"
"border-radius:30px;\n"
"\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(20, 10, 61, 61))
        self.frame_12.setStyleSheet(u"background-image: url(:/newPrefix/icon/day/113.png);\n"
"border:none;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 70, 211, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Historic")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"border:none;\n"
"color:#FFF;\n"
"")
        self.userlabel = QLabel(self.frame_3)
        self.userlabel.setObjectName(u"userlabel")
        self.userlabel.setGeometry(QRect(40, 110, 211, 41))
        self.userlabel.setFont(font1)
        self.userlabel.setStyleSheet(u"border:none;\n"
"color:#FFF;\n"
"")
        self.status_label1 = QLabel(self.frame_3)
        self.status_label1.setObjectName(u"status_label1")
        self.status_label1.setGeometry(QRect(40, 160, 231, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Historic")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.status_label1.setFont(font2)
        self.status_label1.setStyleSheet(u"border:none;\n"
"color:#FFF;\n"
"background-color:none;")
        self.see_more = QPushButton(self.frame_3)
        self.see_more.setObjectName(u"see_more")
        self.see_more.setGeometry(QRect(40, 240, 81, 21))
        self.see_more.setStyleSheet(u"background:none;\n"
"text-align:left;\n"
"font: 75 9pt \"Segoe UI Historic\";\n"
"color: rgb(0, 85, 255);")
        self.status_label2 = QLabel(self.frame_3)
        self.status_label2.setObjectName(u"status_label2")
        self.status_label2.setGeometry(QRect(40, 190, 231, 31))
        self.status_label2.setFont(font2)
        self.status_label2.setStyleSheet(u"border:none;\n"
"color:#FFF;\n"
"background-color:none;")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(420, 130, 420, 300))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.98, y1:0.471364, x2:1, y2:0.472, stop:1 rgba(0, 0, 0, 18));\n"
"border-style: outset;\n"
"border-color:#FFF;\n"
"border-width:2px;\n"
"border-radius:30px;\n"
"\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 90, 181, 41))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Historic")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(99)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background-color:none;\n"
"font: 75 14pt \"Segoe UI Historic\";\n"
"border:none;\n"
"font-weight:800;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.frame_13 = QFrame(self.frame_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(20, 10, 61, 61))
        self.frame_13.setStyleSheet(u"background-image: url(:/newPrefix/icon/icons8-fan-64.png);\n"
"background-color:none;\n"
"border:none;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.ariconditioner_label = QLabel(self.frame_4)
        self.ariconditioner_label.setObjectName(u"ariconditioner_label")
        self.ariconditioner_label.setGeometry(QRect(20, 130, 271, 101))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Historic")
        font4.setPointSize(72)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setWeight(99)
        self.ariconditioner_label.setFont(font4)
        self.ariconditioner_label.setStyleSheet(u"color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(8, 137, 231, 255));\n"
"border :none;\n"
"background-color:none;\n"
"\n"
"font: 75 72pt \"Segoe UI Historic\";\n"
"font-weight:900;")
        self.airconditione_slider = QSlider(self.frame_4)
        self.airconditione_slider.setObjectName(u"airconditione_slider")
        self.airconditione_slider.setGeometry(QRect(330, 50, 51, 221))
        self.airconditione_slider.setStyleSheet(u"QSlider::groove:vertical {\n"
"    position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"    left: 2px; right: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 10px;\n"
"    background: green;\n"
"    margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"   \n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.512, y1:1, x2:0.492478, y2:0, stop:0.835821 rgba(4, 131, 237, 240), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    \n"
"	background-color: rgb(222, 223, 220);\n"
"\n"
"}")
        self.airconditione_slider.setValue(30)
        self.airconditione_slider.setOrientation(Qt.Vertical)
        self.airdevice = QLabel(self.frame_4)
        self.airdevice.setObjectName(u"airdevice")
        self.airdevice.setGeometry(QRect(30, 240, 251, 31))
        self.airdevice.setStyleSheet(u"background-color:none;\n"
"font: 75 10pt \"Segoe UI Historic\";\n"
"border:none;\n"
"color: rgb(108, 108, 108);")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(899, 130, 411, 300))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.98, y1:0.471364, x2:1, y2:0.472, stop:1 rgba(0, 0, 0, 18));\n"
"border-style: outset;\n"
"border-color:#FFF;\n"
"border-width:2px;\n"
"border-radius:30px;\n"
"\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_15 = QFrame(self.frame_5)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(10, 10, 81, 81))
        self.frame_15.setStyleSheet(u"background-image: url(:/newPrefix/icon/icons8-reflector-bulb-80.png);\n"
"border:none;\n"
"background-color:none;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.lightintensity_label_2 = QLabel(self.frame_5)
        self.lightintensity_label_2.setObjectName(u"lightintensity_label_2")
        self.lightintensity_label_2.setGeometry(QRect(20, 130, 271, 101))
        self.lightintensity_label_2.setFont(font4)
        self.lightintensity_label_2.setStyleSheet(u"color: rgb(255, 170, 0);\n"
"border :none;\n"
"background-color:none;\n"
"font: 75 72pt \"Segoe UI Historic\";\n"
"font-weight:900;")
        self.lightintensity_slider_2 = QSlider(self.frame_5)
        self.lightintensity_slider_2.setObjectName(u"lightintensity_slider_2")
        self.lightintensity_slider_2.setGeometry(QRect(330, 50, 51, 221))
        self.lightintensity_slider_2.setStyleSheet(u"QSlider::groove:vertical {\n"
"    position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"    left: 2px; right: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 10px;\n"
"    background: green;\n"
"    margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"   \n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.527, y1:1, x2:0.532338, y2:0, stop:0.751244 rgba(255, 170, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"\n"
"	background-color: rgb(222, 223, 220);\n"
"\n"
"}")
        self.lightintensity_slider_2.setValue(30)
        self.lightintensity_slider_2.setOrientation(Qt.Vertical)
        self.airdevice_2 = QLabel(self.frame_5)
        self.airdevice_2.setObjectName(u"airdevice_2")
        self.airdevice_2.setGeometry(QRect(40, 240, 251, 31))
        self.airdevice_2.setStyleSheet(u"background-color:none;\n"
"font: 75 10pt \"Segoe UI Historic\";\n"
"border:none;\n"
"color: rgb(108, 108, 108);")
        self.lightintensity_label_2.raise_()
        self.lightintensity_slider_2.raise_()
        self.frame_15.raise_()
        self.airdevice_2.raise_()
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(1350, 130, 420, 300))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.98, y1:0.471364, x2:1, y2:0.472, stop:1 rgba(0, 0, 0, 18));\n"
"border-style: outset;\n"
"border-color:#FFF;\n"
"border-width:2px;\n"
"border-radius:30px;\n"
"\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_16 = QFrame(self.frame_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(10, 10, 71, 71))
        self.frame_16.setStyleSheet(u"background-image: url(:/newPrefix/icon/icons8-home-64.png);\n"
"border:none;\n"
"background-color:none;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_17 = QFrame(self.frame_6)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(20, 140, 111, 151))
        self.frame_17.setStyleSheet(u"QFrame{\n"
"background-color:none;\n"
"\n"
"}\n"
"QFrame:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_17)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 0, 91, 91))
        self.label_6.setStyleSheet(u"background:none;\n"
"background-image: url(:/newPrefix/icon/icons8-lock-96.png);\n"
"border:none;\n"
"")
        self.airdevice_3 = QLabel(self.frame_17)
        self.airdevice_3.setObjectName(u"airdevice_3")
        self.airdevice_3.setGeometry(QRect(20, 100, 71, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.airdevice_3.sizePolicy().hasHeightForWidth())
        self.airdevice_3.setSizePolicy(sizePolicy)
        self.airdevice_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.airdevice_3.setStyleSheet(u"background-color:none;\n"
"font: 75 10pt \"Segoe UI Historic\";\n"
"border:none;\n"
"color: rgb(108, 108, 108);")
        self.airdevice_3.setScaledContents(False)
        self.airdevice_3.setWordWrap(True)
        self.frame_18 = QFrame(self.frame_6)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(160, 140, 111, 151))
        self.frame_18.setStyleSheet(u"QFrame{\n"
"background-color:none;\n"
"\n"
"}\n"
"QFrame:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_18)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 91, 91))
        self.label_7.setStyleSheet(u"background:none;\n"
"background-image: url(:/newPrefix/icon/icons8-lock-96.png);\n"
"border:none;\n"
"")
        self.airdevice_4 = QLabel(self.frame_18)
        self.airdevice_4.setObjectName(u"airdevice_4")
        self.airdevice_4.setGeometry(QRect(30, 100, 71, 51))
        sizePolicy.setHeightForWidth(self.airdevice_4.sizePolicy().hasHeightForWidth())
        self.airdevice_4.setSizePolicy(sizePolicy)
        self.airdevice_4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.airdevice_4.setStyleSheet(u"background-color:none;\n"
"font: 75 10pt \"Segoe UI Historic\";\n"
"border:none;\n"
"color: rgb(108, 108, 108);")
        self.airdevice_4.setScaledContents(False)
        self.airdevice_4.setWordWrap(True)
        self.frame_19 = QFrame(self.frame_6)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(290, 140, 111, 151))
        self.frame_19.setStyleSheet(u"QFrame{\n"
"background-color:none;\n"
"}\n"
"QFrame:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"}")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_19)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 91, 91))
        self.label_8.setStyleSheet(u"background:none;\n"
"background-image: url(:/newPrefix/icon/icons8-lock-96.png);\n"
"border:none;\n"
"")
        self.airdevice_5 = QLabel(self.frame_19)
        self.airdevice_5.setObjectName(u"airdevice_5")
        self.airdevice_5.setGeometry(QRect(40, 90, 71, 51))
        sizePolicy.setHeightForWidth(self.airdevice_5.sizePolicy().hasHeightForWidth())
        self.airdevice_5.setSizePolicy(sizePolicy)
        self.airdevice_5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.airdevice_5.setStyleSheet(u"background-color:none;\n"
"font: 75 10pt \"Segoe UI Historic\";\n"
"border:none;\n"
"color: rgb(108, 108, 108);")
        self.airdevice_5.setScaledContents(False)
        self.airdevice_5.setWordWrap(True)
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(90, 490, 300, 300))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.98, y1:0.471364, x2:1, y2:0.472, stop:1 rgba(0, 0, 0, 18));\n"
"border-style: outset;\n"
"border-color:#FFF;\n"
"border-width:2px;\n"
"border-radius:30px;\n"
"\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 10, 251, 81))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Historic")
        font5.setPointSize(24)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setWeight(99)
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"background-color:none;\n"
"font: 75 24pt \"Segoe UI Historic\";\n"
"border:none;\n"
"font-weight:800;\n"
"color: rgb(0, 170, 127);\n"
"")
        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 180, 211, 101))
        font6 = QFont()
        font6.setFamily(u"Segoe UI Historic")
        font6.setPointSize(54)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(9)
        self.label_10.setFont(font6)
        self.label_10.setStyleSheet(u"background-color:none;\n"
"border:none;\n"
"font-weight:1200;\n"
"font: 75 54pt \"Segoe UI Historic\";\n"
"color: rgb(0, 170, 127);")
        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(50, 90, 191, 61))
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"background-color:none;\n"
"font: 75 14pt \"Segoe UI Historic\";\n"
"border:none;\n"
"font-weight:800;\n"
"color: rgb(0, 170, 127);")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(420, 490, 611, 311))
        self.frame_8.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.98, y1:0.471364, x2:1, y2:0.472, stop:1 rgba(0, 0, 0, 18));\n"
"border-style: outset;\n"
"border-color:#FFF;\n"
"border-width:2px;\n"
"border-radius:30px;\n"
"\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_20 = QFrame(self.frame_8)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(20, 10, 121, 131))
        self.frame_20.setStyleSheet(u"background-image: url(:/newPrefix/icon/icons8-temperature-128.png);\n"
"background-color:none;\n"
"border:none;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.ariconditioner_label_2 = QLabel(self.frame_8)
        self.ariconditioner_label_2.setObjectName(u"ariconditioner_label_2")
        self.ariconditioner_label_2.setGeometry(QRect(30, 180, 271, 101))
        self.ariconditioner_label_2.setFont(font4)
        self.ariconditioner_label_2.setStyleSheet(u"color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(8, 137, 231, 255));\n"
"border :none;\n"
"background-color:none;\n"
"\n"
"font: 75 72pt \"Segoe UI Historic\";\n"
"font-weight:900;")
        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 140, 231, 41))
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"background-color:none;\n"
"font: 75 14pt \"Segoe UI Historic\";\n"
"border:none;\n"
"font-weight:800;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.circularProgress = QFrame(self.frame_8)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(310, 10, 291, 291))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"	border-radius: 140px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:228.3, stop:0.940299 rgba(255, 255, 255, 255), stop:0.970149 rgba(0, 255, 25, 255));\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularbg = QFrame(self.circularProgress)
        self.circularbg.setObjectName(u"circularbg")
        self.circularbg.setGeometry(QRect(0, 0, 291, 291))
        self.circularbg.setStyleSheet(u"QFrame{\n"
"\n"
"\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0.98, y1:0.471364, x2:1, y2:0.472, stop:1 rgba(0, 0, 0, 18));\n"
"}\n"
"")
        self.circularbg.setFrameShape(QFrame.StyledPanel)
        self.circularbg.setFrameShadow(QFrame.Raised)
        self.dial = QDial(self.circularbg)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(0, 0, 291, 291))
        self.dial.setStyleSheet(u"")
        self.dial.setMaximum(60)
        self.dial.setSingleStep(5)
        self.dial.setPageStep(5)
        self.dial.setValue(5)
        self.dial.setSliderPosition(5)
        self.dial.setOrientation(Qt.Vertical)
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(True)
        self.dial.setWrapping(False)
        self.dial.setNotchTarget(0.050000000000000)
        self.dial.setNotchesVisible(True)
        self.ariconditioner_label_3 = QLabel(self.frame_8)
        self.ariconditioner_label_3.setObjectName(u"ariconditioner_label_3")
        self.ariconditioner_label_3.setGeometry(QRect(170, 180, 271, 101))
        self.ariconditioner_label_3.setFont(font4)
        self.ariconditioner_label_3.setStyleSheet(u"color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(8, 137, 231, 255));\n"
"border :none;\n"
"background-color:none;\n"
"\n"
"font: 75 72pt \"Segoe UI Historic\";\n"
"font-weight:900;")
        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(1080, 490, 311, 311))
        self.frame_9.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.98, y1:0.471364, x2:1, y2:0.472, stop:1 rgba(0, 0, 0, 18));\n"
"border-style: outset;\n"
"border-color:#FFF;\n"
"border-width:2px;\n"
"border-radius:30px;\n"
"\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(1450, 490, 311, 311))
        self.frame_10.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.98, y1:0.471364, x2:1, y2:0.472, stop:1 rgba(0, 0, 0, 18));\n"
"border-style: outset;\n"
"border-color:#FFF;\n"
"border-width:2px;\n"
"border-radius:30px;\n"
"\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.frame_21 = QFrame(self.frame_10)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(-100, -20, 531, 281))
        self.frame_21.setStyleSheet(u"border:none;\n"
"background:none;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(110, 30, 61, 61))
        self.frame_22.setStyleSheet(u"background-image: url(:/newPrefix/icon/icons8-eye-64.png);\n"
"border:none;\n"
"background-color:none;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(930, 220, 181, 41))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background-color:none;\n"
"font: 75 14pt \"Segoe UI Historic\";\n"
"border:none;\n"
"font-weight:800;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1380, 220, 241, 41))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"background-color:none;\n"
"font: 75 14pt \"Segoe UI Historic\";\n"
"border:none;\n"
"font-weight:800;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.frame_23 = QFrame(self.frame)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(0, 0, 1801, 871))
        self.frame_23.setStyleSheet(u"background-color: rgb(222, 223, 220);\n"
"border-top-right-radius:60;\n"
"border-top-left-radius:60;")
        self.frame_23.setFrameShape(QFrame.WinPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.frame_23.setLineWidth(10)
        self.frame_23.setMidLineWidth(5)
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(0, 0, 1801, 80))
        self.frame_24.setStyleSheet(u"background-color: rgb(41, 42, 55);\n"
"border-top-right-radius:60;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(80, 10, 61, 61))
        self.frame_25.setStyleSheet(u"background-image: url(:/newPrefix/icon/icons8-smart-home-64.png);")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.frame_24)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(160, 20, 211, 41))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color:#FFF;\n"
"")
        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(910, 140, 120, 80))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.frame_27 = QFrame(self.frame_23)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(90, 130, 300, 300))
        self.frame_27.setStyleSheet(u"QFrame{\n"
"background-color: rgb(41, 42, 55);\n"
"border-style: outset;\n"
"border-color:#FFF;\n"
"border-width:2px;\n"
"border-radius:30px;\n"
"\n"
"}\n"
"")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(20, 10, 61, 61))
        self.frame_28.setStyleSheet(u"background-image: url(:/newPrefix/icon/day/113.png);\n"
"border:none;")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.label_14 = QLabel(self.frame_27)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(40, 70, 211, 41))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"border:none;\n"
"color:#FFF;\n"
"")
        self.userlabel_2 = QLabel(self.frame_27)
        self.userlabel_2.setObjectName(u"userlabel_2")
        self.userlabel_2.setGeometry(QRect(40, 110, 211, 41))
        self.userlabel_2.setFont(font1)
        self.userlabel_2.setStyleSheet(u"border:none;\n"
"color:#FFF;\n"
"")
        self.status_label1_2 = QLabel(self.frame_27)
        self.status_label1_2.setObjectName(u"status_label1_2")
        self.status_label1_2.setGeometry(QRect(40, 160, 231, 31))
        self.status_label1_2.setFont(font2)
        self.status_label1_2.setStyleSheet(u"border:none;\n"
"color:#FFF;\n"
"background-color:none;")
        self.see_more_2 = QPushButton(self.frame_27)
        self.see_more_2.setObjectName(u"see_more_2")
        self.see_more_2.setGeometry(QRect(40, 240, 81, 21))
        self.see_more_2.setStyleSheet(u"background:none;\n"
"text-align:left;\n"
"font: 75 9pt \"Segoe UI Historic\";\n"
"color: rgb(0, 85, 255);")
        self.status_label2_2 = QLabel(self.frame_27)
        self.status_label2_2.setObjectName(u"status_label2_2")
        self.status_label2_2.setGeometry(QRect(40, 190, 231, 31))
        self.status_label2_2.setFont(font2)
        self.status_label2_2.setStyleSheet(u"border:none;\n"
"color:#FFF;\n"
"background-color:none;")
        self.frame_29 = QFrame(self.frame_23)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setGeometry(QRect(420, 130, 420, 300))
        self.frame_29.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.98, y1:0.471364, x2:1, y2:0.472, stop:1 rgba(0, 0, 0, 18));\n"
"border-style: outset;\n"
"border-color:#FFF;\n"
"border-width:2px;\n"
"border-radius:30px;\n"
"\n"
"}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.label_15 = QLabel(self.frame_29)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(30, 90, 181, 41))
        self.label_15.setFont(font3)
        self.label_15.setStyleSheet(u"background-color:none;\n"
"font: 75 14pt \"Segoe UI Historic\";\n"
"border:none;\n"
"font-weight:800;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setGeometry(QRect(20, 10, 61, 61))
        self.frame_30.setStyleSheet(u"background-image: url(:/newPrefix/icon/icons8-fan-64.png);\n"
"background-color:none;\n"
"border:none;")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.ariconditioner_label_4 = QLabel(self.frame_29)
        self.ariconditioner_label_4.setObjectName(u"ariconditioner_label_4")
        self.ariconditioner_label_4.setGeometry(QRect(-10, 130, 171, 101))
        self.ariconditioner_label_4.setFont(font4)
        self.ariconditioner_label_4.setStyleSheet(u"color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(8, 137, 231, 255));\n"
"border :none;\n"
"background-color:none;\n"
"\n"
"font: 75 72pt \"Segoe UI Historic\";\n"
"font-weight:900;")
        self.ariconditioner_label_4.setAlignment(Qt.AlignCenter)
        self.airconditione_slider_2 = QSlider(self.frame_29)
        self.airconditione_slider_2.setObjectName(u"airconditione_slider_2")
        self.airconditione_slider_2.setGeometry(QRect(330, 50, 51, 221))
        self.airconditione_slider_2.setStyleSheet(u"QSlider::groove:vertical {\n"
"    position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"    left: 2px; right: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 10px;\n"
"    background: green;\n"
"    margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"   \n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.512, y1:1, x2:0.492478, y2:0, stop:0.835821 rgba(4, 131, 237, 240), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    \n"
"	background-color: rgb(222, 223, 220);\n"
"\n"
"}")
        self.airconditione_slider_2.setValue(30)
        self.airconditione_slider_2.setOrientation(Qt.Vertical)
        self.airdevice_6 = QLabel(self.frame_29)
        self.airdevice_6.setObjectName(u"airdevice_6")
        self.airdevice_6.setGeometry(QRect(30, 240, 251, 31))
        self.airdevice_6.setStyleSheet(u"background-color:none;\n"
"font: 75 10pt \"Segoe UI Historic\";\n"
"border:none;\n"
"color: rgb(108, 108, 108);")
        self.ariconditioner_label_7 = QLabel(self.frame_29)
        self.ariconditioner_label_7.setObjectName(u"ariconditioner_label_7")
        self.ariconditioner_label_7.setGeometry(QRect(160, 140, 41, 81))
        self.ariconditioner_label_7.setFont(font4)
        self.ariconditioner_label_7.setStyleSheet(u"color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(8, 137, 231, 255));\n"
"border :none;\n"
"background-color:none;\n"
"\n"
"font: 75 72pt \"Segoe UI Historic\";\n"
"font-weight:900;")
        self.ariconditioner_label_8 = QLabel(self.frame_29)
        self.ariconditioner_label_8.setObjectName(u"ariconditioner_label_8")
        self.ariconditioner_label_8.setGeometry(QRect(290, 160, 31, 31))
        font7 = QFont()
        font7.setFamily(u"Segoe UI Historic")
        font7.setPointSize(22)
        font7.setBold(True)
        font7.setItalic(False)
        font7.setWeight(99)
        self.ariconditioner_label_8.setFont(font7)
        self.ariconditioner_label_8.setStyleSheet(u"color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(8, 137, 231, 255));\n"
"border :none;\n"
"background-color:none;\n"
"\n"
"font: 75 22pt \"Segoe UI Historic\";\n"
"font-weight:900;")
        self.ariconditioner_label_8.setAlignment(Qt.AlignCenter)
        self.ariconditioner_label_9 = QLabel(self.frame_29)
        self.ariconditioner_label_9.setObjectName(u"ariconditioner_label_9")
        self.ariconditioner_label_9.setGeometry(QRect(270, 110, 61, 31))
        self.ariconditioner_label_9.setFont(font7)
        self.ariconditioner_label_9.setStyleSheet(u"color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(8, 137, 231, 255));\n"
"border :none;\n"
"background-color:none;\n"
"\n"
"font: 75 22pt \"Segoe UI Historic\";\n"
"font-weight:900;")
        self.ariconditioner_label_9.setAlignment(Qt.AlignCenter)
        self.ariconditioner_label_10 = QLabel(self.frame_29)
        self.ariconditioner_label_10.setObjectName(u"ariconditioner_label_10")
        self.ariconditioner_label_10.setGeometry(QRect(260, 250, 61, 31))
        self.ariconditioner_label_10.setFont(font7)
        self.ariconditioner_label_10.setStyleSheet(u"color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(8, 137, 231, 255));\n"
"border :none;\n"
"background-color:none;\n"
"\n"
"font: 75 22pt \"Segoe UI Historic\";\n"
"font-weight:900;")
        self.ariconditioner_label_10.setAlignment(Qt.AlignCenter)
        self.ariconditioner_label_11 = QLabel(self.frame_29)
        self.ariconditioner_label_11.setObjectName(u"ariconditioner_label_11")
        self.ariconditioner_label_11.setGeometry(QRect(270, 30, 61, 31))
        self.ariconditioner_label_11.setFont(font7)
        self.ariconditioner_label_11.setStyleSheet(u"color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(8, 137, 231, 255));\n"
"border :none;\n"
"background-color:none;\n"
"\n"
"font: 75 22pt \"Segoe UI Historic\";\n"
"font-weight:900;")
        self.ariconditioner_label_11.setAlignment(Qt.AlignCenter)
        self.frame_31 = QFrame(self.frame_23)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setGeometry(QRect(899, 130, 411, 300))
        self.frame_31.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.98, y1:0.471364, x2:1, y2:0.472, stop:1 rgba(0, 0, 0, 18));\n"
"border-style: outset;\n"
"border-color:#FFF;\n"
"border-width:2px;\n"
"border-radius:30px;\n"
"\n"
"}")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setGeometry(QRect(10, 10, 81, 81))
        self.frame_32.setStyleSheet(u"background-image: url(:/newPrefix/icon/icons8-reflector-bulb-80.png);\n"
"border:none;\n"
"background-color:none;")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.lightintensity_label_3 = QLabel(self.frame_31)
        self.lightintensity_label_3.setObjectName(u"lightintensity_label_3")
        self.lightintensity_label_3.setGeometry(QRect(20, 130, 271, 101))
        self.lightintensity_label_3.setFont(font4)
        self.lightintensity_label_3.setStyleSheet(u"color: rgb(255, 170, 0);\n"
"border :none;\n"
"background-color:none;\n"
"font: 75 72pt \"Segoe UI Historic\";\n"
"font-weight:900;")
        self.lightintensity_slider_3 = QSlider(self.frame_31)
        self.lightintensity_slider_3.setObjectName(u"lightintensity_slider_3")
        self.lightintensity_slider_3.setGeometry(QRect(330, 50, 51, 221))
        self.lightintensity_slider_3.setStyleSheet(u"QSlider::groove:vertical {\n"
"    position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"    left: 2px; right: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 10px;\n"
"    background: green;\n"
"    margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"   \n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.527, y1:1, x2:0.532338, y2:0, stop:0.751244 rgba(255, 170, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"\n"
"	background-color: rgb(222, 223, 220);\n"
"\n"
"}")
        self.lightintensity_slider_3.setValue(30)
        self.lightintensity_slider_3.setOrientation(Qt.Vertical)
        self.airdevice_7 = QLabel(self.frame_31)
        self.airdevice_7.setObjectName(u"airdevice_7")
        self.airdevice_7.setGeometry(QRect(40, 240, 251, 31))
        self.airdevice_7.setStyleSheet(u"background-color:none;\n"
"font: 75 10pt \"Segoe UI Historic\";\n"
"border:none;\n"
"color: rgb(108, 108, 108);")
        self.frame_33 = QFrame(self.frame_23)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(1350, 130, 420, 300))
        self.frame_33.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.98, y1:0.471364, x2:1, y2:0.472, stop:1 rgba(0, 0, 0, 18));\n"
"border-style: outset;\n"
"border-color:#FFF;\n"
"border-width:2px;\n"
"border-radius:30px;\n"
"\n"
"}")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setGeometry(QRect(10, 10, 71, 71))
        self.frame_34.setStyleSheet(u"background-image: url(:/newPrefix/icon/icons8-home-64.png);\n"
"border:none;\n"
"background-color:none;")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setGeometry(QRect(20, 140, 111, 151))
        self.frame_35.setStyleSheet(u"QFrame{\n"
"background-color:none;\n"
"\n"
"}\n"
"QFrame:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"\n"
"}")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame_35)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 0, 91, 91))
        self.label_16.setStyleSheet(u"background:none;\n"
"background-image: url(:/newPrefix/icon/icons8-lock-96.png);\n"
"border:none;\n"
"")
        self.airdevice_8 = QLabel(self.frame_35)
        self.airdevice_8.setObjectName(u"airdevice_8")
        self.airdevice_8.setGeometry(QRect(20, 100, 71, 51))
        sizePolicy.setHeightForWidth(self.airdevice_8.sizePolicy().hasHeightForWidth())
        self.airdevice_8.setSizePolicy(sizePolicy)
        self.airdevice_8.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.airdevice_8.setStyleSheet(u"background-color:none;\n"
"font: 75 10pt \"Segoe UI Historic\";\n"
"border:none;\n"
"color: rgb(108, 108, 108);")
        self.airdevice_8.setScaledContents(False)
        self.airdevice_8.setWordWrap(True)
        self.pushButton = QPushButton(self.frame_35)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 0, 111, 151))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color:none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));\n"
"\n"
"}")
        self.frame_36 = QFrame(self.frame_33)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setGeometry(QRect(160, 140, 111, 151))
        self.frame_36.setStyleSheet(u"QFrame{\n"
"background-color:none;\n"
"\n"
"}\n"
"QFrame:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"}")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.frame_36)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 10, 91, 91))
        self.label_17.setStyleSheet(u"background:none;\n"
"background-image: url(:/newPrefix/icon/icons8-lock-96.png);\n"
"border:none;\n"
"")
        self.airdevice_9 = QLabel(self.frame_36)
        self.airdevice_9.setObjectName(u"airdevice_9")
        self.airdevice_9.setGeometry(QRect(30, 100, 71, 51))
        sizePolicy.setHeightForWidth(self.airdevice_9.sizePolicy().hasHeightForWidth())
        self.airdevice_9.setSizePolicy(sizePolicy)
        self.airdevice_9.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.airdevice_9.setStyleSheet(u"background-color:none;\n"
"font: 75 10pt \"Segoe UI Historic\";\n"
"border:none;\n"
"color: rgb(108, 108, 108);")
        self.airdevice_9.setScaledContents(False)
        self.airdevice_9.setWordWrap(True)
        self.pushButton_2 = QPushButton(self.frame_36)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 0, 111, 141))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background-color:none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));\n"
"\n"
"}")
        self.frame_37 = QFrame(self.frame_33)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setGeometry(QRect(290, 140, 111, 151))
        self.frame_37.setStyleSheet(u"QFrame{\n"
"background-color:none;\n"
"}\n"
"QFrame:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"}")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame_37)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 10, 91, 91))
        self.label_18.setStyleSheet(u"background:none;\n"
"background-image: url(:/newPrefix/icon/icons8-lock-96.png);\n"
"border:none;\n"
"")
        self.airdevice_10 = QLabel(self.frame_37)
        self.airdevice_10.setObjectName(u"airdevice_10")
        self.airdevice_10.setGeometry(QRect(40, 100, 71, 51))
        sizePolicy.setHeightForWidth(self.airdevice_10.sizePolicy().hasHeightForWidth())
        self.airdevice_10.setSizePolicy(sizePolicy)
        self.airdevice_10.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.airdevice_10.setStyleSheet(u"background-color:none;\n"
"font: 75 10pt \"Segoe UI Historic\";\n"
"border:none;\n"
"color: rgb(108, 108, 108);")
        self.airdevice_10.setScaledContents(False)
        self.airdevice_10.setWordWrap(True)
        self.pushButton_3 = QPushButton(self.frame_37)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 0, 111, 141))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background-color:none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));\n"
"\n"
"}")
        self.frame_38 = QFrame(self.frame_23)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setGeometry(QRect(90, 490, 300, 300))
        self.frame_38.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.98, y1:0.471364, x2:1, y2:0.472, stop:1 rgba(0, 0, 0, 18));\n"
"border-style: outset;\n"
"border-color:#FFF;\n"
"border-width:2px;\n"
"border-radius:30px;\n"
"\n"
"}")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.label_19 = QLabel(self.frame_38)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(-20, 10, 331, 81))
        font8 = QFont()
        font8.setFamily(u"sans-serif")
        font8.setPointSize(25)
        font8.setBold(True)
        font8.setItalic(False)
        font8.setWeight(75)
        self.label_19.setFont(font8)
        self.label_19.setStyleSheet(u"background-color:none;\n"
"font: 75 25pt \"sans-serif\";\n"
"border:none;\n"
"font-weight:600;\n"
"color: rgb(0, 170, 127);\n"
"")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_20 = QLabel(self.frame_38)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(-30, 150, 371, 131))
        font9 = QFont()
        font9.setFamily(u"sans-serif")
        font9.setPointSize(54)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setWeight(99)
        self.label_20.setFont(font9)
        self.label_20.setStyleSheet(u"background-color:none;\n"
"font: 75 54pt \"sans-serif\";\n"
"border:none;\n"
"font-weight:3000;\n"
"\n"
"color: rgb(0, 170, 127);")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_21 = QLabel(self.frame_38)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 90, 301, 61))
        font10 = QFont()
        font10.setFamily(u"sans-serif")
        font10.setPointSize(26)
        font10.setBold(True)
        font10.setItalic(False)
        font10.setWeight(99)
        self.label_21.setFont(font10)
        self.label_21.setStyleSheet(u"background-color:none;\n"
"\n"
"font: 75 26pt \"sans-serif\";\n"
"border:none;\n"
"font-weight:800;\n"
"color: rgb(0, 170, 127);")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.frame_39 = QFrame(self.frame_23)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setGeometry(QRect(420, 490, 611, 311))
        self.frame_39.setStyleSheet(u"QFrame{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.98, y1:0.471364, x2:1, y2:0.472, stop:1 rgba(0, 0, 0, 18));\n"
"border-style: outset;\n"
"border-color:#FFF;\n"
"border-width:2px;\n"
"border-radius:30px;\n"
"\n"
"}")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.frame_40 = QFrame(self.frame_39)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setGeometry(QRect(20, 10, 121, 131))
        self.frame_40.setStyleSheet(u"background-image: url(:/newPrefix/icon/icons8-temperature-128.png);\n"
"background-color:none;\n"
"border:none;")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.ariconditioner_label_5 = QLabel(self.frame_39)
        self.ariconditioner_label_5.setObjectName(u"ariconditioner_label_5")
        self.ariconditioner_label_5.setGeometry(QRect(-50, 180, 271, 101))
        self.ariconditioner_label_5.setFont(font4)
        self.ariconditioner_label_5.setStyleSheet(u"color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(8, 137, 231, 255));\n"
"border :none;\n"
"background-color:none;\n"
"\n"
"font: 75 72pt \"Segoe UI Historic\";\n"
"font-weight:900;")
        self.ariconditioner_label_5.setAlignment(Qt.AlignCenter)
        self.label_22 = QLabel(self.frame_39)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(40, 140, 231, 41))
        self.label_22.setFont(font3)
        self.label_22.setStyleSheet(u"background-color:none;\n"
"font: 75 14pt \"Segoe UI Historic\";\n"
"border:none;\n"
"font-weight:800;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.circularProgress_2 = QFrame(self.frame_39)
        self.circularProgress_2.setObjectName(u"circularProgress_2")
        self.circularProgress_2.setGeometry(QRect(310, 10, 291, 291))
        self.circularProgress_2.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"	border-radius: 140px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:228.3, stop:0.940299 rgba(255, 255, 255, 255), stop:0.970149 rgba(0, 255, 25, 255));\n"
"}")
        self.circularProgress_2.setFrameShape(QFrame.NoFrame)
        self.circularProgress_2.setFrameShadow(QFrame.Raised)
        self.circularbg_2 = QFrame(self.circularProgress_2)
        self.circularbg_2.setObjectName(u"circularbg_2")
        self.circularbg_2.setGeometry(QRect(0, 0, 291, 291))
        self.circularbg_2.setStyleSheet(u"QFrame{\n"
"\n"
"\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0.98, y1:0.471364, x2:1, y2:0.472, stop:1 rgba(0, 0, 0, 18));\n"
"}\n"
"")
        self.circularbg_2.setFrameShape(QFrame.StyledPanel)
        self.circularbg_2.setFrameShadow(QFrame.Raised)
        self.dial_2 = QDial(self.circularbg_2)
        self.dial_2.setObjectName(u"dial_2")
        self.dial_2.setGeometry(QRect(0, 0, 291, 291))
        self.dial_2.setStyleSheet(u"")
        self.dial_2.setMaximum(60)
        self.dial_2.setSingleStep(5)
        self.dial_2.setPageStep(5)
        self.dial_2.setValue(5)
        self.dial_2.setSliderPosition(5)
        self.dial_2.setOrientation(Qt.Vertical)
        self.dial_2.setInvertedAppearance(False)
        self.dial_2.setInvertedControls(True)
        self.dial_2.setWrapping(False)
        self.dial_2.setNotchTarget(0.050000000000000)
        self.dial_2.setNotchesVisible(True)
        self.ariconditioner_label_6 = QLabel(self.frame_39)
        self.ariconditioner_label_6.setObjectName(u"ariconditioner_label_6")
        self.ariconditioner_label_6.setGeometry(QRect(170, 180, 271, 101))
        self.ariconditioner_label_6.setFont(font4)
        self.ariconditioner_label_6.setStyleSheet(u"color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(8, 137, 231, 255));\n"
"border :none;\n"
"background-color:none;\n"
"\n"
"font: 75 72pt \"Segoe UI Historic\";\n"
"font-weight:900;")
        self.label_29 = QLabel(self.frame_39)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(120, 10, 191, 41))
        self.label_29.setFont(font3)
        self.label_29.setStyleSheet(u"background-color:none;\n"
"font: 75 14pt \"Segoe UI Historic\";\n"
"border:none;\n"
"font-weight:800;\n"
"color: rgb(255, 0, 127);\n"
"")
        self.ariconditioner_label_12 = QLabel(self.frame_39)
        self.ariconditioner_label_12.setObjectName(u"ariconditioner_label_12")
        self.ariconditioner_label_12.setGeometry(QRect(230, 50, 31, 51))
        font11 = QFont()
        font11.setFamily(u"Segoe UI Historic")
        font11.setPointSize(40)
        font11.setBold(True)
        font11.setItalic(False)
        font11.setWeight(99)
        self.ariconditioner_label_12.setFont(font11)
        self.ariconditioner_label_12.setStyleSheet(u"color: rgb(255, 0, 127);\n"
"border :none;\n"
"background-color:none;\n"
"\n"
"font: 75 40pt \"Segoe UI Historic\";\n"
"font-weight:900;")
        self.ariconditioner_label_13 = QLabel(self.frame_39)
        self.ariconditioner_label_13.setObjectName(u"ariconditioner_label_13")
        self.ariconditioner_label_13.setGeometry(QRect(160, 50, 71, 71))
        self.ariconditioner_label_13.setFont(font11)
        self.ariconditioner_label_13.setStyleSheet(u"color: rgb(255, 0, 127);\n"
"border :none;\n"
"background-color:none;\n"
"\n"
"font: 75 40pt \"Segoe UI Historic\";\n"
"font-weight:900;")
        self.ariconditioner_label_13.setAlignment(Qt.AlignCenter)
        self.frame_41 = QFrame(self.frame_23)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setGeometry(QRect(1080, 490, 311, 311))
        self.frame_41.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.98, y1:0.471364, x2:1, y2:0.472, stop:1 rgba(0, 0, 0, 18));\n"
"border-style: outset;\n"
"border-color:#FFF;\n"
"border-width:2px;\n"
"border-radius:30px;\n"
"\n"
"}")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.frame_47 = QFrame(self.frame_41)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setGeometry(QRect(100, 140, 101, 101))
        self.frame_47.setStyleSheet(u"background-image: url(:/newPrefix/icon/icons8-cyber-security-100.png);\n"
"border:none;\n"
"background-color:none;")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.label_28 = QLabel(self.frame_41)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(20, 70, 241, 41))
        self.label_28.setFont(font3)
        self.label_28.setStyleSheet(u"background-color:none;\n"
"font: 75 14pt \"Segoe UI Historic\";\n"
"border:none;\n"
"font-weight:800;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.frame_48 = QFrame(self.frame_41)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setGeometry(QRect(20, 20, 51, 51))
        self.frame_48.setStyleSheet(u"background-image: url(:/newPrefix/icon/icons8-secure-50.png);\n"
"border:none;\n"
"background-color:none;")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.frame_42 = QFrame(self.frame_23)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setGeometry(QRect(1450, 490, 311, 311))
        self.frame_42.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.98, y1:0.471364, x2:1, y2:0.472, stop:1 rgba(0, 0, 0, 18));\n"
"border-style: outset;\n"
"border-color:#FFF;\n"
"border-width:2px;\n"
"border-radius:30px;\n"
"\n"
"}")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setGeometry(QRect(10, -20, 421, 341))
        self.frame_43.setStyleSheet(u"border:none;\n"
"background:none;")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setGeometry(QRect(10, 30, 61, 61))
        self.frame_44.setStyleSheet(u"background-image: url(:/newPrefix/icon/icons8-eye-64.png);\n"
"border:none;\n"
"background-color:none;")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.frame_45 = QFrame(self.frame_43)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setGeometry(QRect(20, 150, 111, 151))
        self.frame_45.setStyleSheet(u"QFrame{\n"
"background-color:none;\n"
"\n"
"}\n"
"QFrame:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"\n"
"}")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.label_25 = QLabel(self.frame_45)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(30, 10, 51, 61))
        self.label_25.setStyleSheet(u"background:none;\n"
"background-image: url(:/newPrefix/icon/icons8-camera-64.png);\n"
"border:none;\n"
"")
        self.airdevice_11 = QLabel(self.frame_45)
        self.airdevice_11.setObjectName(u"airdevice_11")
        self.airdevice_11.setGeometry(QRect(30, 100, 71, 51))
        sizePolicy.setHeightForWidth(self.airdevice_11.sizePolicy().hasHeightForWidth())
        self.airdevice_11.setSizePolicy(sizePolicy)
        self.airdevice_11.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.airdevice_11.setStyleSheet(u"background-color:none;\n"
"font: 75 10pt \"Segoe UI Historic\";\n"
"border:none;\n"
"color: rgb(108, 108, 108);")
        self.airdevice_11.setScaledContents(False)
        self.airdevice_11.setWordWrap(True)
        self.frame_46 = QFrame(self.frame_43)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setGeometry(QRect(160, 150, 111, 151))
        self.frame_46.setStyleSheet(u"QFrame{\n"
"background-color:none;\n"
"\n"
"}\n"
"QFrame:hover{\n"
"\n"
"background-color:rgb(48,57,66);\n"
"\n"
"\n"
"\n"
"}")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.airdevice_12 = QLabel(self.frame_46)
        self.airdevice_12.setObjectName(u"airdevice_12")
        self.airdevice_12.setGeometry(QRect(30, 100, 71, 51))
        sizePolicy.setHeightForWidth(self.airdevice_12.sizePolicy().hasHeightForWidth())
        self.airdevice_12.setSizePolicy(sizePolicy)
        self.airdevice_12.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.airdevice_12.setStyleSheet(u"background-color:none;\n"
"font: 75 10pt \"Segoe UI Historic\";\n"
"border:none;\n"
"color: rgb(108, 108, 108);")
        self.airdevice_12.setScaledContents(False)
        self.airdevice_12.setWordWrap(True)
        self.label_27 = QLabel(self.frame_43)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 90, 241, 41))
        self.label_27.setFont(font3)
        self.label_27.setStyleSheet(u"background-color:none;\n"
"font: 75 14pt \"Segoe UI Historic\";\n"
"border:none;\n"
"font-weight:800;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_23 = QLabel(self.frame_23)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(930, 220, 181, 41))
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet(u"background-color:none;\n"
"font: 75 14pt \"Segoe UI Historic\";\n"
"border:none;\n"
"font-weight:800;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_24 = QLabel(self.frame_23)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(1380, 220, 241, 41))
        self.label_24.setFont(font3)
        self.label_24.setStyleSheet(u"background-color:none;\n"
"font: 75 14pt \"Segoe UI Historic\";\n"
"border:none;\n"
"font-weight:800;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.pushButton_4 = QPushButton(self.frame_23)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(1440, 820, 121, 31))
        self.pushButton_5 = QPushButton(self.frame_23)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(1590, 820, 121, 31))
        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(1660, 640, 51, 61))
        self.label_26.setStyleSheet(u"background:none;\n"
"background-image: url(:/newPrefix/icon/icons8-camera-64.png);\n"
"border:none;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SmarT Tech IOT Dashboard", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Good Morning,", None))
        self.userlabel.setText(QCoreApplication.translate("MainWindow", u"Selcuk !", None))
        self.status_label1.setText(QCoreApplication.translate("MainWindow", u"Bedroom TV is ON.", None))
        self.see_more.setText(QCoreApplication.translate("MainWindow", u"see more >", None))
        self.status_label2.setText(QCoreApplication.translate("MainWindow", u"Speaker is playing.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Air Conditioner", None))
        self.ariconditioner_label.setText(QCoreApplication.translate("MainWindow", u"22.5\u00b0", None))
        self.airdevice.setText(QCoreApplication.translate("MainWindow", u"2 devices active", None))
        self.lightintensity_label_2.setText(QCoreApplication.translate("MainWindow", u"54 %", None))
        self.airdevice_2.setText(QCoreApplication.translate("MainWindow", u"4 lights ON right now", None))
        self.label_6.setText("")
        self.airdevice_3.setText(QCoreApplication.translate("MainWindow", u"Bedroom Windows", None))
        self.label_7.setText("")
        self.airdevice_4.setText(QCoreApplication.translate("MainWindow", u"Front Door", None))
        self.label_8.setText("")
        self.airdevice_5.setText(QCoreApplication.translate("MainWindow", u"Door", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"25 JAN 2022", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"00:52", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"MONDAY", None))
        self.ariconditioner_label_2.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Global Temperature", None))
        self.ariconditioner_label_3.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Light Intensity", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Doors and Windows", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"SmarT Tech IOT Dashboard", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Good Morning,", None))
        self.userlabel_2.setText(QCoreApplication.translate("MainWindow", u"Selcuk !", None))
        self.status_label1_2.setText(QCoreApplication.translate("MainWindow", u"Bedroom TV is ON.", None))
        self.see_more_2.setText(QCoreApplication.translate("MainWindow", u"see more >", None))
        self.status_label2_2.setText(QCoreApplication.translate("MainWindow", u"Speaker is playing.", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Air Conditioner", None))
        self.ariconditioner_label_4.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.airdevice_6.setText(QCoreApplication.translate("MainWindow", u"2 devices active", None))
        self.ariconditioner_label_7.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.ariconditioner_label_8.setText(QCoreApplication.translate("MainWindow", u"5\u00b0", None))
        self.ariconditioner_label_9.setText(QCoreApplication.translate("MainWindow", u"15\u00b0", None))
        self.ariconditioner_label_10.setText(QCoreApplication.translate("MainWindow", u"-15\u00b0", None))
        self.ariconditioner_label_11.setText(QCoreApplication.translate("MainWindow", u"30\u00b0", None))
        self.lightintensity_label_3.setText(QCoreApplication.translate("MainWindow", u"54 %", None))
        self.airdevice_7.setText(QCoreApplication.translate("MainWindow", u"4 lights ON right now", None))
        self.label_16.setText("")
        self.airdevice_8.setText(QCoreApplication.translate("MainWindow", u"Bedroom Windows", None))
        self.pushButton.setText("")
        self.label_17.setText("")
        self.airdevice_9.setText(QCoreApplication.translate("MainWindow", u"Front Door", None))
        self.pushButton_2.setText("")
        self.label_18.setText("")
        self.airdevice_10.setText(QCoreApplication.translate("MainWindow", u"Door", None))
        self.pushButton_3.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"25 JAN 2022", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"00:52", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"MONDAY", None))
        self.ariconditioner_label_5.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Global Temperature", None))
        self.ariconditioner_label_6.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Set Temperature:", None))
        self.ariconditioner_label_12.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.ariconditioner_label_13.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Security", None))
        self.label_25.setText("")
        self.airdevice_11.setText(QCoreApplication.translate("MainWindow", u"Outdoor corner", None))
        self.airdevice_12.setText(QCoreApplication.translate("MainWindow", u"Outdoor garden", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Surveillance Cameras", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Light Intensity", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Doors and Windows", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"connect", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"disconnect", None))
        self.label_26.setText("")
    # retranslateUi

