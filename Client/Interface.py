# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import mainWindow
from mainWindow import *

import nameDialog
from nameDialog import *

import Client 
from Client import *
import socket
from threading import Thread
from queue import Queue
import random

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(lambda: ui.connectClicked())
    MainWindow.show()
    sys.exit(app.exec_())