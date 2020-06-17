        # -*- coding: utf-8 -*-

        # Form implementation generated from reading ui file 'chat.ui'
        #
        # Created by: PyQt5 UI code generator 5.13.0
        #
        # WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QThread, QThreadPool

import Client
from Client import ClientChat
from threading import Thread
from queue import Queue

class Ui_MainWindow(object):
        msgQueue = Queue()
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(499, 591)
                MainWindow.setStyleSheet("")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
                self.groupBox.setGeometry(QtCore.QRect(18, 10, 461, 81))
                font = QtGui.QFont()
                font.setFamily("Microsoft PhagsPa")
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.groupBox.setFont(font)
                self.groupBox.setStyleSheet("background-color:rgb(233, 210, 255);\n"
                "border-radius: 5px")
                self.groupBox.setObjectName("groupBox")
                self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
                self.lineEdit.setGeometry(QtCore.QRect(84, 40, 111, 20))
                font = QtGui.QFont()
                font.setFamily("Microsoft PhagsPa")
                font.setPointSize(8)
                self.lineEdit.setFont(font)
                self.lineEdit.setStyleSheet("background-color: rgb(220, 239, 255)")
                self.lineEdit.setObjectName("lineEdit")
                self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
                self.lineEdit_2.setGeometry(QtCore.QRect(252, 39, 91, 20))
                font = QtGui.QFont()
                font.setFamily("Microsoft PhagsPa")
                font.setPointSize(8)
                self.lineEdit_2.setFont(font)
                self.lineEdit_2.setStyleSheet("background-color: rgb(220, 239, 255)")
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.pushButton = QtWidgets.QPushButton(self.groupBox)
                self.pushButton.setGeometry(QtCore.QRect(362, 33, 75, 23))
                font = QtGui.QFont()
                font.setFamily("Microsoft PhagsPa")
                font.setPointSize(10)
                self.pushButton.setFont(font)
                self.pushButton.setStyleSheet("background-color: rgb(137, 178, 255);\n"
                "border-radius:0px")
                self.pushButton.setObjectName("pushButton")
                self.label = QtWidgets.QLabel(self.groupBox)
                self.label.setGeometry(QtCore.QRect(43, 43, 47, 13))
                font = QtGui.QFont()
                font.setFamily("Microsoft PhagsPa")
                font.setPointSize(10)
                self.label.setFont(font)
                self.label.setStyleSheet("background-color: rgb(134, 74, 255)rgb(255, 48, 238)")
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.groupBox)
                self.label_2.setGeometry(QtCore.QRect(219, 43, 47, 13))
                font = QtGui.QFont()
                font.setFamily("Microsoft PhagsPa")
                font.setPointSize(10)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("background-color: rgb(134, 74, 255)rgb(255, 48, 238)")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.groupBox)
                self.label_3.setGeometry(QtCore.QRect(29, 59, 391, 20))
                font = QtGui.QFont()
                font.setFamily("Microsoft PhagsPa")
                font.setPointSize(10)
                self.label_3.setFont(font)
                self.label_3.setFrameShape(QtWidgets.QFrame.Panel)
                self.label_3.setAlignment(QtCore.Qt.AlignCenter)
                self.label_3.setObjectName("label_3")
                self.label_10 = QtWidgets.QLabel(self.groupBox)
                self.label_10.setGeometry(QtCore.QRect(42, 15, 81, 16))
                font = QtGui.QFont()
                font.setFamily("Microsoft PhagsPa")
                font.setPointSize(9)
                self.label_10.setFont(font)
                self.label_10.setStyleSheet("background-color: rgb(134, 74, 255)rgb(255, 48, 238)")
                self.label_10.setObjectName("label_10")
                self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
                self.lineEdit_3.setGeometry(QtCore.QRect(108, 14, 131, 20))
                font = QtGui.QFont()
                font.setFamily("Microsoft PhagsPa")
                font.setPointSize(8)
                self.lineEdit_3.setFont(font)
                self.lineEdit_3.setStyleSheet("background-color: rgb(220, 239, 255)")
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.label_3.raise_()
                self.lineEdit.raise_()
                self.lineEdit_2.raise_()
                self.label.raise_()
                self.label_2.raise_()
                self.pushButton.raise_()
                self.label_10.raise_()
                self.lineEdit_3.raise_()
                self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
                self.textEdit.setGeometry(QtCore.QRect(18, 502, 391, 31))
                font = QtGui.QFont()
                font.setFamily("Microsoft PhagsPa")
                font.setPointSize(10)
                self.textEdit.setFont(font)
                self.textEdit.setStyleSheet("border-radius: 10px")
                self.textEdit.setTabChangesFocus(False)
                self.textEdit.setObjectName("textEdit")
                self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
                self.groupBox_2.setGeometry(QtCore.QRect(18, 93, 461, 31))
                font = QtGui.QFont()
                font.setFamily("Microsoft PhagsPa")
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.groupBox_2.setFont(font)
                self.groupBox_2.setStyleSheet("background-color:rgb(233, 210, 255);\n"
                "border-radius: 5px")
                self.groupBox_2.setObjectName("groupBox_2")
                self.label_4 = QtWidgets.QLabel(self.groupBox_2)
                self.label_4.setGeometry(QtCore.QRect(77, 11, 47, 13))
                font = QtGui.QFont()
                font.setFamily("Microsoft PhagsPa")
                font.setPointSize(10)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("background-color: rgb(134, 74, 255)rgb(255, 48, 238)")
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.groupBox_2)
                self.label_5.setGeometry(QtCore.QRect(258, 12, 47, 13))
                font = QtGui.QFont()
                font.setFamily("Microsoft PhagsPa")
                font.setPointSize(10)
                self.label_5.setFont(font)
                self.label_5.setStyleSheet("background-color: rgb(134, 74, 255)rgb(255, 48, 238)")
                self.label_5.setObjectName("label_5")
                self.label_7 = QtWidgets.QLabel(self.groupBox_2)
                self.label_7.setGeometry(QtCore.QRect(116, 11, 121, 20))
                font = QtGui.QFont()
                font.setFamily("Microsoft PhagsPa")
                font.setPointSize(10)
                self.label_7.setFont(font)
                self.label_7.setStyleSheet("background-color: rgb(134, 74, 255)rgb(255, 48, 238)")
                self.label_7.setObjectName("label_7")
                self.label_8 = QtWidgets.QLabel(self.groupBox_2)
                self.label_8.setGeometry(QtCore.QRect(293, 11, 141, 16))
                font = QtGui.QFont()
                font.setFamily("Microsoft PhagsPa")
                font.setPointSize(10)
                self.label_8.setFont(font)
                self.label_8.setStyleSheet("background-color: rgb(134, 74, 255)rgb(255, 48, 238)")
                self.label_8.setObjectName("label_8")
                self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_3.setGeometry(QtCore.QRect(418, 506, 61, 23))
                font = QtGui.QFont()
                font.setFamily("Microsoft PhagsPa")
                font.setPointSize(10)
                self.pushButton_3.setFont(font)
                self.pushButton_3.setStyleSheet("background-color: rgb(137, 178, 255);\n"
                "border-radius:5px")
                self.pushButton_3.setObjectName("pushButton_3")
                self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
                self.groupBox_3.setGeometry(QtCore.QRect(18, 130, 461, 361))
                self.groupBox_3.setStyleSheet("border-radius:  10px;\n"
                "background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.318182 rgba(180, 100, 171, 169), stop:1 rgba(137, 171, 255, 255))")
                self.groupBox_3.setTitle("")
                self.groupBox_3.setObjectName("groupBox_3")
                self.scrollArea = QtWidgets.QScrollArea(self.groupBox_3)
                self.scrollArea.setGeometry(QtCore.QRect(7, 7, 445, 345))
                self.scrollArea.setAlignment(QtCore.Qt.AlignTop)
                self.scrollArea.setStyleSheet("")
                self.scrollArea.setWidgetResizable(True)
                self.scrollArea.setObjectName("scrollArea")
                self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
                self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 445, 345))
                self.scrollAreaWidgetContents_2.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
                self.label_11 = QtWidgets.QLabel(self.centralwidget)
                self.label_11.setGeometry(QtCore.QRect(190, 540, 391, 20))
                self.label_11.setObjectName("label_11")
                self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 499, 21))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                self.formLay = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_2)
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.groupBox.setTitle(_translate("MainWindow", "Chat"))
                self.lineEdit.setText(_translate("MainWindow", "Enter server host"))
                self.lineEdit_2.setText(_translate("MainWindow", "Enter server port"))
                self.pushButton.setText(_translate("MainWindow", "Connect"))
                self.label.setText(_translate("MainWindow", "Host     :"))
                self.label_2.setText(_translate("MainWindow", "Port:"))
                self.label_3.setText(_translate("MainWindow", "Please connect!"))
                self.label_10.setText(_translate("MainWindow", "Your Name"))
                self.lineEdit_3.setText(_translate("MainWindow", "Name..."))
                self.groupBox_2.setTitle(_translate("MainWindow", "YourAdd"))
                self.label_4.setText(_translate("MainWindow", "Host:"))
                self.label_5.setText(_translate("MainWindow", "Port:"))
                self.label_7.setText(_translate("MainWindow", "...."))
                self.label_8.setText(_translate("MainWindow", "...."))
                self.pushButton_3.setText(_translate("MainWindow", "Send"))
        def addOtherMessageLabel(self,message):
                label_ = QtWidgets.QLabel()
                label_.setFixedSize( 331, 20)
                label_.setStyleSheet("background-color:rgb(126, 167, 255)")
                label_.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                label_.setText(message) 
                self.formLay.addRow(label_)
                self.scrollAreaWidgetContents_2.show()
        def addMyMessageLabel(self,message):
                label_ = QtWidgets.QLabel()
                label_.setFixedSize( 331, 20)
                label_.setStyleSheet("background-color:rgb(145, 167, 255)")
                label_.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                label_.setText(message)
                self.formLay.addRow(label_)
                self.scrollAreaWidgetContents_2.show()
        def render(self):
                while True:
                        try:
                                message, address = self.client.messageQueue.get()
                                self.addOtherMessageLabel(message)
                        except:
                                pass
        class MyThread(QThread):
                # Create a counter thread
                def __init__(self,msgQueue):
                        QThread.__init__(self)
                        self.msgQueue = msgQueue
                def
                notEmpty = pyqtSignal(str)
                def run(self, msgQueue):
                        while not msgQueue.empty():
                                message, address = msgQueue.get()
                                try:
                                        message = message.decode('utf-8')
                                except:
                                        pass
                                self.notEmpty.emit(message)

        def connectButton(self):
                self.name = self.lineEdit_3.text()
                if (self.name == "" or self.name == "Name..."):
                        self.name = "Guest"
                        self.lineEdit_3.setText(self.name)
                hostS = self.lineEdit.text()
                portS = self.lineEdit_2.text()
                try:
                        self.client = ClientChat(hostS, portS)
                        check0 = self.client.createSocket()
                        self.client.defineUser(self.name)
                        if (check0 == 1):
                                self.label_3.setText("Connected to Server")
                                global self.msgQueue 
                                self.msgQueue= self.client.messageQueue
                                self.client.startThread()
                                Thread(target = self.render).start()
                                self.MyThread.notEmpty.connect(self.addOtherMessageLabel)
                                self.label_7.setText(self.client.hostC)
                                self.label_8.setText(str(self.client.portC))
                        else:
                                self.label_3.setText("Failed to connect")
                except:
                        self.label_3.setText("Please enter correct syntax")
        
        def sendButton(self):
                message = self.textEdit.toPlainText()
                
                if self.label_3.text() == "Connected to Server":
                        if len(message) > 256:
                                self.label_11.setText("Maximum 256 character")
                        elif message != "":
                                self.textEdit.setText("")
                                self.client.sendMessage(message)
                                self.label_11.setText("")
                                self.addMyMessageLabel(message)
                else:
                        self.label_11.setText("Please connect to Server")      

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        ui.pushButton.clicked.connect(lambda: ui.connectButton())
        ui.pushButton_3.clicked.connect(lambda: ui.sendButton())
        MainWindow.show()
        sys.exit(app.exec_())
