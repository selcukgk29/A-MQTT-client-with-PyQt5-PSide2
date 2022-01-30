import sys
import platform

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QLocale, QThread, QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QTimer, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap,QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5.QtCore import Qt, QThread, pyqtSignal

from ui_dashboard import Ui_MainWindow
import datetime
import time
import paho.mqtt.client as paho

broker = "localhost"

class thread(QThread):
    global globaltemp
    def __init__(self,parent=None):
        super(thread, self).__init__(parent)
    def run(self):
        def on_message(client, userdata, message):
            time.sleep(1)
            print("received message =", str(message.payload.decode("utf-8")))
            self.globaltemp=(str(message.payload.decode("utf-8")))
        globaltemp =0
        print("connecting to broker ", broker)
        print("subscribing ")
        client1 = paho.Client("TEMP")
        client1.connect(broker,port=1883)  # connect
        client1.on_message = on_message
        while True:
            client1.loop_start()
            client1.subscribe("heater/globaltemp")
            time.sleep(1)
            """client.disconnect() #disconnect"""
            client1.loop_stop()  # stop loop

class Dashboard(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.backthread = thread()
        self.backthread.start()
        self.defdial()
        self.defslider()
        self.deflightslider()
        self.doorwindow()
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.timeout.connect(self.temperature)
        self.dooroftime=QTimer(self)
        self.frontdoorofftime=QTimer(self)
        self.datime = datetime.datetime.now()
        timer.start(1000)
        self.show()
    def doorwindow(self):
        self.ui.pushButton.setCheckable(True)
        self.ui.pushButton_2.setCheckable(True)
        self.ui.pushButton.clicked.connect(self.bedwindow)
        self.ui.pushButton_2.clicked.connect(self.frontdooron)
        self.ui.pushButton_3.clicked.connect(self.dooron)
    def dooron(self):
        client = paho.Client("door")
        client.connect(broker, port=1883)
        butonstyle = """
                    background-color:none;          
                    background-image: url(:/newPrefix/icon/icons8-unlock-96.png);
                    border:none;
                    """
        self.ui.label_18.setStyleSheet(butonstyle)
        client.publish("Doorwindow/door", "on")
        self.ui.frame_37.setStyleSheet(
            "border-color:green; background-color: qlineargradient(spread:pad, x1:0, y1:0.267045, x2:1, y2:1, stop:1 rgba(0, 255, 0, 169));");
        self.dooroftime.start(1000)
        self.dooroftime.timeout.connect(self.dooroff)
    def dooroff(self):
        self.dooroftime.stop()
        client = paho.Client("door")
        client.connect(broker, port=1883)
        client.publish("Doorwindow/door", "off")

        butonstyle = """
                           background:none;
                           background-image: url(:/newPrefix/icon/icons8-lock-96.png);
                           border:none;                 
                           """
        self.ui.label_18.setStyleSheet(butonstyle)
        self.ui.frame_37.setStyleSheet(
            "border-color:red; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 178));")
    def frontdooron(self):
        client = paho.Client("frontdoor")
        client.connect(broker, port=1883)
        butonstyle = """
                    background-color:none;          
                    background-image: url(:/newPrefix/icon/icons8-unlock-96.png);
                    border:none;
                    """
        self.ui.label_17.setStyleSheet(butonstyle)
        client.publish("Doorwindow/frontdoor", "on")
        self.ui.frame_36.setStyleSheet(
            "border-color:green; background-color: qlineargradient(spread:pad, x1:0, y1:0.267045, x2:1, y2:1, stop:1 rgba(0, 255, 0, 169));");
        self.frontdoorofftime.start(1000)
        self.frontdoorofftime.timeout.connect(self.frontdooroff)
    def frontdooroff(self):
        self.frontdoorofftime.stop()
        client = paho.Client("door")
        client.connect(broker, port=1883)
        client.publish("Doorwindow/frontdoor", "off")

        butonstyle = """
                                   background:none;
                                   background-image: url(:/newPrefix/icon/icons8-lock-96.png);
                                   border:none;                 
                                   """
        self.ui.label_17.setStyleSheet(butonstyle)
        self.ui.frame_36.setStyleSheet(
            "border-color:red; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 178));")
    def bedwindow(self):
        client = paho.Client("bedwindowclient")
        client.connect(broker, port=1883)
        if self.ui.pushButton.isChecked():
            butonstyle = """
            background-color:none;          
            background-image: url(:/newPrefix/icon/icons8-unlock-96.png);
            border:none;
            """
            self.ui.label_16.setStyleSheet(butonstyle)
            client.publish("Doorwindow/bedwindow", "on")
            self.ui.frame_35.setStyleSheet(
                "border-color:green; background-color: qlineargradient(spread:pad, x1:0, y1:0.267045, x2:1, y2:1, stop:1 rgba(0, 255, 0, 169));");
        else:
            client.publish("Doorwindow/bedwindow", "off")

            butonstyle = """
                    background:none;
                    background-image: url(:/newPrefix/icon/icons8-lock-96.png);
                    border:none;                 
                    """
            self.ui.label_16.setStyleSheet(butonstyle)
            self.ui.frame_35.setStyleSheet(
                "border-color:red; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 178));")
    def frontdoor(self):
        client = paho.Client("frontdoor")
        client.connect(broker, port=1883)
        if self.ui.pushButton_2.isChecked():
            client.publish("Doorwindow/frontdoor", "on")

            butonstyle = """
            background-color:none;          
            background-image: url(:/newPrefix/icon/icons8-unlock-96.png);
            border:none;
            """
            self.ui.label_17.setStyleSheet(butonstyle)
            self.ui.frame_36.setStyleSheet(
                "border-color:green; background-color: qlineargradient(spread:pad, x1:0, y1:0.267045, x2:1, y2:1, stop:1 rgba(0, 255, 0, 169));");
        else:
            client.publish("Doorwindow/frontdoor", "off")

            butonstyle = """
                    background:none;
                    background-image: url(:/newPrefix/icon/icons8-lock-96.png);
                    border:none;                 
                    """
            self.ui.label_17.setStyleSheet(butonstyle)
            self.ui.frame_36.setStyleSheet(
                "border-color:red; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 178));")
    def showtime(self):
        current_time = QTime.currentTime()
        datetime = QDateTime.currentDateTime()
        self.ui.label_21.setText(self.datime.strftime("%A"))
        self.ui.label_19.setText(datetime.toString("dd.MM.yyyy"))
        self.ui.label_20.setText(current_time.toString('hh:mm'))
    def defslider(self):
        self.ui.airconditione_slider_2.setValue(15)
        self.ui.airconditione_slider_2.setMinimum(-15)
        self.ui.airconditione_slider_2.setMaximum(30)
        self.ui.airconditione_slider_2.valueChanged.connect(self.slider)
    def slider(self):
        client = paho.Client("airconditioner")
        client.connect(broker, port=1883)
        val = self.ui.airconditione_slider_2.value()
        client.publish("sliders/Airconditioner",val)
        self.ui.ariconditioner_label_4.setText(str(val))
    def deflightslider(self):
        self.ui.lightintensity_slider_3.setMinimum(0)
        self.ui.lightintensity_slider_3.setMaximum(100)
        self.ui.lightintensity_slider_3.setValue(80)
        self.ui.lightintensity_label_3.setText("80 %")
        self.ui.lightintensity_slider_3.valueChanged.connect(self.lightslider)
    def lightslider(self):
        client = paho.Client("airconditioner")
        client.connect(broker, port=1883)
        val = self.ui.lightintensity_slider_3.value()
        client.publish("sliders/lightslider", val)
        self.ui.lightintensity_label_3.setText(str(val) + "%")
    def defdial(self):
        self.ui.dial.setMinimum(0)
        self.ui.dial.setMaximum(60)
        self.ui.dial_2.setValue(20)
        self.progressBarValue(20)
        self.ui.ariconditioner_label_5.setText("19")
        self.ui.dial_2.valueChanged.connect(self.dialmoved)
    def dialmoved(self):
        self.value=self.ui.dial_2.value()
        self.ui.ariconditioner_label_13.setText(str(self.value))
        self.progressBarValue(self.value)
        client = paho.Client("client1")
        client.connect(broker,port=1883)
        client.publish("heater/settemp", self.value)
    def temperature(self):
        self.ui.ariconditioner_label_5.setText(self.backthread.globaltemp)
        if int(self.backthread.globaltemp) > 0 and int(self.backthread.globaltemp) <= 20:
            bg = """
                        QFrame{
            	background-color: qlineargradient(spread:pad, x1:0.885373, y1:0.483, x2:1, y2:0.482955, stop:0.960199 rgba(174, 201, 255, 255), stop:1 rgba(255, 255, 255, 255));
            border-style: outset;border-color:#FFF;
            border-width:2px;
            border-radius:30px;
            }
                        """
            self.ui.frame_39.setStyleSheet(bg)
            self.ui.ariconditioner_label_5.setStyleSheet(
                "color:rgb(52, 107, 235); background-color:none; border:none;")
            self.ui.ariconditioner_label_6.setStyleSheet(
                "color:rgb(52, 107, 235); background-color:none; border:none;")
            self.ui.label_22.setStyleSheet("color:rgb(52, 107, 235); background-color:none; border:none;")

        if  int(self.backthread.globaltemp)>= 20 and  int(self.backthread.globaltemp)<= 40:
            bg = """
                                    QFrame{
            	background-color: qlineargradient(spread:pad, x1:0.965174, y1:0, x2:1, y2:0, stop:0.318408 rgba(255, 175, 134, 255), stop:1 rgba(255, 255, 255, 255));            border-width:2px;
                        border-radius:30px;
                        }
                                    """

            self.ui.frame_39.setStyleSheet(bg)
            self.ui.ariconditioner_label_5.setStyleSheet(
                "	color: rgb(255, 85, 0); background-color:none; border:none;")
            self.ui.ariconditioner_label_6.setStyleSheet(
                "	color: rgb(255, 85, 0); background-color:none; border:none;")
            self.ui.label_22.setStyleSheet("color:rgb(255, 85, 0); background-color:none; border:none;")

        if  int(self.backthread.globaltemp) > 40 and  int(self.backthread.globaltemp) <= 60:
            bg = """
                                                QFrame{
            	                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.965174 rgba(255, 83, 83, 255), stop:1 rgba(255, 153, 153, 255));                        border-radius:30px;
                                    }
                                                """

            self.ui.frame_39.setStyleSheet(bg)
            self.ui.ariconditioner_label_5.setStyleSheet(
                "color: rgb(255, 0, 0);background-color:none; border:none;")
            self.ui.ariconditioner_label_6.setStyleSheet(
                "color: rgb(255, 0, 0); background-color:none; border:none;")
            self.ui.label_22.setStyleSheet("color:rgb(255, 0, 0); background-color:none; border:none;")
    def progressBarValue(self, value):
        styleSheet = """
               QFrame{
               border-radius:140px;
               background-color:qconicalgradient(cx:0.509975, cy:0.506, angle:240.9, stop:{STOP_1} rgba(255,0,127,0), stop:{STOP_2} rgba(85,170,255,255));
               }     
               """
        progress = (70 - value) / 60.0
        stop_1 = str(progress - 0.07)
        stop_2 = str(progress)
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
        self.ui.circularProgress_2.setStyleSheet(newStylesheet)

app = QApplication(sys.argv)
dashboard = Dashboard()
sys.exit(app.exec_())
