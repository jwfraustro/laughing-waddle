# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginProgress(QtWidgets.QDialog):

    def setupUi(self):
        self.setObjectName("loginProgress")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(358, 100)
        self.setSizeGripEnabled(False)
        self.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel()
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.loadingLbl = QtWidgets.QLabel()
        self.loadingLbl.setObjectName("loadingLbl")
        self.verticalLayout.addWidget(self.loadingLbl)
        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("loginProgress", "Loading HangarSwap Seller App..."))
        self.label.setText(_translate("loginProgress", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Loading HangarSwap Seller App...</span></p></body></html>"))
        self.loadingLbl.setText(_translate("loginProgress", "......"))

