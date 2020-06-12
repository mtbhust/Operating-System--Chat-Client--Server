# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NameDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(263, 84)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 241, 61))
        self.groupBox.setStyleSheet("background-color:rgb(233, 210, 255);\n"
"border-radius: 5px")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(170, 20, 61, 23))
        self.pushButton.setStyleSheet("background-color:rgb(222, 242, 255);\n"
"border-radius: 5px")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 131, 20))
        self.lineEdit.setStyleSheet("background-color:rgb(222, 242, 255);\n"
"border-radius: 5px")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.returnName)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Enter your name:"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.lineEdit.setText(_translate("Dialog", "Name..."))
    def returnName(self):
        return self.lineEdit.text()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
