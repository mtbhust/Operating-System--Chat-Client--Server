# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import socket

import socket
from threading import Thread
from queue import Queue
import random
def encoding(message):
    message = message.encode("utf-8")
    return message
def decoding(message):
    message = message.decode("utf-8")
    return message
class ClientChat:
    def __init__(self, host, port):
        host = socket.gethostbyname(socket.gethostname())
        port = random.randint(6000,10000)
        self.host = host
        self.port = port
        self.name = "Guest"
        self.messageQueue = Queue()
        self.server = (self.host, 1235)
    def createSocket(self):
        try:
            print(f"Creating chat client on host {self.host}, port {self.port}")
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.clientSocket.bind((self.host, self.port))
            print(f"Creating chat client on host {self.host}, port {self.port} sucessfully")
        except Exception as e:
            print(e)
            print(f"Creating chat client on host {self.host}, port {self.port} failed")
    def defineUser(self):
        name = input("Enter your name: ")
        if name != "":
            self.name = name
        try:
            self.clientSocket.sendto(encoding(self.name + "join the chat server"), self.server)
        except:
            print("error")
    def messageReciever(self):
        while True:
            try:
                message, address = self.clientSocket.recvfrom(1024)
                print(message)
                self.messageQueue.put((message, address))
            except: 
                pass
    def startThread(self):
        reciever = Thread(target= self.messageReciever)
        reciever.start()

    def run(self):
        while True:
            message = input()
            if (message == 'quit'):
                break
            if message =='':
                continue
            message = self.name +":" + message
            message = encoding(message)
            self.clientSocket.sendto(message,self.server)
        self.clientSocket.sendto(encoding('qqq'), server)
        self.clientSocket.close(
        os._exit(1)
        )

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/chat.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 461, 91))
        self.groupBox.setStyleSheet("background-color:rgb(233, 210, 255)")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(50, 20, 113, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(220, 239, 255)")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 20, 61, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(220, 239, 255)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(330, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label.setStyleSheet("background-color: rgb(134, 74, 255)rgb(255, 48, 238)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 47, 13))
        self.label_2.setStyleSheet("background-color: rgb(134, 74, 255)rgb(255, 48, 238)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(190, 50, 47, 13))
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 130, 461, 381))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 520, 371, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 530, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Server"))
        self.lineEdit.setText(_translate("MainWindow", "host"))
        self.lineEdit_2.setText(_translate("MainWindow", "port"))
        self.pushButton.setText(_translate("MainWindow", "connect"))
        self.label.setText(_translate("MainWindow", "host"))
        self.label_2.setText(_translate("MainWindow", "port"))
        self.label_3.setText(_translate("MainWindow", "status"))
        self.pushButton_2.setText(_translate("MainWindow", "Send"))
def connectClicked():
        Thread(target=clientThread).start()
def clientThread():
    client =  ClientChat(1, 1)
    client.createSocket()
    client.name = "ManhTruong"
    client.startThread()
    client.run()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(lambda: connectClicked())
    MainWindow.show()
    sys.exit(app.exec_())


