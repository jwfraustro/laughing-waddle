# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loadingDialog(object):
    def setupUi(self, loadingDialog):
        loadingDialog.setObjectName("loadingDialog")
        loadingDialog.resize(400, 104)
        loadingDialog.setMinimumSize(QtCore.QSize(400, 104))
        loadingDialog.setMaximumSize(QtCore.QSize(400, 104))
        self.verticalLayout = QtWidgets.QVBoxLayout(loadingDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(loadingDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.loadingLbl = QtWidgets.QLabel(loadingDialog)
        self.loadingLbl.setObjectName("loadingLbl")
        self.verticalLayout.addWidget(self.loadingLbl)
        self.progressBar = QtWidgets.QProgressBar(loadingDialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(loadingDialog)
        QtCore.QMetaObject.connectSlotsByName(loadingDialog)

    def retranslateUi(self, loadingDialog):
        _translate = QtCore.QCoreApplication.translate
        loadingDialog.setWindowTitle(_translate("loadingDialog", "HS Seller App - Loading..."))
        self.label.setText(_translate("loadingDialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Loading HangarSwap Seller App...</span></p></body></html>"))
        self.loadingLbl.setText(_translate("loadingDialog", "......"))

