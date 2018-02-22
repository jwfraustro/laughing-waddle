# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orders_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_catalogWidget(object):
    def setupUi(self, catalogWidget):
        catalogWidget.setObjectName("catalogWidget")
        catalogWidget.resize(614, 463)
        catalogWidget.setStyleSheet("background-color: rgb(231, 234, 239);")
        self.gridLayout = QtWidgets.QGridLayout(catalogWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.showLbl = QtWidgets.QLabel(catalogWidget)
        self.showLbl.setObjectName("showLbl")
        self.gridLayout.addWidget(self.showLbl, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(catalogWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.catalogTable = QtWidgets.QTableView(catalogWidget)
        self.catalogTable.setStyleSheet("alternate-background-color: rgb(241, 241, 241);\n"
"background-color: rgb(255, 255, 255);")
        self.catalogTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.catalogTable.setSortingEnabled(True)
        self.catalogTable.setObjectName("catalogTable")
        self.catalogTable.horizontalHeader().setCascadingSectionResizes(True)
        self.catalogTable.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.catalogTable, 4, 0, 1, 3)
        self.showCombo = QtWidgets.QComboBox(catalogWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showCombo.sizePolicy().hasHeightForWidth())
        self.showCombo.setSizePolicy(sizePolicy)
        self.showCombo.setMinimumSize(QtCore.QSize(81, 20))
        self.showCombo.setMaximumSize(QtCore.QSize(158, 20))
        self.showCombo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.showCombo.setObjectName("showCombo")
        self.showCombo.addItem("")
        self.showCombo.addItem("")
        self.showCombo.addItem("")
        self.showCombo.addItem("")
        self.gridLayout.addWidget(self.showCombo, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(catalogWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(catalogWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.retranslateUi(catalogWidget)
        QtCore.QMetaObject.connectSlotsByName(catalogWidget)

    def retranslateUi(self, catalogWidget):
        _translate = QtCore.QCoreApplication.translate
        catalogWidget.setWindowTitle(_translate("catalogWidget", "Form"))
        self.showLbl.setText(_translate("catalogWidget", "Show:"))
        self.label.setText(_translate("catalogWidget", "Search:"))
        self.showCombo.setItemText(0, _translate("catalogWidget", "10"))
        self.showCombo.setItemText(1, _translate("catalogWidget", "25"))
        self.showCombo.setItemText(2, _translate("catalogWidget", "50"))
        self.showCombo.setItemText(3, _translate("catalogWidget", "100"))
        self.label_2.setText(_translate("catalogWidget", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Order History</span></p></body></html>"))

