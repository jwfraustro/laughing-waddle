# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_product_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ListItemWidget(object):
    def setupUi(self, ListItemWidget):
        ListItemWidget.setObjectName("ListItemWidget")
        ListItemWidget.resize(628, 658)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ListItemWidget.sizePolicy().hasHeightForWidth())
        ListItemWidget.setSizePolicy(sizePolicy)
        ListItemWidget.setMaximumSize(QtCore.QSize(628, 658))
        ListItemWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.verticalLayoutWidget = QtWidgets.QWidget(ListItemWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 591))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.newproduct_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newproduct_lbl.sizePolicy().hasHeightForWidth())
        self.newproduct_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.newproduct_lbl.setFont(font)
        self.newproduct_lbl.setObjectName("newproduct_lbl")
        self.verticalLayout.addWidget(self.newproduct_lbl)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.name_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.name_lbl.setObjectName("name_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_lbl)
        self.name_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.name_le.setObjectName("name_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_le)
        self.desc_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.desc_lbl.setObjectName("desc_lbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.desc_lbl)
        self.desc_te = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.desc_te.setObjectName("desc_te")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.desc_te)
        self.cat_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cat_lbl.setObjectName("cat_lbl")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.cat_lbl)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.cat_options = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cat_options.sizePolicy().hasHeightForWidth())
        self.cat_options.setSizePolicy(sizePolicy)
        self.cat_options.setObjectName("cat_options")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.cat_options.addItem("")
        self.horizontalLayout_10.addWidget(self.cat_options)
        self.subcat_options = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.subcat_options.setObjectName("subcat_options")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.subcat_options.addItem("")
        self.horizontalLayout_10.addWidget(self.subcat_options)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_10)
        self.cond_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cond_lbl.setObjectName("cond_lbl")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.cond_lbl)
        self.cond_options = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cond_options.sizePolicy().hasHeightForWidth())
        self.cond_options.setSizePolicy(sizePolicy)
        self.cond_options.setMinimumSize(QtCore.QSize(50, 20))
        self.cond_options.setBaseSize(QtCore.QSize(50, 0))
        self.cond_options.setObjectName("cond_options")
        self.cond_options.addItem("")
        self.cond_options.addItem("")
        self.cond_options.addItem("")
        self.cond_options.addItem("")
        self.cond_options.addItem("")
        self.cond_options.addItem("")
        self.cond_options.addItem("")
        self.cond_options.addItem("")
        self.cond_options.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cond_options)
        self.qty_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qty_lbl.setObjectName("qty_lbl")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.qty_lbl)
        self.qty_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.qty_le.setObjectName("qty_le")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.qty_le)
        self.mpn_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mpn_lbl.setObjectName("mpn_lbl")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.mpn_lbl)
        self.pn_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pn_le.setObjectName("pn_le")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pn_le)
        self.ampn_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ampn_lbl.setObjectName("ampn_lbl")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.ampn_lbl)
        self.apn_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.apn_le.setObjectName("apn_le")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.apn_le)
        self.sn_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sn_lbl.setObjectName("sn_lbl")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.sn_lbl)
        self.sn_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.sn_le.setObjectName("sn_le")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.sn_le)
        self.sku_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sku_lbl.setObjectName("sku_lbl")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.sku_lbl)
        self.sku_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.sku_le.setObjectName("sku_le")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.sku_le)
        self.mfr_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mfr_lbl.setObjectName("mfr_lbl")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.mfr_lbl)
        self.mfr_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.mfr_le.setObjectName("mfr_le")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.mfr_le)
        self.price_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.price_lbl.setObjectName("price_lbl")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.price_lbl)
        self.price_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.price_le.setObjectName("price_le")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.price_le)
        self.ship_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ship_lbl.setObjectName("ship_lbl")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.ship_lbl)
        self.ship_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.ship_le.setObjectName("ship_le")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.ship_le)
        self.core_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.core_lbl.setObjectName("core_lbl")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.core_lbl)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.core_yes = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.core_yes.sizePolicy().hasHeightForWidth())
        self.core_yes.setSizePolicy(sizePolicy)
        self.core_yes.setObjectName("core_yes")
        self.coreBtnGroup = QtWidgets.QButtonGroup(ListItemWidget)
        self.coreBtnGroup.setObjectName("coreBtnGroup")
        self.coreBtnGroup.addButton(self.core_yes)
        self.horizontalLayout.addWidget(self.core_yes)
        self.core_no = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.core_no.sizePolicy().hasHeightForWidth())
        self.core_no.setSizePolicy(sizePolicy)
        self.core_no.setObjectName("core_no")
        self.coreBtnGroup.addButton(self.core_no)
        self.horizontalLayout.addWidget(self.core_no)
        self.formLayout.setLayout(12, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.img_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.img_lbl.setObjectName("img_lbl")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.img_lbl)
        self.img_upload_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_upload_btn.sizePolicy().hasHeightForWidth())
        self.img_upload_btn.setSizePolicy(sizePolicy)
        self.img_upload_btn.setObjectName("img_upload_btn")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.img_upload_btn)
        self.active_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.active_lbl.setObjectName("active_lbl")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.active_lbl)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.active_yes = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.active_yes.sizePolicy().hasHeightForWidth())
        self.active_yes.setSizePolicy(sizePolicy)
        self.active_yes.setObjectName("active_yes")
        self.activeBtnGroup = QtWidgets.QButtonGroup(ListItemWidget)
        self.activeBtnGroup.setObjectName("activeBtnGroup")
        self.activeBtnGroup.addButton(self.active_yes)
        self.horizontalLayout_6.addWidget(self.active_yes)
        self.active_no = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.active_no.setObjectName("active_no")
        self.activeBtnGroup.addButton(self.active_no)
        self.horizontalLayout_6.addWidget(self.active_no)
        self.formLayout.setLayout(14, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.onsale_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.onsale_lbl.setObjectName("onsale_lbl")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.onsale_lbl)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sale_yes = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sale_yes.sizePolicy().hasHeightForWidth())
        self.sale_yes.setSizePolicy(sizePolicy)
        self.sale_yes.setObjectName("sale_yes")
        self.saleBtnGroup = QtWidgets.QButtonGroup(ListItemWidget)
        self.saleBtnGroup.setObjectName("saleBtnGroup")
        self.saleBtnGroup.addButton(self.sale_yes)
        self.horizontalLayout_7.addWidget(self.sale_yes)
        self.sale_no = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.sale_no.setObjectName("sale_no")
        self.saleBtnGroup.addButton(self.sale_no)
        self.horizontalLayout_7.addWidget(self.sale_no)
        self.formLayout.setLayout(15, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.offer_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.offer_lbl.setObjectName("offer_lbl")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.offer_lbl)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.offer_yes = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offer_yes.sizePolicy().hasHeightForWidth())
        self.offer_yes.setSizePolicy(sizePolicy)
        self.offer_yes.setObjectName("offer_yes")
        self.offerBtnGroup = QtWidgets.QButtonGroup(ListItemWidget)
        self.offerBtnGroup.setObjectName("offerBtnGroup")
        self.offerBtnGroup.addButton(self.offer_yes)
        self.horizontalLayout_8.addWidget(self.offer_yes)
        self.offer_no = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.offer_no.setObjectName("offer_no")
        self.offerBtnGroup.addButton(self.offer_no)
        self.horizontalLayout_8.addWidget(self.offer_no)
        self.formLayout.setLayout(16, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.feat_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.feat_lbl.setObjectName("feat_lbl")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.feat_lbl)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.feat_yes = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feat_yes.sizePolicy().hasHeightForWidth())
        self.feat_yes.setSizePolicy(sizePolicy)
        self.feat_yes.setObjectName("feat_yes")
        self.featBtnGroup = QtWidgets.QButtonGroup(ListItemWidget)
        self.featBtnGroup.setObjectName("featBtnGroup")
        self.featBtnGroup.addButton(self.feat_yes)
        self.horizontalLayout_9.addWidget(self.feat_yes)
        self.feat_no = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.feat_no.setObjectName("feat_no")
        self.featBtnGroup.addButton(self.feat_no)
        self.horizontalLayout_9.addWidget(self.feat_no)
        self.formLayout.setLayout(17, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_9)
        self.verticalLayout.addLayout(self.formLayout)
        self.img_groupbox = QtWidgets.QGroupBox(ListItemWidget)
        self.img_groupbox.setGeometry(QtCore.QRect(399, 9, 221, 601))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.img_groupbox.setFont(font)
        self.img_groupbox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.img_groupbox.setObjectName("img_groupbox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.img_groupbox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 201, 571))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.img1_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img1_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img1_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img1_lbl.setText("")
        self.img1_lbl.setObjectName("img1_lbl")
        self.gridLayout.addWidget(self.img1_lbl, 0, 0, 1, 1)
        self.img2_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img2_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img2_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img2_lbl.setText("")
        self.img2_lbl.setObjectName("img2_lbl")
        self.gridLayout.addWidget(self.img2_lbl, 0, 1, 1, 1)
        self.img7_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img7_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img7_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img7_lbl.setText("")
        self.img7_lbl.setObjectName("img7_lbl")
        self.gridLayout.addWidget(self.img7_lbl, 3, 0, 1, 1)
        self.img4_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img4_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img4_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img4_lbl.setText("")
        self.img4_lbl.setObjectName("img4_lbl")
        self.gridLayout.addWidget(self.img4_lbl, 1, 1, 1, 1)
        self.img8_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img8_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img8_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img8_lbl.setText("")
        self.img8_lbl.setObjectName("img8_lbl")
        self.gridLayout.addWidget(self.img8_lbl, 3, 1, 1, 1)
        self.img5_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img5_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img5_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img5_lbl.setText("")
        self.img5_lbl.setObjectName("img5_lbl")
        self.gridLayout.addWidget(self.img5_lbl, 2, 0, 1, 1)
        self.img6_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img6_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img6_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img6_lbl.setText("")
        self.img6_lbl.setObjectName("img6_lbl")
        self.gridLayout.addWidget(self.img6_lbl, 2, 1, 1, 1)
        self.img3_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img3_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img3_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img3_lbl.setText("")
        self.img3_lbl.setObjectName("img3_lbl")
        self.gridLayout.addWidget(self.img3_lbl, 1, 0, 1, 1)
        self.img9_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img9_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img9_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img9_lbl.setText("")
        self.img9_lbl.setObjectName("img9_lbl")
        self.gridLayout.addWidget(self.img9_lbl, 4, 0, 1, 1)
        self.img10_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img10_lbl.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.img10_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img10_lbl.setText("")
        self.img10_lbl.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.img10_lbl.setObjectName("img10_lbl")
        self.gridLayout.addWidget(self.img10_lbl, 4, 1, 1, 1)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(ListItemWidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 610, 381, 41))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.upload_new_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.upload_new_button.setObjectName("upload_new_button")
        self.horizontalLayout_11.addWidget(self.upload_new_button)
        self.cancel_new_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.cancel_new_button.setObjectName("cancel_new_button")
        self.horizontalLayout_11.addWidget(self.cancel_new_button)

        self.retranslateUi(ListItemWidget)
        self.cat_options.setCurrentIndex(0)
        self.cancel_new_button.clicked.connect(ListItemWidget.close)
        QtCore.QMetaObject.connectSlotsByName(ListItemWidget)
        ListItemWidget.setTabOrder(self.name_le, self.desc_te)
        ListItemWidget.setTabOrder(self.desc_te, self.cat_options)
        ListItemWidget.setTabOrder(self.cat_options, self.subcat_options)
        ListItemWidget.setTabOrder(self.subcat_options, self.cond_options)
        ListItemWidget.setTabOrder(self.cond_options, self.qty_le)
        ListItemWidget.setTabOrder(self.qty_le, self.pn_le)
        ListItemWidget.setTabOrder(self.pn_le, self.apn_le)
        ListItemWidget.setTabOrder(self.apn_le, self.sn_le)
        ListItemWidget.setTabOrder(self.sn_le, self.sku_le)
        ListItemWidget.setTabOrder(self.sku_le, self.mfr_le)
        ListItemWidget.setTabOrder(self.mfr_le, self.price_le)
        ListItemWidget.setTabOrder(self.price_le, self.ship_le)
        ListItemWidget.setTabOrder(self.ship_le, self.core_yes)
        ListItemWidget.setTabOrder(self.core_yes, self.core_no)
        ListItemWidget.setTabOrder(self.core_no, self.img_upload_btn)
        ListItemWidget.setTabOrder(self.img_upload_btn, self.active_yes)
        ListItemWidget.setTabOrder(self.active_yes, self.active_no)
        ListItemWidget.setTabOrder(self.active_no, self.sale_yes)
        ListItemWidget.setTabOrder(self.sale_yes, self.sale_no)
        ListItemWidget.setTabOrder(self.sale_no, self.offer_yes)
        ListItemWidget.setTabOrder(self.offer_yes, self.offer_no)
        ListItemWidget.setTabOrder(self.offer_no, self.feat_yes)
        ListItemWidget.setTabOrder(self.feat_yes, self.feat_no)
        ListItemWidget.setTabOrder(self.feat_no, self.upload_new_button)
        ListItemWidget.setTabOrder(self.upload_new_button, self.cancel_new_button)

    def retranslateUi(self, ListItemWidget):
        _translate = QtCore.QCoreApplication.translate
        ListItemWidget.setWindowTitle(_translate("ListItemWidget", "Edit a Product - HS Dashboard App"))
        self.newproduct_lbl.setText(_translate("ListItemWidget", "Edit Product"))
        self.name_lbl.setText(_translate("ListItemWidget", "Product Name*"))
        self.desc_lbl.setText(_translate("ListItemWidget", "Product Description*"))
        self.cat_lbl.setText(_translate("ListItemWidget", "Product Category*"))
        self.cat_options.setItemText(0, _translate("ListItemWidget", "Airboat"))
        self.cat_options.setItemText(1, _translate("ListItemWidget", "Aircraft For Sale"))
        self.cat_options.setItemText(2, _translate("ListItemWidget", "Airframe"))
        self.cat_options.setItemText(3, _translate("ListItemWidget", "Art"))
        self.cat_options.setItemText(4, _translate("ListItemWidget", "Avionics"))
        self.cat_options.setItemText(5, _translate("ListItemWidget", "Electrical"))
        self.cat_options.setItemText(6, _translate("ListItemWidget", "Experimental"))
        self.cat_options.setItemText(7, _translate("ListItemWidget", "Hardware & Tools"))
        self.cat_options.setItemText(8, _translate("ListItemWidget", "Landing Gear"))
        self.cat_options.setItemText(9, _translate("ListItemWidget", "Misc"))
        self.cat_options.setItemText(10, _translate("ListItemWidget", "Pilot Supplies"))
        self.cat_options.setItemText(11, _translate("ListItemWidget", "Powerplant"))
        self.cat_options.setItemText(12, _translate("ListItemWidget", "Wheels & Brakes"))
        self.subcat_options.setItemText(0, _translate("ListItemWidget", "---"))
        self.subcat_options.setItemText(1, _translate("ListItemWidget", "Aerobatic"))
        self.subcat_options.setItemText(2, _translate("ListItemWidget", "Aeronca"))
        self.subcat_options.setItemText(3, _translate("ListItemWidget", "Amphibian"))
        self.subcat_options.setItemText(4, _translate("ListItemWidget", "Antique"))
        self.subcat_options.setItemText(5, _translate("ListItemWidget", "Beechcraft"))
        self.subcat_options.setItemText(6, _translate("ListItemWidget", "Bellanca"))
        self.subcat_options.setItemText(7, _translate("ListItemWidget", "Cessna"))
        self.subcat_options.setItemText(8, _translate("ListItemWidget", "Cirrus"))
        self.subcat_options.setItemText(9, _translate("ListItemWidget", "Control Surfaces"))
        self.subcat_options.setItemText(10, _translate("ListItemWidget", "General Parts"))
        self.subcat_options.setItemText(11, _translate("ListItemWidget", "Helicopter"))
        self.subcat_options.setItemText(12, _translate("ListItemWidget", "Interior"))
        self.subcat_options.setItemText(13, _translate("ListItemWidget", "Luscombe"))
        self.subcat_options.setItemText(14, _translate("ListItemWidget", "Mooney"))
        self.subcat_options.setItemText(15, _translate("ListItemWidget", "Other"))
        self.subcat_options.setItemText(16, _translate("ListItemWidget", "Piper"))
        self.subcat_options.setItemText(17, _translate("ListItemWidget", "Taylorcraft"))
        self.subcat_options.setItemText(18, _translate("ListItemWidget", "Warbird"))
        self.subcat_options.setItemText(19, _translate("ListItemWidget", "Antennas"))
        self.subcat_options.setItemText(20, _translate("ListItemWidget", "Audio Panels"))
        self.subcat_options.setItemText(21, _translate("ListItemWidget", "AutoPilot"))
        self.subcat_options.setItemText(22, _translate("ListItemWidget", "ELTs"))
        self.subcat_options.setItemText(23, _translate("ListItemWidget", "Engine Monitors"))
        self.subcat_options.setItemText(24, _translate("ListItemWidget", "GPS"))
        self.subcat_options.setItemText(25, _translate("ListItemWidget", "Indicators"))
        self.subcat_options.setItemText(26, _translate("ListItemWidget", "Intercoms"))
        self.subcat_options.setItemText(27, _translate("ListItemWidget", "Nav/Coms"))
        self.subcat_options.setItemText(28, _translate("ListItemWidget", "Other"))
        self.subcat_options.setItemText(29, _translate("ListItemWidget", "Packages"))
        self.subcat_options.setItemText(30, _translate("ListItemWidget", "Pitot Tubes"))
        self.subcat_options.setItemText(31, _translate("ListItemWidget", "Transponders"))
        self.subcat_options.setItemText(32, _translate("ListItemWidget", "Trays & Connectors"))
        self.subcat_options.setItemText(33, _translate("ListItemWidget", "Weather Systems"))
        self.subcat_options.setItemText(34, _translate("ListItemWidget", "Batteries"))
        self.subcat_options.setItemText(35, _translate("ListItemWidget", "Lighting"))
        self.subcat_options.setItemText(36, _translate("ListItemWidget", "Other"))
        self.subcat_options.setItemText(37, _translate("ListItemWidget", "Jacks"))
        self.subcat_options.setItemText(38, _translate("ListItemWidget", "Nuts & Bolts"))
        self.subcat_options.setItemText(39, _translate("ListItemWidget", "Other"))
        self.subcat_options.setItemText(40, _translate("ListItemWidget", "Rivets"))
        self.subcat_options.setItemText(41, _translate("ListItemWidget", "Testing Equipment"))
        self.subcat_options.setItemText(42, _translate("ListItemWidget", "Tools"))
        self.subcat_options.setItemText(43, _translate("ListItemWidget", "Amphibian"))
        self.subcat_options.setItemText(44, _translate("ListItemWidget", "Skis"))
        self.subcat_options.setItemText(45, _translate("ListItemWidget", "Tailwheel"))
        self.subcat_options.setItemText(46, _translate("ListItemWidget", "Tires & Tubes"))
        self.subcat_options.setItemText(47, _translate("ListItemWidget", "Wheels & Brakes"))
        self.subcat_options.setItemText(48, _translate("ListItemWidget", "Aviator Accessories"))
        self.subcat_options.setItemText(49, _translate("ListItemWidget", "Bags"))
        self.subcat_options.setItemText(50, _translate("ListItemWidget", "Books"))
        self.subcat_options.setItemText(51, _translate("ListItemWidget", "Collectibles"))
        self.subcat_options.setItemText(52, _translate("ListItemWidget", "Covers & Accessories"))
        self.subcat_options.setItemText(53, _translate("ListItemWidget", "Headsets"))
        self.subcat_options.setItemText(54, _translate("ListItemWidget", "Manuals"))
        self.subcat_options.setItemText(55, _translate("ListItemWidget", "Oils, Liquids & Sprays"))
        self.subcat_options.setItemText(56, _translate("ListItemWidget", "Other"))
        self.subcat_options.setItemText(57, _translate("ListItemWidget", "Pilot Wear"))
        self.subcat_options.setItemText(58, _translate("ListItemWidget", "Safety"))
        self.subcat_options.setItemText(59, _translate("ListItemWidget", "Stickers & Decals"))
        self.subcat_options.setItemText(60, _translate("ListItemWidget", "Tow"))
        self.subcat_options.setItemText(61, _translate("ListItemWidget", "Engine Parts"))
        self.subcat_options.setItemText(62, _translate("ListItemWidget", "Engines"))
        self.subcat_options.setItemText(63, _translate("ListItemWidget", "Environmental"))
        self.subcat_options.setItemText(64, _translate("ListItemWidget", "Exhaust"))
        self.subcat_options.setItemText(65, _translate("ListItemWidget", "Fuel System"))
        self.subcat_options.setItemText(66, _translate("ListItemWidget", "General Parts"))
        self.subcat_options.setItemText(67, _translate("ListItemWidget", "Propellers"))
        self.cond_lbl.setText(_translate("ListItemWidget", "Product Condition*"))
        self.cond_options.setItemText(0, _translate("ListItemWidget", "As Removed"))
        self.cond_options.setItemText(1, _translate("ListItemWidget", "Serviceable"))
        self.cond_options.setItemText(2, _translate("ListItemWidget", "Overhauled"))
        self.cond_options.setItemText(3, _translate("ListItemWidget", "New Stock"))
        self.cond_options.setItemText(4, _translate("ListItemWidget", "Repairable"))
        self.cond_options.setItemText(5, _translate("ListItemWidget", "New Surplus (NOS)"))
        self.cond_options.setItemText(6, _translate("ListItemWidget", "Beyond Repair"))
        self.cond_options.setItemText(7, _translate("ListItemWidget", "Unknown"))
        self.cond_options.setItemText(8, _translate("ListItemWidget", "Core"))
        self.qty_lbl.setText(_translate("ListItemWidget", "Qty Available*"))
        self.mpn_lbl.setText(_translate("ListItemWidget", "Part Number"))
        self.ampn_lbl.setText(_translate("ListItemWidget", "Alt Part Number"))
        self.sn_lbl.setText(_translate("ListItemWidget", "Serial Number"))
        self.sku_lbl.setText(_translate("ListItemWidget", "SKU"))
        self.mfr_lbl.setText(_translate("ListItemWidget", "Manufacturer"))
        self.price_lbl.setText(_translate("ListItemWidget", "Price*"))
        self.ship_lbl.setText(_translate("ListItemWidget", "Shipping Cost*"))
        self.core_lbl.setText(_translate("ListItemWidget", "Has Core Charge?"))
        self.core_yes.setText(_translate("ListItemWidget", "Yes"))
        self.core_no.setText(_translate("ListItemWidget", "No"))
        self.img_lbl.setText(_translate("ListItemWidget", "Default Image:"))
        self.img_upload_btn.setText(_translate("ListItemWidget", "Choose Image"))
        self.active_lbl.setText(_translate("ListItemWidget", "Active"))
        self.active_yes.setText(_translate("ListItemWidget", "Yes"))
        self.active_no.setText(_translate("ListItemWidget", "No"))
        self.onsale_lbl.setText(_translate("ListItemWidget", "On Sale"))
        self.sale_yes.setText(_translate("ListItemWidget", "Yes"))
        self.sale_no.setText(_translate("ListItemWidget", "No"))
        self.offer_lbl.setText(_translate("ListItemWidget", "Allow Best Offer"))
        self.offer_yes.setText(_translate("ListItemWidget", "Yes"))
        self.offer_no.setText(_translate("ListItemWidget", "No"))
        self.feat_lbl.setText(_translate("ListItemWidget", "Featured"))
        self.feat_yes.setText(_translate("ListItemWidget", "Yes"))
        self.feat_no.setText(_translate("ListItemWidget", "No"))
        self.img_groupbox.setTitle(_translate("ListItemWidget", "Product Images"))
        self.upload_new_button.setText(_translate("ListItemWidget", "Submit"))
        self.cancel_new_button.setText(_translate("ListItemWidget", "Cancel"))

