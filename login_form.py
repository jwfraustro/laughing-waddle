# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(399, 284)
        LoginDialog.setMinimumSize(QtCore.QSize(399, 284))
        LoginDialog.setMaximumSize(QtCore.QSize(399, 284))
        self.buttonBox = QtWidgets.QDialogButtonBox(LoginDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(LoginDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gridLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 9, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.login_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_lbl.sizePolicy().hasHeightForWidth())
        self.login_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.login_lbl.setFont(font)
        self.login_lbl.setScaledContents(False)
        self.login_lbl.setWordWrap(True)
        self.login_lbl.setObjectName("login_lbl")
        self.verticalLayout.addWidget(self.login_lbl)
        self.userName_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userName_lbl.sizePolicy().hasHeightForWidth())
        self.userName_lbl.setSizePolicy(sizePolicy)
        self.userName_lbl.setObjectName("userName_lbl")
        self.verticalLayout.addWidget(self.userName_lbl)
        self.userName_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userName_le.sizePolicy().hasHeightForWidth())
        self.userName_le.setSizePolicy(sizePolicy)
        self.userName_le.setObjectName("userName_le")
        self.verticalLayout.addWidget(self.userName_le)
        self.pswd_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pswd_lbl.sizePolicy().hasHeightForWidth())
        self.pswd_lbl.setSizePolicy(sizePolicy)
        self.pswd_lbl.setObjectName("pswd_lbl")
        self.verticalLayout.addWidget(self.pswd_lbl)
        self.pswd_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pswd_le.setObjectName("pswd_le")
        self.verticalLayout.addWidget(self.pswd_le)

        self.retranslateUi(LoginDialog)
        self.buttonBox.accepted.connect(LoginDialog.accept)
        self.buttonBox.rejected.connect(LoginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "HangarSwap Dashboard Login"))
        self.login_lbl.setText(_translate("LoginDialog", "HangarSwap Seller Login"))
        self.userName_lbl.setText(_translate("LoginDialog", "    Username or Email:"))
        self.pswd_lbl.setText(_translate("LoginDialog", "    Password:"))

