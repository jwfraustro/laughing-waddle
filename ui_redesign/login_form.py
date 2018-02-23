# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(547, 391)
        Dialog.setStyleSheet("font: 9pt \"Open Sans\";")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hs_logoLbl = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hs_logoLbl.sizePolicy().hasHeightForWidth())
        self.hs_logoLbl.setSizePolicy(sizePolicy)
        self.hs_logoLbl.setText("")
        self.hs_logoLbl.setPixmap(QtGui.QPixmap(":/imgs/HangarSwapLogo_sm1_new.png"))
        self.hs_logoLbl.setScaledContents(True)
        self.hs_logoLbl.setObjectName("hs_logoLbl")
        self.verticalLayout.addWidget(self.hs_logoLbl)
        self.sellerappLbl = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sellerappLbl.sizePolicy().hasHeightForWidth())
        self.sellerappLbl.setSizePolicy(sizePolicy)
        self.sellerappLbl.setObjectName("sellerappLbl")
        self.verticalLayout.addWidget(self.sellerappLbl)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.unLbl = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unLbl.sizePolicy().hasHeightForWidth())
        self.unLbl.setSizePolicy(sizePolicy)
        self.unLbl.setObjectName("unLbl")
        self.verticalLayout.addWidget(self.unLbl)
        self.unLE = QtWidgets.QLineEdit(Dialog)
        self.unLE.setObjectName("unLE")
        self.verticalLayout.addWidget(self.unLE)
        self.passLbl = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passLbl.sizePolicy().hasHeightForWidth())
        self.passLbl.setSizePolicy(sizePolicy)
        self.passLbl.setObjectName("passLbl")
        self.verticalLayout.addWidget(self.passLbl)
        self.passLE = QtWidgets.QLineEdit(Dialog)
        self.passLE.setObjectName("passLE")
        self.verticalLayout.addWidget(self.passLE)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.handleLogin)
        self.pushButton_2.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HangarSwap Seller App Login"))
        self.sellerappLbl.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Seller App Login</span></p></body></html>"))
        self.unLbl.setText(_translate("Dialog", "Username / Email Address:"))
        self.passLbl.setText(_translate("Dialog", "Password:"))
        self.pushButton.setText(_translate("Dialog", "Submit"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))

    def reject(self):
        return

    def handleLogin(self):
        if (self.unLE.text()=='admin' and
            self.passLE.text()=='test'):
            return True
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Bad user or password', QtWidgets.QMessageBox.Ok )

import RESOURCES
