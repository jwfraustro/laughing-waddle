# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'catalog_widget.ui'
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
        self.catLbl = QtWidgets.QLabel(catalogWidget)
        self.catLbl.setObjectName("catLbl")
        self.gridLayout.addWidget(self.catLbl, 1, 0, 1, 1)
        self.categoryCombo = QtWidgets.QComboBox(catalogWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryCombo.sizePolicy().hasHeightForWidth())
        self.categoryCombo.setSizePolicy(sizePolicy)
        self.categoryCombo.setMinimumSize(QtCore.QSize(81, 20))
        self.categoryCombo.setMaximumSize(QtCore.QSize(158, 20))
        self.categoryCombo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.categoryCombo.setObjectName("categoryCombo")
        self.gridLayout.addWidget(self.categoryCombo, 2, 0, 1, 1)
        self.addProductBtn = QtWidgets.QPushButton(catalogWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addProductBtn.sizePolicy().hasHeightForWidth())
        self.addProductBtn.setSizePolicy(sizePolicy)
        self.addProductBtn.setMinimumSize(QtCore.QSize(81, 20))
        self.addProductBtn.setMaximumSize(QtCore.QSize(111, 20))
        self.addProductBtn.setStyleSheet("border-color: rgb(62, 112, 201);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(62, 112, 201);\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"")
        self.addProductBtn.setObjectName("addProductBtn")
        self.gridLayout.addWidget(self.addProductBtn, 2, 2, 1, 1)
        self.catalogTable = QtWidgets.QTableView(catalogWidget)
        self.catalogTable.setStyleSheet("alternate-background-color: rgb(241, 241, 241);\n"
"background-color: rgb(255, 255, 255);")
        self.catalogTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.catalogTable.setSortingEnabled(True)
        self.catalogTable.setObjectName("catalogTable")
        self.catalogTable.horizontalHeader().setCascadingSectionResizes(True)
        self.catalogTable.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.catalogTable, 3, 0, 1, 3)

        self.retranslateUi(catalogWidget)
        QtCore.QMetaObject.connectSlotsByName(catalogWidget)

    def retranslateUi(self, catalogWidget):
        _translate = QtCore.QCoreApplication.translate
        catalogWidget.setWindowTitle(_translate("catalogWidget", "Form"))
        self.catLbl.setText(_translate("catalogWidget", "Category Filter:"))
        self.addProductBtn.setText(_translate("catalogWidget", "Add Product +"))

