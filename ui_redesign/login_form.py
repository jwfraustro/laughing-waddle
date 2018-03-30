# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

import requests, bs4, requests.exceptions

from PyQt5 import QtCore, QtGui, QtWidgets

s = None
username = None

payload = {
    'Username':"",
    'Password':"",
    # 'authToken':""
}

class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Ui_Dialog, self).__init__(parent)
        self.setObjectName("Dialog")
        self.resize(547, 391)
        self.setStyleSheet("font: 9pt \"Open Sans\";")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hs_logoLbl = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hs_logoLbl.sizePolicy().hasHeightForWidth())
        self.hs_logoLbl.setSizePolicy(sizePolicy)
        self.hs_logoLbl.setText("")
        self.hs_logoLbl.setPixmap(QtGui.QPixmap("assets/imgs/HangarSwapLogo_sm1_new.png"))
        self.hs_logoLbl.setScaledContents(True)
        self.hs_logoLbl.setObjectName("hs_logoLbl")
        self.verticalLayout.addWidget(self.hs_logoLbl)
        self.sellerappLbl = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sellerappLbl.sizePolicy().hasHeightForWidth())
        self.sellerappLbl.setSizePolicy(sizePolicy)
        self.sellerappLbl.setObjectName("sellerappLbl")
        self.verticalLayout.addWidget(self.sellerappLbl)
        self.line = QtWidgets.QFrame(self)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.unLbl = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unLbl.sizePolicy().hasHeightForWidth())
        self.unLbl.setSizePolicy(sizePolicy)
        self.unLbl.setObjectName("unLbl")
        self.verticalLayout.addWidget(self.unLbl)
        self.unLE = QtWidgets.QLineEdit(self)
        self.unLE.setObjectName("unLE")
        self.verticalLayout.addWidget(self.unLE)
        self.passLbl = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passLbl.sizePolicy().hasHeightForWidth())
        self.passLbl.setSizePolicy(sizePolicy)
        self.passLbl.setObjectName("passLbl")
        self.verticalLayout.addWidget(self.passLbl)
        self.passLE = QtWidgets.QLineEdit(self)
        self.passLE.setObjectName("passLE")
        self.passLE.setEchoMode(2)
        self.verticalLayout.addWidget(self.passLE)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icons/HSAPP.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.handleLogin)
        self.pushButton_2.clicked.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HangarSwap Seller App Login"))
        self.sellerappLbl.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Seller App Login</span></p></body></html>"))
        self.unLbl.setText(_translate("Dialog", "Username / Email Address:"))
        self.passLbl.setText(_translate("Dialog", "Password:"))
        self.pushButton.setText(_translate("Dialog", "Submit"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))

    def reject(self):
        self.done(0)

    def handleLogin(self):
        try:
            foo = self.loginConnect()
        except requests.exceptions.ConnectionError:
            QtWidgets.QMessageBox.warning(self, 'Network Error', 'Network Connection Error: please check network, and restart program.', QtWidgets.QMessageBox.Ok)
            return
        if foo is True:
            self.accept()
        if foo is False:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Bad username or password', QtWidgets.QMessageBox.Ok )

    def loginConnect(self):
        payload['Username'] = self.unLE.text()
        payload['Password'] = self.passLE.text()

        global s
        global username

        s = requests.Session()
        p = s.post('https://www.hangarswap.com/Main/ProcessLogin', data=payload, verify=False, allow_redirects=False)
        print('posted login')
        if 'location' not in p.headers.keys():
            return False
        else:
            username = payload['Username']
            return True


    def getNetSesh(self):
        return s, username

import RESOURCES
